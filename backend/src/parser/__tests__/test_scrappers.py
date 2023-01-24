from .fixtures import (
    SHERDOG_EVENT_SITE,
    SHERDOG_FIGHT_SITE,
)


from ..events.scrappers import EventFightsScrapper, LatestEventsScrapper


def test_latest_events_scrapper_custom_limit(mocker):
    expected_data = [
        {
            "name": "UFC on ESPN 42 - Thompson vs. Jan Pawel II",
            "date": "2022-12-03T00:00:00-08:00",
            "href": "/events/UFC-on-ESPN-42-Thompson-vs-Holland-94046",
        },
        {
            "name": "UFC Fight Night 215 - Nzechukwu vs. Cutelaba",
            "href": "/events/UFC-Fight-Night-215-Nzechukwu-vs-Cutelaba-94045",
            "date": "2022-11-19T00:00:00-08:00",
        },
        {
            "name": "UFC 281 - Adesanya vs. Pereira",
            "href": "/events/UFC-281-Adesanya-vs-Pereira-94041",
            "date": "2022-11-12T00:00:00-08:00",
        },
    ]
    mocker.patch(
        "src.parser.commons.scrappers.get_site_content", return_value=SHERDOG_FIGHT_SITE
    )
    scrapper = LatestEventsScrapper()
    assert scrapper.data == expected_data


def test_latest_events_scrapper_limit_one(mocker):
    expected_data = [
        {
            "name": "UFC on ESPN 42 - Thompson vs. Jan Pawel II",
            "date": "2022-12-03T00:00:00-08:00",
            "href": "/events/UFC-on-ESPN-42-Thompson-vs-Holland-94046",
        }
    ]
    mocker.patch(
        "src.parser.commons.scrappers.get_site_content", return_value=SHERDOG_FIGHT_SITE
    )
    scrapper = LatestEventsScrapper(limit=1)
    assert scrapper.data == expected_data


def test_latest_event_fights_scrapper(mocker):
    expected_data = [
        [
            {"href": "/fighter/Sean-Strickland-30452", "name": "Sean Strickland"},
            {
                "href": "/fighter/Nassourdine-Imavov-217405",
                "name": "Nassourdine Imavov",
            },
        ],
        [
            {"href": "/fighter/Dan-Ige-136499", "name": "DanIge"},
            {"href": "/fighter/Damon-Jackson-113767", "name": "DamonJackson"},
        ],
    ]
    mocker.patch(
        "src.parser.commons.scrappers.get_site_content", return_value=SHERDOG_EVENT_SITE
    )
    scrapper = EventFightsScrapper("UFC-Fight-Night-217-Strickland-vs-Imavov-94946")
    assert scrapper.data == expected_data

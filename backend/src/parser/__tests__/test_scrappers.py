from .fixtures import (
    SHERDOG_FIGHT_SITE,
)


from ..events.scrappers import LatestEventsScrapper


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

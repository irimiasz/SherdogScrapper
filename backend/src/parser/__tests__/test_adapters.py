from datetime import date

from ..events.adapters import (
    EventAdapter,
    EventListAdapter,
    FightListAdapter,
)


def test_event_adapter():
    input_data = {
        "name": "UFC on ESPN 42 - Thompson vs. Jan Pawel II",
        "date": "2022-12-03T00:00:00-08:00",
        "href": "/events/UFC-on-ESPN-42-Thompson-vs-Holland-94046",
    }
    expected_data = {
        "name": "UFC on ESPN 42 - Thompson vs. Jan Pawel II",
        "date": date(year=2022, month=12, day=3),
        "href": "UFC-on-ESPN-42-Thompson-vs-Holland-94046",
    }
    adapter = EventAdapter(data=input_data)
    assert adapter.to_dict() == expected_data


def test_event_list_adapter(mocker):
    input_data = [
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
        "src.parser.commons.adapters.ScrapperDataSetupMixin.set_up_data",
        return_value=input_data,
    )
    expected_data = {
        "events": [
            {
                "name": "UFC on ESPN 42 - Thompson vs. Jan Pawel II",
                "date": date(year=2022, month=12, day=3),
                "href": "UFC-on-ESPN-42-Thompson-vs-Holland-94046",
            },
            {
                "name": "UFC Fight Night 215 - Nzechukwu vs. Cutelaba",
                "date": date(year=2022, month=11, day=19),
                "href": "UFC-Fight-Night-215-Nzechukwu-vs-Cutelaba-94045",
            },
            {
                "name": "UFC 281 - Adesanya vs. Pereira",
                "date": date(year=2022, month=11, day=12),
                "href": "UFC-281-Adesanya-vs-Pereira-94041",
            },
        ]
    }
    adapter = EventListAdapter()
    assert adapter.to_dict() == expected_data


def test_fight_list_adapter(mocker):
    input_data = [
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
        "src.parser.commons.adapters.ScrapperDataSetupMixin.set_up_data",
        return_value=input_data,
    )
    imavov = {
        "href": "/fighter/Nassourdine-Imavov-217405",
        "name": "Nassourdine Imavov",
    }
    strickland = {"href": "/fighter/Sean-Strickland-30452", "name": "Sean Strickland"}
    ige = {"href": "/fighter/Dan-Ige-136499", "name": "Dan Ige"}
    jackson = {"href": "/fighter/Damon-Jackson-113767", "name": "Damon Jackson"}
    data = FightListAdapter().to_dict()
    assert strickland in data["fights"][0]["fighters"]
    assert imavov in data["fights"][0]["fighters"]
    assert ige in data["fights"][1]["fighters"]
    assert jackson in data["fights"][1]["fighters"]

from fastapi.testclient import TestClient
from src.app import app


def test_latest_events(mocker):
    expected_response = {
        "events": [
            {
                "name": "UFC on ESPN 42 - Thompson vs. Hollando",
                "href": "https://www.sherdog.com/events/UFC-on-ESPN-42-Thompson-vs-Holland-94046",
                "date": "2022-12-03",
            },
            {
                "name": "UFC Fight Night 215 - Nzechukwu vs. Cutelaba",
                "href": "https://www.sherdog.com/events/UFC-Fight-Night-215-Nzechukwu-vs-Cutelaba-94045",
                "date": "2022-11-19",
            },
            {
                "name": "UFC 281 - Adesanya vs. Pereira",
                "href": "https://www.sherdog.com/events/UFC-281-Adesanya-vs-Pereira-94041",
                "date": "2022-11-12",
            },
        ]
    }
    mocker.patch(
        "src.api.v1.events.routers.EventListAdapter.to_dict", return_value=expected_response
    )
    client = TestClient(app)
    response = client.get("api/v1/events/latest")
    assert response.status_code == 200
    assert response.json() == expected_response

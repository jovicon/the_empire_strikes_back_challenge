import json

import pytest


def test_create_crew(test_app_with_db):
    data = {
        "name": "among us",
        "crew_quantity": 10,
        "ship_name": "skeld",
        "ship_cost": 123456789,
        "ship_max_speed": 198,
    }

    response = test_app_with_db.post("/crews/", data=json.dumps(data))

    assert response.status_code == 201
    assert response.json()["name"] == data["name"]
    assert response.json()["crew_quantity"] == data["crew_quantity"]
    assert response.json()["ship_name"] == data["ship_name"]
    assert response.json()["ship_cost"] == data["ship_cost"]
    assert response.json()["ship_max_speed"] == data["ship_max_speed"]


def test_create_crew_invalid_json(test_app):
    response = test_app.post("/crews/", data=json.dumps({}))
    assert response.status_code == 422

    # this assert is dynamic
    # from missing request fields
    print(response.json())
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "payload", "name"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "payload", "crew_quantity"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "payload", "ship_name"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "payload", "ship_cost"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "payload", "ship_max_speed"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ]
    }


def test_read_crew(test_app_with_db):
    data = {
        "name": "among us",
        "crew_quantity": 10,
        "ship_name": "skeld",
        "ship_cost": 123456789,
        "ship_max_speed": 198,
    }

    response = test_app_with_db.post("/crews/", data=json.dumps(data))
    crew_id = response.json()["id"]

    response = test_app_with_db.get(f"/crews/{crew_id}/")
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == crew_id
    assert response_dict["name"] == data["name"]
    assert response_dict["crew_quantity"] == data["crew_quantity"]
    assert response_dict["ship_name"] == data["ship_name"]
    assert response_dict["ship_cost"] == data["ship_cost"]
    assert response_dict["ship_max_speed"] == data["ship_max_speed"]


def test_read_summary_incorrect_id(test_app_with_db):
    response = test_app_with_db.get("/crews/123123/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Crew not found"


def test_read_all_sumaries(test_app_with_db):
    data = {
        "name": "among us",
        "crew_quantity": 10,
        "ship_name": "skeld",
        "ship_cost": 123456789,
        "ship_max_speed": 198,
    }
    response = test_app_with_db.post("/crews/", data=json.dumps(data))
    crew_id = response.json()["id"]

    response = test_app_with_db.get(f"/crews")
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == crew_id, response_list))) == 1

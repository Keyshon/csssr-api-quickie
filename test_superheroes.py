import pytest
import requests
import json

api_url = "https://superhero.qa-test.csssr.com"


@pytest.mark.dependency()
def test_status_200():
    request_url = "/superheroes"
    pytest.req = requests.get(api_url + request_url)

    assert pytest.req.status_code == 200


@pytest.mark.dependency(depends=["test_status_200"])
def test_length_greater_than_0():
    response_length = len(pytest.req.json())

    assert response_length > 0


@pytest.mark.dependency(depends=["test_length_greater_than_0"])
def test_first_item_contains_superhero():
    superhero = json.dumps(pytest.req.json()[0])
    expected_attributes = ["birthDate", "city",
                           "fullName", "gender", "mainSkill", "phone"]
    is_containing_superhero_attributes = all(
        attrs in superhero for attrs in expected_attributes)

    assert is_containing_superhero_attributes

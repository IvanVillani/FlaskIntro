import pytest
from datetime import datetime
from flask import Response
from pilots.helpers import (
    format_pilots_output,
    build_pilot_based_on_form_data,
    update_pilot_based_on_form_data,
)
from pilots.models import Pilot
from app import app


@pytest.fixture
def mocked_pilots() -> list[Pilot]:
    # Create mock Pilot objects
    pilotTest = Pilot(
        id="1",
        email="test@test.com",
        username="Test",
        dob=datetime.strptime("01/01/2000", "%d/%m/%Y").date(),
        country="Bulgaria",
        phone_number="0888888888",
    )

    pilotIvan = Pilot(
        id="2",
        email="ivan@test.com",
        username="Ivan",
        dob=datetime.strptime("01/01/2000", "%d/%m/%Y").date(),
        country="Bulgaria",
        phone_number="0888888888",
    )

    pilotGeorgi = Pilot(
        id="3",
        email="georgi@test.com",
        username="Georgi",
        dob=datetime.strptime("01/01/2000", "%d/%m/%Y").date(),
        country="Bulgaria",
        phone_number="0888888888",
    )

    return [pilotTest, pilotIvan, pilotGeorgi]


@pytest.fixture
def mocked_form_data() -> dict:
    pilotTestFormData = {
        "email": "test2@test.com",
        "username": "Test2",
        "dob": "19/08/2000",
        "country": "TestCountry",
        "phone_number": "0999999999",
    }

    return pilotTestFormData


def test_format_pilots_output(mocked_pilots):
    with app.app_context():
        # setup
        ...

        # act
        result: Response = format_pilots_output(mocked_pilots)

        # verify
        data: list[dict] = result.get_json()
        checked_data: dict = {"Ivan": False, "Georgi": False, "Test": False}

        for pilot in data:
            checked_data[pilot["username"]] = True

        for value in checked_data.values():
            assert value == True


def test_build_pilot_based_on_form_data(mocked_form_data):
    with app.app_context():
        # setup
        ...

        # act
        pilot: Pilot = build_pilot_based_on_form_data(mocked_form_data)

        # verify
        assert pilot.username == "Test2"
        assert pilot.email == "test2@test.com"
        assert str(pilot.dob) == "2000-08-19"
        assert pilot.country == "TestCountry"
        assert pilot.phone_number == "0999999999"


def test_update_pilot_based_on_form_data(mocked_pilots, mocked_form_data):
    with app.app_context():
        # setup
        pilotToUpdate: Pilot = mocked_pilots[0]  # Test Pilot

        # act
        update_pilot_based_on_form_data(pilotToUpdate, mocked_form_data)

        # verify
        assert pilotToUpdate.id == "1"  # id is the same
        assert pilotToUpdate.username == "Test2"
        assert pilotToUpdate.email == "test2@test.com"
        assert str(pilotToUpdate.dob) == "2000-08-19"
        assert pilotToUpdate.country == "TestCountry"
        assert pilotToUpdate.phone_number == "0999999999"

import uuid
from datetime import datetime
from flask import jsonify, Response

from pilots.models import Pilot


def format_pilots_output(pilots: list[Pilot]) -> Response:
    response: list = []
    for pilot in pilots:
        response.append(pilot.toDict())
    return jsonify(response)


def build_pilot_based_on_form_data(form_data: dict) -> Pilot:
    id: str = str(uuid.uuid4())
    new_pilot: Pilot = Pilot(
        id=id,
        email=form_data["email"],
        username=form_data["username"],
        dob=datetime.strptime(form_data["dob"], "%d/%m/%Y").date(),
        country=form_data["country"],
        phone_number=form_data["phone_number"],
    )

    new_pilot.validate_fields()

    return new_pilot


def update_pilot_based_on_form_data(pilot: Pilot, form_data: dict):
    pilot.email = form_data["email"]
    pilot.username = form_data["username"]
    pilot.dob = datetime.strptime(form_data["dob"], "%d/%m/%Y").date()
    pilot.country = form_data["country"]
    pilot.phone_number = form_data["phone_number"]

    pilot.validate_fields()


if __name__ == "__main__":
    pilot = Pilot(
        id="1",
        email="test@test.com",
        username="test",
        dob=datetime.strptime("01/01/2000", "%d/%m/%Y").date(),
        country="Bulgaria",
        phone_number="0888888888",
    )
    update_pilot_based_on_form_data(
        pilot=pilot,
        form_data={
            "email": "ivan@test.com",
            "username": "Ivan",
            "dob": "01/01/2001",
            "country": "Italy",
            "phone_number": "0888888889",
        },
    )
    print(pilot)
    print(pilot.toDict())

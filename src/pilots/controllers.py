from flask import request, jsonify
from config import db
from pilots.models import Pilot
from pilots.helpers import (
    format_pilots_output,
    build_pilot_based_on_form_data,
    update_pilot_based_on_form_data,
)


def retrieve_all_pilots() -> str:
    pilots: list[Pilot] = Pilot.query.all()
    return format_pilots_output(pilots)


def create_pilot() -> str:
    request_form: dict = request.form.to_dict()

    new_pilot: Pilot = build_pilot_based_on_form_data(request_form)

    try:
        db.session.add(new_pilot)
        db.session.commit()
    except Exception:
        return "There was a problem, creating a new F1 Pilot!"

    response: Pilot = Pilot.query.get(id).toDict()
    return jsonify(response)


def retrieve_pilot(pilot_id: str) -> str:
    response: Pilot = Pilot.query.get(pilot_id).toDict()
    return jsonify(response)


def update_pilot(pilot_id: str) -> str:
    request_form: dict = request.form.to_dict()

    pilot: Pilot = Pilot.query.get(pilot_id)

    update_pilot_based_on_form_data(pilot, request_form)

    try:
        db.session.commit()
    except Exception:
        return ('There was a problem, updating F1 Pilot with Id "{}"!').format(pilot_id)

    response: Pilot = Pilot.query.get(pilot_id).toDict()
    return jsonify(response)


def delete_pilot(pilot_id: str) -> str:
    try:
        Pilot.query.filter_by(id=pilot_id).delete()
        db.session.commit()
    except Exception:
        return ('There was a problem, deleting F1 Pilot with Id "{}"!').format(pilot_id)

    return ('F1 Pilot with Id "{}" has been deleted successfully!').format(pilot_id)

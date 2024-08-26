from sqlalchemy import inspect
from datetime import datetime
from validation.validate_email import ValidateEmail
from validation.validate_username import ValidateUsername
from validation.validate_country import ValidateCountry

from config import db


class Pilot(db.Model):
    # Auto-generated Fields:
    id = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated = db.Column(
        db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )

    # User Input Fields:
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date)
    country = db.Column(db.String(100))
    phone_number = db.Column(db.String(20))

    def validate_fields(self):
        ValidateEmail(self.email, required=True, unique=True)
        ValidateUsername(self.username, required=True, not_empty=True)
        ValidateCountry(self.country, required=True, not_empty=True)

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<%r - %r>" % (self.username, self.email)

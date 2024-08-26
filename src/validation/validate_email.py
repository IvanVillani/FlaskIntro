import re

class ValidateEmail:
    def __init__(self, value, required=False, unique=False, message="Invalid email"):
        self.value = value
        self.required = required
        self.unique = unique
        self.message = message

        # Regular expression for validating an Email
        self.email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        
        self.validate()

    def validate(self):
        if self.required and not self.value:
            raise ValueError("Email is required.")
        
        if not re.match(self.email_regex, self.value):
            raise ValueError(self.message)
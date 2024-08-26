class ValidateUsername:
    def __init__(self, value, required=False, not_empty=False, message="Invalid username"):
        self.value = value
        self.required = required
        self.not_empty = not_empty
        self.message = message

        self.validate()

    def validate(self):
        if self.required and self.value is None:
            raise ValueError("This field is required.")
        
        if not isinstance(self.value, str):
            raise ValueError(self.message)
        
        if self.not_empty and not self.value.strip():
            raise ValueError("String cannot be empty.")
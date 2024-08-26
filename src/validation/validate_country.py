class ValidateCountry:
    def __init__(self, value, required=False, not_empty=False, message="Invalid country"):
        self.value = value
        self.required = required
        self.not_empty = not_empty
        self.message = message

        # List of invalid countries
        self.invalid_countries = ["India"]

        self.validate()

    def validate(self):
        if self.required and not self.value:
            raise ValueError("Country is required.")
        
        if not isinstance(self.value, str):
            raise ValueError("Country name must be a string.")
        
        if self.not_empty and not self.value.strip():
            raise ValueError("Country cannot be empty.")
        
        if self.value in self.invalid_countries:
            raise ValueError(self.message)

class StateNotFoundError(Exception):
    """Exception raised when a state is not found in the database."""

    def __init__(self, state, message="State not found"):
        self.state = state
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.state} -> {self.message}'
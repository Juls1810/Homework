class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_first_name(self):
        return self.first_name

    def say_last_name(self):
        return self.last_name

    def say_full_name(self):
        return f"User: {self.first_name}, {self.last_name}"

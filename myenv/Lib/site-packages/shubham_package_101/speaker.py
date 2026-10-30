
class Speaker:

    name = "default"
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"{self.name} is speaking.")
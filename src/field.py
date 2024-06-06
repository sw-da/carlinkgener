class Field:
    code = ""
    name = ""
    value = ""

    def __init__(self, code, name, value=""):
        self.code = code
        self.name = name
        self.value = value

    def is_set(self):
        return self.value != ""
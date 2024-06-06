from src.website import Website
from src.field import Field

class Kurumaerabi(Website):
    code = "kurumaerabi"
    name = "www.kurumaerabi.com"
    url = "https://www.kurumaerabi.com/form.php"
    is_post = True
    template = "kurumaerabi"
    sort_name = "od"
    sort_value = "N"

    makers = {
        "Lexus": "142",
        "Toyota": "1",
        "Nissan": "2",
        "Honda": "3",
        "Mazda": "4",
        "Subaru": "7",
        "Suzuki": "9",
        "Mitsubishi": "6",
        "Daihatsu": "10",
        "Isuzu": "8",
        "Mitsuoka": "29",
        "Hino": "73",
        "Mercedes-Benz": "12",
        "BMW": "11",
        "Audi": "13",
        "Volkswagen": "14",
        "Porsche": "15",
        "Mini": "",
        "Chevrolet": "54",
        "Jeep": "",
        "Jaguar": "17",
        "Volvo": "24",
        "Peugeot": "23",
        "Alfa Romeo": "20",
    }

    body_types = {
        "Coupe": "2",
        "Wagon": "4",
        "Convertible": "7",
        "SUV/Pickup Truck": "6",
        "Sedan": "1",
        "Truck": "13",
    }

    def set_filter(self, filter):
        transmission_key = 'transmission'

        if transmission_key in self.form_names and self.code in self.form_names[transmission_key]:
            name = self.form_names[transmission_key][self.code]
            transmission_value = filter[transmission_key] if transmission_key in filter else ""
            value = "m0" if transmission_value == "MT" else ""
        setattr(self, transmission_key, Field(transmission_key, name, value))

        return False


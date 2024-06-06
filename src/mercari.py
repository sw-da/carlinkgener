from src.website import Website
from src.field import Field

class Mercari(Website):
    code = "mercari"
    name = "jp.mercari.com"
    url = "https://jp.mercari.com/search"
    template = "mercari"
    sort_name = "sort"
    sort_value = "created_time"

    makers = {
        "Lexus": "4247",
        "Toyota": "4241",
        "Nissan": "4242",
        "Honda": "4143",
        "Mazda": "4243",
        "Subaru": "4246",
        "Suzuki": "4144",
        "Mitsubishi": "4245",
        "Daihatsu": "4244",
        "Isuzu": "4249",
        "Mitsuoka": "4248",
        "Hino": "",
        "Mercedes-Benz": "4253",
        "BMW": "4147",
        "Audi": "4250",
        "Volkswagen": "4251",
        "Porsche": "4252",
        "Mini": "4259",
        "Chevrolet": "3390",
        "Jeep": "",
        "Jaguar": "4256",
        "Volvo": "4262",
        "Peugeot": "4261",
        "Alfa Romeo": "4260",
    }
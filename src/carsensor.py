from src.website import Website

class Carsensor(Website):
    code = "carsensor"
    name = "www.carsensor.net"
    url = "https://www.carsensor.net/usedcar/search.php"
    sort_name = "SORT"
    sort_value = "19"

    makers = {
        "Lexus": "LE",
        "Toyota": "TO",
        "Nissan": "NI",
        "Honda": "HO",
        "Mazda": "MA",
        "Subaru": "SB",
        "Suzuki": "SZ",
        "Mitsubishi": "MI",
        "Daihatsu": "DA",
        "Isuzu": "IS",
        "Mitsuoka": "MT",
        "Hino": "HI",
        "Mercedes-Benz": "ME",
        "BMW": "BM",
        "Audi": "AD",
        "Volkswagen": "VW",
        "Porsche": "PO",
        "Mini": "MN",
        "Chevrolet": "CH",
        "Jeep": "JE",
        "Jaguar": "JA",
        "Volvo": "VO",
        "Peugeot": "PE",
        "Alfa Romeo": "AF",
    }

    body_types = {
        "Coupe": "C",
        "Wagon": "W",
        "Convertible": "O",
        "SUV/Pickup Truck": "X*P",
        "Sedan": "S",
        "Truck": "T",
    }

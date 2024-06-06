from src.website import Website
from src.field import Field

class Yahoo(Website):
    code = "yahoo"
    name = "auctions.yahoo.co.jp"
    url = "https://auctions.yahoo.co.jp/category/list/26360/"
    sort_name = "select"
    sort_value = "22"

    makers = {
        "Lexus": "11968",
        "Toyota": "32298",
        "Nissan": "20143",
        "Honda": "7099",
        "Mazda": "12673",
        "Subaru": "27864",
        "Suzuki": "30225",
        "Mitsubishi": "16458",
        "Daihatsu": "3854",
        "Isuzu": "10868",
        "Mitsuoka": "19892",
        "Hino": "44128",
        "Mercedes-Benz": "14945",
        "BMW": "1376",
        "Audi": "457",
        "Volkswagen": "42319",
        "Porsche": "26373",
        "Mini": "16233",
        "Chevrolet": "3236",
        "Jeep": "44128",
        "Jaguar": "11070",
        "Volvo": "42776",
        "Peugeot": "25975",
        "Alfa Romeo": "1",
    }

    body_types = {
        "Coupe": "C_181:14781",
        "Wagon": "C_181:14782",
        "Convertible": "C_181:14784",
        "SUV/Pickup Truck": "C_181:14785",
        "Sedan": "C_181:14779",
        # "Truck": "T",
    }

    def set_filter(self, filter):
        maker_key = 'maker'
        body_type_key = 'body_type'
        year_key = 'year'
        transmission_key = 'transmission'

        body_type_value = self.handle(body_type_key, filter[body_type_key]) if body_type_key in filter else ""
        if body_type_value != "":
            body_type_name = self.form_names[body_type_key][self.code] if body_type_key in self.form_names and self.code in self.form_names[body_type_key] else body_type_key
            
            year_value = filter[year_key] if year_key in filter else ""
            if year_value:
                body_type_value += "/N_241:[" + year_value + "0101,]"
            
            transmission_value = filter[transmission_key] if transmission_key in filter else ""
            if transmission_value == "MT":
                body_type_value += "/C_4:91,917,5379"
            setattr(self, body_type_key, Field(body_type_key, body_type_name, body_type_value))

        
        maker_name = self.form_names[maker_key][self.code] if maker_key in self.form_names and self.code in self.form_names[maker_key] else maker_key
        maker_value = self.handle(maker_key, filter[maker_key]) if maker_key in filter else ""
        setattr(self, maker_key, Field(maker_key, maker_name, maker_value))
        return True

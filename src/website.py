from src.field import Field
import json

class Website:
    code = "website_undefined"
    name = "Undefined website"
    url = "/website_undefined"
    template = "website"
    is_post = False

    makers = {}
    body_types = {}
    
    form_names = {
        'maker': {'goonet': 'maker', 'carsensor': 'BRDC', 'kurumaerabi': 'cmi', 'yahoo': 'brand_id', 'mercari': 'brand_id'},
        'transmission': {'goonet': 'mission', 'carsensor': 'SLST', 'kurumaerabi': 'mi'},
        'year': {'goonet': 'syear1', 'carsensor': 'YMIN', 'kurumaerabi': 'frds'},
        'body_type': {'goonet': 'body', 'carsensor': 'BT', 'kurumaerabi': 'cbi', 'yahoo': 'spec'},
    }

    def set_filter(self, filter):
        return False

    def __init__(self, filter):
        pass_filter = self.set_filter(filter)
        if not pass_filter:
            for key in ['maker', 'transmission', 'year', 'body_type']:
                is_already_set = (getattr(self, key) if hasattr(self, key) else "") or ""
                if is_already_set == "" and key in self.form_names and self.code in self.form_names[key]:
                    name = self.form_names[key][self.code]
                    value = self.handle(key, filter[key]) if key in filter else ""
                    setattr(self, key, Field(key, name, value))

    def handle(self, key, value):
        if key == 'maker':
            return self.makers[value] if value in self.makers else ""
        elif key == 'body_type':
            return self.body_types[value] if value in self.body_types else ""
        return value
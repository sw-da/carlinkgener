from src.goonet import Goonet
from src.carsensor import Carsensor
from src.kurumaerabi import Kurumaerabi
from src.yahoo import Yahoo
from src.mercari import Mercari

class Generator:
    filter = None

    def __init__(self, filter):
        self.filter = filter

    def goonet(self):
        return Goonet(self.filter)

    def carsensor(self):
        return Carsensor(self.filter)

    def kurumaerabi(self):
        return Kurumaerabi(self.filter)

    def yahoo(self):
        return Yahoo(self.filter)

    def mercari(self):
        return Mercari(self.filter)
    
    def create_all_links(self):
        websites = []
        websites.append(self.goonet())
        websites.append(self.carsensor())
        websites.append(self.kurumaerabi())
        websites.append(self.yahoo())
        websites.append(self.mercari())
        return websites

class Medicine:
    ''' Class to rep each object of medicine '''
    def __init__(self,name,brand,stock,rate_tab,rate_strip,tabs_per_strip):
        self.name = name
        self.brand = brand
        self.stock = int(stock)
        self.rate_tab = float(rate_tab)
        self.rate_strip = float(rate_strip)
        self.tabs_per_strip = int(tabs_per_strip)

    def __str__(self):
        '''to string method'''
        return f"{self.name},{self.brand},{self.stock},{self.rate_tab},{self.rate_strip},{self.tabs_per_strip}"

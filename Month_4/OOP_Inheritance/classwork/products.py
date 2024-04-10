class Meva:
    def __init__(self):
        self.price = None
        self.nomi = None
        self.count = None
    
    def set_info(self,price,nomi,count):
        self.price = price
        self.nomi = nomi
        self.count = count
    
    def get_total_price(self):
        S = self.price * self.count
        return S
    
class Kiyim:
    def __init__(self):
        self.brand_name = None
        self.optom_narxi = None
        self.sotilish_narxi = None
        self.count = None
    
    def set_info(self,brand_name,optom_narxi,sotilish_narxi,count):
        self.brand_name = brand_name
        self.optom_narxi = optom_narxi
        self.sotilish_narxi = sotilish_narxi
        self.count = count
    
    def get_total_price(self):
        S = (self.sotilish_narxi - self.optom_narxi) * self.count
        return S

meva = Meva()
meva.set_info(22000,"Banan",5)

kiyim = Kiyim()
kiyim.set_info("Finka",10000,20000,3)

products = [meva,kiyim]

for x in products:
    print("Umumiy narxi : ",x.get_total_price())
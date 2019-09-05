from pkg.parent_hh import car

class bus(car) :
    def __init__(self, a):
        self.bus_name = a
        bus_price = 15000


b1 = bus("버스1")

b2 = bus("버스2")

# print(b1.bus_price)

#
# car.add()

print(__name__)

print("*"*100)

print(b1.print_main_name())
# 결과값이 왜
# pkg.parent_hh
# None
# 로 나오는지.
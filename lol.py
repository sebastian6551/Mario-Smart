from operator import attrgetter


class Siuu:
    def __init__(self, i):
        self.__lol = i

    def getNum(self):
        return self.__lol


li = [Siuu(3), Siuu(1), Siuu(1)]

min_num = min(li, key=lambda x: x.getNum())
print(min_num.getNum())
li.remove(min_num)
print(li)
for i in li:
    print(i.getNum())

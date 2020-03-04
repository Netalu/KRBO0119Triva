class City():
    
    def __init__(self, name, days, old, kid, money_per_day, price):
        print("Выберите город:\n•Мадрид\n•Париж\n•Берлин\n•Варшава\n•Минск\nдля выхода напишите выход\n")
        self.name = input()
        if self.name == "выход":
            exit()
        self.days = int(input("Введите количество дней поездки: "))
        self.old = int(input("Введите количество взрослых: "))
        self.kid = int(input("Введите количество детей: "))
        self.money_per_day = int(input("Введите количество денег, которые вы готовы потратить в день(руб): "))
        self.price = 0


def parse_param():
    while True:
        if city1.days < 1 or city1.days > 20:
            print("Введите верное количестно дней поездки(от 1 до 20)\n")
            city1.days = int(input())
        elif city1.old < 1 or city1.kid > 10:
            print("Введите верное количестно взрослых (от 1 до 10)\n")
            city1.old = int(input())
        elif city1.kid < 0 or city1.kid > 10:
            print("Введите верное количестно детей(от 0 до 10)\n")
            city1.kid = int(input())
        elif city1.money_per_day < 100 or city1.money_per_day > 10000:
            print("Введите верное количестно денег, которые вы готовы потратить в день(от 100руб до 10000руб)\n")
            city1.money_per_day = int(input())
        else:
            break

def check_city():
    if city1.name == "Мадрид":
        madrid()
    elif city1.name == "Париж":
        paris()
    elif city1.name == "Берлин":
        berlin()
    elif city1.name == "Варшава":
        warsaw()
    elif city1.name == "Минск":
        minsk()

def madrid():
    city1.price = 1

def paris():
    city1.price = 2

def berlin():
    city1.price = 3

def warsaw():
    city1.price = 4

def minsk():
    city1.price = 5



while True:
    city1 = City(0, 0, 0, 0, 0, 0)
    parse_param()
    check_city()
    print(city1.price)

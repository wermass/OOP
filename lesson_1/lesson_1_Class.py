"Объект - единица информации в памяти"
"Экземпляр - конкретный объект какого-то класса"
"Класс - инструкция по созданию объектов определенного типа"
"Метод - функция в классе для воздействия на объект"
"Поля и Свойства - переменные в классе"
"Атрибуты - все имена в классе: переменных и методов"


class Purse:
    def __init__(self, valuta, name='Unkown'):
        if valuta not in('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany

    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            print('Недостаточно средств')
            raise ValueError ('Недостаточно средств')
        self.__money = self.__money - howmany
        return howmany

    def info(self):
        print(self.__money)

    def __del__(self):
        print('Кошелек удален')


x = Purse('USD')
y = Purse('USD', 'Bill')
y.top_up_balance(10)
x.top_up_balance(y.top_down_balance(7))
x.info()
y.info()

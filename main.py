# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Calculadora():
    _portion1 = 0
    _portion2 = 0
    _scraps = 0
    _result = 0

    def portion1(self):
        return self._portion1

    def portion1(self, portion):
        try:
            portion = int(portion)
        except:
            print('valor incorreto')
            return False
        else:
            self._portion1 = portion
            return True

    def portion2(self):
        return self._portion2

    def portion2(self, portion):
        try:
            portion = int(portion)
        except:
            pass
        else:
            self._portion2 = portion


class Viewer():
    def __init__(self):
        self.counter = int
        self.home()
        self.loop()

    def loop(self):
        self.counter = 1
        while self.counter > 0:
            print('Deu certo')
            self.menu()
            self.counter = 0

    def home(self):
        print('CalculadoraPy Janaina Lessa')

    def menu(self):
        print('Menu de Operações')
        print('Escolha as seguintes opções. ')
        print('1 -> Somar')
        print('2 -> Subtrair')
        print('3 -> Multiplicar')
        print('4 -> Divisão')
        print('5 -> Função exponencial')
        print('0 -> Sair')
        control = int(input('>>>'))
        if control == 1:
            calc = Calculadora()
            calc.portion1(input('Entre com primeiro valor:\n>>>'))
            calc.portion2(input('Entre com segundo valor:\n>>>'))
            print(calc.sum())

        elif control == 2:
            pass
        elif control == 3:
            pass
        elif control == 4:
            pass
        elif control == 5:
            pass
        elif control == 0:
            pass
        else:
            self.counter = 0

    def menu_division(self):
        print('Menu de Divisão')
        print('Escolha as seguintes opções. ')
        print('1 -> Somar')
        print('2 -> Subtrair')
        int(input('>>>'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screen = Viewer()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class calculadora():
    def __init__(self):
        self.portion1 = int()
        self.portion2 = int()
        self.scraps = float()
        self.result = float()

    def get_portion1(self):
        return self.portion1

    def get_portion1(self):
        return self.portion2

    def get_scraps(self):
        return self.scraps

    def get_result(self):
        return self.result

    def set_portion1(self, portion1):
        try:
            portion1 = int(portion1)
        except ValueError:
            return False;
        else:
            self.portion1 = portion1
            return True

    def set_portion1(self, portion2):
        try:
            portion2 = int(portion2)
        except ValueError:
            return False
        else:
            self.portion1 = portion2
            return True

    def set_scraps(self, scraps):
        self.scraps = scraps

    def set_total(self, result):
        self.result = result

    def sum(self):
        self.result = self.portion1 + self.portion2

    def subtraction(self):
        self.result = self.portion1 - self.portion2

    def multiplication(self):
        self.result = self.portion1 * self.portion2

    def division(self):
        self.result = self.portion1 / self.portion2

    def scraps(self):
        self.scraps = self.portion1 % self.portion2


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
        int(input('>>>'))

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

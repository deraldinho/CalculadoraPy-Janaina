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
        except ValueError:
            pass
        else:
            self._portion2 = portion

    def sum(self):
        self._result = self._portion1 + self._portion2
        return self._result

    def sum(self, portion1, portion2):
        self.portion1(portion1)
        self.portion2(portion2)
        self._result = self._portion1 + self._portion2
        return self._result

    def subtraction(self):
        self._result = self._portion1 - self._portion2
        return self._result

    def subtraction(self, portion1, portion2):
        self.portion1(portion1)
        self.portion2(portion2)
        self._result = self._portion1 - self._portion2
        return self._result

    def multiplication(self):
        self._result = self._portion1 * self._portion2
        return self._result

    def multiplication(self, portion1, portion2):
        self.portion1(portion1)
        self.portion2(portion2)
        self._result = self._portion1 * self._portion2
        return self._result

    def division(self):
        try:
            self._result = self._portion1 / self._portion2
            if self._result < 1:
                self._scraps = 0
                return self._result, self._scraps
            self._scraps = self._portion1 % self._portion2
            return self._result, self._scraps
        except:
            pass
        else:
            print('ok')

    def division(self, portion1, portion2):
        self.portion1(portion1)
        self.portion2(portion2)
        try:
            self._result = self._portion1 / self._portion2
            if self._result < 1:
                self._scraps = 0
                return self._result, self._scraps
            self._scraps = self._portion1 % self._portion2
            return self._result, self._scraps
        except:
            pass
        else:
            print('ok')

class Viewer():
    def __init__(self):
        self._counter = 0
        self.home()
        self.loop()

    def loop(self):
        self._counter = 1
        while self._counter > 0:
            self.menu()

    def home(self):
        self.Tittle('CalculadoraPy Janaina Lessa', 30)

    def menu(self):
        self.Tittle('Menu de Operações')
        print('Escolha as seguintes opções.')
        print('1 -> Somar')
        print('2 -> Subtrair')
        print('3 -> Multiplicar')
        print('4 -> Divisão')
        print('5 -> Função exponencial')
        print('0 -> Sair')
        control = input('>>>')
        if not control.isnumeric():
            print("Digite apenas numeros!")
        else:
            control = int(control)
            if control == 1:
                calc = Calculadora()
                result = calc.sum(input('Entre com primeiro valor:\n>>>'), input('Entre com segundo valor:\n>>>'))
                print('Resultado:', result)
            elif control == 2:
                calc = Calculadora()
                result = calc.subtraction(input('Entre com primeiro valor:\n>>>'), input('Entre com segundo valor:\n>>>'))
                print('Resultado:', result)
            elif control == 3:
                calc = Calculadora()
                result = calc.multiplication(input('Entre com primeiro valor:\n>>>'),
                                             input('Entre com segundo valor:\n>>>'))
                print('Resultado:', result)
            elif control == 4:
                calc = Calculadora()
                result = calc.division(input('Entre com primeiro valor:\n>>>'), input('Entre com segundo valor:\n>>>'))
                print('Resultado:', result[0], ' Sobras:', result[1])
            elif control == 5:
                calc = Calculadora()
                print(calc.sum(input('Entre com primeiro valor:\n>>>'), input('Entre com segundo valor:\n>>>')))
            elif control == 0:
                self._counter = 0
            else:
                print('opção invalida')

    def Tittle(self, texto, size=25):
        for i in range(size):
            print('-', end='')
        print(texto, end='')
        for i in range(size):
            print('-', end='')
        print('')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screen = Viewer()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

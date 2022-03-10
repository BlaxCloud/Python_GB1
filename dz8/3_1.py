class NumberTakeExeption(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(f'{self.number} не являеются числом')

class NumberTake:
    NewList: list

    def __init__(self):
        self.NewList = []

    def operation(self):
        while True:
            ch = input('Осуществите ввод>>> ')
            if ch.isdigit():
                self.NewList.append(ch)
                print(f'Список на данный момент:{self.NewList}')
            else:
                if ch == 'Q':
                    print('Exit')
                    exit()
                else:
                    raise NumberTakeExeption(ch)

                   # print(str(1f'На вход поступило отличное от цифры значение'))

                # raise NumberTake(ch)
                # if ch == 'Q' or ch == 'q':
                #     return str(f'Выход из программы')
                # else:
                #     self.NewList.append(ch)
                #     print(f'Список на данный момент:{self.NewList}')



try_ex = NumberTake()
print(try_ex.operation())





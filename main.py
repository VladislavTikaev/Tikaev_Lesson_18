# Создайте класс BankAccount, который представляет банковский счет. У класса есть приватные свойства __account_number (номер счета) и __balance (баланс). Инициализатор __init__ используется для инициализации номера счета и начального баланса.
class BankAccount:
    def __init__(self, ac_number, bal):
        self.__account_number = ac_number
        self.__balance = bal
# Методы get_account_number и get_balance предоставляют доступ к приватным свойствам __account_number и __balance соответственно. Методы deposit и withdraw позволяют пополнять и снимать деньги со счета, при этом проверяя валидность операции (достаточно ли средств, корректно ли введена сумма для снятия).
    def get_account_number(self):
        print(f'Номер аккаунта: {self.__account_number}')
    def get_balance(self):
        print(f'Ваш баланс: {self.__balance}')
    def deposit(self, money):
        if (type(money) == int or type(money) == float) and money>0:
            self.__balance += money
            print(f'Успешно пополнили {money} рублей')
    def withdraw(self, money):
        if (type(money) == int or type(money) == float) and money>0 and self.__balance>=money:
            self.__balance -= money
            print(f'Успешно сняли {money} рублей')
# В основной части кода мы создаем экземпляр класса BankAccount с номером счета "123456789" и начальным балансом 1000. Затем мы используем методы для получения номера счета и баланса, а также для пополнения и снятия средств. Выводятся результаты операций.
my_deposit = BankAccount(123456789, 1000)
my_deposit.get_account_number()
my_deposit.get_balance()
my_deposit.deposit(1000)
my_deposit.get_balance()
my_deposit.withdraw(2000)
my_deposit.get_balance()
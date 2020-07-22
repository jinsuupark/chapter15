class Account:
    def __init__(self,balance): # 생성자 함수
        self.balance = balance

    def deposit(self,money):
        self.balance += money

    def inquire(self):
        print(f"잔액은 {self.balance} 입니다.")


account = Account(6000) #Account 의 인스턴스 생성
account.deposit(1000)
account.inquire()

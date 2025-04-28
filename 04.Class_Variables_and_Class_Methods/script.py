class Bank:
    bank_name = "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank: {Bank.bank_name}")

acc1 = Bank("Hurmat")
acc2 = Bank("Areeba")

acc1.show_info()
acc2.show_info()

print("Changing bank name...")

Bank.change_bank_name("Gleam & Glitz Bank")

acc1.show_info()
acc2.show_info()

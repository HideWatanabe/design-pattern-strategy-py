import types

class Strategy:
    def __init__(self, func = None):
        self.action = "Transação de cartão recebida!"
        if func is not None:
            self.execute = types.MethodType(func,self)

    def execute(self):
        print(self.action)

class BrandsStrategy:
    def visa_transaction(self):
        print(f"{self.action} Enviando requisição para a Visa")

    def mastercard_transaction(self):
        print(f"{self.action} Enviando requisição para a Mastercard")


if __name__ == "__main__":
    strategy = Strategy()
    visa_strategy = Strategy(BrandsStrategy.visa_transaction)
    master_strategy = Strategy(BrandsStrategy.mastercard_transaction)

    strategy.execute()
    visa_strategy.execute()
    master_strategy.execute()
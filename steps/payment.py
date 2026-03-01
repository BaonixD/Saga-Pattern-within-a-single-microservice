import random

class PaymentStep:

    def do(self, order_id: str, amount: float) -> dict:

        print( f"[Payment] Списываем ${amount}  за заказ {order_id} ")

        # симулируем банк,  иногда платеж может отклониться
        if random.random() < 0.2:
            raise Exception ( "платеж отклонен" )

        print( f"[Payment] Платёж прошёл успешно" )
        return {"status": "charged", "order_id": order_id, "amount": amount}

    def compensate(self, order_id: str, amount: float):
        # Возвращаем деньги клиенту (откат)
        print(f"[Payment] Возвращаем деньги ${amount} за заказ {order_id}")
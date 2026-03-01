import random

class ShippingStep:

    def do(self, order_id: str, user_id: str) -> dict:
        print ( f"[Shipping] создали доставку для пользователя" )


    # симуляция курьерской службы,  в реальном проекте здесь был бы запрос к службе доставки
        if random.random() < 0.2:
            print( "Нет свободных курьеров" )

        print( f"[Shipping] Курьер назначен доставка едет" )
        return {"status": "shipped", "order_id": order_id, "user_id": user_id}

    def compensate(self, order_id: str, user_id: str):
        # Вызывается автоматически если что-то упало после создания доставки
        print(f"[Shipping] Отменяем доставку для заказа {order_id}")
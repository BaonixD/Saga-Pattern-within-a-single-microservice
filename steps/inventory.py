import random

class InventoryStep:

    def do(self, order_id: str, product_id: str, quantity: int) -> dict:
        print ( f"[Inventory] резервируем {quantity} штук товара. {product_id}" )


        # что то вроде склада, иногда в скаладе не может быть товара. В продакшне тут был бы запрос к БД
        if random.random() < 0.2:
            raise Exception ( f"товар {product_id} закончился на складе " )

        print ( f"[Inventory] товар успешно взялся" )
        return {"status": "reserved", "order_id": order_id, "product_id": product_id, "quantity": quantity}

    def compensate(self, order_id: str, product_id: str, quantity: int):
        # Вызывается автоматически если упал следующий шаг (Shipping)
        # Снимаем резерв — товар снова доступен для других покупателей
        print(f"[Inventory] Снимаем резерв {quantity} штук товара {product_id}")


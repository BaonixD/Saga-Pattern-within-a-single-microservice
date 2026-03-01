from steps.payment import PaymentStep
from steps.inventory import InventoryStep
from steps.shipping import ShippingStep

class CheckOutSaga:

    def __init__(self):
        self.payment = PaymentStep()
        self.inventory = InventoryStep()
        self.shipping = ShippingStep()

    def execute(self, order_id: str, user_id: str, amount: float, product_id: str, quantity: int) -> dict:
        completed_steps = []

        try:
            # Шаг 1 — Payment
            payment_result = self.payment.do(order_id, amount)
            completed_steps.append("payment")

            # Шаг 2 — Inventory
            inventory_result = self.inventory.do(order_id, product_id, quantity)
            completed_steps.append("inventory")

            # Шаг 3 — Shipping
            shipping_result = self.shipping.do(order_id, user_id)
            completed_steps.append("shipping")

            # Все шаги прошли успешно
            return {
                "status": "SUCCESS",
                "order_id": order_id,
                "payment": payment_result,
                "inventory": inventory_result,
                "shipping": shipping_result
            }

        except Exception as e:
            print(f"\n[Saga] FAILED at step. Starting compensation...")
            print(f"[Saga] Error: {str(e)}")
            print(f"[Saga] Completed steps to rollback: {completed_steps}")

            # Откатываем в обратном порядке
            for step in reversed(completed_steps):
                if step == "payment":
                    self.payment.compensate(order_id, amount)
                elif step == "inventory":
                    self.inventory.compensate(order_id, product_id, quantity)
                elif step == "shipping":
                    self.shipping.compensate(order_id, user_id)
            return {
                "status": "FAILED",
                "order_id": order_id,
                "error": str(e),
                "compensated_steps": list(reversed(completed_steps))
            }
from pydantic import BaseModel

class CheckoutRequest(BaseModel):
    order_id: str
    user_id: str
    amount: float
    product_id: str
    quantity: int
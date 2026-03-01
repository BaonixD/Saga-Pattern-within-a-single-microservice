from fastapi import FastAPI
from models import CheckoutRequest
from saga import CheckOutSaga


app = FastAPI(title="Saga Pattern - Checkout")

@app.get("/")
def root():
    return {"message": "Saga Pattern API is running"}

@app.post("/checkout")
def checkout(request: CheckoutRequest):
    saga = CheckOutSaga()
    result = saga.execute(
        order_id=request.order_id,
        user_id=request.user_id,
        amount=request.amount,
        product_id=request.product_id,
        quantity=request.quantity
    )
    return result
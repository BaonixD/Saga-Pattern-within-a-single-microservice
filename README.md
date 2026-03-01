# Saga Pattern — E-Commerce Checkout

Implementation of the Saga Pattern within a single microservice using FastAPI.

## What is Saga Pattern?

Saga is a pattern for managing transactions across multiple steps. If any step fails, all previously completed steps are automatically rolled back using compensating transactions.

## How it works
```
POST /checkout
      │
      ▼
1. Payment.do()        → charge the card
      │
      ▼
2. Inventory.do()      → reserve the product
      │
      ▼
3. Shipping.do()       → assign a courier
      │
      ▼
   SUCCESS ✅

If any step fails → compensate in reverse order:
   Shipping fails  → Inventory.compensate() → Payment.compensate()
   Inventory fails → Payment.compensate()
```

## Project Structure
```
Saga Pattern/
├── main.py          # FastAPI app and endpoints
├── saga.py          # Saga orchestrator (manages steps and rollback)
├── models.py        # Request/Response models
├── requirements.txt
└── steps/
    ├── payment.py   # Charge card / Refund
    ├── inventory.py # Reserve product / Release
    └── shipping.py  # Assign courier / Cancel
```

## Steps

Each step has two methods:
- `do()` — executes the action
- `compensate()` — rolls back the action if a later step fails

| Step | do() | compensate() |
|------|------|--------------|
| Payment | Charge the card | Refund the money |
| Inventory | Reserve the product | Release the reservation |
| Shipping | Assign a courier | Cancel the delivery |

## How to run
```bash
# Clone the repo
git clone https://github.com/BaonixD/Saga-Pattern-within-a-single-microservice.git
cd Saga-Pattern-within-a-single-microservice

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

Open **http://127.0.0.1:8000/docs** to test via Swagger UI.

## Example

**SUCCESS response:**
```json
{
  "status": "SUCCESS",
  "order_id": "order_001",
  "payment": { "status": "charged", "amount": 49.99 },
  "inventory": { "status": "reserved", "quantity": 1 },
  "shipping": { "status": "shipped" }
}
```

**FAILED response (with compensation):**
```json
{
  "status": "FAILED",
  "order_id": "order_002",
  "error": "Товар macbook_pro закончился на складе",
  "compensated_steps": ["payment"]
}
```

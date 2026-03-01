# Saga Pattern — Checkout Workflow

This project implements the Saga Pattern inside a single FastAPI microservice. 
The idea is simple — if something breaks during checkout, everything that 
already happened gets rolled back automatically.

## Why Saga?

Normal transactions work fine in one database. But when you have multiple 
steps that can fail independently, you need a way to undo what already 
happened. That's what Saga does.

## Checkout flow

There are 3 steps — Payment, Inventory, Shipping. Each step knows how to 
do its job and how to undo it if something goes wrong later.

If Inventory fails after Payment already went through — the money gets 
refunded automatically. If Shipping fails — inventory reservation gets 
released and money gets refunded. All in reverse order.

## Project structure
```
├── main.py        # entry point, single /checkout endpoint
├── saga.py        # orchestrator, runs steps and handles rollback
├── models.py      # checkout request model
└── steps/
    ├── payment.py    # charge / refund
    ├── inventory.py  # reserve / release
    └── shipping.py   # assign courier / cancel
```

## Running locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/docs and try the /checkout endpoint. 
Each step has a 20% chance to fail so just hit Execute a few times 
and you'll see both success and compensation in action.

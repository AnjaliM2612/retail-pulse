import json
import random
from datetime import datetime
import os

print("Retail Pulse Producer Started - Free Tier Version")

def create_sample_event():
    products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Chair"]
    return {
        "event_id": f"evt_{random.randint(10000,99999)}",
        "event_type": random.choice(["view", "add_to_cart", "purchase"]),
        "product": random.choice(products),
        "customer_id": random.randint(1000, 9999),
        "price": round(random.uniform(10, 1000), 2),
        "event_time": datetime.now().isoformat(),
        "is_late": random.random() < 0.05
    }

os.makedirs("producer/data", exist_ok=True)

for i in range(10):
    event = create_sample_event()
    file_path = f"producer/data/event_{i}.json"
    with open(file_path, 'w') as f:
        json.dump(event, f)
    print(f"Created: {file_path}")

print("Done! 10 events created")
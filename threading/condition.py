# Condition
#   Used for producer-consumer problems — one thread waits for a condition to be met, another notifies.
# ✅ Real-World Analogy:
#   A chef (producer) cooks only if there are empty plates. A waiter (consumer) serves only if food is ready.

import threading
import time

condition = threading.Condition()
item_available = False

def producer():
    global item_available
    time.sleep(2)
    with condition:
        item_available = True
        print("🥪 Item produced")
        condition.notify()

def consumer():
    with condition:
        print("👀 Waiting for item...")
        condition.wait()
        if item_available:
            print("🍽️ Item consumed")

threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()
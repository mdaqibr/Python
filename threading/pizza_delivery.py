import threading
import time

# Target function
def deliver_pizza(customer, size="medium"):
    print(f"🚴 Delivering a {size} pizza to {customer}")
    time.sleep(2)  # Simulate delivery time
    print(f"✅ Delivered to {customer}")

# Create threads with args and kwargs
t1 = threading.Thread(target=deliver_pizza, args=("Aqib",), kwargs={"size": "large"})
t2 = threading.Thread(target=deliver_pizza, args=("Ravi",))
t3 = threading.Thread(target=deliver_pizza, args=("Yashwnt",), kwargs={"size": "small"})

# Start all threads
t1.start()
print(t1.is_alive())
t2.start()
t3.start()

# Wait until all deliveries are done
t1.join()
t2.join()
t3.join()
print(t1.is_alive())
print("🍕 All deliveries completed!")
import threading

item_available = False

def consumer():
    if not item_available:
        print("❌ Nothing to consume, but no wait mechanism")
    else:
      print("Item is ready.")

def producer():
    global item_available
    item_available = True
    print("✅ Item produced")

threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()
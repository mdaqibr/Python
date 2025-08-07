# Event
#   An Event is used to signal threads to start, stop, or wait.
# ✅ Real-World Analogy:
#   Race starts only when flag is raised. All runners (threads) wait for the flag (event.set()).

import threading
import time

event = threading.Event()

def wait_for_signal():
    print("⏱️ Waiting for signal...")
    event.wait()
    print("🏃 Signal received! Thread running...")

threading.Thread(target=wait_for_signal).start()

time.sleep(3)
print("Providing signal...")
# event.set()  # Signals the thread

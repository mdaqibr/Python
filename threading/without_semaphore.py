# Without Semaphore: Overloading a Limited Resource
# Example: Only 3 database connections allowed, but 6 threads try at once.

import threading
import time

def db_query(user):
    print(f"{user} is querying database...")
    time.sleep(2)
    print(f"{user} done.")

for i in range(6):
    threading.Thread(target=db_query, args=(f"User-{i+1}",)).start()

# with semaphore ---------------------------------------------------
"""
sem = threading.Semaphore(3)

def db_query(user):
    with sem:
        print(f"{user} is querying database...")
        time.sleep(2)
        print(f"{user} done.")

for i in range(6):
    threading.Thread(target=db_query, args=(f"User-{i+1}",)).start()

"""
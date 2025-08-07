import threading

barrier = threading.Barrier(2)

def ready_player(n):
    print(f"🎮 Player {n} is ready")
    # It will wait for threads count defined in the barrier then it will proceed otherwise it will stuck.
    barrier.wait()
    print(f"🚀 Player {n} starts playing")

for i in range(6):
    threading.Thread(target=ready_player, args=(i+1,)).start()

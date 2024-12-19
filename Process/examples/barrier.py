import multiprocessing as mp
import time
import os


def run_target(wait_time: int, has_barrier: bool, barrier: mp.Barrier):
    time.sleep(wait_time)
    if has_barrier:
        barrier.wait()
    print(f'PID {os.getpid()} pass the barrier at {time.time()}')


# These three variables can be adjusted to see different bahaviors.
has_barrier = True
process_num = 5
parties = 5

barrier = mp.Barrier(parties)
processes = [mp.Process(target=run_target, args=(i, has_barrier, barrier)) 
             for i in range(process_num)]

for i in range(process_num):
    processes[i].start()

for i in range(process_num):
    processes[i].join()

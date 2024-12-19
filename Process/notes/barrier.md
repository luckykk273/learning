# Barrier
## What is barrier
From wiki,  
> In parallel computing, a barrier is a type of synchronization method. A barrier for a group of threads or processes in the source code means any thread/process must stop at this point and cannot proceed until all other threads/processes reach this barrier.

## Usage
Please refer to the [reference](#reference).

## When to use
Use the barrier when you want multiple processes to synchronize their execution at a specific point.  
**Common use cases for** `multiprocessing.Barrier`:  
1. **Coordinating Tasks**  
Use a barrier when you want multiple processes to perform tasks in phases, ensuring all processes complete one phase before moving to the next.
2. **Simulating Step-by-Step Systems**  
In simulations or computations that require synchronized progression across multiple processes.
3. **Parallel Algorithms**  
In parallel implementations of algorithms that require intermediate synchronization points.
4. **Coordination in Tests**      
When testing code, you might use a barrier to synchronize the start or progression of multiple processes to control timing and behavior.

## Description for the example
In the example, the target function is to wait for `wait_time` seconds and then print some messages.
We simply assign `wait_time` from 0 to (`process_num` - 1) seconds, so without the barrier, it is expected that the printing message displayed every 1-second interval.
```bash
$ python3 Process/examples/barrier.py
PID 449049 pass the barrier at 1734568209.1522014
PID 449050 pass the barrier at 1734568210.153451
PID 449051 pass the barrier at 1734568211.1548154
PID 449052 pass the barrier at 1734568212.1560242
PID 449053 pass the barrier at 1734568213.1573203
```

If `has_barrier` is set to `True`, the processes will wait each other until the number of parties for the barrier are reached; and then the timestamps to print message will be almost the same:
```bash
$ python Process/examples/barrier.py
PID 447796 pass the barrier at 1734567456.9425428
PID 447800 pass the barrier at 1734567456.942529
PID 447798 pass the barrier at 1734567456.9426644
PID 447799 pass the barrier at 1734567456.942783
PID 447797 pass the barrier at 1734567456.9428985
```

What will happen if we set the parties of the barrier less than `process_num`?  
e.g. parties of the barrier is 2 and `process_num` is 5:
```bash
$ python Process/examples/barrier.py 
PID 450064 pass the barrier at 1734568619.648575
PID 450063 pass the barrier at 1734568619.6486037
PID 450066 pass the barrier at 1734568621.651529
PID 450065 pass the barrier at 1734568621.6516266

``` 
We will see the printing message displayed every 2-second interval and the last process will always hang on **indefinitely** as it cannot wait another one process to help it reach the parties of the barrier.  

In practice, parameter `timeout` is provided in `Barrier.wait`. If `timeout` is set, the processes will wait until the number of parties reaches or until a timeout occurs. If the timeout occurs, the `BrokenBarrierError` will be raised. 

## Reference
1. [Python Docs - multiprocessing.Barrier](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Barrier)
2. [Python Docs - threading.Barrier](https://docs.python.org/3/library/threading.html#threading.Barrier)
3. [Wiki - Barrier (computer science)](https://en.wikipedia.org/wiki/Barrier_(computer_science))

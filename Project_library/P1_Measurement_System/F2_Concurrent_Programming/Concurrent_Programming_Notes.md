# Concurrent programming in Micropython

There are two main ways of doing concurrent programming in MPy: 1) Multi Threading, 2) Event Driven programming. These methods differ in their underlying mechanisms and how they handle concurrency. 

### Multithreading

Multithreading involves executing multiple threads concurrently, where each thread represents a separate sequence of execution within the program. 
Threads can run in parallel on multicore processors or concurrently on single-core processors through time slicing. 
By using Multi threading in MicroPython, it is possible to divide a program into smaller tasks that can run concurrently. 
For example tasks such as handling user input, performing background calculations, or communicating with external devices. 
Another example of the use of multi-threading is when an IoT device needs to acquire sensor data and publish it to a server. 
These two tasks can run concurrently. If done correctly (with good concurrency design), these threads run independently of each other and perform tasks simultaneously without blocking. 
Multithreading enables true parallelism and can be beneficial for computationally intensive tasks or scenarios where true parallel execution is required.


### Event driven programming

In event-driven programming, tasks are triggered by events or interrupts rather than being executed sequentially or concurrently. 
The program typically consists of an event loop that listens for events and dispatches tasks to handle them. 
Event-driven programming typically uses a single-threaded approach, where tasks are executed sequentially within the event loop. 
Tasks are executed cooperatively, with each task yielding control back to the event loop when waiting for I/O or other asynchronous operations. 
It is well-suited for applications that involve handling I/O-bound tasks or responding to external events quickly.

### Keywords and Terminology for concurrent programming

- Event driven programming
- Multi-threading
- Cooperative vs preemptive multithreading
- Coroutines, Lightweight threads
- Deadlocks
- Race conditions
- Asynchronous functions
- Locks
- Semaphores 
- Scheduling
- Concurrency Primitives
- Asynchronous I/O
- Queues
- Event loops, Event flags, Event Handlers, Event Emitters
- Awaitable Objects
- Shared resources
- Callbacks
- Design of concurrency model

***

### Functions and code snippets related to multithreading and event driven programming


|  Functions                         | Description |
| -------------                      | ------------- |
| asyc def function_name():          | Asynchronous function for non blocking code |
| await uasyncio.sleep(time1)        | Non-blocking sleep, allows event scheduler to run something else |
| loop = uasyncio.get_event_loop()   | Creates an event loop |
| loop.create_task(function1())      | Can create and schedule multiple tasks for multiple functions f1, f2...|
| lock = _thread.allocate_lock()     | Create a lock object|
| lock.acquire()                     | Method to acquire lock for threads | 
| lock.release()                     | Method to release lock for threads | 




#### Multithreading

| Function/Command                           | Description                                                      |
|--------------------------------            |------------------------------------------------------------------|
| `_thread.start_new_thread(func, args)`     | Start a new thread to execute the given function with arguments. |
| `_thread.allocate_lock()`                  | Create and return a new lock object for thread synchronization.  |
| `lock.acquire(blocking=True, timeout=-1)`  | Acquire the lock, optionally blocking or with a timeout.      |
| `lock.release()`                           | Release the lock, allowing other threads to acquire it.          |
| `_thread.get_ident()`                      | Return the identifier of the current thread.                     |
| `time.sleep(secs)`                         | Suspend execution of the current thread for the given number of seconds. |


***

#### Event Driven Programming

| Function/Command                          | Description                                                   |
|------------------------------------------|---------------------------------------------------------------|
| `uasyncio.get_event_loop()`              | Get the event loop instance for scheduling and running tasks. |
| `uasyncio.create_task(coroutine)`        | Create a task to execute the given coroutine asynchronously. |
| `uasyncio.sleep(seconds)`                | Suspend execution of the current task for the given duration. |
| `await coroutine`                        | Pause the execution of the current coroutine until the awaited coroutine completes. |
| `loop.run_forever()`                     | Run the event loop indefinitely, processing tasks and events. |
| `loop.run_until_complete(coroutine)`     | Run the event loop until the given coroutine completes.       |
| `asyncio.ensure_future(coroutine)`       | Create a Future object for the given coroutine.                |
| `asyncio.call_later(delay, callback)`    | Schedule a callback to be called after the specified delay.   |
| `loop.add_reader(fd, callback)`          | Register a callback to be called when data is available for reading from the given file descriptor. |
| `loop.remove_reader(fd)`                 | Remove the callback registered for the given file descriptor. |




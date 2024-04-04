# Concurrent programming in Micropython

There are two main ways of doing concurrent programming in MPy: 1) Multi Threading, 2) Event Driven programming. These methods differ in their underlying mechanisms and how they handle concurrency. 

### Keywords and Terminology for concurrent programming

- Event driven programming
- Multithreading
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

### Multithreading

Multi-threading is a programming technique where multiple threads of execution run concurrently within a single process.
Multithreading involves executing multiple threads concurrently, where each thread represents a separate sequence of execution within the program. 
Threads can run in parallel on multicore processors or concurrently on single-core processors through time slicing. 
By using Multi threading in MicroPython, it is possible to divide a program into smaller tasks that can run concurrently. 
For example tasks such as handling user input, performing background calculations, or communicating with external devices. 
Another example of the use of multi-threading is when an IoT device needs to acquire sensor data and publish it to a server. 
These two tasks can run concurrently. If done correctly (with good concurrency design), these threads run independently of each other and perform tasks simultaneously without blocking. 
Multithreading enables true parallelism and can be beneficial for computationally intensive tasks or scenarios where true parallel execution is required.


### Event driven programming

Event-driven programming is a paradigm where the flow of the program is determined by events such as user actions, sensor readings, or system notifications. 
In event-driven programming, programs consist of an event loop that continuously listens for events. 
Tasks are triggered by events or interrupts rather than being executed sequentially or concurrently. Tasks are executed cooperatively, with each task yielding control back to the event loop when waiting for I/O or other asynchronous operations. 
The program typically consists of an event loop that listens for events and dispatches tasks to handle them. 
Event-driven programming typically uses a single-threaded approach, where tasks are executed sequentially within the event loop. 
It is well-suited for applications that involve handling I/O-bound tasks or responding to external events quickly.

### Cooperative vs preemptive multithreading
Cooperative multithreading involves threads voluntarily yielding control to each other, whereas preemptive multithreading involves the operating system forcibly switching between threads. MicroPython primarily uses cooperative multithreading to simplify concurrency management and reduce overhead.

### Coroutines, Lightweight threads
Coroutines are special functions that can be paused and resumed during execution. They are lightweight and enable asynchronous programming by allowing tasks to execute concurrently without blocking the main program's execution.

### Deadlocks
Deadlocks occur when two or more threads are blocked indefinitely, waiting for each other to release resources they need. They can occur in concurrent programs when threads acquire locks or resources in a way that creates a circular dependency.

### Race conditions
Race conditions occur when the outcome of a program depends on the timing or interleaving of operations between multiple threads. They can lead to unpredictable behavior and data corruption when multiple threads access shared resources without proper synchronization.

### Asynchronous functions
Asynchronous functions are functions that can perform I/O operations or time-consuming tasks without blocking the execution of other tasks. They enable non-blocking I/O and improve responsiveness by allowing tasks to execute asynchronously.

### Locks
Locks are synchronization primitives used to control access to shared resources by multiple threads. They allow only one thread to access a resource at a time, preventing race conditions and ensuring data integrity.

### Semaphores
Semaphores are synchronization primitives that maintain a count of available resources. They allow multiple threads to access shared resources concurrently, up to a specified limit defined by the semaphore's count.

### Scheduling
Scheduling involves determining the order in which tasks or threads are executed. In concurrent programming, scheduling decisions impact performance, responsiveness, and resource utilization.

### Concurrency Primitives
Concurrency primitives are fundamental building blocks used to synchronize and coordinate the activities of concurrent tasks or threads. Examples include locks, semaphores, queues, and event flags.

### Asynchronous I/O
Asynchronous I/O enables non-blocking I/O operations by allowing tasks to perform I/O operations concurrently without waiting for each operation to complete sequentially.

### Queues
Queues are data structures used for inter-thread communication and synchronization. They allow tasks to communicate by passing messages or data between them in a thread-safe manner.

### Event loops, Event flags, Event Handlers, Event Emitters
Event loops manage the execution of tasks and event-driven programming. Event flags are synchronization primitives that allow tasks to wait for specific conditions or events to occur. Event handlers are functions or coroutines that process events asynchronously, and event emitters notify event handlers when events occur.

### Awaitable Objects
Awaitable objects are objects that can be awaited in asynchronous functions or coroutines. They include coroutines, Future objects, and other types that implement the `__await__()` method.

### Shared resources
Shared resources are data or hardware components accessed by multiple threads or tasks concurrently. Synchronizing access to shared resources is essential to prevent race conditions and ensure data integrity in concurrent programs.

### Callbacks
Callbacks are functions or coroutines registered to be called when specific events occur. They are commonly used in event-driven programming to handle asynchronous events such as sensor readings, user input, or network events.

### Design of concurrency model
The design of a concurrency model involves selecting appropriate concurrency primitives, synchronization mechanisms, and programming patterns to ensure correctness, efficiency, and scalability in concurrent programs. It requires careful consideration of factors such as task synchronization, resource management, and performance optimization.

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




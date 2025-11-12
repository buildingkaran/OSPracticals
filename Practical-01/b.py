import os

pid = os.fork()

if pid == 0:
    print(f"Child Process running code block | PID: {os.getpid()}")
    for i in range(5):
        print(f"Child counting: {i+1}")
else:
    print(f"Parent Process running code block | PID: {os.getpid()}")
    for i in range(3):
        print(f"Parent counting: {i+1}")

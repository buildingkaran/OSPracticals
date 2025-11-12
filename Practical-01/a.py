import os

pid = os.fork()

if pid == 0:
    print(f"Child Process | PID: {os.getpid()} | Parent PID: {os.getppid()}")
else:
    print(f"Parent Process | PID: {os.getpid()} | Child PID: {pid}")

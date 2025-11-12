import os
import time

pid = os.fork()

if pid == 0:
    print(f"Child Process started | PID: {os.getpid()}")
    time.sleep(2)
    print("Child Process finished work.")
else:
    print(f"Parent waiting for Child (PID: {pid}) to complete...")
    os.wait()
    print("Parent resumes after child completion.")

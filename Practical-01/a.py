# 🧠 OS Practical 1(a)
# Topic: Using fork() where parent and child execute the same code
# Author: Karan Kumar

import os

def main():
    print("\n--- Practical 1(a): Same Program, Same Code ---")
    pid = os.fork()  # Create a child process

    # Both parent and child execute this part
    print(f"Process ID: {os.getpid()}, Parent ID: {os.getppid()}")

if __name__ == "__main__":
    main()

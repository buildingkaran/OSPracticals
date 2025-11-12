import os

with open("/proc/meminfo") as f:
    lines = f.readlines()

total = int(lines[0].split()[1]) // 1024
free = int(lines[1].split()[1]) // 1024
used = total - free

print("Total Memory:", total, "MB")
print("Used Memory:", used, "MB")
print("Free Memory:", free, "MB")

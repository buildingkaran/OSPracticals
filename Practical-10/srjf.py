n = int(input("Enter number of processes: "))
bt = []
for i in range(n):
    bt.append(int(input(f"Enter burst time for P{i+1}: ")))

rt = bt.copy()
time = 0
complete = 0
small = 0
minm = 99999
finish_time = 0
wt = [0] * n

while complete != n:
    for j in range(n):
        if rt[j] < minm and rt[j] > 0:
            minm = rt[j]
            small = j
    rt[small] -= 1
    minm = rt[small]
    if minm == 0:
        minm = 99999
    if rt[small] == 0:
        complete += 1
        finish_time = time + 1
        wt[small] = finish_time - bt[small]
    time += 1

print("Process\tBurst Time\tWaiting Time")
for i in range(n):
    print(f"P{i+1}\t{bt[i]}\t\t{wt[i]}")

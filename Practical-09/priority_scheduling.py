n = int(input("Enter number of processes: "))
bt = []
pr = []

for i in range(n):
    bt.append(int(input(f"Enter burst time for process {i+1}: ")))
    pr.append(int(input(f"Enter priority for process {i+1}: ")))

processes = list(range(1, n + 1))

for i in range(n):
    for j in range(i + 1, n):
        if pr[i] > pr[j]:
            pr[i], pr[j] = pr[j], pr[i]
            bt[i], bt[j] = bt[j], bt[i]
            processes[i], processes[j] = processes[j], processes[i]

wt = [0] * n
tat = [0] * n

for i in range(1, n):
    wt[i] = wt[i - 1] + bt[i - 1]

for i in range(n):
    tat[i] = wt[i] + bt[i]

print("\nProcess\tPriority\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{processes[i]}\t{pr[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

avg_wt = sum(wt) / n
avg_tat = sum(tat) / n
print(f"\nAverage Waiting Time: {avg_wt}")
print(f"Average Turnaround Time: {avg_tat}")

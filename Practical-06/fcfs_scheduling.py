n = int(input("Enter number of processes: "))
bt = []
for i in range(n):
    bt.append(int(input(f"Enter burst time for process {i+1}: ")))

wt = [0] * n
tat = [0] * n

for i in range(1, n):
    wt[i] = wt[i-1] + bt[i-1]

for i in range(n):
    tat[i] = wt[i] + bt[i]

print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{i+1}\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

avg_wt = sum(wt) / n
avg_tat = sum(tat) / n
print(f"\nAverage Waiting Time: {avg_wt}")
print(f"Average Turnaround Time: {avg_tat}")

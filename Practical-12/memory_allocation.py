blocks = list(map(int, input("Enter block sizes: ").split()))
processes = list(map(int, input("Enter process sizes: ").split()))

def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    b = blocks[:]
    for i in range(len(processes)):
        for j in range(len(b)):
            if b[j] >= processes[i]:
                allocation[i] = j
                b[j] -= processes[i]
                break
    return allocation

def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    b = blocks[:]
    for i in range(len(processes)):
        best = -1
        for j in range(len(b)):
            if b[j] >= processes[i]:
                if best == -1 or b[j] < b[best]:
                    best = j
        if best != -1:
            allocation[i] = best
            b[best] -= processes[i]
    return allocation

def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    b = blocks[:]
    for i in range(len(processes)):
        worst = -1
        for j in range(len(b)):
            if b[j] >= processes[i]:
                if worst == -1 or b[j] > b[worst]:
                    worst = j
        if worst != -1:
            allocation[i] = worst
            b[worst] -= processes[i]
    return allocation

print("First Fit:", first_fit(blocks, processes))
print("Best Fit:", best_fit(blocks, processes))
print("Worst Fit:", worst_fit(blocks, processes))

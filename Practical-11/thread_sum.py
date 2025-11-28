import threading

numbers = []
n = int(input("Enter how many numbers: "))
for i in range(n):
    numbers.append(int(input()))

total = 0

def calc_sum():
    global total
    for x in numbers:
        total += x

t = threading.Thread(target=calc_sum)
t.start()
t.join()

print("Sum =", total)

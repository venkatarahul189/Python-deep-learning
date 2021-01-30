l1 = []
l2 = []
n = int(input("No. of students:"))
print("height in feet")
for i in range(0, n):
    meter = float(input())
    l1.append(meter)
print(l1)
for k in l1:
    centimeter = k * 30.48
    l2.append(centimeter)
print(l2)
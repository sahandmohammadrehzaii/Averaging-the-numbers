n = int(input("تعداد عدد ها = "))
s = 0.0
for i in range(1,n+1):
    x = float(input("عدد  ها " + str(i) + " = "))
    s += x
m = s / n
print("میانگین = ", m)
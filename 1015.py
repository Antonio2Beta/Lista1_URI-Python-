from math import sqrt as raiz

x1, y1 = input().split(" ")
x1 = float(x1)
y1 = float(y1)
x2, y2 = input().split(" ")
x2 = float(x2)
y2 = float(y2)

distance = raiz(((x2-x1)**2)+((y2-y1)**2))

print("{:.4f}".format(distance))

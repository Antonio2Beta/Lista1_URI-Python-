from math import sqrt as raiz

val = input().split(" ")
x1, y1 = val
x1 = float(x1)
y1 = float(y1)
val2 = input().split(" ")
x2, y2 = val2
x2 = float(x2)
y2 = float(y2)

distance = raiz(((x2-x1)**2)+((y2-y1)**2))

print("{:.4f}".format(distance))

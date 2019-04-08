a, b, c, d = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if b>c and d>a and (c+d)>(a+b) and (c,d>0) and (c,d==a):
  print('Valores aceitos')
else:
  print('Valores não aceitos')
  

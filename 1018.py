n = int(input())
if (0<n<1000000):
  
  notas100 = n//100
  resto100 = n%100
  
  notas50 = resto100//50
  resto50 = resto100%50
  
  notas20 = resto50//20
  resto20 = resto50%20
  
  notas10 = resto20//10
  resto10 = resto20%10
  
  notas5 = resto10//5
  resto5 = resto10%5
  
  notas2 = resto5//2
  resto2 = resto5%2
  
  notas1 = resto2//1
  
print(n)
print("{} nota(s) de R$ 100.00".format(notas100))
print("{} nota(s) de R$ 50.00".format(notas50))
print("{} nota(s) de R$ 20.00".format(notas20))
print("{} nota(s) de R$ 10.00".format(notas10))
print("{} nota(s) de R$ 5.00".format(notas5))
print("{} nota(s) de R$ 2.00".format(notas2))
print("{} nota(s) de R$ 1.00".format(notas1))





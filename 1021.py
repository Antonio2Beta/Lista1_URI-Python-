N = float(input())
if (N>=0) and (N<=1000000.00):

    notascem = N//100
    restocem = N%100

    notascin = restocem//50
    restocin = restocem%50

    notasvinte = restocin//20
    restovinte = restocin%20

    notasdez = restovinte//10
    restodez = restovinte%10

    notascinco = restodez//5
    restocinco = restodez%5

    notasdois = restocinco//2
    restodois = restocinco%2

    notasum = restodois//1
    restoum = restodois%1

    cincents = restoum//0.50
    restocincents = restoum%0.50

    vintecents = restocincents//0.25
    restovintecents = restocincents%0.25

    dezcents = restovintecents//0.10
    restodezcents = restovintecents%0.10

    cincocents = restodezcents//0.05
    restocincocents = restodezcents%0.05

    umcents = restocincocents/0.01

print("NOTAS:")
print("{:.0f} nota(s) de R$ 100.00".format(notascem))
print("{:.0f} nota(s) de R$ 50.00".format(notascin))
print("{:.0f} nota(s) de R$ 20.00".format(notasvinte))
print("{:.0f} nota(s) de R$ 10.00".format(notasdez))
print("{:.0f} nota(s) de R$ 5.00".format(notascinco))
print("{:.0f} nota(s) de R$ 2.00".format(notasdois))
print("MOEDAS:")
print("{:.0f} moeda(s) de R$ 1.00".format(notasum))
print("{:.0f} moeda(s) de R$ 0.50".format(cincents))
print("{:.0f} moeda(s) de R$ 0.25".format(vintecents))
print("{:.0f} moeda(s) de R$ 0.10".format(dezcents))
print("{:.0f} moeda(s) de R$ 0.05".format(cincocents))
print("{:.0f} moeda(s) de R$ 0.01".format(umcents))

dia = int(input()) 

ano = dia//365
resto = dia%365
mes = resto//30
dias = resto%30

print("{} ano(s)".format(ano))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dias))

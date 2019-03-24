segs = int(input())

hrs = segs//3600
segs_restantes = segs%3600
minutos = segs_restantes//60
segs_restantes_finais = segs_restantes%60

print("{}:{}:{}".format(hrs,minutos,segs_restantes_finais))

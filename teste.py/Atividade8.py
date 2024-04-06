seg_user = int(input("digite a quantidade de segundos: "))

seg = seg_user%60
minu = (seg_user//60)%60
hora = ((seg_user//60)/60)%24
dia = ((seg_user//60)/60)//4

print(f"{dia} dias - {hora:.2f}:{minu:.2f}:{seg:.2f}")
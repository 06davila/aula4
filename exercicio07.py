intervalo = 0
fora = 0
for i in range (10):
        n= int (input(" digite um numero"))
        if n >9 and n <21:
            intervalo+=1
        else:
            fora=fora+1
print(f"{intervalo} estao dentro e {fora} fora")
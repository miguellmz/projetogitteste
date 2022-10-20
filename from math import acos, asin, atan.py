from math import sin, cos, tan, radians 
angulo = float(input("insira o angulo que deseja: "))
seno =sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("""--------------\n{:.3f}\n{:.3f}\n{:.3f}\n--------------""".format(seno, cosseno , tangente))
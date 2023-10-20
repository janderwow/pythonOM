a = 'A'
b = 'B'
c = 1.1
#string = 'a={0} b={0} c={:.2f}' # acessando por idexacao
#formato = string.format(a,b,c)

string2 = 'a={nome2} b={nome2} c={nome1}' # acessando por parametro nomeado
formato2 = string2.format(nome1=a, nome2=b, nome3=c) 

#print(formato)
print(formato2)
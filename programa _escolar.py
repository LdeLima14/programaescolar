nome = input("Qual o seu nome: ")
matricula = int(input("Qual a sua matricula: "))

b1 = float(input("Qual foi a sua nota no 1º bimestre: "))
b2 = float(input("Qual foi a sua nota no 2º bimestre: "))
b3 = float(input("Qual foi a sua nota no 3º bimestre: "))
b4 = float(input("Qual foi a sua nota no 4º bimestre: "))

media = (b1 + b2 + b3 + b4) / 4

print("<----------------------------------------->")

print("Aluno:" , nome)
print("Matricula:" , matricula)
print("Media do ensino medio:" , media)

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

maior_nota = max(b1, b2, b3, b4)

print("A sua maior nota foi:" , maior_nota)



print("<----------------------------------------->")
soma_idades = 0

for i in range(5):
        idade = int(input(f"Digite a idade da {i + 1}ª pessoa: "))
        soma_idades += idade

media_idades = soma_idades / 5

if media_idades <= 25:
        print("Turma jovem")
elif media_idades <= 60:
        print("Turma adulta")
else:
        print("Turma idosa")

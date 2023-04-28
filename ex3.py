# Fazer um programa para ler a idade de uma pessoa e
# imprimir sua situação de acordo com os critérios
# abaixo:
# – Idade <= 0 --> ERRO
# – 1 <= idade <= 3 --> BEBE
# – 4 <= idade <= 11 --> CRIANÇA
# – 12 <= idade <= 17 --> TEEN
# – 18 <= idade <= 30 --> JOVEM
# – 31 <= idade <= 64 --> ADULTO
# – idade >= 65 --> SENIOR

idade = int(input('Idade: '))
if idade <= 0:
    print ('ERRO ', idade)
elif idade <= 3:
    print ('BEBE ', idade)
elif idade <= 11:
    print ('CRIANCA ', idade)
elif idade <= 17:
    print ('TEEN ', idade)
elif idade <= 30:
    print ('JOVEM ', idade)
elif idade <= 64:
    print ('ADULTO ', idade)
else:
    print ('SENIOR ', idade)
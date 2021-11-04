from datetime import date
atual = date.today().year
ano = int(input('Informe o ano do seu nascimento: '))
idade = date.today().year - ano
print('Quem nasceu em {} tem {} anos'.format(ano, idade))
if idade <= 9:
    print('Portanto, você é classificado como MIRIM')
elif idade > 9 and idade <= 14:
    print('Portanto, você é classificado como INFANTIL')
elif idade > 14 and idade <= 19:
    print('Portanto, você é classificado como JÚNIOR')
elif idade > 19 and idade <= 25:
    print('Portanto, você é classificado como SÊNIOR')
elif idade > 25:
    print('Portanto, você é classificado como MASTER')

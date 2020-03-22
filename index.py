import datetime

minhaIdade = 32
hoje = datetime.date.today()
anoAtual = hoje.strftime("%Y")
mesAtual = hoje.strftime("%m")
diaAtual = hoje.strftime("%d")

nome = input("Insira seu nome: ")
print("Olá", nome, "vamos começar?")
diaAniversario = input("Qual o dia do seu aniversario: Ex: DD - ")
mesAniversario = input(
    "Certo, agora informe o mês do seu aniversário: ex: MM - ")
anoAniversario = input(
    "Estamos acabando, agora informe o Anoo do seu aniversário: ex: AAAA - ")

idade = (int(anoAtual) - int(anoAniversario)) - 1
if(mesAniversario < mesAtual):
    if(diaAniversario < diaAtual):
        idade = (int(anoAtual) - int(anoAniversario))

print("Perfeito,", idade,  "anos é uma excelente idade:")
cidade = input("Em qual cidade você mora: ")
print(nome, ", Obrigado por sua participar deste exercicio de Python!")

if(minhaIdade == idade):
    print("Temos a mesma Idade", minhaIdade, "anos, olha que legal!")
else:
    print("Tenho", minhaIdade, "e você", idade,
          " mas isso não quer dizer nada.. kkkkk!")

print("Confira na pasta os prints e código deste exercício, até breve ;)")

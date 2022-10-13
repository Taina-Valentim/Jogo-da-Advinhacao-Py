# -*- coding: utf-8 -*-

def da_boas_vindas():
	print('\n')
	print('────(♥)(♥)(♥)────(♥)(♥)(♥)__ ')
	print('──(♥)██████(♥)(♥)██████(♥) ')
	print('─(♥)████████(♥)████████(♥) 			BEM VINDO(A) AO...')
	print('─(♥)██████████████████(♥) ')
	print('──(♥)████████████████(♥)          ╔═══════••••••═══════╗ ')
	print('────(♥)████████████(♥)__           JOGO DA AVINHAÇÃO!')
	print('──────(♥)████████(♥) 	         ╚═══════••••••═══════╝')
	print('────────(♥)████(♥) __ 	')
	print('─────────(♥)██(♥) ')
	print('───────────(♥) __ ')
	print("\n\n\n")
	nome = input("Digite o seu nome: ")
	print("\n\n\n")
	print(f"O jogo irá começar, {nome}")
	print("\n\n")
	return nome

def pede_dificuldade():
	print("Escolha um nivel de dificuldade\n\n")
	print("❶ - Muito fácil    ❷ - Fácil    ❸ - Normal    ❹ - Difícil    ❺ - Muito difícil\n\n")
	dificuldade =  int(input("Dificuldade escolhida: "))
	return dificuldade

def sorteia_numero(dificuldade):
	if dificuldade == 1:
		maximo = 30
	elif dificuldade == 2:
		maximo = 50
	elif dificuldade == 3:
		maximo = 100
	elif dificuldade == 4:
		maximo = 150
	else:
		maximo = 200

	print(f"Escolhendo um número entre 1 e {maximo}...")

	from random import randint
	sorteado = randint(1,maximo)
	print("\nLoading…\n█▒▒▒▒▒▒▒▒▒")
	print("10%\n███▒▒▒▒▒▒▒")
	print("30%\n█████▒▒▒▒▒")
	print("50%\n███████▒▒▒")
	print("100%\n██████████")
	print("\n\nNúmero escolhido! Tente advinhá-lo!")
	return sorteado

def pedeNumero(chutes, tentativa, limiteDeTentativas):
	print(f"Tentativa {tentativa} de {limiteDeTentativas}")
	print(f"\n\n\nVocê já chutou: {chutes}\n\n")
	print("Qual o seu chute?")
	chute = int(input("\nChute: "))
	print(f"Você chutou: {chute}")
	return chute

def verifica_se_acertou(chute, numero):
	acertou = chute == numero
	if acertou:
		print("\n\n")
		print("________0000000000000000________")
		print("_____0000000000000000000000_____")
		print("__000000000__00000__0000000000__")
		print("_0000000000__00000__00000000000_")
		print("_0000000000__00000__00000000000_")
		print("_000000000000000000000000000000_")
		print("_000000000000000000000000000000_")
		print("_000000__________________000000_")
		print("_000000__________________000000_")
		print("__000000_________________00000__")
		print("___0000000_____________000000___")
		print("_____0000000_________0000000____")
		print("_______ 00000000000000000_______\n\n")
		print("Parabéns! Você acertou!")
		return True
	print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ")
	print("████▌▄▌▄▐▐▌█████ ")
	print("████▌▄▌▄▐▐▌▀████ ")
	print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ \n\n")
	print("\n\nVish. Você errou!")
	maior = numero > chute
	if maior:
		print("O número é maior!")
	else:
		print("O número é menor!")
	False

def joga(nome, dificuldade):
	numero = sorteia_numero(dificuldade)
	pontos_atuais = 1000
	limiteDeTentativas = 5
	chutes = []
	tentativa = 1
	for tentativa in range(1,limiteDeTentativas+1,1):
		chute = pedeNumero(chutes, tentativa, limiteDeTentativas)
		chutes.append(chute)
		if nome == "Taina":
			print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ")
			print("░░░░ ░░░░▀█▄▀▄▀██████░▀█▄▀▄▀████▀ ")
			print("░░░ ░░░░░░░▀█▄█▄███▀░░░▀██▄█▄█\n\n")
			print("Parabéns! Você acertou!")
			print(f"O número era {chute}")
			print(f"Você ganhou {pontos_atuais} pontos!")
			break
		pontos_perdidos = abs((chute - numero)) / 2.0
		pontos_atuais -= pontos_perdidos
		if verifica_se_acertou(chute, numero):
			break
	if nome != "Taina":
		print(f"O número era {numero}")
		print(f"Você ganhou {pontos_atuais} pontos!")

def nao_quer_jogar():
	print("+88_________________+880_______")
	print("_+880_______________++80_______")
	print("_++88______________+880________")
	print("_++88_____________++88________")
	print("__+880___________++88_________")
	print("__+888_________++880__________")
	print("__++880_______++880___________")
	print("__++888_____+++880____________")
	print("__++8888__+++8880++88_________")
	print("__+++8888+++8880++8888________")
	print("___++888++8888+++888888+80____")
	print("___++88++8888++8888888++888___")
	print("___++++++888888fx88888888888___")
	print("____++++++88888888888888888___")
	print("____++++++++000888888888888___")
	print("_____+++++++00008f8888888888___")
	print("______+++++++00088888888888___")
	print("_______+++++++0888f8888888____")

	quero_jogar = input("Deseja jogar novamente? (S/N): ")
	nao_quero_jogar = quero_jogar.upper() == "N"
	return nao_quero_jogar

nome = da_boas_vindas()
while True:
	dificuldade = pede_dificuldade()
	joga(nome, dificuldade)
	if nao_quer_jogar():
		break
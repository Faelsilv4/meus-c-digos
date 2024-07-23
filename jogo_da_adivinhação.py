#  Jogo de adivinhação
from random import randint
computador=randint(0,10)
print("Sou seu computador a cabei de pensar em um numero entre 0 e 10.")
print("Será que voce consegue adivinhar,qual foi?")
acertou=False
palpite=0
while not acertou:
	jogador=int(input("Qual e o seu palpite? "))
	palpite+=1
	if jogador==computador:
		acertou=True
	else:
		if jogador<computador:
			print("\033[33mMAIS...\033[mTente outra vez...")
		elif jogador>computador:
			print("\033[36mMENOS...\033[mTente outra vez...")
print("\033[32mACERTOU!\033[m com {} tentativas.Parabéns!".format(palpite))
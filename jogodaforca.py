import os

stringA = input("Digite a palavra secreta: ")
os.system('cls')
tentativa = len(stringA) * 2
palavra = list(stringA)

# Inicializar a palavra adivinhada com sublinhados
secreto = ['_' for _ in palavra]

# Mostrar o estado inicial da palavra adivinhada
print(f'\033[33m DICA >>> a palavra tem {len(stringA)} letras \033[0m')
print('>>>>', end=' ')
for char in secreto:
  print(char, end=' ')
print('')

while tentativa > 0:
  print(f'Você tem \033[91m{tentativa}\033[0m tentativas')
  guess = input('Adivinhe uma letra ou palavra: ')

  # Verifique se o palpite corresponde à palavra inteira
  if guess == stringA:
    print(
        f'\033[92m Parabéns!!, você descobriu a palavra secreta: {stringA}\033[0m'
    )
    break

  # Verifique se o palpite corresponde a alguma letra na palavra
  elif len(guess) == 1:
    guess_found = False
    i = 0
    while i < len(palavra):
      if palavra[i] == guess:
        guess_found = True
        secreto[i] = guess
      i += 1

    # Imprimir a palavra adivinhada atualizada
    print('>>>>', end=' ')
    for char in secreto:
      print(char, end=' ')
    print('')

    if guess_found:
      print('Esta letra está na palavra!')
    else:
      print('Esta letra não está na palavra!')
      tentativa -= 1

  else:
    print('\033[91m Palavra incorreta!\033[0m')

  # Verifique se o jogador adivinhou todas as letras
  if '_' not in secreto:
    print(
        f'\033[92m Parabéns!!, você descobriu a palavra secreta: {stringA}\033[0m'
    )
    break

  # Verifique se o jogador ficou sem tentativas
  if tentativa == 0:
    print('\033[91m Você perdeu!!!\033[0m')
    break

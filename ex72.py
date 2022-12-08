n = 'zero', 'um', 'dois', 'três', 'quatro','cinco'
while True:
    value = int(input('Digite um valor entre 0 e 5: '))
    if value in range(0, len(n)):
        print(f'Você digitou {n[value]}')
        break
    print('Tente novamente. ', end='')






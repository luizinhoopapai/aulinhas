lista = []

while True:
    addItem = input('adicione um item:')
    if addItem == 'fim':
        break

    lista.append(addItem)

    print(f'o tamanho da minha lista é: {len(lista)}')
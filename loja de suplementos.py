produtos = {
    1: {"nome": "Camisa", "preco": 99.90},
    2: {"nome": "Creatine 300g", "preco": 100.00},
    3: {"nome": "Durateston", "preco": 177.90},
    4: {"nome": "Whey da Groufi", "preco": 105.90}
}

carrinho = []

def exibir_produtos():
    print("\nProdutos disponíveis:")
    for codigo, produto in produtos.items():
        print(f"{codigo} - {produto['nome']} - R$ {produto['preco']:.2f}")

def adicionar_ao_carrinho():
    exibir_produtos()
    codigo = int(input("Digite o código do produto que deseja adicionar: "))
    if codigo in produtos:
        carrinho.append(produtos[codigo])
        print(f"{produtos[codigo]['nome']} adicionado ao carrinho.")
    else:
        print("Código inválido. Tente novamente.")

def remover_do_carrinho():
    if len(carrinho) == 0:
        print("O carrinho está vazio.")
        return

    print("\nProdutos no carrinho:")
    for i, produto in enumerate(carrinho, start=1):
        print(f"{i} - {produto['nome']} - R$ {produto['preco']:.2f}")

    indice = int(input("Digite o número do produto que deseja remover: ")) - 1
    if 0 <= indice < len(carrinho):
        produto_removido = carrinho.pop(indice)
        print(f"{produto_removido['nome']} removido do carrinho.")
    else:
        print("Número inválido. Tente novamente.")

def exibir_carrinho():
    if len(carrinho) == 0:
        print("O carrinho está vazio.")
    else:
        print("\nCarrinho de compras:")
        total = 0
        for produto in carrinho:
            print(f"{produto['nome']} - R$ {produto['preco']:.2f}")
            total += produto["preco"]
        print(f"Total: R$ {total:.2f}")

def finalizar_compra():
    if len(carrinho) == 0:
        print("O carrinho está vazio. Adicione produtos antes de finalizar a compra.")
        return

    exibir_carrinho()
    confirmacao = input("Deseja finalizar a compra? (s/n): ")
    if confirmacao.lower() == 's':
        print("Compra finalizada com sucesso! Obrigado pela preferência.")
        carrinho.clear()
    else:
        print("Compra não finalizada.")

def menu():
    while True:
        print("\n--- Loja Virtual ---")
        print("1 - Exibir produtos")
        print("2 - Adicionar produto ao carrinho")
        print("3 - Remover produto do carrinho")
        print("4 - Exibir carrinho")
        print("5 - Finalizar compra")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            exibir_produtos()
        elif opcao == '2':
            adicionar_ao_carrinho()
        elif opcao == '3':
            remover_do_carrinho()
        elif opcao == '4':
            exibir_carrinho()
        elif opcao == '5':
            finalizar_compra()
        elif opcao == '6':
            print("Saindo da loja. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
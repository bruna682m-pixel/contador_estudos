# %%
dias_estudo = 0

while True:
    opcao = int(input("""
======================================
         DIÀRIO DE PYTHON
======================================

Dias estudados: 0

1- Registrar estudo
2- Ver dias estudados
3- Sair

"""))
    if opcao == 1:
        print("Você estudou hoje!")

        dias_estudo += 1

        print("Dias estudados:",dias_estudo)

    elif opcao == 2:
        print("Você já estudou programação por:",dias_estudo,"dias.")


    elif opcao == 3:
        print("Saindo...")
        break

    else:
        print("Opção inavalida.")






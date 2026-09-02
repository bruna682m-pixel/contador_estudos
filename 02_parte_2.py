# %%
dias_estudo = 0
meta = 30
resto_meta = 0

while True:
    opcao = int(input("""
======================================
         DIÀRIO DE PYTHON
======================================

Dias estudados: 0

1- Registrar estudo
2- Ver dias estudados
3- Sair
4- Mostrar progresso
5- Meta

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

    elif opcao == 4:
        print("Dias estudados:",dias_estudo)

        for i in range(1, dias_estudo+1):
            print("Dia",i,"check.")

    elif opcao == 5:
        resto_meta = meta - dias_estudo

        print(f"""
=============================
        Meta: {meta}
=============================

Dias estudados: {dias_estudo}
Faltam: {resto_meta}
""")

        if meta == resto_meta:
            print("Atigiu meta.")
        else:
            print("Faltam:",resto_meta,"dias.")

    else:
        print("Opção inavalida.")






# %%

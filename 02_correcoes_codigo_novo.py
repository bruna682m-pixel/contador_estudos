# %%


dias_estudados = 0
meta = 30
resto_meta = 0
progresso = 0
subtracao_dias_estudados = 0

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

        dias_estudados += 1

        print("Dias estudados:",dias_estudados)

    elif opcao == 2:
        print("Você já estudou programação por:",dias_estudados,"dias.")


    elif opcao == 3:
        print("Saindo...")
        break

    elif opcao == 4:
        print("Dias estudados:",dias_estudados)
        for i in range(1, dias_estudados+1):
            print("Dia",i,"✓.")

        subtracao_dias_estudados = meta - dias_estudados
        print(subtracao_dias_estudados,"/",meta)

    elif opcao == 5:
        resto_meta = meta - dias_estudados
        progresso = dias_estudados / 30
        progresso = progresso * 100

        print(f"""
=============================
        Meta: {meta}
=============================F

Dias estudados: {dias_estudados}
Faltam: {resto_meta}
Progresso: {progresso}%
""")

        if dias_estudados >= meta:
            print("Atigiu meta.")
        else:
            print("Faltam:",resto_meta,"dias.")

    else:
        print("Opção inavalida.")



# %%
import datetime

historico_dias_estudados = []

dias_meta = 0

arquivo = open("teste.txt", "a")
arquivo.close()

arquivo = open("teste.txt", "r")

linhas = arquivo.readlines()

arquivo.close()

arquivo_meta = open("meta.txt", "a")
arquivo_meta.close()

arquivo_meta = open("meta.txt", "r")

linha_meta = arquivo_meta.readlines()

arquivo_meta.close()

arquivo_progresso = open("progresso_meta.txt", "a")
arquivo_progresso.close()

arquivo_progresso = open("progresso_meta.txt", "r")
linha_progresso = arquivo_progresso.readlines()
arquivo_progresso.close()


for linha in linhas:
    linha = linha.strip()

    data = datetime.datetime.strptime(linha, "%d/%m/%Y").date()

    historico_dias_estudados.append(data)

if linha_meta == []:

    while True:
        meta = int(input("Digite sua meta de dias de estudos:"))

        if meta > 0:
            break

        print("A meta deve ser maior que 0.")

    arquivo_meta = open("meta.txt", "w")
    arquivo_meta.write(str(meta))
    arquivo_meta.close()
else:
    meta = int(linha_meta[0])

if linha_progresso == []:
    dias_meta = 0
else: 
    dias_meta = int(linha_progresso[0])

while True:
    data_atual = datetime.date.today()

    opcao = int(input(f"""
======================================
         DIÀRIO DE PYTHON
======================================

Ofensiva: {len(historico_dias_estudados)}
Meta: {meta}
Faltam: {meta - len(historico_dias_estudados)}

1- Registrar estudo
2- Ver ofensiva
3- Ver historico
4- Ver meta
5- Sair

"""))
    if opcao == 1:
        print("registrar estudo")

        if data_atual in historico_dias_estudados:
            print("Você já registrou o estudo de hoje.")
        else:
            historico_dias_estudados.append(data_atual)
            dias_meta += 1

            arquivo_progresso = open("progresso_meta.txt", "w")
            arquivo_progresso.white(str(dias_meta))
            arquivo_progresso.close()

            print("Dias estudados:", len(historico_dias_estudados))

            arquivo = open("teste.txt", "a")

            arquivo.write(data_atual.strftime("%d/%m/%Y") + "\n")

            arquivo.close()

    
    elif opcao == 2:
            print("ver ofensiva")

            if historico_dias_estudados == []:
                print("Ainda não há estudos registrados.")
            else:
                sequencia = 0

                dia_anterior = data_atual + datetime.timedelta(days= -1)

                if data_atual in historico_dias_estudados:
                    sequencia += 1

                while True:
                    numero_semana = dia_anterior.isoweekday()

                    if numero_semana == 6 or numero_semana == 7:
                        if dia_anterior in historico_dias_estudados:
                            sequencia +=1

                        dia_anterior = dia_anterior + datetime.timedelta(days= -1)
                    else:
                        if dia_anterior in historico_dias_estudados:
                            dia_anterior = dia_anterior + datetime.timedelta(days= -1)
                            sequencia += 1
                        else:
                            break
      
                       
        
                print("Sequencia atual:",sequencia, "dia(s)")

    elif opcao == 3:
        print("Hístórico de estudos:")

        if historico_dias_estudados == []:
            print("Ainda não há estudos registrados.")
        
        for data in historico_dias_estudados:
            data_formatada = data.strftime("%d/%m/%Y")
            print(data_formatada)

    elif opcao == 4:
        print("Ver meta")

        faltam = meta - dias_meta

        if dias_meta >= meta:
            faltam = 0

        progresso = dias_meta / meta * 100
        
        if progresso >= 100:
            progresso = 100


        print(f"""
======================================
              Meta
======================================
Meta: {meta} dias
Días estudados: {dias_meta}
Faltam: {faltam} dias
Progresso: {progresso:.1f}%
""")
     
        if dias_meta >= meta:
            print("Meta atinginda!")

            while True:
                meta = int(input("Digite sua nova meta de dias de estudos:"))

                if meta > 0:
                    break

                print("A nova meta dever ser maior que 0.")

            dias_meta = 0

            arquivo_meta = open("meta.txt", "w")
            arquivo_meta.write(str(meta))
            arquivo_meta.close
        else:
            print("Continue estudando!")
                
    elif opcao == 5:
        print("Saindo...")
        break 
                                    
    else:
        print("Opção inavalida.")

    
        



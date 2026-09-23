# %%
import datetime

historico_dias_estudados = []

arquivo = open("teste.txt", "a")
arquivo.close()

arquivo = open("teste.txt", "r")

linhas = arquivo.readlines()

arquivo.close()

for linha in linhas:
    linha = linha.strip()

    data = datetime.datetime.strptime(linha, "%d/%m/%Y").date()

    historico_dias_estudados.append(data)

meta = 30

while True:
    data_atual = datetime.date.today()

    opcao = int(input(f"""
======================================
         DIÀRIO DE PYTHON
======================================

Ofensiva: {len(historico_dias_estudados)}
Meta: 
Faltam: 

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
            print("Dias estudados:", len(historico_dias_estudados))

            arquivo = open("teste.txt", "a")

            arquivo.write(data_atual.strftime("%d/%m/%Y") + "\n")

            arquivo.close()

    
    elif opcao == 2:
            print("ver ofensiva")

            if historico_dias_estudados == []:
                print("Ainda não há estudos registrados.")
            else:
                data_atual = datetime.date.today()
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
     print("ver historico")

    elif opcao == 4:
     print("Ver meta")
                
    elif opcao == 5:
        print("Saindo...")
        break 
                                    
    else:
        print("Opção inavalida.")

    
        



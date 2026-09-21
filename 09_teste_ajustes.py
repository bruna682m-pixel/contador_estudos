# %%
import datetime

historico_dias_estudados = [
    
]

#data_atual_formatada = data_atual.strftime('%d/%m/%Y')
#print(data_atual_formatada)


meta = 30

while True:
    data_atual = datetime.date.today()

    opcao = int(input(f"""
======================================
         DIÀRIO DE PYTHON
======================================

Dias estudados: {len(historico_dias_estudados)}

1- Registrar estudo
2- Ver dias estudados
3- Sair
4- Mostrar progresso
5- Meta

"""))
    if opcao == 1:

        if data_atual in historico_dias_estudados:
            print("Você já registrou o estudo de hoje.")
        else:
            historico_dias_estudados.append(data_atual)
            print("Dias estudados:", len(historico_dias_estudados))
        
    elif opcao == 2:
        print("Você já estudou programação por:",len(historico_dias_estudados), "dias.")


    elif opcao == 3:
        print("Saindo...")
        break

    elif opcao == 4:

        print("Dias estudados:",len(historico_dias_estudados))
        for i in historico_dias_estudados:
            data_atual_formatada = i.strftime('%d/%m/%Y')

            print("Dia",data_atual_formatada,"✓")

        subtracao_dias_estudados = meta - len(historico_dias_estudados)
        print(subtracao_dias_estudados,"/",meta)

    elif opcao == 5:
        resto_meta = meta - len(historico_dias_estudados)
        progresso = len(historico_dias_estudados) / 30
        progresso = progresso * 100

        print(f"""
=============================
        Meta: {meta}
=============================F

Dias estudados: {len(historico_dias_estudados)}
Faltam: {resto_meta}
Progresso: {progresso}%
""")

        if len(historico_dias_estudados) >= meta:
            print("Atigiu meta.")
        else:
            print("Faltam:",resto_meta,"dias.")

    elif opcao == 6:
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


                
                



                            

    else:
        print("Opção inavalida.")

    
        



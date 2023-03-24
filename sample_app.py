import streamlit as st
import csv
import datetime

# Cria o arquivo CSV se ele não existir
try:
    with open('resultado.csv', 'x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data", "Time", "Participante"])
except FileExistsError:
    pass

# Define as opções de time e participantes
TIMES = ["Palmeiras", "Água Santa"]
PARTICIPANTES = ["Kraucer", "Andrea", "Fideles", "Rodrigo", "Vitor", "André", "Joca", "Marcelo", "Seiti", "Alexandre"]

# Define a função para adicionar um resultado
def adicionar_resultado(data, time, participante):
    with open('resultado.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data, time, participante])

# Define a função para excluir um resultado
def excluir_resultado(data, time, participante):
    linhas = []
    with open('resultado.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row != [data, time, participante]:
                linhas.append(row)
    with open('resultado.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(linhas)

# Define a página principal
def pagina_principal():
    st.title("Campeonato Paulista 2023")
    st.write("Escolha o time campeão e o participante que faz a escolha.")

    # Seleciona o time
    time = st.selectbox("Time", TIMES)

    # Seleciona o participante
    participante = st.selectbox("Participante", PARTICIPANTES)

    # Adiciona ou exclui um resultado
    acao = st.radio("Ação", ["Adicionar resultado", "Excluir resultado"])
    if acao == "Adicionar resultado":
        data = datetime.date.today().strftime("%d/%m/%Y")
        adicionar_resultado(data, time, participante)
        st.success("Resultado adicionado!")
    elif acao == "Excluir resultado":
        data = st.text_input("Data do resultado (DD/MM/AAAA)")
        if st.button("Excluir"):
            excluir_resultado(data, time, participante)
            st.success("Resultado excluído!")

    # Mostra a tabela de resultados
    with open('resultado.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        resultados = list(reader)
    if len(resultados) > 1:
        st.write("Resultados:")
        st.table(resultados)

# Executa o aplicativo
pagina_principal()

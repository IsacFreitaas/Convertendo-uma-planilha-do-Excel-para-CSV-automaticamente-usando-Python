import pandas

# Caminho do Arquivo Excel e o nome da planilha
excel_file = "C:/Users/Usuario/Desktop/caminho_do_arquivo.xlsx"
sheet_name = "Página2"

# Ler a planilha do Excel
DataFrames = pandas.read_excel(excel_file, sheet_name=sheet_name)


# Configurar o caminho de saída do arquivo e o nome
csv_saida = "C:/Users/Usuario/Desktop/caminho_de_saida.csv"

# Salvar DataFrames em CSV
DataFrames.to_csv(csv_saida, index=False)

print(f"Arquivo CSV salvo como {csv_saida} com sucesso!")
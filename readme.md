# Convertendo uma planilha do Excel (.xlsx) para CSV

#### Neste repositório, mostrarei um script simples em Python que automatiza esse processo. Para fazer isso, usaremos duas bibliotecas do Python:
    - Pandas,         # <---- para ler e manipular base de dados.
    - OpenPyXl.         # <----  extensão para o pandas trabalhar com o Excel.
#### Para usar essas e outras bibliotecas no seu computador com Python, você precisará instalá-las.

--------------------------------------

# 1 - Instalação (Windows, Linux e MacOS):
    - pip install pandas openpyxl # (Terminal)
    - !pip install pandas openpyxl # (No Jupyter Notebook (.ipynb))

### -> EM CASO DE ERRO NA INSTALAÇÃO TENTE AS SEGUINTES POSSIBILIDADES:
    - pip3 install pandas openpyxl
    - pip install pandas openpyxl --break-system-packages # (USE COM CUIDADO!)



# 2.1 - Script:

### Agora com as bibliotecas instaladas, vamos por a mão na massa.
#### Iniciamos importando o pandas pra dentro de nosso código (você precisa já ter ele instalado na sua máquina, como vimos no passo anterior). Para isso, fazemos assim:

    import pandas

### Simples assim. Com importamos o Pandas pra dentro do nosso script Python. 
##### Agora precisamos especificar o local em que a planilha Excel que queremos converter está localizada em nosso computador. Fazemos assim:

    # Caminho do Arquivo Excel
    excel_file = "C:/Users/Usuario/Desktop/caminho_do_arquivo.xlsx"

##### Porém, precisaremos do nome da página da planilha que usaremos mais na frente nesse script. Por exemplo, você tem uma planilha do Excel com várias páginas, mas você só quer converter para CSV uma delas. Pra isso vá no seu vizualizador de planilhas e verifique.

<div align="center">
<img src="https://github.com/IsacFreitaas/Convertendo-uma-planilha-do-Excel-para-CSV-automaticamente-usando-Python/assets/65254733/3bca3418-6915-49ca-b639-0a39a52f141e" width="600px" />
</div>


##### * No meu caso, o nome da página que estou vizualizando é "Página2", então:

    # Nome da página da planilha
    sheet_name = "Página2"

# 2.2 - Data frames:

## Agora, precisamos que o pandas leia essa planilha e armazene em uma variável, onde ficarão guardados esses dados.
#### É comum esses dados serem guardados em uma variável "DataFrames" (ou só "df").
##### Veja a seguir como se faz isso:

    # Ler a planilha do Excel e armazenar os dados no DataFrames
    DataFrames = pandas.read_excel(excel_file, # Recebe o arquivo Excel
                                   sheet_name=sheet_name) # Especifica a página da planilha

# 2.3 - Salvando o DataFrames em CSV e exportando:
##### Para finalizar a conversão e salvar nosso arquivo, vamos precisar especificar o nome, ou o local que será salvo, pois essa variável sera usada no "DataFrames.to_csv()", pois devemos especificar no primeiro argumento o local de saida ou nome do arquivo. Após o arquivo ser salvo como CSV, iremos imprimir (print) que o arquivo foi salvo com sucesso, como vemos abaixo:

    # Configurar o caminho de saída do arquivo e o nome
    csv_saida = "C:/Users/Usuario/Desktop/caminho_de_saida.csv"

    # Salvar DataFrames em CSV
    DataFrames.to_csv(csv_saida, index=False)

    print(f"Arquivo CSV salvo como {csv_saida} com sucesso!")

# 3 - Fim
### Obrigado por me acompanhar até aqui.
##### Caso fique alguma dúvida, me chama nas redes sociais que vou tentar te ajudar.



Lembrando que fiz um vídeo no YouTube ensinando todo esse processo:



[![Youtube_Video_Play_Button: Como converter uma planilha do Excel para CSV no Python](https://github.com/IsacFreitaas/Convertendo-uma-planilha-do-Excel-para-CSV-automaticamente-usando-Python/assets/65254733/ec8007c4-6647-4dce-92bc-f5a7f207c88d)](https://www.youtube.com/watch?v=PJNba-tHeZY&t)



##### Sobre mim:
Isac Freitas 
------------------- 


Estudante de Ciência de Dados e Inteligência Artificial.  <div><img align="right" src="https://github.com/IsacFreitaas/IsacFreitaas/assets/65254733/00d94d72-7789-4961-b1b2-d0313bc80b48" width="400" ></img></div>





### Me encontre:





Insta: [@isac.sfreitas](https://www.instagram.com/isac.sfreitas/)  Twitter: [isaczeitgeist](https://x.com/isaczeitgeist)  Canal: [isac zeitgeist](https://www.youtube.com/@chuckbum)



Obrigado pela atenção!

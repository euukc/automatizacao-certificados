# Pegar os dados da planilha: nome do curso, nome do participante, tipo de participação, data do inicio, data do final, carga horária, data da emissao do certificado
#transferir para a imagem do certificado 


#Pegando os dados 

import openpyxl 
from PIL import Image, ImageDraw, ImageFont

# Abrindo a planilha

workbook_alunos = openpyxl .load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1']

# Definindo a fonte a ser usada

fonte_nome = ImageFont.truetype('./tahomabd.ttf', 80)
fonte_geral = ImageFont.truetype('./tahoma.ttf', 80)
fonte_data = ImageFont.truetype('./tahoma.ttf', 55)


for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):

# Acessar cada celula que contem a info que precisamos 
    
    nome_curso = linha[0].value 
    nome_participante = linha[1].value
    tipo_participacao = linha[2].value
    data_inicio = linha[3].value
    data_final = linha[4].value
    carga_horaria = linha[5].value
    data_emissao = linha[6].value

# Transferir para a imagem do certificado

image = Image.open('./certificado_padrao.jpg')
desenhar = ImageDraw.Draw(image)


desenhar.text((1060, 830), nome_participante, fill='black', font=fonte_nome)
desenhar.text((1090, 950), nome_curso, fill='black', font=fonte_geral)
desenhar.text((1440, 1065), tipo_participacao, fill='black',font=fonte_geral)
desenhar.text((1480,1182), str(carga_horaria), fill='black', font=fonte_geral)

desenhar.text((750, 1770), data_inicio, fill='blue', font=fonte_data)
desenhar.text((750, 1930), data_final, fill='blue', font=fonte_data)

desenhar.text((2220, 1930), data_emissao, fill='blue', font=fonte_data)

image.save(f'./{indice}_{nome_participante}_certificado.png')


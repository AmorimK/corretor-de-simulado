import csv

# Lendo o gabarito



gabarito = []

arquivoGab = open('gabarito/gabarito.txt', 'r')

for i, j in enumerate(arquivoGab):

    print(j)

    if i < 10:
        gabarito.append(j[3::])

    elif i < 100:
        gabarito.append(j[4::])
    
    else:
        gabarito.append(j[5::])
    
    gabarito[i] = gabarito[i].upper().rstrip('\n')

print(f'Gabarito = {gabarito}')

arquivoGab.close()

# Lendo CSV

resultados = open('resultados.txt', 'w')

with open('csv/resultados.csv', newline='') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = next(reader)  # pula a linha do cabeçalho

# Conferindo os acertos

    for row in reader:

        row = row[0].split(';')
        
        nomeAluno = row[0]        
        alternativasAluno = row[1::]

        erros = open(f'erros/{nomeAluno}.txt', 'w')

        print(nomeAluno)
        print(alternativasAluno)

        acertos = 0


        respostas = [''] * len(gabarito)

        j = 0

        while j < len(alternativasAluno):
            
            if len(respostas) == j: break
            else:
                respostas[j] = alternativasAluno[j]
                j+=1

        print('respostas = ',respostas)


        for i in range(len(gabarito)):
            
            if respostas[i] == gabarito[i]:
                acertos += 1
                erros.write(f'Questão {i+1} correta\n')
            else:
                erros.write(f'Questão {i+1} = {respostas[i]}\n')

        
        resultados.write(f'{nomeAluno} - {acertos}\n')

    
    erros.close()
    resultados.close()

        



        
        




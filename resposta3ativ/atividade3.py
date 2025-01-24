import csv
import matplotlib.pyplot as plt


with open('D:/OneDrive/Documentos/1/Atividade 3/dados - Copia.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    data = [row for row in reader if any(field.strip() for field in row)]
    columns = data[0]    

if not data:
    print("Erro: Não foi possível ler o arquivo.")
    exit()

if len(columns) > 1:
    for row in data[1:]:
        seqName = row[1]
        last_pipe = seqName.rfind('|')
        date = seqName[last_pipe + 1:]
        row[1] = date
else:
    print("Erro: Não há colunas suficientes.")

data[1:] = sorted(data[1:], key=lambda x: x[1], reverse=False)

print('Dados em ordem crescente salvos com sucesso.')


data[0].append('numMutations')

for row in data[1:]:
    try:
        num_mutations = int(row[10]) + int(row[11]) + int(row[12])
    except ValueError:
        num_mutations = 0
    row.append(num_mutations)


dates = {}
for row in data[1:]:
    date = row[1]
    num_mutations = row[-1]
    if date in dates:
        dates[date] += num_mutations
    else:
        dates[date] = num_mutations

# Exibe no gráfico apenas os meses e anos
def format_date(date):
    return date[:7]

dates = {format_date(date): num_mutations for date, num_mutations in dates.items()}
dates = dict(sorted(dates.items(), key=lambda x: x[0]))


dates_list = list(dates.keys())
mutations_list = list(dates.values())


plt.figure(figsize=(10, 6))
plt.plot(dates_list, mutations_list, marker='o', color='b')
plt.title('Evolução Genômica ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Número de Mutações')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

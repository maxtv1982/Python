from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    # чтение csv-файла и заполнение контекста
    data = []
    year = []
    total = []
    with open('inflation_russia.csv', newline='', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            data.append(row)
    head = data.pop(0)
    # for i in range(len(data)):
    #     print(data[i][0])
    for line in data:
        year.append(line.pop(0))
        total.append(line.pop(len(line)-1))

    context = {'data': data, 'head': head, 'year': year, 'total': total }

    return render(request, template_name,
                  context)

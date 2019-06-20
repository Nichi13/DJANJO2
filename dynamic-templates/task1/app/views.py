from django.shortcuts import render
from django.conf import settings
import csv
import os


def inflation_view(request):
    template_name = 'inflation.html'
    # path = os.path.join(settings.BASE_DIR)
    path2 = os.path.join(settings.PATH)
    with open((path2), encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        file_list = []
        for item in reader:
            keys = item.keys()
            file_list.append(item)
    data = {"message": file_list, 'keys': keys}
    context = data

    return render(request, template_name,
                  context)


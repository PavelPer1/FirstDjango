from django.shortcuts import render

items = [
    {'id': 1, 'name': 'Кроссовки', 'quantity': 5},
    {'id': 2, 'name': 'Куртка', 'quantity': 2},
    {'id': 3, 'name': 'Coca-cola', 'quantity': 3},
    {'id': 4, 'name': 'Картофель фри', 'quantity': 4},
    {'id': 5, 'name': 'Кепка', 'quantity': 40}
]


def items_add(request):
    array = []
    for i in items:
        array.append(i['name'])
    return render(request, 'main/items_add.html', {'array': array})


def basic(request, url):
    title = ''; num = 0
    for i in items:
        if i['name'] == url:
            title = i['name']
            num = i['quantity']
    return render(request, 'main/basic.html', {'title': title, 'num': num})

def Codding(_list):
    for i in range(len(_list)): _list[i] = _list[i].encode('utf-8')
    return _list

def Uncodding(_list):
    for i in range(len(_list)): _list[i] = _list[i].decode('utf-8')
    return _list

a = ['Привет', 'Тензор', 'dwdewde']
a = Codding(a)
print(f'Список байт кодов - {a}')
print(f'Список строк - {Uncodding(a)}')
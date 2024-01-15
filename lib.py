# это наш модуль и мы хотим в нем создать набор своих функций
def get_count(string, symbol):
    cnt = 0
    for i in string:
        if i == symbol:
            cnt += 1
    return cnt
def get_len(string):
    c = 0
    for i in string:
        c += 1
    return c

print(__name__) # в less30 - lib, а при запуске этого файла - __main__

if __name__ == '__main__':
    print('код который не выполняется в файлах куда подключается этот файл')
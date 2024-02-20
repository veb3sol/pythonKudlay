import os


# print(dir(os))  -- море функций, констант
# print(os.getcwd()) #C:\Users\Ruslan_WORK\PycharmProjects\pythonKudlay - путь к текущей папке
# print(os.name) # nt - названи ос
# print(os.environ) #словарь перменных окружения - ключи - наименование переменных окружения, а
# print(os.environ['PATH']) # строка с путями среды окружения -- пути к прогам которые доступны с ком строки везде
# добавляем путь к путям среды окружения
# p = os.environ['PATH']
# print(p)
# p += ';E:\KURSY\Python' добавили путь к путям переменной окружения
# print(p)
# print(os.getlogin()) #Ruslan_WORK - под каким логином вошли в систему
# print(os.getpid()) #10636 - номер процесса запущеного на компе - процессы с диспетчера задач

# поменять текущую дерикторию
# os.chdir('E:\KURSY\Python') - переходим в эту папку
# print(os.getcwd())  - E:\KURSY\Python

#print(os.listdir('E:\KURSY\JS\projects\kurs\kurs')) # список файлов и папок в папке по этому пути

# os.mkdir(r"E:\new")  -- создание папки new в корне диска E
# os.rmdir(r"E:\new")  -- удаление папки

# print(help(os.remove)) -- справка по os.remove

# print(os.listdir()) -- без аргументов вернет список файлов и папок в текущей папке

# print(os.system('dir'))  -- выполнение команд в командной строке в текущей папке

# os.mkdir(r"E:\\news")
# os.chdir(r"E:\\news")
# print(os.listdir())  #[] - пустой список - в созданной папке ничего нету

# сами создаем в созданой папке news файл base.txt
# print(os.path.isfile(r"E:\\news\\base.txt"))  # True - такой файл и путь к нему существуют
# print(os.path.isdir(r"E:\\news"))  # True - такая папка есть

# os.startfile(r"E:\\news\\base.txt") -- запускает - открывает файл

# print(os.path.basename(r"E:\\news\\base.txt"))  -- base.txt  название файла
# print(os.path.dirname(r"E:\\news\\base.txt"))  #-- E:\\news  путь к файлу

# print(os.path.getsize('E:\\news\\base.txt')) # 24 - размер файла в байтах

# переименование файла
# os.chdir('E:\\news')  # изначально переходим в нужную папку
# ff = os.listdir('E:\\news') # список файлов - у нас 1 файл
# # ff[0] - наш файл
# print(ff[0][-4:])  # .txt - получаем расширение файла
# newff = 'newbase'+ff[0][-4:]
# print(newff) #newbase.txt
# os.rename(ff[0], newff) # файл переименовался

# Переименование папок
# os.rename('E:\\news', 'E:\\super') # название папки изменилось

# os.chdir('E:\\super')
# for root,dirs,fls in os.walk('E:\\super'):
#     print(root)
#     print(dirs)
#     print(fls)

#     получаем такое
# E:\super
# ['8888', 'sub']
# ['exelka.xlsx', 'img.bmp', 'newbase.txt', 'wordik.docx']
# E:\super\8888
# ['yuyu']
# ['hhh.zip']
# E:\super\8888\yuyu
# []
# []
# E:\super\sub
# ['10']
# ['cvc.txt']
# E:\super\sub\10
# []
# []


# sys
# import sys
# # print(sys.exec_prefix) # где именно установлен питон
# # print(sys.executable)  # путь к интерпритатору питона
# print(sys.getwindowsversion())  # данные о текущей версии винды

# ДЗ
# ot = '  '
# od = True
# for root,dirs,fls in os.walk('E:\\super'):
#     print(ot + root)
#     if(fls):
#         for f in fls:
#             print(ot*2+f)
#     if(dirs):
#         for d in dirs:
#             print(ot*2+d)

# Дз-2

def get_tree_path(fold):
    for root, fld, fls in os.walk(fold):
        kol_sep = root.count(os.sep)
        kol_prob = ' ' * 4 * kol_sep
        print(f'{kol_prob} [{os.path.basename(root)}]')
        kol_prob_2 = kol_prob + '    '
        print(f'{kol_prob_2} {fls}')


get_tree_path('E:\\super')
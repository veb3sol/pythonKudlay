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

# 42 min





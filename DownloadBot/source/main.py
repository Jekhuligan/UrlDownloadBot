from pywebcopy import save_webpage, save_website
import validators

def warning(text):
	print("\033[1m\033[31m{}\033[0m".format(text))

def webpage(url, folder, name):
	save_webpage(
		url=url,
		project_folder=folder,
		project_name=name,
		bypass_robots=True,
		debug=True,
		open_in_browser=True,
		delay=None,
		threaded=False,
	)

def website(url, folder, name):
	save_website(
		url=url,
		project_folder=folder,
		project_name=name,
		bypass_robots=True,
		debug=True,
		open_in_browser=True,
		delay=None,
		threaded=False,
	)

url="https://habr.com/ru/companies/pvs-studio/articles/855108/"
folder="..//..//site//"
name="youtube123"

webpage(url, folder,name)

print("File = " + name + url + '.html')

#
# print("""Выберите цифру:
# 1 - Сохранить страницу
# 2 - Сохранить сайт""")
# b=False
#
# while b==False:
# 	try:
# 		a = int(input())
# 		if a==1 or a==2:
# 			b=True
# 		else:
# 			warning("Выберите корректный номер!")
# 	except:
# 		warning("Только цифры!")
#
# c=False
# while c==False:
# 	url = input("Введите ссылку: ")
# 	if validators.url(url):
# 		c=True
# 	else:
# 		warning("Некорректная ссылка!")
#
# folder=input("Куда сохранять: ")
# name=input("Название проекта: ")
# if a==1:
# 	webpage(url, folder, name)
# else:
# 	website(url, folder, name)
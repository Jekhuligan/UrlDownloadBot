import requests



def savePage(url, folder, name):
    r = requests.get(url)
    with open(folder + name + '.html', 'w', encoding="utf-8") as file:
        file.write(r.text)


savePage("https://habr.com/ru/companies/pvs-studio/articles/855108/", "..//..//site//", "855106")

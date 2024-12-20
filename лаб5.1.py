class Book():
    #описание
    def __init__(self, title, author, year):
        #свойства
        self.title = title
        self.author = author
        self.year = year


    def get_info(self):
        print("Название книги: " + self.title + ", Автор: " + self.author + ", Год издания: " + str(self.year))
        
B1=Book("Чебупели", "Рояль Гуслинг", 2077)
B2=Book("Как стать худшим", "Вин Дизель", 1043)

B1.get_info()  
 
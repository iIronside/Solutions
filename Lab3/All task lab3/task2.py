# Напишите классы «Книга» (с обязательными полями: название, автор, код),
# «Библиотека» (с обязательными полями: адрес, номер) и корректно свяжите их.
# Код книги должен назначаться автоматически при добавлении книги в библиотеку
# (используйте для этого статический член класса). Если в конструкторе книги
# указывается в параметре пустое название, необходимо сгенерировать исключение
# (например, ValueError). Книга должна реализовывать интерфейс Taggable с методом
# tag(), который создает на основе строки набор тегов (разбивает строку на слова
# и возвращает только те, которые начинаются с большой буквы). Например, tag() для
# книги с названием ‘War and Peace’ вернет список тегов [‘War’, ‘Peace’].


from zope.interface import Interface, implementer


class ITaggable(Interface):

    def tag(self):
        """Create tags"""


class Library(object):

    def __init__(self, address, number):
        self.lib_address = address
        self.lib_number = number
        self.books = []

    def add_book(self, book):
        #book.
        self.books.append(book)



@implementer(ITaggable)
class Book(object):

    def __init__(self, name, author):
        self.name_book = name
        self.author_book = author
        self.code_book = -1

    def tag(self):
        print('555')


book1 = Book('111','')
book2 = Book('2','1')
lib = Library('fgfkldngljfkb', 55)
lib.add_book(book1)
print(lib.books[0])

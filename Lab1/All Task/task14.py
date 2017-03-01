# Напишите декоратор non_empty, который дополнительно проверяет списковый
# результат любой функции: если в нем содержатся пустые строки или значение
# None, то они удаляются.


def non_empty(func):
    def _wrapper():
        pages = [i for i in func() if i != '' and i is not None]  # func()???
        return pages
    return _wrapper


@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1', None]

print(get_pages())

# Напишите параметризированный декоратор pre_process, который осуществляет
# предварительную обработку (цифровую фильтрацию) списка по алгоритму:
# s[i] = s[i]–a∙s[i–1]. Параметр а можно задать в коде (по умолчанию равен 0.97).

s = [5, 1, 3, 4, 2]


def pre_process(a):
    def _decorator(func):
        def _wrapper(args):
            arg = [round(args[i]-a*s[i-1], 2) for i in range(len(args))]
            return func(arg)
        return _wrapper
    return _decorator


@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)


plot_signal(s)

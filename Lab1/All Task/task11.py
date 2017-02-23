# Напишите генератор frange как аналог range() с дробным шагом.


def frange(stop, start=0.0, step=0.1):
    while start < stop:
        yield round(start + step, 1)
        start += step

for x in frange(5, 1, 0.1):
    print(x)
help(range)
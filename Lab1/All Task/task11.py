# Напишите генератор frange как аналог range() с дробным шагом.


def frange(start=0.0, stop=None, step=None):
    while start < stop - step:
        start = round(start + step, 1)
        yield start

for x in frange(0, 5, 0.1):
    print(x)

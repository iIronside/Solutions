# Напишите генератор get_frames(), который производит «оконную декомпозицию» сигнала:
# на основе входного списка генерирует набор списков – перекрывающихся отдельных
# фрагментов сигнала размера size со степенью перекрытия overlap.

def frange(start=0.0, stop=None, step=None):
    while start < stop - step:
        start = round(start + step, 1)
        yield start

for frame in get_frames(signal, size=1024, overlap=0.5):
    print(frame)


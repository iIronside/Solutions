# Напишите генератор get_frames(), который производит «оконную декомпозицию» сигнала:
# на основе входного списка генерирует набор списков – перекрывающихся отдельных
# фрагментов сигнала размера size со степенью перекрытия overlap.

import random


def get_frames(sig, size, overlap):
    step = int(size*overlap)
    start = 0
    end = size
    while end < len(sig)+step:
        cutSig = sig[start:end]
        start += step
        end += step
        yield cutSig


signal =[random.randint(0,12) for i in range(7)]
print(signal)

for frame in get_frames(signal, size=4, overlap=0.5):
    print(frame)

import time
import numpy as np
import matplotlib.pyplot as plt
massiv = np.random.normal(-10, 10, 10)
massiv2 = []
massiv2.extend(massiv)
#график исходного массива
fig, ax = plt.subplots()
X=list(range(1,len(massiv)+1))
ax.bar(X,massiv)
ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)    #  ширина Figure
fig.set_figheight(6)    #  высота Figure
plt.title('Линейчатая диаграмма исходного массива')
plt.xlabel('Значения индекса переменных массива', fontsize=16)
plt.ylabel('Значение переменной', fontsize=16)
plt.show()

chet = 0
chet1 = 0
print("-------------------------------------------------------------")
print("Сортировка массива методом выбора (Selection sort)")
print("\nисходный массив: \n",massiv)

def selection_sort(alist):
    global chet
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]
        chet += 1

start = time.time()
selection_sort(massiv)
end = time.time()
total = end - start
print("\nВремя выполнения сортировки методом Шелла: ", total)
print("Количество перемещений элементов методом Шелла:", chet)
print("Вид полученных значений в массив: численное")
print('Отсортированный массив методом выбора(Selection sort)\n')
print(massiv)
print("-------------------------------------------------------------")
print("Сортировка массива пирамидальной сортировкой(Heapsort)")
def heapsort(alist):
    global chet1
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)

def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1

def max_heapify(alist, index, size):
    global chet1
    l = left(index)
    r = right(index)
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)
        chet1 += 1

start = time.time()
heapsort(massiv2)
end = time.time()
total = end - start
print("\nВремя выполнения сортировки методом Heapsort: ", total)
print("Количество перемещений элементов методом Heapsort:", chet1)
print("Вид полученных значений в массив: численное")
print('Отсортированный массив методом Heapsort:\n')
print(massiv)

#отсортированная гистограмма метода выбора
fig, ax = plt.subplots()
X=list(range(1,len(massiv)+1))
ax.bar(X,massiv)
ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)    #  ширина Figure
fig.set_figheight(6)    #  высота Figure
plt.title('Линейчатая диаграмма полученного массива данных методом выбора')
plt.xlabel('Значения индекса переменных массива', fontsize=16)
plt.ylabel('Значение переменной', fontsize=16)

plt.show()

#отсортированная гистограмма метода Heapsort
fig, ax = plt.subplots()
X=list(range(1,len(massiv2)+1))
ax.bar(X,massiv2)
ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)    #  ширина Figure
fig.set_figheight(6)    #  высота Figure
plt.title('Линейчатая диаграмма полученного массива данных методом Heapsort')
plt.xlabel('Значения индекса переменных массива', fontsize=16)
plt.ylabel('Значение переменной', fontsize=16)

plt.show()
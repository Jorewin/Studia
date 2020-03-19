import random
import numpy
import sys


sys.setrecursionlimit(10**6)


def insertionsort(arr, start, stop):
    for i in range(stop + 1):
        p = i
        for j in range(i - 1, -1, -1):
            if arr[p] < arr[j]:
                arr[p], arr[j] = arr[j], arr[p]
                p = j
            else:
                break
    return


def bubblesort(arr, start, stop):
    for i in range(stop, -1, -1):
        done = True
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                done = False
        if done:
            return arr
    return


def selectionsort(arr, start, stop):
    for i in range(stop + 1):
        p = min(range(i, stop + 1), key=lambda key: arr[key])
        arr[i], arr[p] = arr[p], arr[i]
    return


def right_quicksort(arr, start, stop):
    if (stop - start + 1) < 2:
        return
    else:
        p = start
        for i in range(start, stop):
            if arr[i] < arr[stop]:
                arr[p], arr[i] = arr[i], arr[p]
                p += 1
        arr[stop], arr[p] = arr[p], arr[stop]
        right_quicksort(arr, start, p-1)
        right_quicksort(arr, p+1, stop)
        return


def random_quicksort(arr, start, stop):
    if (stop - start + 1) < 2:
        return
    else:
        p = random.randint(start, stop)
        arr[stop], arr[p] = arr[p], arr[stop]
        p = start
        for i in range(start, stop):
            if arr[i] < arr[stop]:
                arr[p], arr[i] = arr[i], arr[p]
                p += 1
        arr[stop], arr[p] = arr[p], arr[stop]
        random_quicksort(arr, start, p-1)
        random_quicksort(arr, p+1, stop)
        return


def mergesort(arr, start, stop):
    if (stop - start + 1) > 1:
        p = (start + stop) // 2
        left, right = numpy.copy(arr[start: p + 1]), numpy.copy(arr[p + 1: stop + 1])
        stop = right.size - 1
        mergesort(left, 0, p)
        mergesort(right, 0, stop)
        i, j = 0, 0
        while i <= p and j <= stop:
            if right[j] < left[i]:
                arr[j + i] = right[j]
                j += 1
            else:
                arr[j + i] = left[i]
                i += 1
        if i <= p:
            for k in range(i, p + 1):
                arr[j + k] = left[k]
        if j <= stop:
            for k in range(j, stop + 1):
                arr[i + k] = right[k]
    return


def heapmove(arr, p, i):
    while True:
        son = (p * 2 + 1)
        daughter = (p * 2 + 2)
        if daughter <= i:
            lower = max(son, daughter, key=lambda key: arr[key])
            if arr[p] < arr[lower]:
                arr[p], arr[lower] = arr[lower], arr[p]
                p = lower
            else:
                break
        elif son <= i:
            if arr[p] < arr[son]:
                arr[p], arr[son] = arr[son], arr[p]
                p = son
            else:
                break
        else:
            break


def heapsort(arr, start, stop):
    for i in range(stop, -1, -1):
        heapmove(arr, i, stop)
    for i in range(stop, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapmove(arr, 0, i-1)
    return


def countingsort(arr, start, stop):
    start = min(min(arr), 0) - 1
    stop = max(arr)
    lenght = stop - start + 1
    count = [0 for _ in range(lenght)]
    for number in arr:
        count[number] += 1
    for i in range(start + 1, stop + 1):
        count[i] += count[i-1]
        p = count[i]
        while p > count[i-1]:
            arr[p-1] = i
            p -= 1
    return


if __name__ == '__main__':
    import sys
    sys.exit()
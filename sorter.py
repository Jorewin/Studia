# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def insertionsort(arr):
    for i in range(len(arr)):
        current = arr.pop(i)
        for j in range(i):
            if current < arr[j]:
                arr.insert(j, current)
                break
        else:
            arr.insert(i, current)
    return


def bubblesort(arr):
    for i in range(len(arr) - 1, -1, -1):
        done = True
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                done = False
        if done:
            return arr
    return


def selectionsort(arr):
    for i in range(len(arr)):
        current = min(range(i, len(arr)), key=lambda key: arr[key])
        arr[i], arr[current] = arr[current], arr[i]
    return


def right_quicksort(arr, start=0, stop=None):
    if stop == None:
        stop = len(arr) - 1
    if (stop - start + 1) < 2:
        return
    else:
        p = start
        for i in range(start, stop):
            if arr[i] < arr[stop]:
                arr[p], arr[i] = arr[i], arr[p]
                p += 1
        arr[stop], arr[p] = arr[p], arr[stop]
        right_quicksort(arr, start= start, stop=p-1)
        right_quicksort(arr, start=p+1, stop=stop)
        return


def random_quicksort(arr, start=0, stop=None):
    if stop == None:
        stop = len(arr) - 1
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
        random_quicksort(arr, start= start, stop=p-1)
        random_quicksort(arr, start=p+1, stop=stop)
        return


def mergesort(arr, start=0, stop=None):
    if stop == None:
        stop = len(arr) - 1
    if (stop - start + 1) > 1:
        p = (start + stop) // 2
        mergesort(arr, start=start, stop=p)
        mergesort(arr, start=p+1, stop=stop)
        i, j = start, p+1
        while i <= p and j <= stop:
            if arr[j] <= arr[i]:
                current = arr.pop(j)
                arr.insert(i, current)
                p += 1
                j += 1
            i += 1
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


def heapsort(arr):
    for i in range(len(arr)):
        p = arr.pop(i)
        arr.insert(0, p)
        heapmove(arr, 0, i)
    for i in range(len(arr)-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapmove(arr, 0, i-1)
    return


def countingsort(arr):
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
    import json
    import random
    import timeit
    import os.path
    import numpy
    import matplotlib.pyplot as plt
    import sys


    data_switch = {}
    switch = {}
    sort_switch = {}


    def addtoswitch(func, name=None, target=switch):
        """Internal function that makes the terminal work"""
        if isinstance(name, str):
            target[name] = func
        else:
            target[func.__name__] = func


    def ascending(arr):
        return sorted(arr)


    def descending(arr):
        return sorted(arr)[::-1]


    def randomized(arr):
        return arr


    def constant(arr):
        current = random.choice(arr)
        arr = [current for i in range(len(arr))]
        return arr


    def A_shaped(arr):
        arr = sorted(arr)
        current = random.randint(0, len(arr))
        return arr[:current:]+ arr[current::][::-1]


    def save(key, value):
        """Internal save function"""
        source = open('save.json', 'r')
        settings = json.load(source)
        source.close()
        if key in settings:
            settings[key] = value
            with open('save.json', 'w') as target:
                json.dump(settings, target)
            print('Setting saved successfully.')
        else:
            print(f'{key} is not a defined setting.')


    def myhelp(name=None, *args):
        """
        ==============
        help command_name
        ==============

        Shows documentation of chosen command.

        Arguments:
        command_name: name of the command

        """
        if len(args) != 0:
            print('Too many arguments were given.')
        elif (func := switch.get(name)) != None:
            print(func.__doc__)
        else:
            print(f'{name} is not a defined command.')


    def mylist(*args):
        """
        ====
        list
        ====

        Shows the list o available commands.
        """
        if len(args) != 0:
            print('Too many arguments were given.')
        else:
            print('Available commands:')
            for command in switch:
                print('\t+', command)
            print('Type help [command_name] to get info about specific command.')


    def mysort(name=None, *arr):
        """
        =======================
        sort sort_algorythm arr
        =======================

        Runs chosen sort function.

        Arguments:
        sort_algorythm: one of the available algorythms name
        arr: set of int with base 10 seperated with spaces
        """
        if (func := sort_switch.get(name)) == None:
            print(f'{name} is not an available sort algorythm')
        else:
            try:
                arr = list(map(int, arr))
            except ValueError:
                print(f'Array should be composed of integers with base 10 only.')
            else:
                func(arr)
                print(arr)


    def sayhi(*args):
        """
        sayhi
        ==

        Says hi
        """
        if len(args) != 0:
            print('Too many arguments were given.')
        else:
            print('hi')


    def myset(key=None, value=0, *args):
        """
        ==============
        set key value
        ==============

        Let's user alter the seetings of data generation.

        Arguments:
        key: one of the following:
                + n - number of repetitions of each lenght
                + l - lenght of base test case
                + d - diiference between test cases lenght
                + s - the lowest number that can  be generated
                + e - the highest number that can be generated
                + seed
        value: int with base 10 which will be assigned to the chosen key
        """
        if len(args) != 0:
            print('Too many arguments were given.')
        else:
            try:
                value = int(value)
            except ValueError:
                print('Every setting argument should be an integer with base 10.')
            else:
                save(key, value)


    def genseed(lenght=1, *args):
        """
        ==============
        genseed lenght
        ==============

        Generates seed.

        Arguments:
        lenght: lenght of the seed default = 1
        """
        if len(args) != 0:
            print('Too many arguments were given.')
        else:
            try:
                lenght = int(lenght)
            except ValueError:
                lenght = 1
            if lenght < 1:
                lenght = 1
            random.seed()
            result = random.randint(10 ** (lenght - 1), 10 ** lenght)
            print(result)
            save('seed', result)


    def backup(*args):
        """
        ======
        backup
        ======

        Backs up the settings."""
        if len(args) != 0:
            print('Too many arguments were given.')
        else:
            with open('save.json', 'r') as source:
                data = json.load(source)
            with open('backup.json', 'w') as target:
                json.dump(data, target)
            print('Backup done successfully.')


    def restore(*args):
        """
        =======
        restore
        =======

        Restores settings from backup.json
        """
        if len(args) != 0:
            print('Too many arguments were given.')
        elif not os.path.isfile('backup.json'):
            print('There is no backup to restore.')
        else:
            with open('backup.json', 'r') as source:
                data = json.load(source)
            with open('save.json', 'w') as target:
                json.dump(data, target)
            print('Data restored successfully.')


    def gendata(*args):
        """
        =======
        gendata type
        =======

        Generates data based on the settings from save.json file, and saves it in 'data.json'.
        """
        if len(args) != 0:
            print('Too many arguments were given.')
        else:
            with open('save.json', 'r') as source:
                settings = json.load(source)
            data = {}
            random.seed(settings['seed'])
            total = len(data_switch) * 10 * settings['n']
            iteration = 0
            printProgressBar(iteration, total, prefix='Progress:', suffix='Complete', length=50)
            for kind in data_switch:
                data[kind] = []
                for i in range(10):
                    block = []
                    for j in range(settings['n']):
                        current = [random.randint(settings['s'], settings['e']) for _ in
                                   range(settings['l'] + settings['d'] * i)]
                        current = data_switch[kind](current)
                        block.append(current)
                        iteration += 1
                        printProgressBar(iteration, total, prefix='Progress:', suffix='Complete', length=50)
                    data[kind].append(block)
            data['settings'] = settings
            with open('data.json', 'w') as target:
                json.dump(data, target)
            print('Data generated successfully.')


    def processdata(*args):
        """
        ===========
        processdata
        ===========

        Tests defined algorythms using data from 'data.json', results are saved in 'processed_data.json'.
        """
        if len(args) != 0:
            print('Too many arguments were given.')
        elif not os.path.isfile('data.json'):
            print('No data found. Use gendata command first.')
        else:
            with open('data.json', 'r') as source:
                data = json.load(source)
            settings = data['settings']
            result = {}
            total = len(data_switch) * len(sort_switch) * 10 * settings['n']
            iteration = 0
            printProgressBar(iteration, total, prefix='Progress:', suffix='Complete', length=50)
            for algorythm in sort_switch:
                result[algorythm] = {}
                for kind in data_switch:
                    result[algorythm][kind] = []
                    for i in range(10):
                        average = 0
                        for arr in data[kind][i]:
                            stmt = 'setrecursionlimit(10**6)\nfunc(arr)'
                            setup = f"from __main__ import {algorythm} as func; from sys import setrecursionlimit; arr = {str(arr)}"
                            current = timeit.timeit(stmt=stmt, setup=setup, number=1)
                            average += current
                            iteration += 1
                            printProgressBar(iteration, total, prefix='Progress:', suffix='Complete', length=50)
                        average /= settings['n']
                        result[algorythm][kind].append(average)
            result['settings'] = settings
            with open('processed_data.json', 'w') as target:
                json.dump(result, target)
            print('Data processed successfully')


    def plotdata(*args):
        if len(args) != 0:
            print('Too many arguments were given.')
        elif not os.path.isfile('processed_data.json'):
            print('No data found. Use processdata command first.')
        else:
            with open('processed_data.json', 'r') as source:
                data = json.load(source)
            settings = data['settings']
            x = numpy.arange(settings['l'], settings['l'] + settings['d'] * 9, settings['d'])
            for algorythm in sort_switch:
                for kind in data_switch:
                    y = numpy.asarray(data[algorythm][kind])
                    plt.plot(x, y,  label=kind)
                plt.title(algorythm)
                plt.legend()
                plt.xlabel('Lenght of the test case')
                plt.ylabel('Time [s]')
                plt.grid(True)
                plt.savefig(f'{algorythm}.png')
                plt.clf()
        print('Plotting done successfully')


    addtoswitch(ascending, target=data_switch)
    addtoswitch(descending, target=data_switch)
    addtoswitch(randomized, target=data_switch)
    addtoswitch(constant, target=data_switch)
    addtoswitch(A_shaped, target=data_switch)
    addtoswitch(insertionsort, target=sort_switch)
    addtoswitch(bubblesort, target=sort_switch)
    addtoswitch(selectionsort, target=sort_switch)
    addtoswitch(right_quicksort, target=sort_switch)
    addtoswitch(random_quicksort, target=sort_switch)
    addtoswitch(mergesort, target=sort_switch)
    addtoswitch(heapsort, target=sort_switch)
    addtoswitch(countingsort, target=sort_switch)
    addtoswitch(myhelp, name='help')
    addtoswitch(mylist, name='list')
    mysort.__doc__ += '\n\t\tAvailable algorythms:'
    for algorythm in sort_switch:
        mysort.__doc__ += ('\n\t\t\t+' + algorythm)
    addtoswitch(mysort, name='sort')
    addtoswitch(sayhi)
    addtoswitch(myset, name="set")
    addtoswitch(genseed)
    addtoswitch(backup)
    addtoswitch(restore)
    addtoswitch(gendata)
    addtoswitch(processdata)
    addtoswitch(plotdata)


    if not os.path.isfile('save.json'):
        with open('save.json', 'w') as target:
            json.dump({'n': 10, 'l': 50, 'd': 50, 's': 1, 'e': 100, 'seed': 9}, target)
    print('Sorter by Jakub Błażejowski', 'Type list to get list of available commands.', sep='\n')
    while True:
        print('>>', end=' ')
        data = input().split()
        while '' in data:
            data.remove('')
        if not data:
            continue
        command, *arguments = data
        if command == 'exit':
            print('Process terminated')
            break
        elif func := switch.get(command):
            func(*arguments)
        else:
            print(f'{command} is not a defined command')


def insertionsort(arr):
    for i in range(len(arr)):
        current = arr.pop(i)
        for j in range(i):
            if current < arr[j]:
                arr.insert(j, current)
                break
        else:
            arr.insert(i, current)
    return arr


def bubblesort(arr):
    for i in range(len(arr) - 1, -1, -1):
        done = True
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                done = False
        if done:
            return arr
    return arr


def selectionsort(arr):
    for i in range(len(arr)):
        current = min(range(i, len(arr)), key=lambda key: arr[key])
        arr[i], arr[current] = arr[current], arr[i]
    return arr


def quicksort(arr):
    pass


if __name__ == '__main__':
    import json
    import random
    import timeit
    import os.path
    import numpy
    import matplotlib.pyplot as plt
    import matplotlib as mpl


    data_switch = {}
    switch = {}
    sort_switch = {}


    def addtoswitch(func, name=None, target=switch):
        """Internal function that makes the terminal work"""
        if name and isinstance(name, str):
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
        if len(args):
            print('Too many arguments were given.')
        elif func := switch.get(name):
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
        if len(args):
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
        if not (func := sort_switch.get(name)):
            print(f'{name} is not an available sort algorythm')
        else:
            try:
                arr = list(map(int, arr))
            except ValueError:
                print(f'Array should be composed of integers with base 10 only.')
            else:
                print(func(arr))


    def sayhi(*args):
        """
        sayhi
        ==

        Says hi
        """
        if len(args):
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
        if len(args):
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
        if len(args):
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
        if len(args):
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
        if len(args):
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
        if len(args):
            print('Too many arguments were given.')
        else:
            with open('save.json', 'r') as source:
                settings = json.load(source)
            data = {}
            random.seed(settings['seed'])
            for kind in data_switch:
                data[kind] = []
                for i in range(10):
                    block = []
                    for j in range(settings['n']):
                        current = [random.randint(settings['s'], settings['e']) for _ in
                                   range(settings['l'] + settings['d'] * i)]
                        current = data_switch[kind](current)
                        block.append(current)
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
        if len(args):
            print('Too many arguments were given.')
        elif not os.path.isfile('data.json'):
            print('No data found. Use gendata command first.')
        else:
            with open('data.json', 'r') as source:
                data = json.load(source)
            settings = data['settings']
            result = {}
            for algorythm in sort_switch:
                result[algorythm] = {}
                for kind in data_switch:
                    result[algorythm][kind] = []
                    for i in range(10):
                        average = 0
                        for arr in data[kind][i]:
                            charray = f"from __main__ import {algorythm} as func; arr = {str(arr)}"
                            current = timeit.timeit(stmt='func(arr)', setup=charray, number=1)
                            average += current
                        average /= settings['n']
                        result[algorythm][kind].append(average)
            result['settings'] = settings
            with open('processed_data.json', 'w') as target:
                json.dump(result, target)
            print('Data processed successfully')


    def plotdata(*args):
        if len(args):
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
    # addtoswitch(quicksort, target=sort_switch)
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


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


if __name__ == '__main__':
    import sys
    import json
    import random
    import timeit
    import os
    import os.path
    import numpy
    import matplotlib.pyplot as plt
    if os.path.isfile('sorts.py'):
        import sorts
    else:
        print('File including sorting algorythms was not detected.')
        sys.exit()
    if sys.version_info < (3, 8):
        print('Please use Python 3.8 or higher')
        sys.exit()

    data_switch = {}
    switch = {}
    sort_switch = {}
    sys.setrecursionlimit(10**6)

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
        source = open('settings.json', 'r')
        settings = json.load(source)
        source.close()
        if key in settings:
            settings[key] = value
            with open('settings.json', 'w') as target:
                json.dump(settings, target)
            print('Setting saved successfully.')
        else:
            print(f'{key} is not a defined setting.')


    def myexit(*args):
        """
        ====
        exit
        ====
        
        Terminates the process.
        """
        if len(args) != 0:
            print('Too many arguments were given')
        else:
            print('Process terminated')
            sys.exit()
        
        
    def myhelp(name=None, *args):
        """
        =================
        help command_name
        =================

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
                arr = numpy.asarray(arr)
                func(arr, 0, arr.size - 1)
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

    
    def currentsettings(*args):
        """
        ========
        settings
        ========

        Shows settings stored in 'settings.json'.
        """
        if len(args) != 0:
            print('Too many arguments were given')
        else:
            with open('settings.json', 'r') as source:
                settings = json.load(source)
            print('Current settings:')
            for setting in settings:
                print(f'\t{setting} -> {settings[setting]}')


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
            with open('settings.json', 'r') as source:
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
            with open('settings.json', 'w') as target:
                json.dump(data, target)
            print('Data restored successfully.')


    def gendata(name=None, *args):
        """
        ============
        gendata type
        ============

        Generates data.

        Arguments:
        type (optional): one of available types of data to be regenerated
        """
        if len(args) != 0:
            print('Too many arguments were given.')
        else:
            if name != None:
                if data_switch.get(name) != None:
                    kinds = {name: data_switch[name]}
                else:
                    print(f'{name} is not an available data type')
                    return
                if os.path.isfile('data/settings.json'):
                   with open('data/settings.json', 'r') as source:
                       settings = json.load(source)
                else:
                   print('To regenerate type of data you have to generate all data first')
                   return
            else:
                kinds = data_switch
                with open('settings.json', 'r') as source:
                    settings = json.load(source)
            random.seed(settings['seed'])
            total = len(kinds) * 10 * settings['n']
            iteration = 0
            printProgressBar(iteration, total, prefix='Progress:', suffix='Complete', length=50)
            for kind in kinds:
                data = []
                for i in range(10):
                    for j in range(settings['n']):
                        current = [random.randint(settings['s'], settings['e']) for _ in
                                   range(settings['l'] + settings['d'] * i)]
                        current = data_switch[kind](current)
                        current = numpy.asarray(current)
                        data.append(current)
                        iteration += 1
                        printProgressBar(iteration, total, prefix='Progress:', suffix='Complete', length=50)
                data = numpy.asarray(data)
                numpy.save(f'data/{kind}.npy', data)
            with open('data/settings.json', 'w') as target:
                json.dump(settings, target)
            print('Data generated successfully.')


    def processdata2(*args):
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
                            stmt = 'setrecursionlimit(10**6)\nfunc(arr, 0, stop)'
                            setup = f"from sorts import {algorythm} as func; from sys import setrecursionlimit; arr = {str(arr)}; stop = {len(arr) - 1}"
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


    def processbyalgorythm(name=None, *args):
        """
        ===================================
        processbyalgorythm [sort_algorythm]
        ===================================

        Tests defined algorythms.

        Arguments:
        sort_algorythm (optional): one of the available algorythms name
        """
        if len(args) != 0:
            print('Too many arguments were given.')
        elif not os.path.isfile('data/settings.json'):
            print('No data found. Use gendata command first.')
        else:
            if name != None:
                if sort_switch.get(name) != None:
                    algorythms = {name: sort_switch[name]}
                else:
                    print(f'{name} is not an available sorting algorythm')
                    return
            else:
                algorythms = sort_switch
            with open('data/settings.json', 'r') as source:
                settings = json.load(source)
            total = len(data_switch) * len(algorythms) * 10 * settings['n']
            iteration = 0
            printProgressBar(iteration, total, prefix='Progress:', suffix='Complete', length=50)
            for algorythm in algorythms:
                if not os.path.isdir(f'processed_data/{algorythm}'):
                    os.mkdir(f'processed_data/{algorythm}')
                for kind in data_switch:
                    data = numpy.load(f'data/{kind}.npy', allow_pickle=True)
                    result = numpy.zeros(10)
                    for i in range(-1, 10):
                        average = 0
                        for j in range(settings['n']):
                            # stmt = 'setrecursionlimit(10**6)\nfunc(arr, 0, stop)'
                            #setup = f"from sorts import {algorythm} as func; from sys import setrecursionlimit; arr = {str(arr)}; stop = {len(arr) - 1}"
                            # current = timeit.timeit(stmt=stmt, setup=setup, number=1)
                            data[i+j] = numpy.asarray(data[i+j])
                            def func():
                                sort_switch[algorythm](data[i+j], 0, data[i+j].size - 1)
                            current = timeit.timeit(func, number=1)
                            average += current
                            iteration += 1
                            printProgressBar(iteration, total, prefix=f'Progress: ', suffix='Complete', length=50)
                        average /= settings['n']
                        result[i] = average

                    numpy.savetxt(f'processed_data/{algorythm}/{kind}.csv', result, delimiter=',')
                with open(f'processed_data/{algorythm}/settings.json', 'w') as target:
                    json.dump(settings, target)
            print('Data processed successfully')


    def processbytype(name=None, *args):
        """
        ============================
        processbytype [type]
        ============================

        Tests defined algorythms.

        Arguments:
        type (optional): one of the available types
        """
        if len(args) != 0:
            print('Too many arguments were given.')
        elif not os.path.isfile('data/settings.json'):
            print('No data found. Use gendata command first.')
        else:
            if name != None:
                if data_switch.get(name) != None:
                    kinds = {name: data_switch[name]}
                else:
                    print(f'{name} is not an available data type')
                    return
            else:
                kinds = data_switch
            with open('data/settings.json', 'r') as source:
                settings = json.load(source)
            total = len(kinds) * len(sort_switch) * 10 * settings['n']
            iteration = 0
            printProgressBar(iteration, total, prefix='Progress:', suffix='Complete', length=50)
            for kind in kinds:
                for algorythm in sort_switch:
                    if not os.path.isdir(f'processed_data/{algorythm}'):
                        os.mkdir(f'processed_data/{algorythm}')
                    data = numpy.load(f'data/{kind}.npy', allow_pickle=True)
                    result = numpy.zeros(10)
                    for i in range(-1, 10):
                        average = 0
                        for j in range(settings['n']):
                            # stmt = 'setrecursionlimit(10**6)\nfunc(arr, 0, stop)'
                            #setup = f"from sorts import {algorythm} as func; from sys import setrecursionlimit; arr = {str(arr)}; stop = {len(arr) - 1}"
                            # current = timeit.timeit(stmt=stmt, setup=setup, number=1)
                            data[i+j] = numpy.asarray(data[i+j])
                            def func():
                                sort_switch[algorythm](data[i+j], 0, data[i+j].size - 1)
                            current = timeit.timeit(func, number=1)
                            average += current
                            iteration += 1
                            printProgressBar(iteration, total, prefix=f'Progress: ', suffix='Complete', length=50)
                        average /= settings['n']
                        result[i] = average
                    numpy.savetxt(f'processed_data/{algorythm}/{kind}.csv', result, delimiter=',')
                    with open(f'processed_data/{algorythm}/settings.json', 'w') as target:
                        json.dump(settings, target)
            print('Data processed successfully')


    def plotdata(*args):
        """
        ========
        plotdata
        ========

        Creates figures.
        """
        if len(args) != 0:
            print('Too many arguments were given.')
        else:
            for algorythm in sort_switch:
                if not os.path.isfile(f'processed_data/{algorythm}/settings.json'):
                    continue
                with open(f'processed_data/{algorythm}/settings.json', 'r') as source:
                    settings = json.load(source)
                x = numpy.arange(settings['l'], settings['l'] + settings['d'] * 10, settings['d'])
                for kind in data_switch:
                    y = numpy.loadtxt(f'processed_data/{algorythm}/{kind}.csv', delimiter=',')
                    plt.plot(x, y, marker='o', label=kind)
                plt.title(algorythm)
                plt.legend()
                plt.xlabel('Lenght of the test case')
                plt.ylabel('Time [s]')
                plt.grid(True)
                plt.savefig(f'figures/{algorythm}.png')
                plt.clf()
            for kind in data_switch:
                for algorythm in sort_switch:
                    if not os.path.isfile(f'processed_data/{algorythm}/settings.json'):
                        continue
                    with open(f'processed_data/{algorythm}/settings.json', 'r') as source:
                        settings = json.load(source)
                    x = numpy.arange(settings['l'], settings['l'] + settings['d'] * 10, settings['d'])
                    y = numpy.loadtxt(f'processed_data/{algorythm}/{kind}.csv', delimiter=',')
                    plt.plot(x, y, marker='o', label=algorythm)
                plt.title(kind)
                plt.legend()
                plt.xlabel('Lenght of the test case')
                plt.ylabel('Time [s]')
                plt.grid(True)
                plt.savefig(f'figures/{kind}.png')
                plt.clf()
        print('Plotting done successfully')


    def createswicthes():
        addtoswitch(ascending, target=data_switch)
        addtoswitch(descending, target=data_switch)
        addtoswitch(randomized, target=data_switch)
        addtoswitch(constant, target=data_switch)
        addtoswitch(A_shaped, target=data_switch)
        addtoswitch(sorts.insertionsort, target=sort_switch)
        addtoswitch(sorts.bubblesort, target=sort_switch)
        addtoswitch(sorts.selectionsort, target=sort_switch)
        addtoswitch(sorts.right_quicksort, target=sort_switch)
        addtoswitch(sorts.random_quicksort, target=sort_switch)
        addtoswitch(sorts.mergesort, target=sort_switch)
        addtoswitch(sorts.heapsort, target=sort_switch)
        addtoswitch(sorts.countingsort, target=sort_switch)
        addtoswitch(myexit, name='exit')
        addtoswitch(myhelp, name='help')
        addtoswitch(mylist, name='list')
        mysort.__doc__ += '\n\t\tAvailable algorythms:'
        processbyalgorythm.__doc__ += '\n\t\tAvailable algorythms:'
        for algorythm in sort_switch:
            mysort.__doc__ += ('\n\t\t\t+' + algorythm)
            processbyalgorythm.__doc__ += ('\n\t\t\t+' + algorythm)
        processbytype.__doc__ += '\n\t\tAvailable data types:'
        gendata.__doc__ += '\n\t\tAvailable data types:'
        for kind in data_switch:
            processbytype.__doc__ += ('\n\t\t\t+' + kind)
            gendata.__doc__ += ('\n\t\t\t+' + kind)
        addtoswitch(mysort, name='sort')
        addtoswitch(sayhi)
        addtoswitch(currentsettings)
        addtoswitch(myset, name="set")
        addtoswitch(genseed)
        addtoswitch(backup)
        addtoswitch(restore)
        addtoswitch(gendata)
        addtoswitch(processbyalgorythm)
        addtoswitch(processbytype)
        addtoswitch(plotdata)


    if not os.path.isfile('settings.json'):
        with open('settings.json', 'w') as target:
            json.dump({'n': 10, 'l': 6000, 'd': 6000, 's': 1, 'e': 60000, 'seed': 736784978}, target)
    if not os.path.isdir('processed_data'):
        os.mkdir('processed_data')
    if not os.path.isdir('figures'):
        os.mkdir('figures')
    if not os.path.isdir('data'):
        os.mkdir('data')
    print('Sorter by Jakub Błażejowski', 'Type list to get list of available commands.', sep='\n')
    createswicthes()
    while True:
        print('>>', end=' ')
        data = input().split()
        while '' in data:
            data.remove('')
        if not data:
            continue
        command, *arguments = data
        if func := switch.get(command):
            func(*arguments)
        else:
            print(f'{command} is not a defined command')


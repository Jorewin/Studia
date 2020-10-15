import sys
import re
import json
import random
import timeit
import os
import os.path
import numpy
import matplotlib.pyplot as plt
import sorts


class Switch():
    def __init__(self):
        self.command_switch = {}
        self.kind_switch = {}
        self.sort_switch = {}


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


def addtoswitch(func, switch, name=None):
    """Internal function that makes the terminal work"""
    if isinstance(name, str):
        switch[name] = func
    else:
        switch[func.__name__] = func


def myexit(control, *args):
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


def myhelp(control, name=None, *args):
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
    elif (func := control.command_switch.get(name)) != None:
        print(func.__doc__)
    else:
        print(f'{name} is not a defined command.')


def mylist(control, *args):
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
        for command in control.command_switch:
            print('\t+', command)
        print('Type help [command_name] to get info about specific command.')


def myclear(control, *args):
    """
    =====
    clear
    =====

    Clear the screen
    """
    if len(args) != 0:
        print('Too many arguments were given.')
    elif os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def mysort(control, name=None, *arr):
    """
    =======================
    sort sort_algorythm arr
    =======================

    Runs chosen sort function.

    Arguments:
    sort_algorythm: one of the available algorythms name
    arr: set of int with base 10 seperated with spaces
    """
    if (func := control.sort_switch.get(name)) == None:
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


def currentsettings(control, *args):
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


def myset(control, key=None, value=0, *args):
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


def genseed(control, lenght=1, *args):
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


def backup(control, *args):
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


def restore(control, *args):
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


def gendata(control, *args):
    """
    ========
    gendata
    ========

    Generates data.
    """
    if len(args) != 0:
        print('Too many arguments were given.')
    else:
        with open('settings.json', 'r') as source:
            settings = json.load(source)
        random.seed(settings['seed'])
        total = len(control.kind_switch) * 10 * settings['n']
        iteration = 0
        printProgressBar(iteration, total, prefix='Progress:', suffix='Complete', length=50)
        for kind in control.kind_switch:
            data = []
            for i in range(10):
                for j in range(settings['n']):
                    current = [random.randint(1, settings['l'] + (settings['d'] * i) // 8) for _ in
                               range(settings['l'] + (settings['d'] * i))]
                    current = control.kind_switch[kind](current)
                    current = numpy.asarray(current)
                    data.append(current)
                    iteration += 1
                    printProgressBar(iteration, total, prefix='Progress:', suffix='Complete', length=50)
            data = numpy.asarray(data)
            numpy.save(f'data/{kind}.npy', data)
        with open('data/settings.json', 'w') as target:
            json.dump(settings, target)
        print('Data generated successfully.')


def processdata(control, *args, **kwargs):
    """
    ======================================================
    processdata -s [sort_algorythm] -t [type] -n [number]
    ======================================================

    Tests defined algorythms.

    Keyword Arguments:
    -s sort_algorythm (optional): one of the available algorythms name
    -t type (optional): one of the available types
    -n number (optional): test case number (1 - 10)
    """
    if len(args) != 0:
        print('Too many arguments were given.')
    elif not os.path.isfile('data/settings.json'):
        print('No data found. Use gendata command first.')
    else:
        if kwargs.get('-s') != None:
            if control.sort_switch.get(kwargs['-s']) != None:
                algorythms = {kwargs['-s']: control.sort_switch[kwargs['-s']]}
            else:
                print(f'{kwargs["-s"]} is not an available sorting algorythm')
                return
        else:
            algorythms = control.sort_switch

        if kwargs.get('-t') != None:
            if control.kind_switch.get(kwargs['-t']) != None:
                kinds = {kwargs['-t']: control.kind_switch[kwargs['-t']]}
            else:
                print(f'{kwargs["-t"]} is not an available data type')
                return
        else:
            kinds = control.kind_switch

        if kwargs.get('-n') != None:
            try:
                case = int(kwargs['-n'])
            except TypeError:
                print('Number has to be an integer with base 10.')
                return
            if case <= 10 and case >= 1:
                cases = [case - 1]
            else:
                print(f'{case} is not an available case number')
                return
        else:
            cases = range(9, -1, -1)

        with open('data/settings.json', 'r') as source:
            settings = json.load(source)
        total = len(kinds) * len(algorythms) * len(cases) * settings['n']
        iteration = 0
        printProgressBar(iteration, total, prefix='Progress:', suffix='Complete', length=50)
        for algorythm in algorythms:
            if not os.path.isdir(f'processed_data/{algorythm}'):
                os.mkdir(f'processed_data/{algorythm}')
            for kind in kinds:
                data = numpy.load(f'data/{kind}.npy', allow_pickle=True)
                if os.path.isfile(f'processed_data/{algorythm}/{kind}.csv'):
                    result = numpy.loadtxt(f'processed_data/{algorythm}/{kind}.csv', delimiter=',')
                else:
                    result = numpy.zeros(10)
                for i in cases:
                    average = 0
                    for j in range(settings['n']):
                        def func():
                            arr = data[i * settings['n'] + j]
                            control.sort_switch[algorythm](arr, 0, arr.size - 1)

                        time = timeit.timeit(stmt=func, number=10)
                        time /= 10
                        average += time
                        iteration += 1
                        printProgressBar(iteration, total, prefix=f'Progress: ', suffix='Complete', length=50)
                    average /= settings['n']
                    result[i] = average
                numpy.savetxt(f'processed_data/{algorythm}/{kind}.csv', result, delimiter=',')
            with open(f'processed_data/{algorythm}/settings.json', 'w') as target:
                json.dump(settings, target)
        print('Data processed successfully')


def plotdata(control, *args):
    """
    ========
    plotdata
    ========

    Creates figures.
    """
    if len(args) != 0:
        print('Too many arguments were given.')
    else:
        for algorythm in control.sort_switch:
            if not os.path.isfile(f'processed_data/{algorythm}/settings.json'):
                continue
            with open(f'processed_data/{algorythm}/settings.json', 'r') as source:
                settings = json.load(source)
            x = numpy.arange(settings['l'], settings['l'] + settings['d'] * 10, settings['d'])
            for kind in control.kind_switch:
                y = numpy.loadtxt(f'processed_data/{algorythm}/{kind}.csv', delimiter=',')
                plt.plot(x, y, marker='o', label=kind)
            plt.title(algorythm)
            plt.legend()
            plt.xlabel('Lenght of the test case')
            plt.ylabel('Time [s]')
            plt.grid(True)
            plt.savefig(f'figures/algorythms/{algorythm}.png')
            plt.clf()
        for kind in control.kind_switch:
            for algorythm in control.sort_switch:
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
            plt.savefig(f'figures/data_types/{kind}.png')
            plt.clf()
    print('Plotting done successfully')


def createswitches(control):
    addtoswitch(ascending, control.kind_switch)
    addtoswitch(descending, control.kind_switch)
    addtoswitch(randomized, control.kind_switch)
    addtoswitch(constant, control.kind_switch)
    addtoswitch(A_shaped, control.kind_switch)
    addtoswitch(sorts.insertionsort, control.sort_switch)
    addtoswitch(sorts.bubblesort, control.sort_switch)
    addtoswitch(sorts.selectionsort, control.sort_switch)
    addtoswitch(sorts.right_quicksort, control.sort_switch)
    addtoswitch(sorts.random_quicksort, control.sort_switch)
    addtoswitch(sorts.mergesort, control.sort_switch)
    addtoswitch(sorts.heapsort, control.sort_switch)
    addtoswitch(sorts.countingsort, control.sort_switch)
    addtoswitch(sorts.shellsort, control.sort_switch)
    addtoswitch(myexit, control.command_switch, name='exit')
    addtoswitch(myhelp, control.command_switch, name='help')
    addtoswitch(mylist, control.command_switch, name='list')
    addtoswitch(myclear, control.command_switch, name='clear')
    mysort.__doc__ += '\n\t\tAvailable algorythms:'
    processdata.__doc__ += '\n\t\tAvailable algorythms:'
    for algorythm in control.sort_switch:
        mysort.__doc__ += ('\n\t\t\t+ ' + algorythm)
        processdata.__doc__ += ('\n\t\t\t+ ' + algorythm)
    processdata.__doc__ += '\n\n\t\tAvailable data types:'
    gendata.__doc__ += '\n\t\tAvailable data types:'
    for kind in control.kind_switch:
        processdata.__doc__ += ('\n\t\t\t+ ' + kind)
        gendata.__doc__ += ('\n\t\t\t+ ' + kind)
    addtoswitch(mysort, control.command_switch, name='sort')
    addtoswitch(currentsettings, control.command_switch, name='settings')
    addtoswitch(myset, control.command_switch, name="set")
    addtoswitch(genseed, control.command_switch)
    addtoswitch(backup, control.command_switch)
    addtoswitch(restore, control.command_switch)
    addtoswitch(gendata, control.command_switch)
    addtoswitch(processdata, control.command_switch)
    addtoswitch(plotdata, control.command_switch)


if __name__ == '__main__':
    if sys.version_info < (3, 8):
        print('Please use Python 3.8 or higher')
        sys.exit()

    control = Switch()
    sys.setrecursionlimit(10**6)

    if not os.path.isfile('settings.json'):
        with open('settings.json', 'w') as target:
            json.dump({'n': 10, 'l': 6000, 'd': 6000, 'seed': 736784978}, target)
    if not os.path.isdir('processed_data'):
        os.mkdir('processed_data')
    if not os.path.isdir('figures'):
        os.mkdir('figures')
    if not os.path.isdir('data'):
        os.mkdir('data')
    if not os.path.isdir('figures/algorythms'):
        os.mkdir('figures/algorythms')
    if not os.path.isdir('figures/data_types'):
        os.mkdir('figures/data_types')
    print('Sorter by Jakub Błażejowski', 'Type list to get list of available commands.', sep='\n')
    createswitches(control)
    while True:
        print('>>', end=' ')
        data = input().split()
        kwarguments = {}
        for i in range(len(data) - 1, -1, -1):
            if data[i] == ' ':
                del data[i]
        if not data:
            continue
        for i in range(len(data) - 1, -1, -1):
            if match := re.match('^-.$', data[i]):
                del data[i]
                try:
                    kwarguments[match.string] = data[i]
                    del data[i]
                except KeyError:
                    print(f'{match.string} value not found.')
        command, *arguments = data
        if func := control.command_switch.get(command):
            func(control, *arguments, **kwarguments)
        else:
            print(f'{command} is not a defined command')
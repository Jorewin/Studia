import types
import functools
import re


def typecheck(value, _type) -> bool:
    """
    Returns 1 if value is _type type, 0 otherwise.

    :param value:
    :param _type:
    :return: 0 or 1
    :rtype: bool
    """
    if not isinstance(value, _type):
        return True
    return False


def addtoswitch(_func: types.FunctionType = None,* , switch: dict = None, name: str = None) -> types.FunctionType:
    """
    Adds function to pointed switch

    :param _func: Any not built-in python function.
    :type _func: types.FunctionType or None
    :param dict switch:
    :param name:
    :type name: str or None
    :return: input function
    :rtype: types.FunctionType
    :raises TypeError: if any of given arguments is of the wrong type
    """
    def decorator_addtoswitch(func: types.FunctionType) -> types.FunctionType:
        if typecheck(switch, dict):
            raise TypeError(f'Switch must be a dictionary, not a {type(switch)}.')
        if name == None:
            name = func.__name__
        if typecheck(name, str):
            raise TypeError(f'Name must be a string, not a {type(name)}.')
        switch[name] = func

        @functools.wraps(func)
        def wrapper_addtoswitch(*args, **kwargs):
            counter = 0
            kcounter = 0
            for label, _type in func.__annotations__.items():
                if kwargs.get(label) is not None:
                    value = kwargs[label]
                    kcounter += 1
                elif counter < len(args):
                    value = args[counter]
                    counter += 1
                else:
                    print(f'Missing argument {label} in {name} command.')
                    break
                if typecheck(value, _type):
                    print(f'{label} must be a {_type}, not a {type(value)}.')
                    break
            else:
                if len(args) == counter and len(kwargs) == kcounter:
                    func(*args, **kwargs)
                else:
                    print('Too many arguments or keyword arguments given.')
        return wrapper_addtoswitch
    if _func is None:
        return decorator_addtoswitch
    else:
        return decorator_addtoswitch(_func)


def main(switch):
    while True:
        print('>> ', end='')
        data = input().strip().split()
        for i in data:
            if data[i] == ' ':
                del data[i]
        if len(data) == 0:
            continue
        kwarguments = {}
        for i in range(len(data) - 1, -1, -1):
            if match := re.match('^-.$', data[i]):
                del data[i]
                try:
                    kwarguments[match.string] = data[i]
                    del data[i]
                except KeyError:
                    print(f'{match.string} value not found.')
        command, *arguments = data
        if (func := switch.get(command.lower())) is not None:
            func(*arguments, **kwarguments)
        else:
            print(f'{command} is not a defined command')


if __name__ == '__main__':
    pass

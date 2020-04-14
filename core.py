import cmd

switch = {}


@cmd.addtoswitch(switch=switch)
def sayhi(surname):
    if surname is not None:
        print(f'Hi {surname}')
    else:
        print('Hello')


if __name__ == '__main__':
    print('Forester by Jakub Błażejowski')
    cmd.main(switch)
import cmd
import numpy


class Toggle(cmd.Switch):
    def __init__(self):
        super().__init__()


toggle = Toggle()
toggle.commands = cmd.switch.commands


@cmd.addtoswitch(switch=toggle.commands)
@cmd.correctness
def myinput(switch: Switch, arr: list):
    """
    Lets user input list into the system
    :param Switch switch:
    :param list arr: example [1,2,3,4,5]
    :return:
    """
    pass


if __name__ == '__main__':
    print('Forester by Jakub Błażejowski', 'Type list to see the list of available commands.', sep='\n')
    cmd.main(toggle)
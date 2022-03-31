import core.bot
from colorama import Fore


def __main__():
    core.bot.menu()


try:
    __main__()
except KeyboardInterrupt:
    print(Fore.YELLOW + '\nMessage_bot Warning: Forced Bot Close')


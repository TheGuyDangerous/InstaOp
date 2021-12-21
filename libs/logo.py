# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo =  """

██╗███╗░░██╗░██████╗████████╗░█████╗░    ██████╗░███████╗██████╗░░█████╗░██████╗░████████╗
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██║██╔██╗██║╚█████╗░░░░██║░░░███████║    ██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║    ██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║    ██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝    ╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░      
                                                                   
                                                                   """


def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)                                                  
    print(Fore.RED + "                                                      LinkedIN" + Fore.CYAN + " linkedin.com/in/sannidhyadubey ")
    print(Fore.RED + "                                                      BY     " + Fore.CYAN + " - @GuyDangerous")
    print(Fore.RED + "                                                      Telegram"+ Fore.CYAN + " - t.me/GuyDangerus ")
    print(Fore.GREEN + "      Other Projects: https://github.com/TheGuyDangerous"+ Style.RESET_ALL + Style.BRIGHT)

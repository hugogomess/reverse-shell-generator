#!/usr/bin/python3

# I don't believe in license.
# You can do whatever you want with this tool.

import colorama
from colorama import Fore, Style

def banner():
    version = 1.0
    print(Fore.RED + """
                                                __         ____                                     __            
   ________ _   _____  _____________      _____/ /_  ___  / / /   ____ ____  ____  ___  _________ _/ /_____  _____
  / ___/ _ \ | / / _ \/ ___/ ___/ _ \    / ___/ __ \/ _ \/ / /   / __ `/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
 / /  /  __/ |/ /  __/ /  (__  )  __/   (__  ) / / /  __/ / /   / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
/_/   \___/|___/\___/_/  /____/\___/   /____/_/ /_/\___/_/_/    \__, /\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
                                                               /____/                                             

            + -- --=[ v""" + str(version) + """ by @0xkaneki

    """ + Style.RESET_ALL)

banner()
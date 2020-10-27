# Reverse Shell Generator
Command line reverse shell generator with multiple languages/tools and encodes.

```text
                                                __         ____                                     __            
   ________ _   _____  _____________      _____/ /_  ___  / / /   ____ ____  ____  ___  _________ _/ /_____  _____
  / ___/ _ \ | / / _ \/ ___/ ___/ _ \    / ___/ __ \/ _ \/ / /   / __ `/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
 / /  /  __/ |/ /  __/ /  (__  )  __/   (__  ) / / /  __/ / /   / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
/_/   \___/|___/\___/_/  /____/\___/   /____/_/ /_/\___/_/_/    \__, /\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
                                                               /____/                                             

            + -- --=[ v1.0 by @0xkaneki

    
usage: python3 reverse_shell_generator.py [-i/--host] HOST [-p/--port] PORT [OPTIONS]

required arguments:
  -i HOST, --host HOST  host listening the connection
  -p PORT, --port PORT  port listening the connection

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  language or tool - Options: bash, nc, python, python3, php, ruby, perl
  -s SHELL, --shell SHELL
                        shell - Options: sh, bash
  -e ENCODE, --encode ENCODE
                        output encode - Options: base64, urlencode, hex
```

## Install

To install dependencies run:
```shell
pip3 install -r requirements.txt
```
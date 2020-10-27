# Reverse Shell Generator
Command line reverse shell generator with multiple languages/tools and encodes.

```shell
Usage: python3 reverse_shell_generator.py [-i/--host] HOST [-p/--port] PORT [OPTIONS]

Examples:
    $ python3 reverse_shell_generator.py --host 10.10.10.10 --port 4444
    $ python3 reverse_shell_generator.py -i 10.10.10.10 -p 4444 --type nc
    $ python3 reverse_shell_generator.py -i 10.10.10.10 -p 4444 -t python --encode base64
```

## Install

To install dependencies run:
```shell
pip3 install -r requirements.txt
```
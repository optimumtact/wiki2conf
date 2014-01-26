wiki2conf
=========

Convert tox wiki page to configuration file
dependencies - docopt, get with pip install docopt
```
Usage:
  wiki2conf.py <infile> <outfile> [--mahomet] [--ipv6] [--skipmaintainer <name>]
  wiki2conf.py -h | --help
  wiki2conf.py --version

Options:
  -m --mahomet  Include mahomets server
  -i --ipv6  Include ipv6
  -h --help  Show this screen
  -s <name> --skipmaintainer <name>  Ignore server with maintainer name
  --version  show the version number
```
Suggested usage
```wget wiki.tox.im/Servers && ./wiki2conf.py Servers server.conf -m -s <yourmaintainername>```


wiki2conf
=========

Convert tox wiki page to configuration file, json or html output

dependencies - docopt, get with pip install docopt
```
Usage:
  wiki2conf.py <infile> <outfile> [--output <out> --mahomet --ipv6 --skipmaintainer <name>]
  wiki2conf.py -h | --help
  wiki2conf.py --version

Options:
  -m --mahomet  Include mahomets server
  -i --ipv6  Include ipdbv6
  -h --help  Show this screen
  -o <out> --output <out>  Output type, either json, html or conf [default: conf].
  -s <name> --skipmaintainer <name>  Ignore server with maintainer name
  --version  show the version number
```
Suggested usage
```
   wget wiki.tox.im/Servers
   cat Servers and verify it looks good
   ./wiki2conf.py Servers server.conf -o conf -m -s <yourmaintainername>
```


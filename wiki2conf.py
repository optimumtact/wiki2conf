#!/usr/bin/python
import sys
import re
from docopt import docopt
strargs ='''
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
'''
#parse args here
args = docopt(strargs, version='0.1')
reg = re.compile('<td>.*(</td>)?')
values = {}
i = 0
name = ''
curr = []

#open and extract values from wiki page
with open(args['<infile>'], 'r') as my_file:
    for line in my_file:
        if reg.match(line):
           line = line.replace('<td>', '')
           line = line.replace('</td>', '')
           line = line.strip('\n')
           curr.append(line)
           i += 1
           if i >= 7:
               values[curr[0]] = curr
               curr = []
               i = 0

#if mahomet specified, add mahomet
if args['--mahomet']:
	values['mahomet'] = ['54.194.92.175', 'NONE', '33445', '19D6BEACB8DBC1FFC39A9AFEEDD5A1ABF73F60FBFC30F397E03A87C71220620C', 'mahomet', 'Unknown', 'WORK']

#now write conf format
with open(args['<outfile>'], 'w') as f:
	count = 1
	for key in values:
            curr = values[key]
            if args['--skipmaintainer'] == curr[4]:
                continue
	    f.write('{ // '+curr[4]+' - '+curr[5]+' - '+curr[6]+'\n')
            if args['--ipv6'] and curr[1] != 'NONE':
                f.write('    address = "'+curr[1]+'"\n')
            else:
                f.write('    address = "'+curr[0]+'"\n')
            f.write('    port = '+curr[2]+'\n')
            f.write('    public_key = "'+curr[3]+'"\n')
            if count == len(values):
                f.write('}\n')
            else:
                f.write('},\n')
            count+=1
f.close()
my_file.close()

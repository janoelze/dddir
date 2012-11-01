import os, commands, inspect
from optparse import OptionParser
from pprint import pprint
from time import time

PATHS = ''
TIME = int(time())

def is_dir(name):
    name = name.split('.')
    try:
        name[1]
    except IndexError, e:
        return True


def is_file(name):
    name = name.split('.')
    if name[1]:
        return True


def get_opts():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="file", help="The file you want to use as the blueprint", metavar="FILE")
    return parser.parse_args()

def search_parent():
    pass

def get_lines(file):
    f = open(file, 'r')
    LINES = []
    i = 0
    for line in f:
        LINES.append(line.replace('\n', '').split('\t'))
        i = i + 1
    return LINES


def setup_lines(LINES):
    MAX_SIZE = 0
    for LINE in LINES:
        size = len(LINE)
        if size > MAX_SIZE:
            MAX_SIZE = size
    for LINE in LINES:
        for i in xrange(1,MAX_SIZE):
            try:
                LINE[i]
            except IndexError, e:
                LINE.append('#null#')
    return LINES

def fill_lines(LINES):
    this_item = ''
    for i in xrange(0,len(LINES[0])):
        for LINE in xrange(0,len(LINES)):
            if LINES[LINE][i] != '#null#':
                if is_dir(str(LINES[LINE][i])):
                    if LINES[LINE][i] != this_item and LINES[LINE][i] != '':
                        this_item = LINES[LINE][i]
                    else:
                        LINES[LINE][i] = this_item
    return LINES

def make_paths(LINES):
    OUTPUT = []
    for i in xrange(0,len(LINES)):
        OUTPUT.append('/'.join(LINES[i]))
    return OUTPUT

def clear_lines(LINES):
    for i in xrange(0,len(LINES[0])):
        for LINE in xrange(0,len(LINES)):
            LINES[LINE] = [x for x in LINES[LINE] if x != '#null#']
    return LINES


def repair_dirs(PATHS):
    x = 0
    for PATH in PATHS:
        if is_dir(PATH):
            PATH = '%s' % PATH
            PATHS[x] = PATH
        x = x + 1
    return PATHS

def create_paths(PATHS):
    commands.getoutput('mkdir ~/dddir-output-%s/' % (TIME) )
    for PATH in PATHS:
        PATH = '~/dddir-output-%s/%s' % (TIME, PATH)
        if is_dir(PATH):
            cmd = 'mkdir'
        else:
            cmd = 'touch'
        commands.getoutput('%s %s' % (cmd,PATH))
        log_message('creating %s' % (PATH))

def log_message(m):
    print '>> %s' % m

def main():
    (opts, args) = get_opts()
    LINES = get_lines(opts.file)
    LINES = setup_lines(LINES)
    LINES = fill_lines(LINES)
    LINES = clear_lines(LINES)
    PATHS = make_paths(LINES)
    PATHS = repair_dirs(PATHS)
    create_paths(PATHS)
    
if __name__ == "__main__":
    main()

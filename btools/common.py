import os
import sys

VERSION = "1.0rc4"

loglevel = 4
template = "/usr/share/bm/bm-config-template"

def debug(msg):
    if loglevel >= 3:
        sys.stderr.write("[DEBUG]   %s\n" % msg)

def info(msg):
    if loglevel >= 2:
        sys.stderr.write("[INFO]    %s\n" % msg)

def warning(msg):
    if loglevel >= 1:
        sys.stderr.write("[WARN]    %s\n" % msg)

def error(msg):
    sys.stderr.write("[ERROR]   %s\n" % msg)
    os.sys.exit(1)


def get_conf_location():
    if os.path.exists(".bm-match"):
        return os.path.realpath("./.bm-match")
    else:
        h = os.environ["HOME"]
        return os.path.join(h, ".bm-match")

def replace_variables(dest, variables):
    res = []
    for d in dest.split():
        if d[0] == "%" and d[-1] == "%":
            if variables.has_key(d[1:-1].lower()):
                d = variables[d[1:-1].lower()]
            else:
                d = ""
        res.append(d)
    return " ".join(res)

def cli_module_help(module):
    cli_output_help( module["name"], module["description"], 
                    module["usage"], module["commands"], module["examples"] )

def cli_output_help(prog, description, usage, commands, examples, option_title = "Options:"):
    cli_version(prog, description)
    cli_usage(prog, usage)
    cli_help(commands, option_title)
    cli_examples(prog, examples)

def cli_version(name, description):
    name = os.path.basename(name)
    print "%s %s - %s" % (name, VERSION, description)
    print "Copyright 2008, 2009, Bart Spaans <onderstekop@gmail.com>"

def cli_usage(prog, usagelist):
    prog = os.path.basename(prog)
    if type(usagelist) == str:
        usagelist = [usagelist]
    print
    print "Usage:", prog, usagelist[0]
    for u in usagelist[1:]:
        print "      ", prog, u
    print


def cli_examples(prog, examples):
    prog = os.path.basename(prog)
    print "Examples:"
    maxcommandlen = -1
    for command, description in examples:
        if len(command) > maxcommandlen:
            maxcommandlen = len(command)
    padding = maxcommandlen + 4
    for command, description in examples:
        print "    ", prog, command,
        print " " * ((maxcommandlen - len(command)) + 4),
        print description





def cli_help(commands, title = "Commands:"):
    print title
    for com, args, description in commands:
            print "\n\t", 
            for c in com:
                    print "%s %s  " % (c, args),
            print "\n\t%s" % description
    print


OUTPUT_COLOR = True

RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
GRAY = "\033[1;30m"
NOCOLOR = "\033[0m"


themes = [("gray-blue-green", GRAY, BLUE, GREEN),
          ("gray-red-green", GRAY, RED, GREEN),
          ("gray-gray-green", GRAY, GRAY, GREEN),
          ("gray-gray-red", GRAY, GRAY, RED),
          ("gray-green-red", GRAY, GREEN, RED),
          ("gray-green-blue", GRAY, GREEN, BLUE),
         ]
theme = themes[0]

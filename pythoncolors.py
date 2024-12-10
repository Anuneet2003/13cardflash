import sys
import random

try:
    sh = sys.stdout.shell
except AttributeError:
    print("pythoncolors only works with IDLE")
    exit()

newcolors  = False
global colorlist
if newcolors :
    colorlist = {"red": "hit",
                "yellow": "COMMENT",
                "orange": "KEYWORD",
                "green": "STRING",
                "blue": "stdout",
                "purple": "BUILTIN",
                "black": "SYNC",
                "brown": "console",

                "user1": "DEFINITION",
                "user2": "sel",
                "user4": "ERROR",
                "user5": "stderr"}
else:
    colorlist = {"red": "hit",
                "yellow": "COMMENT",
                "orange": "KEYWORD",
                "green": "STRING",
                "blue": "stdout",
                "purple": "BUILTIN",
                "black": "SYNC",
                "brown": "console"}

def printc(text, end="\n"):
    s = ""
    for i in text:
        if i == "{":
            sh.write(s, colorlist["black"])
            s = ""
        elif i == "}":
            tag_write = s.split(":")
            sh.write(tag_write[0], tag_write[1])
            s = ""
        else:
            s += i

    sys.stdout.write( end )


# Individual colour functions
def red(text):
    return "{"+ text + ":" + colorlist["red"] + "}"

def yellow(text):
    return "{"+ text + ":" + colorlist["yellow"] + "}"

def orange(text):
    return "{"+ text  + ":" + colorlist["orange"] + "}"

def green(text):
    return "{"+ text + ":" + colorlist["green"] + "}"

def blue(text):
    return "{"+ text  + ":" + colorlist["blue"] + "}"

def purple(text):
    return "{"+ text + ":" + colorlist["purple"] + "}"

def black(text):
    return "{"+ text  + ":" + colorlist["black"] + "}"

def brown(text):
    return "{"+ text + ":" + colorlist["brown"] + "}"

def randcol(text):
    color = random.choice(list(colorlist.keys()))
    return "{"+ text + ":" + colorlist[color] + "}"

# User defined colours
def user1(text):
    return "{"+ text + ":" + colorlist["user1"] + "}"

def user2(text):
    return "{"+ text + ":" + colorlist["user2"] + "}"

def user4(text):
    return "{"+ text + ":" + colorlist["user4"] + "}"

def user5(text):
    return "{"+ text + ":" + colorlist["user5"] + "}"

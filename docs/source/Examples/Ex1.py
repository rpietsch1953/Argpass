#!/usr/bin/env python3
# vim: expandtab:ts=4:sw=4:noai
"""Example 1"""
import sys
from pcs_argpass.Param import Param #, Translation_de_DE
from pcs_argpass.GPL3 import LGPL_Preamble_DE, GPL3_2007, LGPL_Preamble, LGPL3_2007

MyParam:Param = None              # to produce an error if not initialized!

Def_LogMqtt = {                             # This is the declaration of the command-line
                                            # options
    'Help':                                 # This is the key value for this Option
                                            # must be str and of couse unique
        {
        's': 'h',                           # the short option for this (e.g. -h)
                                            # if more characters are given all of
                                            # them are matched.
        'l': 'help',                        # the long option(s) (e.g. --help). Long
                                            # options can be abbrevated to minimal 2
                                            # characters as long as the abbrevation
                                            # is unique within all long options,
                                            # so also --he or --hel is supported. If this
                                            # entry is a list or tuple then any of this
                                            # entries match.
        'm': 'H',                           # The modus for this option (see details
                                            # in "SetDef" function)
                                            # 'H' means this is one of the "help"
                                            # entries. Since "Help" is a "special" case
                                            # as also "Export" os "Licence" are it is
                                            # possible to have more than one such entry
                                            # in the definition
        'd': 'Show this text and quit.'     # the help-text for this option. Can of
                                            # course be also multi-line.
        },
    'MqttBroker':
        {
        's': 'm',
        'l': 'mqttbroker',
        'm': 't',                           # this is a text-entry
        'r': True,                          # it is required
        'o': True,                          # it needs an parameter ("-m" allone makes
                                            # no sense, must be "-m 10.11.12.13" or
                                            # --mqtt=10.11.12.13)
        'v': 'localhost',                   # the default value used if this is not on the
                                            # command-line
        'd': 'Address of MQTT-Broker',
        },
    'MqttPort':
        {
        's': 'p',
        'l': 'port',
        'm': 'i',                           # This is an integer
        'L': 1024,                          # lower limit. The entered value must
                                            # be >= this value
                                            # (works also for float and str)
        'U': 32766,                         # upper limit. The entered value must
                                            # be <= this value
        'r': True,
        'o': True,
        'v': 1883,
        'd': 'Port of MQTT-Broker',
        },
    'Topic':
        {
        's': 't',
        'l': 'topic',
        'm': 't',                           # also a text entry
        'o': True,
        'M': True,                          # but allow multiple occurences.
                                            # The variable in the resulting
                                            # dictionary is a list!
        'v': [],
        'd': 'Topic to dump',
        },
    'OutFile':
        {
        's': 'f',
        'l': 'file',
        'm': 'p',                           # this is a path, not a file, because
                                            # a file (mode = f) must exist. File is
                                            # used for input-files, path for non
                                            # existing output (file or dir). It is
                                            # only tested if the format is valid
                                            # on this operating system.
        'o': True,
        'v': '',
        'd': 'Output path',
        },
    'License':
        {
        's': '§l',                          # here we have 2 possible short options
        'l': 'license',
        'm': '§',                           # This will show the "short" license
        'd': 'Show license and exit'
        },
    'GPL':
        {
        's': 'g',
        'l': ('gpl','GPL','Gpl'),           # here all of this entries are valid
                                            # on the command-line
        'm': 'L',                           # This will show the complete license
                                            # in this example realy a lot of text.
        'd': 'Show complete license and exit'
        },
}

Version = "1.0.0"
try:                                            # catch illegal definitions
    MyParam = Param(Def=Def_LogMqtt,
                    Desc="dump MQTT-Topics to file",
                    AllParams=True,
                    Version=Version,
#                    translation=Translation_de_DE, # remove this line for english
                                                    # messages
                    License=('\\nCopyright (c) 2022 <your name>\\n' + LGPL_Preamble_DE,
                        LGPL_Preamble,
                        LGPL3_2007,
                        GPL3_2007),
                    )

    if not MyParam.Process():                   # This does the "REAL" processing of
                                                # the command-line args. return True
                                                # if everything is done and the program
                                                # should exit (e.g. Help etc.)

# do your work here.

        # You can use the Param-class like a normal dictionary,
        # so this is perfectly legal
        if len(MyParam['Topic']) == 0:          # no topics given
            MyParam['Topic'].append('#')        # use "ALL" topics

        # if you want to display the given command line options do the following:
        print(MyParam.ParamStr())   # this function returns the
                                                # complete parameters entered

except Param.ParamError as RunExc:      # here we catch any parameter errors and inform the user
    print(f"{RunExc }",file=sys.stderr)
    sys.exit(1)
sys.exit(0)

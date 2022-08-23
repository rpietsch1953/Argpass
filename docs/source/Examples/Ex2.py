#!/usr/bin/env python3
# vim: expandtab:ts=4:sw=4:noai

import sys
from pcs_argpass.Param import Param, Translation_de_DE
from pcs_argpass.GPL3 import LGPL_Preamble_DE, GPL3_2007, LGPL_Preamble, LGPL3_2007
from Ex2_Args import Def_LogMqtt

MyParam:Param = None              # to produce an error if not initialized!
Version = "1.0.0"

def main():

    # do your work here.
    print(MyParam.ParamStr())       # only to do something

if __name__ == '__main__':
    try:                                            # catch illegal definitions
        MyParam = Param(Def=Def_LogMqtt,
                        Desc="dump MQTT-Topics to file",
                        AllParams=True,
                        Version=Version,
#                        translation=Translation_de_DE, # remove this line for english messages
                        License=('\\nCopyright (c) 2022 <your name>\\n' + LGPL_Preamble_DE,
                            LGPL_Preamble, LGPL3_2007, GPL3_2007))
        if not MyParam.Process():
            main()
    except Param.ParamError as RunExc:      # here we catch any parameter errors and inform the user
        print(f"{RunExc }",file=sys.stderr)
        sys.exit(1)
    sys.exit(0)


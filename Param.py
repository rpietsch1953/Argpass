#!/usr/bin/env python3
# vim: expandtab:ts=4:sw=4:noai
"""
Deals with command-line parameters

Copyright (c) 2022 Ing. Rainer Pietsch <r.pietsch@pcs-at.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.


"""


import copy
import inspect
import json
import os
import pprint
import sys
import textwrap
import types
from itertools import chain
from pathlib import Path, PurePath
from typing import Dict, Union, Optional

# Use json5 for imports if it is avallable
# else use json (json5 allowes comments within the json-data)
# data is ALLWAYS printed as pure json.
try:
    import json5
    JsonLoads = json5.loads
    JsonLoad = json5.load
except ModuleNotFoundError:
    JsonLoads = json.loads
    JsonLoad = json.load

__updated__ = '257.220823174107'
Version = f"1.12.{__updated__}"

GLOBAL_NAME = 'global'


Translation_en_US:dict = {
    'PrefixError':
        "Error in prefixed parameter {OptionName}",
    'JsonError':
        "Import failed '{wMsg}' in {OptionPath} ({FullPath}) for parameter {OptionName}",
    'PathNoFile':
        "The path '{OptionPath}' ({FullPath}) for parameter {OptionName} is not a file",
    'PathNoDir':
        "The path '{OptionPath}' ({FullPath}) for parameter {OptionName} is not a directory",
    'PathNoPath':
        "The path '{OptionPath}' ({FullPath}) for parameter {OptionName} is not valid on this filesystem",
    'LessLow':
        "Value '{OptValue}' for parameter {ParKey} is less than lower limit ({LowLimit})",
    'HigherUp':
        "Value '{OptValue}' for parameter {ParKey} is bigger than upper limit ({UppLimit})",
    'NoInt':
        "Value '{OptValue}' for parameter {ParKey} is not a valid integer",
    'NoFloat':
        "Value '{OptValue}' for parameter {ParKey} is not a valid floating point number",
    'NoBool':
        "Value '{OptValue}' for parameter {ParKey} is not valid boolean (YyTtJj1NnFf0)",
    'OptionNotDefined':
        "No action defined for {OptionName}",
    'OptionRequired':
        "{DefArgName} ({ParList}) required but not given",
    'TypePath':
        "path",
    'TypeInteger':
        "integer",
    'TypeBool':
        "bool",
    'TypeFloat':
        "float",
    'TypeFile':
        "file",
    'TypeDir':
        "directory",
    'TypeCount':
        "counter",
    'TypeHelp':
        "help",
    'TypeImport':
        "import",
    'TypeExport':
        "export",
    'TypeGlobImport':
        "global import",
    'TypeGlobExport':
        "global export",
    'TypeStr':
        "string",
    'HelpDefault':
        "Default",
    'HelpValue':
        "value",
    'HelpUsage':
        "Usage:",
    'HelpVersion':
        "Version:",
    'HelpOptions':
        "Options:",
    'HelpOptionInline':
        "[OPTIONS ...]",
    'OptionRequiresArgumentLong':
        "option --{opt} requires argument",
    'OptionNeedNoArgs':
        "option --{opt} must not have an argument",
    'OptionNotRecognizedLong':
        "option --{opt} not recognized",
    'ParNoUniquePrefix':
        "option --{opt} not a unique prefix",
    'OptionRequiresArgumentShort':
        "option -{opt} requires argument",
    'OptionNotRecognizedShort':
        "option -{opt} not recognized",
    'UndefinedOptionSingle':
        "option {OptStr} not recognized",
    'UndefinedOptionMultiple':
        "options {OptStr} not recognized",
    }

Translation_de_DE:dict = {
   'HigherUp':
        "Der Wert '{OptValue}' für den Parameter {ParKey} ist größer als das obere Limit ({UppLimit})",
    'JsonError':
        "Fehler beim Import '{wMsg}' aus der Datei {OptionPath} ({FullPath}) für den Parameter {OptionName}",
    'LessLow':
        "Der Wert '{OptValue}' für den Parameter {ParKey} ist kleiner als das untere Limit ({LowLimit})",
    'NoBool':
        "Der Wert '{OptValue}' für den Parameter {ParKey} ist kein Wahrheitswert (YyTtJj1NnFf0)",
    'NoFloat':
        "Der Wert '{OptValue}' für den Parameter {ParKey} ist keine gültige Fließkommazahl",
    'NoInt':
        "Value '{OptValue}' für den Parameter {ParKey} ist keine gültige Ganzzahl",
    'OptionNotDefined':
        "Die Option '{OptionName}' ist ungültig",
    'OptionRequired':
        "Der Parameter '{DefArgName}' ({ParList}) muß angegeben werden",
    'PathNoDir':
        "Die Pfadangabe '{OptionPath}' ({FullPath}) für die Option {OptionName} ist kein Verzeichnis",
    'PathNoFile':
        "Die Pfadangabe '{OptionPath}' ({FullPath}) für die Option {OptionName} ist keine Datei",
    'PathNoPath':
        "Die Pfadangabe '{OptionPath}' ({FullPath}) für den Option {OptionName} ist bei diesem Dateisystem ungültig",
    'PrefixError':
        "Der angegebene Prefix für die Option '{OptionName}' ist ungültig",
    'TypePath':
        "Pfad",
    'TypeInteger':
        "Ganzzahl",
    'TypeBool':
        "Wahrheitswert",
    'TypeFloat':
        "Fliesskommazahl",
    'TypeFile':
        "Datei",
    'TypeDir':
        "Verzeichnis",
    'TypeCount':
        "Zähler",
    'TypeHelp':
        "Hilfe",
    'TypeImport':
        "Import",
    'TypeExport':
        "Export",
    'TypeGlobImport':
        "Globaler Import",
    'TypeGlobExport':
        "Global Export",
    'TypeStr':
        "Zeichenkette",
    'HelpDefault':
        "Standardwert",
    'HelpValue':
        "Wert",
    'HelpUsage':
        "Verwendung:",
    'HelpVersion':
        "Version:",
    'HelpOptions':
        "Folgende Optionen sind möglich:",
    'HelpOptionInline':
        "[OPTION ...]",
    'OptionRequiresArgumentLong':
        "Option --{opt} verlangt einen Wert",
    'OptionNeedNoArgs':
        "Option --{opt} darf keinen Wert haben",
    'OptionNotRecognizedLong':
        "Option --{opt} ist unbekannt",
    'ParNoUniquePrefix':
        "Option --{opt} ist mehrdeutig",
    'OptionRequiresArgumentShort':
        "Option -{opt} verlangt einen Wert",
    'OptionNotRecognizedShort':
        "Option -{opt} ist unbekannt",
    'UndefinedOptionSingle':
        "Unbekannte Option {OptStr} angegeben",
    'UndefinedOptionMultiple':
        "Unbekannte Optionen {OptStr} angegeben",
    }

class Param():
    """
Main class and also the result-dictionary.
A member of this class acts like a dictionary. There are some special cases
if you use nested childs. (Check out the :doc:`usage` section for further information)

    """
    class __ExceptionTemplate(Exception):
        def __call__(self, *args):
                return self.__class__(*(self.args + args))

        def __str__(self):
                return ': '.join(self.args)

    class DeclarationError(__ExceptionTemplate):
        """
        this exception is raised if there is an declaration error within the
        parameters of the class.

        .. note::
            This error messages are NEVER translated since they are not user
            initiated errors.

        """
        pass                            # pylint: disable=unnecessary-pass

    class ParamError(__ExceptionTemplate):
        """
        This exception is raised if there is an error within the runtime-parameters.
        This is only raised within the :func:`Param.Process`-function.

        .. note::
            This errors are translated with the 'translation' dictionary. There
            is the initial state of this dict using 'en_US' texts.

            This module also provide a 'Translation_de_DE' entry giving a german
            translation of the error-messages, and a 'Translation_en_US' table only vor completeness.

            If you can provide translations to other languages send me this
            declarations to <r.pietsch@pcs-at.com> and I will add them to this
            module.

        """
        pass                            # pylint: disable=unnecessary-pass

    class __PathEncoder(json.JSONEncoder):
        """Subclass to encode path for json
        """
        def default(self, o):
            """The "real" encoder

            Args:
                obj (any): the object to encode

            Returns:
                any: the encoded Path or the default result
            """
            if isinstance(o, Path) or isinstance(o, PurePath):
                return str(o)             # return the string representation of the Path
            else:
                return super().default(o)   # let the default library do the work

    _InitTranslation = {
            'PrefixError':
                "Error in prefixed parameter {OptionName}",
            'JsonError':
                "Import failed '{wMsg}' in {OptionPath} ({FullPath}) for parameter {OptionName}",
            'PathNoFile':
                "The path '{OptionPath}' ({FullPath}) for parameter {OptionName} is not a file",
            'PathNoDir':
                "The path '{OptionPath}' ({FullPath}) for parameter {OptionName} is not a directory",
            'PathNoPath':
                "The path '{OptionPath}' ({FullPath}) for parameter {OptionName} is not valid on this filesystem",
            'LessLow':
                "Value '{OptValue}' for parameter {ParKey} is less than lower limit ({LowLimit})",
            'HigherUp':
                "Value '{OptValue}' for parameter {ParKey} is bigger than upper limit ({UppLimit})",
            'NoInt':
                "Value '{OptValue}' for parameter {ParKey} is not a valid integer",
            'NoFloat':
                "Value '{OptValue}' for parameter {ParKey} is not a valid floating point number",
            'NoBool':
                "Value '{OptValue}' for parameter {ParKey} is not valid boolean (YyTtJj1NnFf0)",
            'OptionNotDefined':
                "No action defined for {OptionName}",
            'OptionRequired':
                "{DefArgName} ({ParList}) required but not given",
            'TypePath':
                "path",
            'TypeInteger':
                "integer",
            'TypeBool':
                "bool",
            'TypeFloat':
                "float",
            'TypeFile':
                "file",
            'TypeDir':
                "directory",
            'TypeCount':
                "counter",
            'TypeHelp':
                "help",
            'TypeImport':
                "import",
            'TypeExport':
                "export",
            'TypeGlobImport':
                "global import",
            'TypeGlobExport':
                "global export",
            'TypeStr':
                "string",
            'HelpDefault':
                "Default",
            'HelpValue':
                "value",
            'HelpUsage':
                "Usage:",
            'HelpVersion':
                "Version:",
            'HelpOptions':
                "Options:",
            'HelpOptionInline':
                "[OPTIONS ...]",
            'OptionRequiresArgumentLong':
                "option --{opt} requires argument",
            'OptionNeedNoArgs':
                "option --{opt} must not have an argument",
            'OptionNotRecognizedLong':
                "option --{opt} not recognized",
            'ParNoUniquePrefix':
                "option --{opt} not a unique prefix",
            'OptionRequiresArgumentShort':
                "option -{opt} requires argument",
            'OptionNotRecognizedShort':
                "option -{opt} not recognized",
            'UndefinedOptionSingle':
                "option {OptStr} not recognized",
            'UndefinedOptionMultiple':
                "options {OptStr} not recognized",
        }


    def __init__(self, *,                          # pylint: disable=dangerous-default-value
            Def:dict = {},
            Args:Optional[list] = None,
            Chk = None,
            Desc:str = "",
            AddPar:str = "",
            AllParams:bool = True,
            UserPars:Optional[dict] = None,
            UserModes:Optional[dict] = None,
            ErrorOnUnknown:bool = True,
            HelpType:int = 0,
            Children:dict = {},
            translation:dict = {},
            Version:str = '',                       # pylint: disable=redefined-outer-name
            License:Union[str,tuple,list,dict,None] = None,             # pylint: disable=too-many-function-args
            ShowPrefixOnHelp:bool = True,
            _Child = False):

        """
        This is the constructor of the Param-class.

        Most of the parameters can be set also later on (if nessasary)

        .. note::
            all parameters are only by name and NOT positional!

        :param Def: For details check out :func:`SetDef`, defaults to None
        :type Def: dict, optional
        :param Args: For details check out :func:`SetArgs`, defaults to None
        :type Args: list, optional
        :param Chk: For details check out :func:`SetChk`, defaults to None
        :type Chk: callable, optional
        :param Desc: For details check out :func:`SetDesc`, defaults to ""
        :type Desc: str, optional
        :param AddPar: For details check out :func:`SetAddPar`, defaults to ""
        :type AddPar: str, optional
        :param AllParams: For details check out :func:`SetAllParams`, defaults to True
        :type AllParams: bool, optional
        :param UserPars: For details check out :func:`SetUserKeys`, defaults to None
        :type UserPars: Optional[dict], optional
        :param UserModes: For details check out :func:`SetUserKeys`, defaults to None
        :type UserModes: Optional[dict], optional
        :param ErrorOnUnknown: If True an error is raised if
                    there are undefined options on the commandline, if False: no error is raised.

                    UnusedArgs is always populated with all undefined args from the commandline.
                    This error is raised only on the topmost Param-object (not on children)
                    Defaults to True.
                    So if set to False you can test the 'UnusedArgs' property after return
                    of the 'Process'-function to get the list of undefined args and process
                    this situation on your own. Defaults to True
        :type ErrorOnUnknown: bool, optional
        :param HelpType: Type of helptext.

                    0: No Type, no standard defaults,
                    1: No Type, all defaults,
                    2: Type, no standard defaults,
                    3: Type and all defaults,

                    defaults to 0
        :type HelpType: int, optional
        :param Children: Dictionary of Child-definition for this class.

                .. code-block:: python

                    { 'Name': {'Def': {}, 'Desc': str, 'AddPar': str, 'Children': {} }, .... }

                Name = The name of this child. Must be unique.
                        Is translated to lower case.
                        Can not be "global" (this is the name of the root-class)

                Def = A definition dictionary like our own "Def" parameter,

                Children (optional) = dict of type Children, describes the grand-childer,
                        this can be done to any level.

                Desc (optional) = A string that describes this class
                        (like our own "Desc"-parameter).

                AddPar (optional) = String used as additional info
                        (like our own "AddPar"-parameter). Defaults to {}

        :type Children: dict, optional
        :param translation: For details check out :func:`SetTranslation`, defaults to None
        :type translation: dict, optional
        :param License: List of license-texts.
                    Thie texts are displayed if a '§' or 'L' -type option is applied.
                    If '§': only the first entry within this list is displayed,
                    if 'L': all entries separated by a newline ('\\n') are displayed.
                    To help there is a separate module "GPL3" which includes the folowing entries:

                        "GPL_Preamble" the suggested preamble (after the copyright notice)

                        "GPL_Preamble_DE" the same preamble in German language.

                        "LGPL_Preamble" the suggested preamble for the LGPL
                            (use after the copyright notice)

                        "LGPL_Preamble_DE" the same preamble in German language.

                        "LGPL3_2007" the additional terms of the Lesser GPL Version 3 from
                            June, 29th 2007, you shold append also the following
                            (GPL3_2007) if you use this license.

                        "GPL3_2007" the complete text of the GPL Version 3 from June, 29th 2007

                    you can use this by

                    .. code-block:: python

                        from pcs_argpass.GPL3 import GPL_Preamble, LGPL3_2007, GPL3_2007

                    and in the constructor of Param par example with:

                    .. code-block:: python

                        MyParam = Param (
                            ....
                        License=('\\nCopyright (c) <date> <your name>\\n' + GPL_Preamble_DE,
                                GPL_Preamble,
                                LGPL3_2007,
                                GPL3_2007),
                            ....
                            )

                    but, of course you can use every other license text you want, as long as this
                    license is compatible with the license of this module, whitch IS LGPL3.
        :type License: list[str], optional
        :param Version: Version string for help-display, defaults to ''
        :type Version: str, optional
        :param ShowPrefixOnHelp: if True a header block in the form

            .. code-block:: text

                ------------------------------------------------------------
                <child-name>
                ------------------------------------------------------------

        is printed within the help-output to divide child help from each other

        :type ShowPrefixOnHelp: bool, optional
        :param _Child: True if this instance should be a child, defaults to False
        :type _Child: bool, optional


        .. note::

            All long options can be abbreviated to at least 2 characters or to the
            length making them unique within the defined long options.

            Example:

                you define 'automatic', 'autonom' and 'testopt'
                at the commandline this can be abbreviated to

                .. code-block::

                    PROG --autom --auton --te

                but not to

                .. code-block::

                    PROG --au

                because this is not unique within the optionlist.

        .. note::

            If children are used, the prefix-name is always optional, but if given, the option
            is ONLY recognized for this child. if there are the same long options for more
            then one child and NO prefix is given, this option is recognized by ALL children
            having this long option within their definition.

            Example:

                you define 'auto' within the root as 'MyOpt'
                you define 'auto' within the child 'alpha' as 'DoAuto'

                the commandline should be

                .. code-block::

                    PROG --auto=yes

                then BOTH options are set to 'yes' e.g. MyParam['MyOpt'] == 'yes' AND MyParam['DoAuto'] == 'yes'
                with the commandline

                .. code-block::

                    PROG --alpha.auto=yes

                only MyParam['DoAuto'] == 'yes' and MyParam['MyOpt'] is either the default or not set depending on
                the definition of this option
                with the commandline

                .. code-block::

                    PROG --alpha.auto=yes --global.auto=no

                MyParam['MyOpt'] == 'no' AND MyParam['DoAuto'] == 'yes'
                REMEMBER: 'global' is ALWAYS the name of the root Param-object!

            please inform your users about this possibility if you use child-definitions!



        """

#---------------------------------------------
# Class-local Data
#---------------------------------------------
        self.__WorkDict:dict = {}           # This is the result dictionary used to make the class look like dicktionary
        self.__Version = Version            # Optional version string for help display
        self.__Children:Dict[str,Param] = {}    # Dictionary of our children (all are our one class! )
        self.__Parent:Union[Param,None] = None        # Our parent if we are a child else None
        self.__MyProgName:str = ""          # the programm-name from __Argumente[0] (only name)
        self.__MyProgPath:str = ""          # the path of the executeable from __Argumente[0]
        self.__MyPwd:str = ""               # Actual directory at invocation of "Process"
        self.__Definition:dict = {}         # the definition-dict
        self.__Description:str = ""         # Description of program for help
        self.__Argumente:list = []          # list of commandline arguments
        self.__ChkFunc = None               # pylint: disable=unused-private-member # external check-funktion (not implemented jet)
        self.__ErrorOnUnknown:bool = ErrorOnUnknown # raise error if unknown options on commandline
        self.__UsageText:str = ""           # Complete help-text
        self.__ShortStr:str = ""            # String of short parameters (e.g. "vhl:m:")
        self.__ShortList:list = []          # List of short parameters (e.g. ["v", "h", "l:", "m:"])
        self.__LongList:list = []           # List of Long parameters (e.g. "help","len="...)
        self.__ParDict:dict = {}            # dict of "argtext" -> "Parameter-name"
        self.__RemainArgs:list = []         # List of remaining arguments from commandline
        self.__UnusedArgs:list = []         # liste aller nicht vorgesehener Parameter
        self.__AddPar:str = ""              # Additional parameter Text (for help)
        self.__UsageTextList:list = []      # List of single help entries (also lists)
        self.__IsPrepared:bool = False      # Marker if "Prepare" is run after changes

        self.__HelpList:list = []           # List of all parameters with type 'H'  (Help)
        self.__ImportList:list = []         # List of all parameters with type 'x'  (single Import)
        self.__ExportList:list = []         # List of all parameters with type 'X'  (single Export)
        self.__LicenseList:list = []        # List of all parameters with type '§'  (License)
        self.__FullLicenseList:list = []    # List of all parameters with type 'L'  (full License)
        self.__Glob_ImportList:list = []    # List of all parameters with type '<'  (global Import)
        self.__Glob_ExportList:list = []    # List of all parameters with type '>'  (Global Export)
        self.__AllParams:bool = True        # True if all parameters are initialized, if False
                                            # only parameters with defaults or on the commandline
                                            # are in the dictionary
        self.__Prefix:str = GLOBAL_NAME
        self.__Glob_ExportStr:str = ''
        self.__HelpType:int = HelpType      # Type of help output
        self.__ShowPrefixOnHelp = ShowPrefixOnHelp

        self._Translation:dict = {}         # Dictionary for translations
        self.__License:list = ['']
        if isinstance(License,str):
            self.__License = [License]
        elif isinstance(License,(tuple,list)):
            self.__License = list(License)
        elif isinstance(License,dict):
            self.__License = list(License.values())
        self.__WorkPars = {
            'shortpar':     's',
            'longpar':      'l',
            'needoption':   'o',
            'default':      'v',
            'mode':         'm',
            'description':  'd',
            'lowlimit':     'L',
            'uplimit':      'U',
            'required':     'r',
            'multiple':     'M'
            }


        self.__WorkModes = {
            'text':         't',
            'bool':         'b',
            'path':         'p',
            'file':         'f',
            'dir':          'd',
            'int':          'i',
            'float':        'F',
            'count':        'C',
            'help':         'H',
            'import':       'x',
            'export':       'X',
            'glob_import':  '<',
            'glob_export':  '>',
            'license':      '§',
            'fullLicense':  'L'
            }
        # Liste der nicht einzufügenden Befehle
        self.__SpecialOpts = self.__WorkModes['help']
        self.__SpecialOpts += self.__WorkModes['import']
        self.__SpecialOpts += self.__WorkModes['export']
        self.__SpecialOpts += self.__WorkModes['glob_import']
        self.__SpecialOpts += self.__WorkModes['glob_export']
        self.__SpecialOpts += self.__WorkModes['license']
        self.__SpecialOpts += self.__WorkModes['fullLicense']

        self.__ModeToList = {
            self.__WorkModes['help']: self.__HelpList,
            self.__WorkModes['import']: self.__ImportList,
            self.__WorkModes['export']: self.__ExportList,
            self.__WorkModes['glob_import']: self.__Glob_ImportList,
            self.__WorkModes['glob_export']: self.__Glob_ExportList,
            self.__WorkModes['license']: self.__LicenseList,
            self.__WorkModes['fullLicense']: self.__FullLicenseList,
            }

# set the parameters with the individual functions
        self.__UserPars = UserPars
        self.__UserModes = UserModes        # pylint: disable=unused-private-member     # Not implemented
        self.SetDesc(Desc)
        self.SetUserKeys(UserPars = UserPars,UserModes = UserModes)
        self.SetDef(Def)
        self.SetArgs(Args)
        self.SetChk(Chk)
        self.SetAllParams(AllParams)
        self.SetAddPar(AddPar)
        if Children is None:            # fix issue if Children is None
            Children = {}
        for wPrefix, wDict in Children.items():
            TheFullPrefix = self.FullPrefix
            # Prefix (=Name) must be a string and not empty
            if not isinstance(wPrefix, str):
                raise self.DeclarationError(f"{TheFullPrefix}: Name of child '{wPrefix} is not a string") # ChildNameNoStr
            wPrefix = wPrefix.strip()
            if wPrefix == '':
                raise self.DeclarationError(f"{TheFullPrefix}: Name of child could not be blank")   # ChildNameBlank

            # the declaration of a child has to bee a dictionary
            if not isinstance(wDict, dict):
                raise self.DeclarationError(f"{self.FullPrefix}: Child definition for '{wPrefix} is not a dictionary")

            # the declaration of a child needs at least a 'Def' entry whitch is a dictionary
            if 'Def' not in wDict:
                raise self.DeclarationError(f"{self.FullPrefix}: Child definition for '{wPrefix} does not include 'Def'")
            if not isinstance(wDict['Def'], dict):
                raise self.DeclarationError(f"{self.FullPrefix}: 'Def' in child definition for '{wPrefix} is not a dictionary")

            # if 'Children' not given set it to an empty dictionary
            if 'Children' not in wDict:
                wDict['Children'] = {}
            if wDict ['Children'] is None:
                wDict['Children'] = {}

            # the declaration of "Children" has to bee a dictionary
            if not isinstance(wDict['Children'], dict):
                raise self.DeclarationError(f"{self.FullPrefix}: 'Children' in child definition for '{wPrefix} is not a dictionary")

            # if 'Desc' not given set it to ''
            if 'Desc' not in wDict:
                wDict['Desc'] = ''

            # the declaration of "Desc" has to bee a string
            if not isinstance(wDict['Desc'], str):
                raise self.DeclarationError(f"{self.FullPrefix}: 'Desc' in child definition for '{wPrefix} is not a string")

            # if 'AddPar' not given set it to ''
            if 'AddPar' not in wDict:
                wDict['AddPar'] = ''

            # the declaration of "AddPar" has to bee a string
            if not isinstance(wDict['AddPar'], str):
                raise self.DeclarationError(f"{self.FullPrefix}: 'AddPar' in child definition for '{wPrefix} is not a string")

            # now add all the children (if necessary also recursive)
            self.AddChild(Prefix = wPrefix,             # pylint: disable=too-many-function-args
                          Def = wDict['Def'],
                          Children = wDict['Children'],
                          Description = wDict['Desc'],
                          Version = self.__Version,
                          License = self.__License,
                          AddPar = wDict['AddPar'])

        self.SetTranslation(translation,_Child)

        # show that we need preparation
        self.__IsPrepared = False

    def SetTranslation(self,translation:dict, IsChild:bool = False) -> None:
        """
        Seta net translation-table

        :param translation: Dictionary with translated error-messages
        :type translation: dict
        :param IsChild: True if we are the root-parent.
                        You should only use this Option if you know what you do. If
                        it is True the **translation** dict is ignored and
                        the translation of the parent is used. Defaults to False
        :type IsChild: bool, optional


        There are 2 'Hidden' function to help debug the translations:

            :func:`_PrintInitTranslation` and

            :func:`_PrintAktualTranslation`

        Theses functions do exactly what they say: print the values out to stdout. You can
        use them to get the exact values used. The following default may not be accurate
        at all - do not rely on this info, print the dict yourselve.

        defaults to:

        .. code-block:: python

            {
            'PrefixError':
                "Error in prefixed parameter {OptionName}",
            'JsonError':
                "Import failed '{wMsg}' in {OptionPath} ({FullPath}) for parameter {OptionName}",
            'PathNoFile':
                "The path '{OptionPath}' ({FullPath}) for parameter {OptionName} is not a file",
            'PathNoDir':
                "The path '{OptionPath}' ({FullPath}) for parameter {OptionName} is not a directory",
            'PathNoPath':
                "The path '{OptionPath}' ({FullPath}) for parameter {OptionName} is not valid on this filesystem",
            'LessLow':
                "Value '{OptValue}' for parameter {ParKey} is less than lower limit ({LowLimit})",
            'HigherUp':
                "Value '{OptValue}' for parameter {ParKey} is bigger than upper limit ({UppLimit})",
            'NoInt':
                "Value '{OptValue}' for parameter {ParKey} is not a valid integer",
            'NoFloat':
                "Value '{OptValue}' for parameter {ParKey} is not a valid floating point number",
            'NoBool':
                "Value '{OptValue}' for parameter {ParKey} is not valid boolean (YyTtJj1NnFf0)",
            'OptionNotDefined':
                "No action defined for {OptionName}",
            'OptionRequired':
                "{DefArgName} ({ParList}) required but not given",
            'TypePath':
                "path",
            'TypeInteger':
                "integer",
            'TypeBool':
                "bool",
            'TypeFloat':
                "float",
            'TypeFile':
                "file",
            'TypeDir':
                "directory",
            'TypeCount':
                "counter",
            'TypeHelp':
                "help",
            'TypeImport':
                "import",
            'TypeExport':
                "export",
            'TypeGlobImport':
                "global import",
            'TypeGlobExport':
                "global export",
            'TypeStr':
                "string",
            'HelpDefault':
                "Default",
            'HelpValue':
                "value",
            'HelpUsage':
                "Usage:",
            'HelpVersion':
                "Version:",
            'HelpOptions':
                "Options:",
            'HelpOptionInline':
                "[OPTIONS ...]",
            'OptionRequiresArgumentLong':
                "option --{opt} requires argument",
            'OptionNeedNoArgs':
                "option --{opt} must not have an argument",
            'OptionNotRecognizedLong':
                "option --{opt} not recognized",
            'ParNoUniquePrefix':
                "option --{opt} not a unique prefix",
            'OptionRequiresArgumentShort':
                "option -{opt} requires argument",
            'OptionNotRecognizedShort':
                "option -{opt} not recognized",
            'UndefinedOptionSingle':
                "option {OptStr} not recognized",
            'UndefinedOptionMultiple':
                "options {OptStr} not recognized",
            }

        """
        if IsChild:
            if self.__Parent is not None:
                self._Translation = self.__Parent._Translation                  # pylint: disable=protected-access
        else:
            self._Translation = copy.deepcopy(self._InitTranslation)

            # Überschreibe die Übersetungen
            if translation is not None and isinstance(translation, dict):
                for k, InitVal in self._InitTranslation.items():
                    try:
                        w = translation[k]
                        if not isinstance(w, str):
                            self._Translation[k] = InitVal
                        else:
                            self._Translation[k] = w
                    except KeyError:
                        self._Translation[k] = InitVal
        for c in self.__Children.values():
            c.SetTranslation(translation,True)


    def _PrintInitTranslation(self):
        """
        Prints the initial translation dict to stdout.

        Only usefull during development!
        """
        print(pprint.pformat(self._InitTranslation, indent=4, width=200))

    def _PrintAktualTranslation(self):
        """
        Prints the actual translation dict to stdout.

        Only usefull during development!
        """
        print(pprint.pformat(self._Translation, indent=4, width=200))


#
#---------------------------------------------
# Make the class look like a dictionary
# but this dictionary also includes all keys
# of all the parents
#---------------------------------------------

    def __len__(self):
        """
        The Python __len__ method returns a positive integer that
        represents the length of the object on which it is called.
        It implements the built-in len() function.

        Needed to make this class act like a dict.
        """
        OwnLen = len(self.__WorkDict)
        if self.__Parent is None:
            return OwnLen
        return len(self.items())

    def __contains__(self, item):
        """
        The Python __contains__() magic method implements the
        membership operation, i.e., the in keyword. Semantically,
        the method returns True if the argument object exists in
        the sequence on which it is called, and False otherwise.

        Needed to make this class act like a dict.
        """
        if item in self.__WorkDict:
            return True
        if self.__Parent is None:
            return False
        return item in self.__Parent                        # Weiss ich besser: Parent is dict!  # pylint: disable=unsupported-membership-test

    def __getitem__(self, item):
        """
        Python’s magic method __getitem__(self, key) to
        evaluate the expression self[key].

        Needed to make this class act like a dict.
        """
        if item in self.__WorkDict:
            return self.__WorkDict[item]
        return self.__SearchItem(item, True)

    def __SearchItem(self, item, Up:bool = True):
        """
        Search for an item

        Needed to make this class act like a dict.

        :param item: the key we are searching
        :type item: any
        :param Up: if True: search also my parent, defaults to True
        :type Up: bool, optional
        :raises KeyError: if key is not found
        :return: the found value for this key
        :rtype: any
        """
        if Up:
            if self.__Parent is None:
                return self.__SearchItem(item,Up=False)
            return self.__Parent.__SearchItem(item,Up)                  # pylint: disable=protected-access
        else:
            if item in self.__WorkDict:
                return self.__WorkDict[item]
            for c in self.__Children.values():
                try:
                    return c.__SearchItem(item,Up)                  # pylint: disable=protected-access
                except KeyError:
                    pass
            raise KeyError(item)

    def __setitem__(self, key, value):
        """
        Python’s magic method __setitem__(self, key, value)
        implements the assignment operation to self[key].

        Needed to make this class act like a dict.
        """
        self.__WorkDict[key] = value

    def __delitem__(self, key):
        """
        Python’s magic method __delitem__(self, key)
        implements the deletion of self[key].

        Needed to make this class act like a dict.
        """
        self.__WorkDict.__delitem__(key)

    def __missing__(self, key):
        """
        The __missing__(self, key) method defines the behavior
        of a dictionary subclass if you access a non-existent key.
        More specifically, Python’s __getitem__() dictionary method
        internally calls the __missing__() method if the key doesn’t
        exist. The return value of __missing__() is the value to be
        returned when trying to access a non-existent key.
        We raise an KexError if we dont have a parent, else we return
        the value from this parent.

        Needed to make this class act like a dict.
        """
        if self.__Parent is None:
            raise KeyError(key)
        return self.__Parent[key]                       # Ich weiss das besser! # pylint: disable=unsupported-membership-test,unsubscriptable-object

    def __get__(self, instance, owner):
        """
        Python’s __get__() magic method defines the dynamic return
        value when accessing a specific instance and class attribute.
        It is defined in the attribute’s class and not in the class
        holding the attribute (= the owner class). More specifically,
        when accessing the attribute through the owner class, Python
        dynamically executes the attribute’s __get__() method to
        obtain the attribute value.

        Needed to make this class act like a dict.
        """
        return self.__get__(instance, owner)

    def __iter__(self):
        """
        The Python __iter__ method returns an iterator object.
        An iterator object is an object that implements the __next__()
        dunder method that returns the next element of the iterable
        object and raises a StopIteration error if the iteration is done.

        Needed to make this class act like a dict.

        :return: the combined iterator of all parents and our own instance
        :rtype: iterator
        """
        if self.__Parent is None:
            return self.__iter__()
        else:
            return chain(self.__Parent.__iter__(), self.__iter__())

    def IsOwnKey(self,key: str) -> bool:
        """
        Check if the key is from the own optionset

        :param key: Key to search for
        :type key: str
        :return: True if key is in the own optionset
        :rtype: bool
        """
        return key in self.__WorkDict

    def IsInherited(self, key: str) -> bool:
        """
        Check if key is from parent

        :param key: Key to search for
        :type key: str
        :return: True if key is inherited from parent
        :rtype: bool
        """
        return not self.IsOwnKey(key)

    def keys(self) -> list:
        """
        Return the keys list including the keys of all parentsof

        :return: return the keys list
        :rtype: list
        """
        if self.__Parent is None:
            KeyList = list(self.__WorkDict.keys())
        else:
            KeyList = list(set(self.__Parent.keys()) | set(self.__WorkDict.keys()))
        KeyList.sort()
        return KeyList

    def values(self) -> list:
        """
        Return the values list including the values of all parents

        :return: return the values list
        :rtype: list
        """
        if self.__Parent is None:
            return list(self.__WorkDict.values())
        return list(self.__Parent.values() + self.__WorkDict.values())

    def items(self) -> list:
        """
        Return the items list including the items of all parents

        :return: return the items list
        :rtype: list
        """
        if self.__Parent is None:
            Res = list(self.__WorkDict.items())
            if Res is None:
                Res = []
        else:
            try:
                p = dict(self.__Parent.items())
            except:                           # pylint: disable=bare-except
                p = {}
            r = {}
            for key,value in p.items():
                r[key] = value
            for key,value in self.__WorkDict.items():
                r[key] = value
            Res = []
            for key,value in r.items():
                Res.append( (key, value))
        Res.sort()
        return Res
#---------------------------------------------
# END Make the class look like a dictionary
#---------------------------------------------
#

    @property
    def Child(self) -> Dict[str, object]:
        """
        Child dict

        :return: return all the children of this instance
        :rtype: Dict[str, :py:class:`Param`]
        """
        return self.__Children

    def AddChild(self,                           # pylint: disable=dangerous-default-value,redefined-outer-name
                 Prefix: str,
                 Def: dict = {},
                 Description: str = '',
                 Children: dict = {},
                 Version:str = '',               # pylint: disable=redefined-outer-name
                 License:list = [''],
                 AddPar: str = '') -> None:
        """
        Add a child to a instance

        :param Def: Definition for this instance (look at :func:`SetDef` for details), defaults to {}
        :type Def: dict, optional
        :param Description: Description of this instance, defaults to ''
        :type Description: str, optional
        :param Children: Dictionary of children to the new instance, defaults to {}
        :type Children: dict, optional
        :param Version: A version string, defaults to ''
        :type Version: str, optional
        :param AddPar: Additional parameter string of this instance, defaults to ''
        :type AddPar: str, optional
        :raises self.DeclarationError: If a parameter is invalid
        """
        if not isinstance(Prefix, str):
            raise self.DeclarationError(f"{self.FullPrefix}: Prefix is not a string")
        p = Prefix.lower().strip()
        if p in self.__Children:
            raise self.DeclarationError(f"{self.FullPrefix}: Prefix '{p}' is already used")
        if p == GLOBAL_NAME:
            raise self.DeclarationError(f"{self.FullPrefix}: Prefix '{p}' is {GLOBAL_NAME} -> invalid!")
        # self.__Children[p] = self.__class__( Def = Def,
        self.__Children[p] = Param( Def = Def,
                                    Args = self.__Argumente,
                                    # Translate = self.__DoTranslate,
                                    UserPars = self.__UserPars,
                                    Desc = Description,
                                    Children = Children,
                                    AddPar = AddPar,
                                    AllParams = self.__AllParams,
                                    _Child = True,
                                    HelpType = self.__HelpType,
                                    Version = Version,
                                    License = License,
                                    ShowPrefixOnHelp=self.__ShowPrefixOnHelp,
                                    ErrorOnUnknown = False          # always False for children
                                    )
        self.__Children[p].__Parent = self                          # pylint: disable=protected-access
        self.__Children[p].__Prefix = p                             # pylint: disable=protected-access
        self.__Children[p]._Translation = self._Translation         # pylint: disable=protected-access

    def SetAllParams(self, AllParams: bool = True) -> None:
        """
        Set the flag for All Params

        :param AllParams: If True, all params are initialized,
            at least with None. If False params with no default and no setting on
            the commandline are not defined within the dictionary, defaults to True
        :type AllParams: bool, optional
        """
        self.__AllParams = AllParams
        self.__IsPrepared = False   # we need a Prepare-call after this


    def SetDef(self, Def: dict = {}) -> None:                           # pylint: disable=dangerous-default-value
        """
        Set the definition for processing arguments

        :param Def: A definition-dict. Defaults to {}.
        :type Def: dict, optional
        :raises TypeError: on error within the definition

        Describes the definition for arg-parsing.

        Def-dict: a dictionary of dictionaries

        .. code-block:: python

            { 'Name1': {.. declaration ..},
            ...
            'Name2': {.. declaration ..}, }

        "NameN" is the key with which, at runtime, you get the values within the resulting dictionary.

        The individual definitions look like:

        .. code-block:: python

            {'s': 'a',
            'l': 'longval',
            'o': True,
            'v': "LuLu",
            'm': 't',
            'd': 'Description',
            'L': 'Low',
            'U': 'Up',
            'r': False },

        where:

        .. code-block::

            m : Mode ->
                    't' = Text,
                    'b' = Bool,
                    'p' = Path must not exist but is valid on this operating system,
                    'f' = Existing File,
                    'd' = Existing Dir,
                    'i' = Integer,
                    'F' = Float,
                    'C' = Counter (start default as 0 and increment each time found)
                            Special case: short option takes no argument,
                            long option NEEDS argument
                            short option increments the value,
                            long option adds the argument to the value
            The following are processed BEVOR all others:
                    'H' = Show help and exit
                    '§' = Display short license and exit
                    'L' = Display long license and exit
                    'x' = Import config-file as json (file must exist like "f")
                                can be given more than once!
                    '<' = MultiImport config-file as json
            The following are processed AFTER all others:
                    'X' = Export config as json to stdout und exit
                    '>' = MultiExport config as json to stdout und exit
            r : Required -> True or False, False is default
            s : Short Option(s) -> string or list or tuple of strings
            l : Long Option(s) -> string or list or tuple of strings
            o : option needs argument -> True oder False, False is default
            v : Default value -> if not given:
                    "" for Text,
                    False for Bool,
                    None for Path, File and Dir,
                    0 for Int und Counter,
                    0. for Float
                    [] for multi-items
            L : Lower Limit, value >= L if present
            U : Upper Limit, value <= U if present
            d : Description for helptext
            M : If True: multiples of this option are accepted.
                the resulting value is a list.

        The entries "m" and ("s" or "l") must be present, all others are optional.

        """
        if isinstance(Def, dict):
            self.__Definition = Def
        else:
            raise TypeError(f"{self.FullPrefix}: Def is not a dict")
        self.__IsPrepared = False   # we need a Prepare-call after this

    @property
    def Definition(self) -> dict:
        """
        Returns s copy of the definition

        :return: a definition dictionary
        :rtype: dict
        """
        return copy.deepcopy(self.__Definition)

    @property
    def FullPrefix(self) -> str:
        """
        Returns the full qualified prefix of this instance
        e.g.: global.alpha.gamma
        if alpha is a child of global and gamma (this instance) is a child of alpha

        :return: full qualified prefix of this instance
        :rtype: str
        """
        Erg = self.Parents
        if Erg != '':
            Erg += '.'
        return Erg + self.__Prefix


    @property
    def PartPrefix(self) -> str:
        """
        Returns the full qualified prefix without global of this instance
        e.g.: alpha.gamma
        if alpha is a child of global and gamma (this instance) is a child of alpha

        :return: full qualified prefix of this instance without root prefix
        :rtype: str
        """
        return self.FullPrefix.replace(GLOBAL_NAME + '.','')

    @property
    def Parents(self) -> str:
        """
        Returns the full qualified parents of this instance
        e.g.: global.alpha
        if alpha is a child of global and gamma (this instance) is a child of alpha

        :return: full qualified parents of this instance
        :rtype: str
        """
        Erg = ''
        if self.__Parent is None:
            return ''
        Erg = self.__Parent.Parents
        if Erg != '':
            Erg += '.'
        Erg += self.__Parent.__Prefix                           # pylint: disable=protected-access
        return Erg

    def GetCmdPar(self, Entry: str, dotted: bool = False, parents: bool = False) -> str:
        """
        Return the commandline-options for one entry

        :param Entry: The entry we are looking for
        :type Entry: str
        :param dotted: show prefix for long params, defaults to False
        :type dotted: bool, optional
        :param parents: show also options from parents, defaults to False
        :type parents: bool, optional
        :return: the command-line options for this entry. E.g. "-h, --help"
        :rtype: str
        """
        Erg = ""
        if parents:
            dotted = True
        try:
            SingleDef = self.__Definition[Entry]
        except KeyError:
            if parents:
                if self.__Parent is None:
                    return ''
                return self.__Parent.GetCmdPar(Entry = Entry, dotted = dotted, parents = parents)
            return ''
        try:
            wText = SingleDef[self.__WorkPars['shortpar']]
            for w in wText:
                if Erg != '':
                    Erg += ', '
                Erg += "-" + w
        except KeyError:
            pass
        if dotted:
            Lp = '[' + self.__Prefix +'.]'
        else:
            Lp = ''
        try:
            wText = SingleDef[self.__WorkPars['longpar']]
            if isinstance(wText, (list, tuple)):
                for w in wText:
                    if Erg != '':
                        Erg += ', '
                    Erg += "--" + Lp + w
            elif isinstance(wText, str):
                if Erg != '':
                    Erg += ', '
                Erg += "--" + Lp + wText
        except KeyError:
            pass
        if Erg == '':
            if parents:
                if self.__Parent is not None:
                    Erg = self.__Parent.GetCmdPar(Entry = Entry, dotted = dotted, parents = parents)
        return Erg

    def SetUserKeys(self, UserPars: Optional[dict] = None, UserModes: Optional[dict] = None) -> None:
        """
        _summary_

        :param UserPars: ignored if None. Defaults to None.
            Dictionary of keys used within the definition-dictionary.
            All key-value pairs are optional.
            Only the keys from self.__WorkPars are valid.
            The value has to be a string. This string replaces the
            keysting for this key.
            After all changes are made the values within self.__WorkPars
            have to be unique!, defaults to None
        :type UserPars: Optional[dict], optional
        :param UserModes: ignored if None. Defaults to None.
            Dictionary of modes used within the definition-dictionary.
            All key-value pairs are optional.
            Only the keys from self.__WorkModes are valid.
            The value has to be a string. This string replaces the
            keysting for this key.
            After all changes are made the values within self.__WorkModes
            have to be unique!, defaults to None
        :type UserModes: Optional[dict], optional
        :raises TypeError: if invalid type
        :raises DeclarationError: if declaration is invalid
        """
        if UserPars is not None:
            if not isinstance(UserPars, dict):
                raise TypeError(f'{self.FullPrefix}: UserPars is not a dict')
            for k in UserPars.keys():
                if not k in self.__WorkPars:
                    raise self.DeclarationError(f"{self.FullPrefix}: UserPars {k} is invalid. Valid values are {self.__WorkPars.keys()}")
                v = UserPars[k]
                if not isinstance(v, str):
                    raise TypeError(f"{self.FullPrefix}: Value of UserPars {k} is not a string")
                self.__WorkPars[k] = v
            Double = self.__CheckMulti(self.__WorkPars)
            if Double:
                raise self.DeclarationError(f"{self.FullPrefix}: UserPars {Double} have the same value {self.__WorkPars[Double[0]]}")

        if UserModes is not None:
            if not isinstance(UserModes, dict):
                raise TypeError(f'{self.FullPrefix}: UserModes is not a dict')
            for k in UserModes.keys():
                if not k in self.__WorkModes:
                    raise self.DeclarationError(f"{self.FullPrefix}: UserModes {k} is invalid. Valid values are {self.__WorkModes.keys()}")
                v = UserModes[k]
                if not isinstance(v, str):
                    raise TypeError(f"{self.FullPrefix}: Value of UserModes {k} is not a string")
                self.__WorkModes[k] = v
            Double = self.__CheckMulti(self.__WorkModes)
            if Double:
                raise self.DeclarationError(f"{self.FullPrefix}: UserModes {Double} have the same value {self.__WorkModes[Double[0]]}")


    def __CheckMulti(self, wDict: dict) -> list:
        return [k for k,v in wDict.items() if list(wDict.values()).count(v)!=1]


    def SetArgs(self, Args:Optional[Union[list, tuple]] = None) -> None:
        """
        Set the argument list to process

        :param Args: Runtime Arguments, if None: use sys.argv as the arguments , defaults to None
        :type Args: Optional[Union[list, tuple]], optional
        :raises TypeError: if Args is not a list or tuple
        """
        if Args is None:
            self.__Argumente = sys.argv
        elif isinstance(Args, (list, tuple)):
            self.__Argumente = Args
        else:
            raise TypeError(f'{self.FullPrefix}: Args is not a list or tuple')
        for c in self.__Children.values():
            c.SetArgs(Args)


    def SetChk(self, Chk = None):
        """
        Set the check-function. Not implementet now

        :param Chk: The user check function
        :type Chk: callable
        :raises TypeError: if function is not of the proper type
        """
        if Chk is None:
            self.__ChkFunc = Chk                # pylint: disable=unused-private-member
        else:
            if isinstance(Chk, types.FunctionType):
                a = inspect.getfullargspec(Chk).args
                if len(a) != 2:
                    raise TypeError(f'{self.FullPrefix}: Check function does not take 2 arguments')
                self.__ChkFunc = Chk                # pylint: disable=unused-private-member
            else:
                raise TypeError(f'{self.FullPrefix}: Check is not a function')
        self.__IsPrepared = False   # we need a Prepare-call after this
        for c in self.__Children.values():
            c.SetChk(Chk)

    def SetDesc(self, Desc: str = '') -> None:
        """
        Set the description of the program for usage-string.

        :param Desc: A descriptive string for the Program.
            printed bevore the parameters. Defaults to ''.
        :type Desc: str, optional
        :raises TypeError: if Desc is not a string.
        """
        if isinstance(Desc, str):
            self.__Description = Desc
        else:
            raise TypeError(f'{self.FullPrefix}: Desc is not a string')
        self.__IsPrepared = False   # we need a Prepare-call after this

    def SetAddPar(self, AddPar: str = "") -> None:
        """
        Description of additional parameters for usage-function.
        printed in first line after "OPTIONS"
        normally used if there are non-option parameters on command line.
        (e.g. file ... file)

        :param AddPar: The text or additional parameters. Defaults to "".
        :type AddPar: str, optional
        :raises TypeError: if AddPar is not a string
        """
        if isinstance(AddPar, str):
            self.__AddPar = AddPar
        else:
            raise TypeError(f'{self.FullPrefix}: AddPar is not a string')
        self.__IsPrepared = False   # we need a Prepare-call after this

    def MyProgName(self) -> str:
        """
        Return the program-name

        :return: Name of the executeable
        :rtype: str
        """
        return self.__MyProgName

    def MyProgPath(self) -> str:
        """
        Return the program-path

        :return: Path of the directory where executeable resides
        :rtype: str
        """
        return self.__MyProgPath

    def MyPwd(self) -> str:
        """
        Return the directory at invocation of "Process"

        :return: Current directory at the time "Process" was called
        :rtype: str
        """
        return self.__MyPwd

    def __GenUsageText(self,ShortLen: int, LongLen: int, IsChild = False) -> None:
        """
        Generate the "Usage"-text

        Args:
            ShortLen (int): Max. length of the "short"-options (0 or 1)
            LongLen (int): Max. length of the "long"-options
        """
        if self.__HelpType == 0:
            ShowType = False
            ShowDef = False
        elif self.__HelpType == 1:
            ShowType = False
            ShowDef = True
        elif self.__HelpType == 2:
            ShowType = True
            ShowDef = False
        elif self.__HelpType == 3:
            ShowType = True
            ShowDef = True


        if self.__Prefix is None:
            wPrefText = ''
        else:
            if self.__Prefix != GLOBAL_NAME:
                wPrefText = ''
            else:
                wPrefText = ''
        wDesc = self.__Description
        if wDesc != '':
            wDesc += '\n'
        VerText = f"{self._Translation['HelpVersion']}: {self.__Version}\n" if self.__Version != '' and self.__Parent is None else ''
        if IsChild:
            Text = f"{VerText}\n{wDesc}"
        else:
            Text = f"{VerText}{self._Translation['HelpUsage']}\n\n    {self.__MyProgName} {self._Translation['HelpOptionInline']} {self.__AddPar}\n\n{wDesc}{wPrefText}{self._Translation['HelpOptions']}\n"
        for Single in self.__UsageTextList:
            Ut_Short = Single[0]
            Ut_Long = Single[1]
            Ut_Param = Single[2]
            Ut_Type = Single[3]
            Ut_Default = Single[4]
            Ut_Low = Single[6]
            Ut_High = Single[7]

            if Ut_Low is None and Ut_High is None:
                LimitText = ''
            if Ut_Low is None and Ut_High is not None:
                if isinstance(Ut_High,str):
                    h = "'" + Ut_High + "'"
                else:
                    h = str(Ut_High)
                LimitText = f"(... {h})"
            if Ut_Low is not None and Ut_High is None:
                if isinstance(Ut_Low,str):
                    l = "'" + Ut_Low + "'"
                else:
                    l = str(Ut_Low)
                LimitText = f"({l} ...)"
            if Ut_Low is not None and Ut_High is not None:
                if isinstance(Ut_High,str):
                    h = "'" + Ut_High + "'"
                else:
                    h = str(Ut_High)
                if isinstance(Ut_Low,str):
                    l = "'" + Ut_Low + "'"
                else:
                    l = str(Ut_Low)
                LimitText = f"({str(l)} ... {h})"
            if ShowType:
                if LimitText != '':
                    LimitText = ' ' + LimitText

            if not ShowDef:
                if Ut_Default == '' or Ut_Default == 0 or not Ut_Default:
                    Ut_Default = None
            if Ut_Default is None:
                Ut_Default = LimitText
            else:

                if isinstance(Ut_Default,str):
                    d = "'" + Ut_Default + "'"
                else:
                    d = str(Ut_Default)
                if LimitText == '':
                    Ut_Default = f"{self._Translation['HelpDefault']}: {d}"
                else:
                    Ut_Default = f"{LimitText}, {self._Translation['HelpDefault']}: {d}"
            Ut_Text = Single[5].splitlines()
            sl = ShortLen + 3 + 1
            ll = LongLen + 3 + 2
            if self.__Prefix is not None:
                if self.__Prefix != '' and self.__Prefix != GLOBAL_NAME:
                    ll = ll + len(self.__Prefix) + 3
            Lines = max(len(Ut_Short),len(Ut_Long),len(Ut_Text)+1)
            while len(Ut_Short) < Lines:
                Ut_Short.append(" ")

            while len(Ut_Long) < Lines:
                Ut_Long.append(" ")
            if ShowType:
                if Ut_Default != '':
                    if not Ut_Default.startswith(' '):
                        Ut_Default = ' ' + Ut_Default
                Ut_Text.insert(0,f"Type: {Ut_Type}{Ut_Default}")
            else:
                if Ut_Default != '':
                   Ut_Text.insert(0,f"{Ut_Default}")
            while len(Ut_Text) < Lines:
                Ut_Text.append(" ")

            for i in range(Lines):
                wLine = "\n   "
                s = Ut_Short[i]
                l = Ut_Long[i]
                if self.__Prefix is not None:
                    if self.__Prefix != '' and self.__Prefix != GLOBAL_NAME and l != " ":
                        l = '[' + self.__Prefix + '.]' + l
                t = Ut_Text[i]
                if s == " ":
                    n = " " * sl
                else:
                    n = ("-" + s + (" " * sl))[:sl]
                wLine += n
                if l == " ":
                    n = " " * ll
                else:
                    if Ut_Param.strip() == "":
                        n = "--" + l
                    else:
                        n = "--" + l + "="
                if i == 0:
                    n += Ut_Param
                n = (n + (" " * (ll + len(Ut_Param) + 2)))[:ll + len(Ut_Param) + 2]
                wLine += n + t
                if wLine.strip() != '':
                    Text += wLine
            Text += "\n"
        self.__UsageText = Text

    def Usage(self, ShowPrefixHeader:bool = True) -> str:
        """
        Return the helptext

        :return: The help-text as would be printet if a "Help" option is set on command-line
        :rtype: str
        """
        if not self.__IsPrepared:
            self.__Prepare()
        Ret = self.__UsageText
        for c in self.__Children.values():
            Ret += f"""
    ------------------------------
    {c.PartPrefix}
    ------------------------------
""" if ShowPrefixHeader else '\n'
            e = c.Usage(ShowPrefixHeader)
            lines = e.splitlines()
            for l in lines:
                Ret += '    ' + l + '\n'
        return Ret

    def __Prepare(self) -> None:
        """
        Prepare the class to be able to be used

        Raises:
            self.DeclarationError: if there are errors within the declaration-dict
        """

        # clear all values
        self.__WorkDict.clear()
        self.__UsageText = ""
        LongParLen = 0
        ShortParLen = 0
        self.__LongList = []
        self.__ShortStr = ""
        self.__ShortList = []
        self.__ParDict = {}
        self.__RemainArgs = []
        self.__UnusedArgs = []
        self.__UsageTextList = []
        self.__MyPwd = str(Path.cwd())
        self.__MyProgName = Path(sys.argv[0]).stem
        self.__MyProgPath = str(Path(sys.argv[0]).parent)

        for c in self.__Children.values():
            if not c.__IsPrepared:                          # pylint: disable=protected-access
                c.__Prepare()                               # pylint: disable=protected-access

        for ParName in self.__Definition.keys():
            SingleDef = self.__Definition[ParName]
            Ut_Short = []
            Ut_Long = []
            Ut_Param = ''
            Ut_Default = ''
            Ut_Text = ''
            Ut_Type = ''
            Ut_Low = None
            Ut_High = None
            ParKeys = SingleDef.keys()
            if self.__WorkPars['lowlimit'] in ParKeys:
                Ut_Low = SingleDef[self.__WorkPars['lowlimit']]
            if self.__WorkPars['uplimit'] in ParKeys:
                Ut_High = SingleDef[self.__WorkPars['uplimit']]

            if self.__WorkPars['multiple'] in ParKeys:
                ParMulti = SingleDef[self.__WorkPars['multiple']]
            else:
                ParMulti = False

            if self.__WorkPars['mode'] in ParKeys:
                ParMode = SingleDef[self.__WorkPars['mode']]
            else:
                raise self.DeclarationError(f"{self.FullPrefix}: No mode setting in Def for {ParName}")
            if ParMode == self.__WorkModes['path']:
                Ut_Type = self._Translation['TypePath']
                SingleDef[self.__WorkPars['needoption']] = True
            elif ParMode == self.__WorkModes['int']:
                Ut_Type = self._Translation['TypeInteger']
                Ut_Default = 0
            elif ParMode == self.__WorkModes['bool']:
                Ut_Type = self._Translation['TypeBool']
                Ut_Default = False
            elif ParMode == self.__WorkModes['float']:
                Ut_Type = self._Translation['TypeFloat']
                Ut_Default = 0.0
            elif ParMode == self.__WorkModes['file']:
                Ut_Type = self._Translation['TypeFile']
                SingleDef[self.__WorkPars['needoption']] = True
            elif ParMode == self.__WorkModes['dir']:
                Ut_Type = self._Translation['TypeDir']
                SingleDef[self.__WorkPars['needoption']] = True
            elif ParMode == self.__WorkModes['count']:
                Ut_Type = self._Translation['TypeCount']
                if self.__WorkPars['longpar'] in ParKeys:
                    SingleDef[self.__WorkPars['needoption']] = True
            elif ParMode == self.__WorkModes['help']:
                Ut_Type = self._Translation['TypeHelp']
            elif ParMode == self.__WorkModes['import']:
                Ut_Type = self._Translation['TypeImport']
                SingleDef[self.__WorkPars['needoption']] = True
            elif ParMode == self.__WorkModes['export']:
                Ut_Type = self._Translation['TypeExport']
            elif ParMode == self.__WorkModes['glob_import']:
                if self.__Parent is not None:
                    raise self.DeclarationError(f"{self.FullPrefix}: {ParName} is invalid in child definition")
                Ut_Type = self._Translation['TypeGlobImport']
                SingleDef[self.__WorkPars['needoption']] = True
            elif ParMode == self.__WorkModes['glob_export']:
                if self.__Parent is not None:
                    raise self.DeclarationError(f"{self.FullPrefix}: {ParName} is invalid in child definition")
                Ut_Type = self._Translation['TypeGlobExport']
            else:
                Ut_Type = self._Translation['TypeStr']

            if self.__WorkPars['default'] in ParKeys:
                wMode = SingleDef[self.__WorkPars['mode']]
                if  wMode != self.__WorkModes['help'] \
                    and wMode != self.__WorkModes['import'] \
                    and wMode != self.__WorkModes['export'] \
                    and wMode != self.__WorkModes['glob_import'] \
                    and wMode != self.__WorkModes['glob_export']:
                    self.__WorkDict[ParName] = SingleDef[self.__WorkPars['default']]
                if ParMode == self.__WorkModes['file']:
                    wText = SingleDef[self.__WorkPars['default']]
                    try:
                        if wText[0] != "/":
                            wText = self.__MyPwd + '/' + wText
                        wFile = Path(wText).absolute()
                        if wFile.is_file():
                            self.__WorkDict[ParName] = str(wFile)
                    except IndexError:
                        wText = ''
                        self.__WorkDict[ParName] = wText
                elif ParMode == self.__WorkPars['description']:
                    wText = SingleDef[self.__WorkPars['default']]
                    if wText[0] != "/":
                        wText = self.__MyPwd + '/' + wText
                    wFile = Path(wText).absolute()
                    if wFile.is_dir():
                        self.__WorkDict[ParName] = str(wFile)
                elif ParMode == self.__WorkModes['path']:
                    wText = SingleDef[self.__WorkPars['default']]
                    if len(wText) > 0:
                        if wText[0] != "/":
                            wText = self.__MyPwd + '/' + wText
                        wFile = Path(wText).absolute()
                        self.__WorkDict[ParName] = str(wFile)
                    else:
                        self.__WorkDict[ParName] = ''
                Ut_Default = SingleDef[self.__WorkPars['default']]
            else:
                if self.__AllParams:
                    if ParMode == self.__WorkModes['bool']:
                        self.__WorkDict[ParName] = False
                    elif ParMode == self.__WorkModes['text']:
                        if ParMulti:
                            self.__WorkDict[ParName] = []
                        else:
                            self.__WorkDict[ParName] = ""
                    elif ParMode == self.__WorkModes['int']:
                        if ParMulti:
                            self.__WorkDict[ParName] = []
                        else:
                            self.__WorkDict[ParName] = 0
                    elif ParMode == self.__WorkModes['float']:
                        if ParMulti:
                            self.__WorkDict[ParName] = []
                        else:
                            self.__WorkDict[ParName] = 0.
                    elif ParMode == self.__WorkModes['count']:
                        self.__WorkDict[ParName] = 0
                    else:
                        if ParMode not in self.__SpecialOpts:
                            if ParMulti:
                                self.__WorkDict[ParName] = []
                            else:
                                self.__WorkDict[ParName] = None
            NeedOpt = False
            if self.__WorkPars['needoption'] in ParKeys:
                if SingleDef[self.__WorkPars['needoption']]:
                    NeedOpt = True
                    Ut_Param = self._Translation['HelpValue']
                else:
                    Ut_Param = ' ' * len(self._Translation['HelpValue'])
            else:
                Ut_Param = ' ' * len(self._Translation['HelpValue'])
            if self.__WorkPars['longpar'] in ParKeys:
                wText = SingleDef[self.__WorkPars['longpar']]
                if isinstance(wText, (list, tuple)):
                    for ws in wText:
                        if not isinstance(ws, str):
                            raise self.DeclarationError(f"{self.FullPrefix}: One of the long values for {ParName} is not a string")
                        l = len(ws)
                        if '--' + ws in self.__ParDict.keys():          # pylint: disable=consider-iterating-dictionary
                            raise self.DeclarationError(f"{self.FullPrefix}: Double long value for {ParName}: {ws}")
                        self.__ParDict['--' + ws] = ParName
                        for ListPar, ListVal in self.__ModeToList.items():
                            if ParMode == ListPar:
                                ListVal.append('--' + ws)

                        Ut_Long.append(ws)
                        if NeedOpt:
                            self.__LongList.append(ws + "=")
                        else:
                            self.__LongList.append(ws)
                        if l > LongParLen:
                            LongParLen = l
                elif not isinstance(wText, str):
                    raise self.DeclarationError(f"{self.FullPrefix}: Long value for {ParName} is not a string")
                else:
                    if '--' + wText in self.__ParDict.keys():          # pylint: disable=consider-iterating-dictionary
                        raise self.DeclarationError(f"{self.FullPrefix}: Double long value for {ParName}: {wText}")
                    self.__ParDict['--' + wText] = ParName
                    for ListPar, ListVal in self.__ModeToList.items():
                        if ParMode == ListPar:
                            ListVal.append('--' + wText)
                    Ut_Long.append(wText)
                    l = len(wText)
                    if NeedOpt:
                        self.__LongList.append(wText + "=")
                    else:
                        self.__LongList.append(wText)
                    if l > LongParLen:
                        LongParLen = l
            if self.__WorkPars['shortpar'] in ParKeys:
                wText = SingleDef[self.__WorkPars['shortpar']]
                if isinstance(wText, (list, tuple)):
                    for ws in wText:
                        if not isinstance(ws, str):
                            raise self.DeclarationError(f"{self.FullPrefix}: One of the short values for {ParName} is not a string")
                        for c in ws:
                            if '-' + c in self.__ParDict.keys():          # pylint: disable=consider-iterating-dictionary
                                raise self.DeclarationError(f"{self.FullPrefix}: Double short value for {ParName}: {c}")
                            self.__ParDict['-' + c] = ParName
                            for ListPar, ListVal in self.__ModeToList.items():
                                if ParMode == ListPar:
                                    ListVal.append('-' + c)

                            Ut_Short.append(c)
                            rEntry = c
                            self.__ShortStr += c
                            if NeedOpt:
                                self.__ShortStr += ":"
                                rEntry += ":"
                            self.__ShortList.append(rEntry)
                elif not isinstance(wText, str):
                    raise self.DeclarationError(f"{self.FullPrefix}: Short value for {ParName} is not a string")
                else:
                    for c in wText:
                        if '-' + c in self.__ParDict.keys():          # pylint: disable=consider-iterating-dictionary
                            raise self.DeclarationError(f"{self.FullPrefix}: Double short value for {ParName}: {c}")
                        self.__ParDict['-' + c] = ParName
                        for ListPar, ListVal in self.__ModeToList.items():
                            if ParMode == ListPar:
                                ListVal.append('-' + c)
                        Ut_Short.append(c)
                        rEntry = c
                        self.__ShortStr += c
                        if NeedOpt:
                            if SingleDef[self.__WorkPars['mode']] != self.__WorkModes['count']:
                                self.__ShortStr += ":"
                                rEntry += ":"
                        self.__ShortList.append(rEntry)
                if ShortParLen == 0:
                    ShortParLen = 1
            if self.__WorkPars['description'] in ParKeys:
                Ut_Text = SingleDef[self.__WorkPars['description']]
            self.__UsageTextList.append( [Ut_Short,Ut_Long,Ut_Param,Ut_Type,Ut_Default,Ut_Text,Ut_Low,Ut_High] )
        IsChild = True
        if self.__Parent is None:
            IsChild = False
        self.__GenUsageText(ShortParLen,LongParLen,IsChild=IsChild)
        self.__IsPrepared = True



    def __Make_OptName(self,OptionNameIn:str):
        OptionName:str = OptionNameIn
        LongOptStr = OptionNameIn
        RemStr = ''
        if OptionName.startswith('--'):
            if '.' in OptionName:
                if '=' in OptionName:
                    w = OptionName.split('=',1)
                    OptionName = w[0]
                    RemStr = '=' + w[1]
                wList = OptionName[2:].split('.')
                if len(wList) != 2:
                    raise self.ParamError(f"Error in prefixed parameter {OptionName}") from None
                if wList[0] == self.__Prefix:
                    LongOptStr = '--' + wList[1] + RemStr
        return LongOptStr

    def Process(self) -> bool:
        """
        Process the runtime-arguments.
        After this call the values of the class are all set.

        .. note::
            You can not access the values bevore you call this function. The results
            are undefined.

        :raises RuntimeError: if an internal error occures. Should never occure!
        :raises ParamError: if an error occures within a parameter
        :return: True if a terminal function is requested. e.g this are "Help", all "License" and all "Export" options
        :rtype: bool
        """
        Erg = self.__Process(True)
        if Erg:
            return Erg
        Erg = self.__Process(False)
        if len(self.UnusedArgs) > 0:
            if self.__ErrorOnUnknown:
                # OptStr = ', '.join(self.UnusedArgs)
                OptStr = ', '.join(["'" + x + "'" for x in self.UnusedArgs])
                if len(self.UnusedArgs) > 1:
                    raise self.ParamError(self._Translation['UndefinedOptionMultiple'].format(
                            **{'OptStr':OptStr})) from None
                else:
                    raise self.ParamError(self._Translation['UndefinedOptionSingle'].format(
                            **{'OptStr':OptStr})) from None
        return Erg

    def __Process(self,IsFirst:bool) -> bool:
        """
        Process the runtime-arguments.

        Args:
            IsFirst (bool): If True: Only "Help", "Global-Import and "Import"
                            types are processed. Childs are processed AFTER
                            our own function
                            If False: All other types are processed. Childs
                            are processed BEFORE our own function
                            This is necessary to correctly handle these special
                            Parameters.
                                "Help" ignores ALL other parameters.
                                Any "Import" has to be done BEFORE any other
                                parameters because they should overwrite the
                                imported values.

        Raises:
            self.ParamError: if an error occures within a parameter
            RuntimeError: if an internal error occures
        """
        if not IsFirst:
            Erg = False
            for c in self.__Children.values():
                if c.__Process(IsFirst):                # pylint: disable=W0212
                    Erg = True


        if not self.__IsPrepared:
            self.__Prepare()
        PreList = []
        for wPar in self.__Argumente[1:]:
            if wPar[0:2] == '--':
                xPar = wPar[2:]
                if '=' in xPar:
                    xPar = xPar.split('=',1)[0]
                if '.' in xPar:
                    xPre = wPar[2:].split('.')[0]
                    if xPre not in PreList:
                        PreList.append(xPre)
        wLongList = []
        for nLong in self.__LongList:
            wLongList.append(nLong)
        if len(PreList) > 0:
            for nPre in PreList:
                for nLong in self.__LongList:
                    wLongList.append(nPre + '.' + nLong)
        try:
            opts, args, unused = self._gnu_getopt(self.__Argumente[1:], self.__ShortStr, wLongList, True)
            # opts, args = self._getopt(self.__Argumente[1:], self.__ShortStr, wLongList, True)
        except self.GetoptError as exc:
            wMsg = exc.msg
            raise self.ParamError(wMsg) from None
        self.__RemainArgs = args
        self.__UnusedArgs = unused
        if IsFirst:
# HELP & Licenses
            for OptionName, a in opts:
                del a
                OptionName = self.__Make_OptName(OptionName)
                if OptionName in self.__HelpList:
                    # Hier geben wir die Hilfe aus. print ist hier richtig! Soll auf StdOut gehen
                    if self.__Prefix is not None:
                        if self.__Prefix != '' and self.__Prefix != GLOBAL_NAME:
                            print(f"#{'-'*60}\n# {self.__Prefix}\n#{'-'*60}\n")
                    print(self.Usage(self.__ShowPrefixOnHelp))
                    if self.__Parent is None:
                        sys.exit(0)
                    return True
                if OptionName in self.__LicenseList:
                    print(self.__License[0])
                    return True
                if OptionName in self.__FullLicenseList:
                    print('\n'.join(self.__License))
                    return True


# GLOBAL IMPORT
            for OptionName,OptionPath in opts:
                OptionName = self.__Make_OptName(OptionName)
                if OptionName in self.__Glob_ImportList:
                    FullPath = Path(OptionPath).expanduser().resolve()
                    if FullPath.exists():
                        if FullPath.is_file():
                            try:
                                wGlobDict = JsonLoad(FullPath.open(encoding='utf-8'))
                            except Exception as exc:
                                wMsg = str(exc)
                                raise self.ParamError(

                                    f"Import failed '{wMsg}' in {OptionPath} ({FullPath}) for parameter {OptionName}") from None # JsonError
                            self.__AssignImportValues(wGlobDict, FileName=str(FullPath))
                        else:
                            raise self.ParamError(self._Translation['PathNoFile'].format(
                        **{'OptionPath':OptionPath, 'OptionName':OptionName, 'FullPath': FullPath})) from None
                                # f"The path {OptionPath} ({FullPath}) for parameter {OptionName} is not a file") from None # PathNoFile
                    else:
                        raise self.ParamError(self._Translation['PathNoFile'].format(
                        **{'OptionPath':OptionPath, 'OptionName':OptionName, 'FullPath': FullPath})) from None
                            # f"The path {OptionPath} ({FullPath}) for parameter {OptionName} is not a file") from None # PathNoFile

# IMPORT
            for OptionName, OptionPath in opts:
                OptionName = self.__Make_OptName(OptionName)
                if OptionName in self.__ImportList:
                    FullPath = Path(OptionPath).expanduser().resolve()
                    if FullPath.exists():
                        if FullPath.is_file():
                            try:
                                wDict = JsonLoad(FullPath.open(encoding='utf-8'))
                            except Exception as exc:
                                wMsg = str(exc)
                                raise self.ParamError(f"Import failed, {OptionPath} for parameter {OptionPath} is not a valid file") from None # JsonError
                            for k in self.__WorkDict.keys():                # pylint: disable=consider-iterating-dictionary
                                try:
                                    self.__WorkDict[k] = wDict[k]
                                except KeyError:
                                    pass
                        else:
                            raise self.ParamError(self._Translation['PathNoFile'].format(
                        **{'OptionPath':OptionPath, 'OptionName':OptionName, 'FullPath': FullPath})) from None
                                # f"The path {OptionPath} ({FullPath}) for parameter {OptionName} is not a file") from None # PathNoFile
                    else:
                        raise self.ParamError(self._Translation['PathNoFile'].format(
                        **{'OptionPath':OptionPath, 'OptionName':OptionName, 'FullPath': FullPath})) from None
                            # f"The path {OptionPath} ({FullPath}) for parameter {OptionName} does not exist") from None # PathNoFile
        else:
# Other Options
            for OptionName, OptionArg in opts:
                OptionName = self.__Make_OptName(OptionName)
                if OptionName in self.__HelpList:
                    continue
                if OptionName in self.__ImportList:
                    continue
                if OptionName in self.__Glob_ImportList:
                    continue
                if OptionName in self.__ExportList:
                    continue
                if OptionName in self.__Glob_ExportList:
                    continue
                try:
                    ParName = self.__ParDict[OptionName]
                except KeyError:
                    continue
                    # raise RuntimeError(f"Error, option {o} not found in ParDict")
                try:
                    wPar = self.__Definition[ParName]
                except:
                    raise RuntimeError(f"Internal error, option {ParName} not found in Definition") from None
                if self.__WorkPars['needoption'] in wPar.keys():
                    if wPar[self.__WorkPars['needoption']]:
                        Res = self.__CheckOption(ParName,OptionName,wPar,OptionArg)
                        if not Res is None:
                            raise self.ParamError(Res) from None
                        if wPar[self.__WorkPars['mode']] != self.__WorkModes['count']:
                            continue
                if wPar[self.__WorkPars['mode']] == self.__WorkModes['bool']:
                    try:
                        bVal = wPar[self.__WorkPars['default']]
                    except KeyError:
                        bVal = False
                    self.__WorkDict[ParName] = not bVal
                elif wPar[self.__WorkPars['mode']] == self.__WorkModes['count']:
                    if '--' not in OptionName:
                        self.__WorkDict[ParName] += 1
                else:
                    raise self.ParamError(self._Translation['OptionNotDefined'].format(
                        **{'OptionName':OptionName}))
                        # f"No action defined for {OptionName}")

            for OptionName, OptionArg in opts:
                OptionName = self.__Make_OptName(OptionName)
                if OptionName in self.__Glob_ExportList:
                    self.__Glob_ExportStr = json.dumps(self.GetExportDict, sort_keys=True, indent=4, cls=self.__PathEncoder)
                    self.__Glob_ExportStr += '\n'
                    if self.__Parent is None:
                        print(self.__Glob_ExportStr)
                        sys.exit(0)
                    return True
                if OptionName in self.__ExportList:
                    if self.__Prefix is not None:
                        if self.__Prefix != '':
                            print(f"//{'-'*60}\n// {self.__Prefix}\n//{'-'*60}\n")
                    print(json.dumps(self.__WorkDict, sort_keys=True, indent=4, cls=self.__PathEncoder))
                    if self.__Parent is None:
                        sys.exit(0)
                    return True

            for DefArgName in self.__Definition.keys():
                v = self.__Definition[DefArgName]
                Req = False
                if self.__WorkPars['required'] in v.keys():
                    Req = v[self.__WorkPars['required']]
                if Req:
                    if not DefArgName in self.keys():
                        ParList = self.__GetOptList(DefArgName)
                        raise self.ParamError(self._Translation['OptionRequired'].format(
                        **{'DefArgName':DefArgName, 'ParList':ParList})) from None
                            # f"{DefArgName} ({ParList}) required but not given") from None
        if IsFirst:
            Erg = False
            for c in self.__Children.values():
                if c.__Process(IsFirst):                    # pylint: disable=W0212
                    Erg = True
        return Erg

    def __AssignImportValues(self, wGlobDict:dict, FileName:str) -> None:
        """Weist die importierten Werte dem Arbeitsbereich - nach überprüfung - zu

        Args:
            wGlobDict (dict): Imported dictionary
            FileName (str): Name of the imported file

        Raises:
            self.ParamError: if values do not meet the limits
        """
        try:
            wDict = wGlobDict[self.__Prefix]    # versuche die gewünschten Werte zu erhalten
        except KeyError:
            wDict = {}  # es sind keine Angaben für diesen Prefix in der Datei -> Nichts zu setzen

        for k in self.__WorkDict.keys():        # versuche Daten für all unsere Keys zu bekommen # pylint: disable=consider-iterating-dictionary
            IsOk = True
            try:
                iVal = wDict[k]
            except KeyError:
                IsOk = False                    # keine Daten für diesen Key
            if IsOk:
                NameStr = f'{k} (Imported from {FileName} [{self.__Prefix}])'   # Bezeichnung für ev. Fehlermeldungen
                if isinstance(iVal,(list, tuple)):      # dind die Daten ein Array?
                     for iVs in iVal:                   # Löse das Array auf
                        Res = self.__CheckOption(k, NameStr, self.__Definition[k], iVs)
                        if not Res is None:
                            raise self.ParamError(Res) from None
                else:
                    Res = self.__CheckOption(k, NameStr, self.__Definition[k], iVal)
                if Res is not None:                     # der übergebene Wert war ungültig
                        raise self.ParamError(Res) from None
        for c in self.__Children.values():
            c.__AssignImportValues(wGlobDict,FileName=FileName) # löse auch für alle Child-Klassen auf # pylint: disable=protected-access

    def __GetOptList(self,Name: str) -> str:
        """Liste der möglichen Commandline-Parameter eines Keys
        Es werden sowohl alle Kurz- als auch alle Langforman zurückgegeben """
        w = self.__Definition[Name]
        Erg = ""
        if self.__WorkPars['shortpar'] in w.keys():
            Short = w[self.__WorkPars['shortpar']]
            if isinstance(Short, str):
                for s in Short:
                    Erg += ('-' + s + ' ')
            else:
                for n in Short:
                    for s in n:
                        Erg += ('-' + s + ' ')
        if self.__WorkPars['longpar'] in w.keys():
            Long = w[self.__WorkPars['longpar']]
            Erg += ('--' + Long + ' ')
        return Erg

    def __CheckOption(self, ParName: str, ParKey: str, wPar: dict, a: str) -> Union[str, None]:
        """Prüft ob der angegebene Inhalt für diesen Parameter gültig ist
        Wenn Ja: Der Wert wird in das Ergebnisdictionary geschrieben und "None" zurückgegeben.
        Wenn Nein: Das Ergebnisdictionary ist unverändert, Rückgabe ist die Fehlermeldung

        Args:
            ParName (string): Name of the parameter (index in class as dictionary)
            ParKey (string): The parameter-value from commandline
            wPar (dict): The definition dictionary for this parameter
            a (string): the option given for this parameter

        Returns:
            None    if no error
            Error-msg   if option is erroneous
        """
        wMod = wPar[self.__WorkPars['mode']]
# Prüfen ob Multiple gesetzt ist
        try:
            wMulti = wPar[self.__WorkPars['multiple']]
        except KeyError:
            wMulti = False
#-------------------------
# Text
#-------------------------
        if wMod == self.__WorkModes['text']:
            if wMulti:
                if ParName not in self:
                   self.__WorkDict[ParName] = []
            a = str(a)
            try:
                ll = wPar[self.__WorkPars['lowlimit']]
                if a < ll:
                    return self._Translation['LessLow'].format(
                        **{'OptValue':a, 'ParKey':ParKey, 'LowLimit':ll})
            except KeyError:
                pass
            try:
                ul = wPar[self.__WorkPars['uplimit']]
                if a > ul:
                    return self._Translation['HigherUp'].format(
                        **{'OptValue':a, 'ParKey':ParKey, 'Upp':ul})
            except KeyError:
                pass
            if wMulti:
                self.__WorkDict[ParName].append(a)
            else:
                self.__WorkDict[ParName] = a
            return None
#-------------------------
# Integer
#-------------------------
        if wMod == self.__WorkModes['int']:
            if wMulti:
                if ParName not in self:
                   self.__WorkDict[ParName] = []
            try:
                n = int(a)
            except ValueError:
                return self._Translation['NoInt'].format(
                    **{'OptValue':a, 'ParKey':ParKey})
                # return f"Value {a} for parameter {ParKey} is not a valid integer"
            try:
                ll = wPar[self.__WorkPars['lowlimit']]
                if n < ll:
                    return self._Translation['LessLow'].format(
                        **{'OptValue':a, 'ParKey':ParKey, 'LowLimit':ll})
                    # return f"Value {a} for parameter {ParKey} is less than lower limit ({ll})"
            except KeyError:
                pass
            try:
                ul = wPar[self.__WorkPars['uplimit']]
                if n > ul:
                    return self._Translation['HigherUp'].format(
                        **{'OptValue':a, 'ParKey':ParKey, 'Upp':ul})
                    # return f"Value {a} for parameter {ParKey} is bigger than upper limit ({ul})"
            except KeyError:
                pass
            if wMulti:
                self.__WorkDict[ParName].append(n)
            else:
                self.__WorkDict[ParName] = n
            return None
#-------------------------
# Count
#-------------------------
        if wMod == self.__WorkModes['count']:
            if a == '':
                return None
            try:
                n = int(a)
            except ValueError:
                return self._Translation['NoInt'].format(
                    **{'OptValue':a, 'ParKey':ParKey})
                # return f"Value {a} for parameter {ParKey} is not a valid integer"
            if ParName in self.__WorkDict:
                self.__WorkDict[ParName] += n
            else:
                self.__WorkDict[ParName] = n
            return None
#-------------------------
# Float
#-------------------------
        if wMod == self.__WorkModes['float']:
            if wMulti:
                if ParName not in self:
                   self.__WorkDict[ParName] = []
            try:
                n = float(a)
            except ValueError:
                return self._Translation['NoFloat'].format(
                    **{'OptValue':a, 'ParKey':ParKey})
                # return f"Value {a} for parameter {ParKey} is not a valid floating point"
            try:
                ll = wPar[self.__WorkPars['lowlimit']]
                if n < ll:
                    return self._Translation['LessLow'].format(
                        **{'OptValue':a, 'ParKey':ParKey, 'LowLimit':ll})
                    # return f"Value {a} for parameter {ParKey} is less than lower limit ({ll})"
            except KeyError:
                pass
            try:
                ul = wPar[self.__WorkPars['uplimit']]
                if n > ul:
                    return self._Translation['HigherUp'].format(
                        **{'OptValue':a, 'ParKey':ParKey, 'Upp':ul})
                    # return f"Value {a} for parameter {ParKey} is bigger than upper limit ({ul})"
            except KeyError:
                pass
            if wMulti:
                self.__WorkDict[ParName].append(n)
            else:
                self.__WorkDict[ParName] = n
            return None
#-------------------------
# Boolean
#-------------------------
        if wMod == self.__WorkModes['bool']:
            try:
                a = str(a)
            except ValueError:
                a = 'F'
            try:
                n = a.lower()[0]
            except IndexError:
                return self._Translation['NoBool'].format(
                    **{'OptValue':a, 'ParKey':ParKey})
                # return f"Value {a} for parameter {ParKey} is not valid"
            if n in 'jyt1':
                self.__WorkDict[ParName] = True
                return None
            if n in 'nf0':
                self.__WorkDict[ParName] = False
                return None
            return self._Translation['NoBool'].format(
                **{'OptValue':a, 'ParKey':ParKey})
            # return f"Value {a} for parameter {ParKey} is not valid"
#-------------------------
# File (existing)
#-------------------------
        if wMod == self.__WorkModes['file']:
            if wMulti:
                if ParName not in self:
                   self.__WorkDict[ParName] = []
            a = str(a).strip()
            if len(a) == 0:
                return self._Translation['PathNoFile'].format(
                    **{'OptionPath':a, 'OptionName':ParKey, 'FullPath': a})
                # return f"The name {a} for parameter {ParKey} is not a valid path"
            if a[0] != "/":
                a = self.__MyPwd + "/" + a
            n = a
            try:
                n = Path(a).expanduser().resolve()
            except (ValueError, OSError):
                return self._Translation['PathNoFile'].format(
                    **{'OptionPath':a, 'OptionName':ParKey, 'FullPath': n})
                    # return f"The name {a} for parameter {ParKey} is not a valid path"
            if n.exists():
                if n.is_file():
                    if wMulti:
                        self.__WorkDict[ParName].append(str(n))
                    else:
                        self.__WorkDict[ParName] = str(n)
                    return None
                else:
                    return self._Translation['PathNoFile'].format(
                        **{'OptionPath':a, 'OptionName':ParKey, 'FullPath': n})
                    # return f"The path {a} ({n}) for parameter {ParKey} is not a file"
            return self._Translation['PathNoFile'].format(
                **{'OptionPath':a, 'OptionName':ParKey, 'FullPath': n})
            # return f"The path {a} ({n}) for parameter {ParKey} does not exist"
#-------------------------
# Directory (existing)
#-------------------------
        if wMod == self.__WorkModes['dir']:
            if wMulti:
                if ParName not in self:
                   self.__WorkDict[ParName] = []
            a = str(a).strip()
            if len(a) == 0:
                return self._Translation['PathNoDir'].format(
                    **{'OptionPath':a, 'OptionName':ParKey, 'FullPath': a})
                # return f"The name {a} for parameter {ParKey} is not a valid path"
            if a[0] != "/":
                a = self.__MyPwd + "/" + a
                n = a
                try:
                    n = Path(a).expanduser().resolve()
                except (ValueError, OSError):
                    return self._Translation['PathNoDir'].format(
                        **{'OptionPath':a, 'OptionName':ParKey, 'FullPath': n})
                    # return f"The name {a} for parameter {ParKey} is not a valid path"
            else:
                n = Path(a).expanduser().resolve()
            if n.exists():
                if n.is_dir():
                    if wMulti:
                        self.__WorkDict[ParName].append(str(n))
                    else:
                        self.__WorkDict[ParName] = str(n)
                    return None
                else:
                    return self._Translation['PathNoDir'].format(
                        **{'OptionPath':a, 'OptionName':ParKey, 'FullPath': n})
                    # return f"The path {a} ({n}) for parameter {ParKey} is not a directory"
            return self._Translation['PathNoDir'].format(
                **{'OptionPath':a, 'OptionName':ParKey, 'FullPath': n})
            # return f"The path {a} ({n}) for parameter {ParKey} does not exist"
#-------------------------
# Path
#-------------------------
        if wMod == self.__WorkModes['path']:
            if wMulti:
                if ParName not in self:
                   self.__WorkDict[ParName] = []
            a = str(a).strip()
            if a != '':
                if a[0] != "/":
                    a = self.__MyPwd + "/" + a
                n = a
                try:
                    n = Path(a).expanduser().resolve()
                except (ValueError, OSError):
                    return self._Translation['PathNoPath'].format(
                        **{'OptionPath':a, 'OptionName':ParKey, 'FullPath': n})
                    # return f"The name {a} for parameter {ParKey} is not a valid path"
            else:
                n = ''
            if wMulti:
                self.__WorkDict[ParName].append(str(n))
            else:
                self.__WorkDict[ParName] = str(n)
        return None

    def __Intersection(self, List1:list, List2:list) -> list:
        if len(List2) > len(List1):
            List1, List2 = List2, List1
        return [value for value in List1 if value in List2]

    def GetRemainder(self) -> list:
        """
        Return list of additionel arguments on command-line

        Returns:
            list: List of additional arguments within runtime-arguments
        """
        Rem = self.__RemainArgs
        for c in self.__Children.values():
            cRem = c.GetRemainder()
            Rem = self.__Intersection(Rem, cRem)
        return Rem

    @property
    def UnusedArgs(self) -> list:
        """ Return list of not defined args from the commandline
        This list is for the current Param-object and all of the children
        of this Param-object.
        So under normal conditions it makes only sense on the root of
        all Param-objects.

        Example:
            root defines '-z'
            child defines '-a'
            commandline is "-a -z --test"

            UnusedArgs of child is ['-z','--test']
            UnusedArgs of root = ['--test']     which is the correct list of undefined args.

        Returns:
            list: list of undefined args (str)
        """
        Un = self.__UnusedArgs
        for c in self.__Children.values():
            cUn = c.UnusedArgs
            Un = self.__Intersection(Un, cUn)
        return Un

    @property
    def LongOptsList(self) -> list:
        """
        Return copied list of long options

        Returns:
            list: List of long options
        """
        return copy.deepcopy(self.__LongList)

    @property
    def ShortOptsList(self) -> list:
        """
        Return copied list of short options
        """
        return copy.deepcopy(self.__ShortList)

    @property
    def ParDict(self) -> dict:
        """
        Return copied dict with references options -> parameter-names

        Returns:
            dict: {option: name, ...}
        """
        return copy.deepcopy(self.__ParDict)

    @property
    def GetExportDict(self):
        """
        Return the dictionary for exporting all parameters

        Returns:
            dict: The complete parameter dictionary
        """
        Erg = {}
        wDict = {}
        for k, val in self.__WorkDict.items():
            wDict[k] = val
        Erg[self.__Prefix] = wDict

        for c in self.__Children.values():
            e = c.GetExportDict
            for n,d in e.items():
                Erg[n] = d
        return Erg

    @property
    def Prefix(self) -> str:
        """Return the prefix of this class

        Returns:
            str: the prefix value
        """
        return self.__Prefix

    def ParamStr(self,
                 indent: int = 4,
                 header: bool = True,
                 allvalues: bool = True,
                 dotted: bool = False,
                 cmdpar: bool = True,
                 parentopts: bool = False,
                 recursive: bool = True) -> str:
        """
        Returns a string with formatted output of the
        processed parameters.

        :param indent: Number of leading spaces for children. Defaults to 4.
                    this value is multiplied with the generation. So grandchildren have
                    two times this number of leading spaces and children only one time
                    this number of spaces.
        :type indent: int, optional
        :param header: If True a header with the name of the object are added, defaults to True
        :type header: bool, optional
        :param allvalues: Outputs all avallable options for this child,
                    included the inherited options. Defaults to True
        :type allvalues: bool, optional
        :param dotted: If True the names of the parameters are prefixed with the names
                    of their parents, defaults to False
        :type dotted: bool, optional
        :param cmdpar: If True the commandline-options ere included in the output, defaults to True
        :type cmdpar: bool, optional
        :param parentopts: If True and cmdpar is also True the commandline-options of the parents
                    are anso included in the output, defaults to False
        :type parentopts: bool, optional
        :param recursive: If True all descendants are include in the output,
                    else only the own parameters are included, defaults to True
        :type recursive: bool, optional
        :return: The formated string of the processed parameters
        :rtype: str


        Examples:

        .. code-block:: text

            Assuming:
                the topmost level includes
                    "NoDaemon", "Quiet", "StdErr", and "Verbose"
                child "alpha" includes
                    "Count", "Text" and "Verbose"
                grandchild "alpha -> gamma" includes
                    "Xy"
                child "beta" includes
                    "Verbose"

            The largest format is like:


            ------------------------------------------------------------
            global
            ------------------------------------------------------------
            global                     -> NoDaemon (-d, --[global.]nodaemon)              : False
            global                     -> Quiet    (-q, --[global.]quiet)                 : False
            global                     -> StdErr   (-s, --[global.]console)               : False
            global                     -> Verbose  (-v, --[global.]verbose)               : 2
                ------------------------------------------------------------
                global.alpha
                ------------------------------------------------------------
                global.alpha           -> Count    (-c, --[alpha.]count, --[alpha.]Count) : 7
                global.alpha           -> NoDaemon (-d, --[global.]nodaemon)              : False
                global.alpha           -> Quiet    (-q, --[global.]quiet)                 : False
                global.alpha           -> StdErr   (-s, --[global.]console)               : False
                global.alpha           -> Text     (-t, --[alpha.]text, --[alpha.]Text)   : ''
                global.alpha           -> Verbose  (-v, --[alpha.]verbose)                : 2
                    ------------------------------------------------------------
                    global.alpha.gamma
                    ------------------------------------------------------------
                    global.alpha.gamma -> Count    (-c, --[alpha.]count, --[alpha.]Count) : 7
                    global.alpha.gamma -> NoDaemon (-d, --[global.]nodaemon)              : False
                    global.alpha.gamma -> Quiet    (-q, --[global.]quiet)                 : False
                    global.alpha.gamma -> StdErr   (-s, --[global.]console)               : False
                    global.alpha.gamma -> Text     (-t, --[alpha.]text, --[alpha.]Text)   : ''
                    global.alpha.gamma -> Verbose  (-v, --[alpha.]verbose)                : 2
                    global.alpha.gamma -> Xy       (-b, --[gamma.]bbbb)                   : False
                ------------------------------------------------------------
                global.beta
                ------------------------------------------------------------
                global.beta            -> NoDaemon (-d, --[global.]nodaemon)              : False
                global.beta            -> Quiet    (-q, --[global.]quiet)                 : False
                global.beta            -> StdErr   (-s, --[global.]console)               : False
                global.beta            -> Verbose  (-v, --[beta.]verbose)                 : 5

            The shortest format is like (recursive = True):

            global -> NoDaemon  : False
            global -> Quiet     : False
            global -> StdErr    : False
            global -> Verbose   : 2
            alpha  -> Count     : 7
            alpha  -> Text      : ''
            alpha  -> Verbose   : 2
            gamma  -> Xy        : False
            beta   -> Verbose   : 5

            The shortest format is like (recursive = False):

            global -> NoDaemon  : False
            global -> Quiet     : False
            global -> StdErr    : False
            global -> Verbose   : 2


        """
        return self.__ParamStr(depth = 0,
                               indent = indent,
                               header = header,
                               allvalues = allvalues,
                               dotted = dotted,
                               dottedbase = '',
                               cmdpar = cmdpar,
                               parentopts = parentopts,
                               recursive = recursive)

    def __ParamStr(self,
                 depth: int = 0,
                 indent: int = 4,
                 header: bool = True,
                 allvalues: bool = True,
                 dotted: bool = False,
                 dottedbase:str = '',
                 cmdpar: bool = True,
                 parentopts: bool = False,
                 recursive: bool = True) -> str:
        """
        This is the internal procedure. Look at "ParamStr" for all the args
        depth and dottedbase are only used internaly so the user can't set them to the exported function

        :param indent: Number of leading spaces for children. Defaults to 4.
                    this value is multiplied with the generation. So grandchildren have
                    two times this number of leading spaces and children only one time
                    this number of spaces.
        :type indent: int, optional
        :param header: If True a header with the name of the object are added, defaults to True
        :type header: bool, optional
        :param allvalues: Outputs all avallable options for this child,
                    included the inherited options. Defaults to True
        :type allvalues: bool, optional
        :param dotted: If True the names of the parameters are prefixed with the names
                    of their parents, defaults to False
        :type dotted: bool, optional
        :param cmdpar: If True the commandline-options ere included in the output, defaults to True
        :type cmdpar: bool, optional
        :param parentopts: If True and cmdpar is also True the commandline-options of the parents
                    are anso included in the output, defaults to False
        :type parentopts: bool, optional
        :param recursive: If True all descendants are include in the output,
                    else only the own parameters are included, defaults to True
        :type recursive: bool, optional
        :return: The formated string of the processed parameters
        :rtype: str
        """
        Erg = ''
        Ls = ' ' * (depth * indent)
        p = self.Prefix
        if dotted:
            if dottedbase != '':
                p = dottedbase + '.' + p
        if header:
            Erg += f"{Ls}{'-' * 60}\n{Ls}{p}\n{Ls}{'-' * 60}\n"
        TheItems = self.items()
        for key,value in TheItems:
            if allvalues or self.IsOwnKey(key):
                if cmdpar:
                    OptStr = self.GetCmdPar(Entry = key, dotted = dotted, parents = parentopts)
                else:
                    OptStr = ''
                if OptStr != '':
                    OptStr = '(' + OptStr + ')'
                if isinstance(value, str):
                    Erg += f"{Ls}{p}\t-> {key}\t{OptStr}\t: '{value}'\n"
                else:
                    Erg += f"{Ls}{p}\t-> {key}\t{OptStr}\t: {value}\n"
        if recursive:
            for n in self.Child.values():
                Erg += n.__ParamStr(depth = depth + 1,                  # pylint: disable=protected-access
                                  indent = indent,
                                  header = header,
                                  allvalues = allvalues,
                                  dotted = dotted,
                                  dottedbase = p,
                                  cmdpar = cmdpar,
                                  parentopts = parentopts,
                                  recursive = recursive)
        if depth == 0:           # Auf der höchsten Ebene
            l = [0,0,0]
            lList = []
            Lines = Erg.splitlines()
            for Line in Lines:
                if '\t' not in Line:
                    lList.append(Line)
                else:
                    w = Line.split('\t')
                    lList.append(w)             # gesplittete zeile anhängen
                    for i in range(3):
                        try:
                            ll = len(w[i])
                            if l[i] < ll:
                                l[i] = ll
                        except KeyError:
                            pass
            Erg = ''
            Pad = ' ' * (max(l) + 1)
            for Line in lList:
                if isinstance(Line, str):
                    Erg += Line + '\n'
                else:
                    wErg = ''
                    for i in range(3):
                        wErg += (Line[i] + Pad)[:l[i] + 1]
                    Erg += wErg + Line[3] + '\n'
        return Erg

    def __UsedShortCommandLineParameter(self, Par, WorkList:list) -> None:
        List = Par.ShortOptsList
        for l in List:
            if l[-1] == ':':
                l = l[:-1]
            m = '-' + l
            if m not in WorkList:
                WorkList.append(m)
        for c in Par.Child.values():
            self.__UsedShortCommandLineParameter(c,WorkList)

    @property
    def OverviewCommandLineParameter(self) -> str:
        """
        Helper for programmers. can be used before "Process".
        Should not be used in production environment. Give
        information about used long and short options and all
        unused (=availlable) short options.

        :return: A formatted string giving all information about command-line parameters, broken to 68 characters a line.
        :rtype: str
        """
        return f"""Used short options:
{self.UsedShortCommandLineParameter}
Free short options:
{self.FreeShortCommandLineParameter}
Used long options:
{self.UsedLongCommandLineParameter}"""

    @property
    def UsedShortCommandLineParameter(self) -> str:
        """
        Helper for programmers. Can be used before "Process".
        Should not be used in production environment

        :return: A formatted string giving all information about short options used, broken to 68 characters a line.
        :rtype: str
        """
        if not self.__IsPrepared:
            self.__Prepare()
        WorkList = []
        self.__UsedShortCommandLineParameter(self,WorkList)
        WorkList.sort()
        return '    ' + '\n    '.join(textwrap.wrap(', '.join(WorkList), 64, break_long_words=False))

    @property
    def FreeShortCommandLineParameter(self) -> str:
        """
        Helper for programmers. Can be used before "Process".
        Should not be used in production environment

        :return: A formatted, sorted list of all unused (free to use) short options broken to 68 characters a line.
        :rtype: str
        """
        UsedList = []
        self.__UsedShortCommandLineParameter(self, UsedList)
        FreeList = []
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyt0123456789':
            if '-' + c not in UsedList:
                FreeList.append('-' + c)
        return '    ' + '\n    '.join(textwrap.wrap(', '.join(FreeList), 64, break_long_words=False))


    @property
    def UsedLongCommandLineParameter(self) -> str:
        """
        Helper for programmers. Can be used before "Process".
        Should not be used in production environment

        :return: A formatted, sorted list of all used long options broken to 68 characters a line.
        :rtype: str
        """
        if not self.__IsPrepared:
            self.__Prepare()
        WorkList = []
        def __UsedLongCommandLineParameter(Par:Param, WorkList:list) -> None:
            List = Par.LongOptsList
            for l in List:
                if l[-1] == '=':
                    l = l[:-1]
                m = '--' + l
                if m not in WorkList:
                    WorkList.append(m)
            for c in Par.Child.values():
                __UsedLongCommandLineParameter(c,WorkList)

        __UsedLongCommandLineParameter(self,WorkList)
        WorkList.sort()
        return '    ' + '\n    '.join(textwrap.wrap(', '.join(WorkList), 64, break_long_words=False))




    @property
    def TestCommandLineParameter(self) -> str:
        """
        Helper for programmers. Can be used before "Process".
        Helps to find problems with the command-line interface.
        Prevent missunderstandig the interface by the user.
        Should not be used in production environment

        :return: A formatted sting giving all informations about errors
                 or possible problems within the definition(s).
        :rtype: str
        """
        if not self.__IsPrepared:
            self.__Prepare()

        Sd = {}
        Ld = {}
        def __AddLists(Par:Param,Sd:dict,Ld:dict) -> None:
            Sd[Par.FullPrefix] = Par.ShortOptsList
            Ld[Par.FullPrefix] = Par.LongOptsList
            for c in Par.Child.values():
                __AddLists(c,Sd,Ld)

        __AddLists(self,Sd,Ld)

        # pprint.pprint(Sd,indent=4,sort_dicts=True)
        # pprint.pprint(Ld,indent=4,sort_dicts=True)

        Sod = {}
        for p,ll in Sd.items():
            for l in ll:
                if l[-1] == ':':
                    HasArg = True
                    l = l[:-1]
                else:
                    HasArg = False
                if l not in Sod:
                    Sod[l] = []
                Sod[l].append([p,HasArg])
        Lod = {}
        for p,ll in Ld.items():
            for l in ll:
                if l[-1] == '=':
                    HasArg = True
                    l = l[:-1]
                else:
                    HasArg = False
                if l not in Lod:
                    Lod[l] = []
                Lod[l].append([p,HasArg])
        # pprint.pprint(Sod,indent=4,sort_dicts=True)
        # pprint.pprint(Lod,indent=4,sort_dicts=True)
        HasErrors = False
        HasDanger = False
        HasErrorsList = []
        HasDangerList = []
        Res = ''
        for Opt, List in Sod.items():
            if len(List) > 1:
                UsedList = []
                HasArg = List[0][1]
                ErrArg = False
                for l in List:
                    UsedList.append(l[0])
                    if l[1] != HasArg:
                        ErrArg = True
                if ErrArg:
                    HasErrors = True
                    HasErrorsList.append("'-" + Opt + "'")
                    Res += f"'-{Opt}':\n    Error:   Inconsisten use of required argument in\n        {', '.join(UsedList)}\n"
                else:
                    Res += f"'-{Opt}':\n    Warning: Possibly unintended double use in\n        {', '.join(UsedList)}\n"
        if Res != '':
            Res += '\n'
        for Opt, List in Lod.items():
            if len(List) > 1:
                UsedList = []
                HasArg = List[0][1]
                ErrArg = False
                for l in List:
                    UsedList.append(l[0])
                    if l[1] != HasArg:
                        ErrArg = True
                if ErrArg:
                    HasDanger = True
                    HasDangerList.append("'--" + Opt + "'")
                    Res += f"'--{Opt}':\n    Danger:  Inconsisten use of required argument (must allways be prefixed by user) in\n        {', '.join(UsedList)}\n"
                else:
                    Res += f"'--{Opt}':\n    Warning: Possibly unintended double use in\n        {', '.join(UsedList)}\n"
        if HasDanger or HasErrors:
            Res += '\n' + '-' * 60 + '\n'
            if HasErrors:
                Res += f"There are errors in options {', '.join(HasErrorsList)}\n"
            if HasDanger:
                Res += f"There are dangerous settings in options {', '.join(HasDangerList)}\n"
            Res += '-' * 60 + '\n'

        return Res



    class GetoptError(Exception):
        """Own error-class for option-errors"""
        opt = ''
        msg = ''
        def __init__(self, msg, opt=''):
            self.msg = msg
            self.opt = opt
            Exception.__init__(self, msg, opt)

        def __str__(self):
            return self.msg

    def _getopt(self, args, shortopts, longopts = [], AcceptAll = False):                 # pylint: disable=dangerous-default-value
        """getopt(args, options[, long_options]) -> opts, args

        Parses command line options and parameter list.  args is the
        argument list to be parsed, without the leading reference to the
        running program.  Typically, this means "sys.argv[1:]".  shortopts
        is the string of option letters that the script wants to
        recognize, with options that require an argument followed by a
        colon (i.e., the same format that Unix getopt() uses).  If
        specified, longopts is a list of strings with the names of the
        long options which should be supported.  The leading '--'
        characters should not be included in the option name.  Options
        which require an argument should be followed by an equal sign
        ('=').

        The return value consists of two elements: the first is a list of
        (option, value) pairs; the second is the list of program arguments
        left after the option list was stripped (this is a trailing slice
        of the first argument).  Each option-and-value pair returned has
        the option as its first element, prefixed with a hyphen (e.g.,
        '-x'), and the option argument as its second element, or an empty
        string if the option has no argument.  The options occur in the
        list in the same order in which they were found, thus allowing
        multiple occurrences.  Long and short options may be mixed.

        """
        unused = []
        opts = []
        if isinstance(longopts, str):
            longopts = [longopts]
        else:
            longopts = list(longopts)
        while args and args[0].startswith('-') and args[0] != '-':
            if args[0] == '--':
                args = args[1:]
                break
            if args[0].startswith('--'):
                opts, args, unused = self._do_longs(opts, args[0][2:], longopts, args[1:],unused,AcceptAll)
            else:
                opts, args, unused = self._do_shorts(opts, args[0][1:], shortopts, args[1:],unused,AcceptAll)

        return opts, args, unused

    def _gnu_getopt(self, args, shortopts, longopts = [], AcceptAll = False):                 # pylint: disable=dangerous-default-value
        """getopt(args, options[, long_options]) -> opts, args

        This function works like getopt(), except that GNU style scanning
        mode is used by default. This means that option and non-option
        arguments may be intermixed. The getopt() function stops
        processing options as soon as a non-option argument is
        encountered.

        If the first character of the option string is `+', or if the
        environment variable POSIXLY_CORRECT is set, then option
        processing stops as soon as a non-option argument is encountered.

        """
        unused = []
        opts = []
        prog_args = []
        if isinstance(longopts, str):
            longopts = [longopts]
        else:
            longopts = list(longopts)

        # Allow options after non-option arguments?
        if shortopts.startswith('+'):
            shortopts = shortopts[1:]
            all_options_first = True
        elif os.environ.get("POSIXLY_CORRECT"):
            all_options_first = True
        else:
            all_options_first = False

        while args:
            if args[0] == '--':
                prog_args += args[1:]
                break

            if args[0][:2] == '--':
                opts, args, unused = self._do_longs(opts, args[0][2:], longopts, args[1:], unused, AcceptAll)
            elif args[0][:1] == '-' and args[0] != '-':
                opts, args, unused = self._do_shorts(opts, args[0][1:], shortopts, args[1:], unused, AcceptAll)
            else:
                if all_options_first:
                    prog_args += args
                    break
                else:
                    prog_args.append(args[0])
                    args = args[1:]

        return opts, prog_args, unused

    def _do_longs(self, opts, opt, longopts, args, unused, AcceptAll = False):
        """
        Process long options
        """
        try:
            i = opt.index('=')
        except ValueError:
            optarg = None
        else:
            opt, optarg = opt[:i], opt[i+1:]
        if AcceptAll:
            try:
                has_arg, opt = self._long_has_args(opt, longopts)
            except self.GetoptError:
                unused.append('--' + opt)
                return opts, args, unused
        else:
            has_arg, opt = self._long_has_args(opt, longopts)
        if has_arg:
            if optarg is None:
                if not args:
                    raise self.GetoptError(self._Translation['OptionRequiresArgumentLong'].format(**{'opt':opt}),opt)
                optarg, args = args[0], args[1:]
        elif optarg is not None:
            raise self.GetoptError(self._Translation['OptionNeedNoArgs'].format(**{'opt':opt}), opt)
        opts.append(('--' + opt, optarg or ''))
        return opts, args, unused

    # Return:
    #   has_arg?
    #   full option name
    def _long_has_args(self, opt, longopts):
        """
        determine if long option has args
        """
        possibilities = [o for o in longopts if o.startswith(opt)]
        if not possibilities:
            raise self.GetoptError(self._Translation['OptionNotRecognizedLong'].format(**{'opt':opt}), opt)
        # Is there an exact match?
        if opt in possibilities:
            return False, opt
        elif opt + '=' in possibilities:
            return True, opt
        # No exact match, so better be unique.
        if len(possibilities) > 1:
            # since possibilities contains all valid continuations, might be
            # nice to work them into the error msg
            raise self.GetoptError(self._Translation['ParNoUniquePrefix'].format(**{'opt':opt}), opt)
        assert len(possibilities) == 1
        unique_match = possibilities[0]
        has_arg = unique_match.endswith('=')
        if has_arg:
            unique_match = unique_match[:-1]
        return has_arg, unique_match

    def _do_shorts(self, opts, optstring, shortopts, args, unused, AcceptAll = False):
        """
        Process short options
        """
        while optstring != '':
            opt, optstring = optstring[0], optstring[1:]
            if AcceptAll:
                try:
                    wHasArgs = self._short_has_arg(opt, shortopts)
                except self.GetoptError:
                    unused.append('-' + opt)
                    wHasArgs = False
            else:
                wHasArgs = self._short_has_arg(opt, shortopts)
            if wHasArgs:
                if optstring == '':
                    if not args:
                        raise self.GetoptError(self._Translation['OptionRequiresArgumentShort'].format(**{'opt':opt}), opt)
                    optstring, args = args[0], args[1:]
                optarg, optstring = optstring, ''
            else:
                optarg = ''
            opts.append(('-' + opt, optarg))
        return opts, args, unused

    def _short_has_arg(self, opt, shortopts):
        """
        Determine if short option has args
        """
        for i in range(len(shortopts)):                         # pylint: disable=consider-using-enumerate
            if opt == shortopts[i] != ':':
                return shortopts.startswith(':', i+1)
        raise self.GetoptError(self._Translation['OptionNotRecognizedShort'].format(**{'opt':opt}), opt)



# if __name__ == '__main__':

#     GlobalDef = {
#         'Help': {
#                 's': 'h',
#                 'l': 'help',
#                 'm': 'H',
#                 'd': 'Diesen Hilfetext anzeigen und beenden'
#                 },
#         'Export': {
#                 's': 'x',
#                 'l': 'export',
#                 'm': 'X',
#                 'd': 'Ausgabe der aktuellen Konfiguration und Beenden'
#                 },
#         'GlobalExport': {
#                 'l': 'globexport',
#                 'm': '>',
#                 'd': 'Ausgabe aller Konfigurationen und Beenden'
#                 },
#         'ConfFile': {
#                 's': 'c',
#                 'l': 'config',
#                 'm': 'x',
#                 'o': True,
#                 'd': '''Zuerst die Werte aus der Datei lesen,
# danach erst die Komandozeilenparameter'''
#                 },
#         'GlobImport': {
#                 's': 'g',
#                 'l': 'globconfig',
#                 'm': '<',
#                 'o': True,
#                 'd': '''Globale Config. Zuerst die Werte aus der Datei lesen,
# danach erst die Komandozeilenparameter'''
#                 },
#             'Verbose': {
#                 's': 'v',
#                 'l': 'verbose',
#                 'r': False,
#                 'm': 'C',
#                 'd': """Ausgabe von Statusmeldungen
# für mehr Details die kurze Option mehrmals angeben oder
# die lange Option mit einer höheren Zahl verwenden.""",
#                 },
#             'Quiet': {
#                 's': 'q',
#                 'l': 'quiet',
#                 'm': 'b',
#                 'd': 'Nur Fehler ausgeben'
#                 },
#             'StdErr': {
#                 's': 's',
#                 'l': 'console',
#                 'm': 'b',
#                 'v': False,
#                 'd': """Ausgabe der Statusmeldungen auf die
# Konsole und nicht auf syslog""",
#                 },
#             'NoDaemon': {
#                 's': 'd',
#                 'l': 'nodaemon',
#                 'm': 'b',
#                 'v': False,
#                 'd': 'Start im Vordergrund (Nicht als Daemon) für Test',
#                 },
# #             'LogPath': {
# #                 'l': 'logpath',
# #                 'r': False,
# #                 'M': True,
# #                 'o': True,
# #                 'm': 'p',
# #                 'v': '',
# #                 'd': 'Pfad zu einer Log-Datei. Diese wird täglich rotiert und neu erstellt'
# #                 },
# #             'LogProcInfo': {
# #                 'l': 'logprocinfo',
# #                 'm': 'b',
# #                 'v': False,
# #                 'd': 'Ausgabe der Procedur und der Zeile',
# #                 },
# #             'LogMultiProc': {
# #                 'l': 'logmultiproc',
# #                 'm': 'b',
# #                 'v': False,
# #                 'd': '''Nur wenn "logprocinfo" gesetzt ist.
# # zusätzlich Ausgabe des Prozessnamens.
# # Macht nur bei Programmen mit mehreren Prozessen sinn''',
# #                 },
# #             'LogMultiThread': {
# #                 'l': 'logmultithread',
# #                 'm': 'b',
# #                 'v': False,
# #                 'd': '''Nur wenn "logprocinfo" gesetzt ist.
# # zusätzlich Ausgabe des Threadnamens.
# # Macht nur bei Programmen mit mehreren Threads sinn''',
# #                 },
# #             'LogLevelType': {
# #                 'l': 'logleveltype',
# #                 'm': 'i',
# #                 'v': 2,
# #                 'd': '''Ausgabe des Loglevels.
# # 0 = Keine Ausgabe
# # 1 = Level-Nummer
# # 2 = Level-Name
# # 3 = Beide''',
# #                 },
# #             'LogStackOnDebug': {
# #                 'l': 'logstack',
# #                 'm': 't',
# #                 'v': 'NONE',
# #                 'd': '''Ausgabe des Anwendungsstacks ab diesem Level.
# # Bei verwendung von "LogP" sind die Levels:
# #     ERROR
# #     STATUS
# #     WARNING
# #     MSG
# #     INFO
# #     DEBUG
# #     TRACE
# #     NONE
# # Alle anderen Werte werden als "NONE" interpretiert
# # Groß- oder Kleinschreibung wird ignoriert''',
# #                 },
# #             'LogStackDepth': {
# #                 'l': 'logstackdepth',
# #                 'm': 'i',
# #                 'v': 0,
# #                 'd': '''Anzahl der auszugebenden Stackzeilen, 0 = Disabled'''
# #                 },

#         }



#     TestDef_Alpha =     {
#         # 'Help': {   's': 'h',
#         #         'l': 'help',
#         #         'm': 'H',
#         #         'd': 'Diesen Hilfetext anzeigen und beenden'},
#     #     'Export': { 's': 'x',
#     #             'l': 'export',
#     #             'm': 'X',
#     #             'd': 'Ausgabe der aktuellen Konfiguration und Beenden'},
#     #     'ConfFile': {   's': 'z',
#     #             'l': 'par',
#     #             'm': 'x',
#     #             'd': '''Zuerst die Werte aus der Datei lesen,
#     # danach erst die Komandozeilenparameter'''},
#         # 'Verbose': {    's': 'v',
#         #         'l': 'verbose',
#         #         'r': False,
#         #         'm': 'C',
#         #         'd': 'Sei gesprächig'},
#         'Count': {
#             's': 'c',
#             'l': ('count','Count'),
#             'r': True,
#             'o': True,
#             'v': 7,
#             'm': 'i',
#             'L': 1,
#             'U': 10,
#             'd': 'Eine Zahl zwischen 1 und 10'
#             },
#         'Text': {   's': 't',
#             'l': ('text','Text'),
#             'o': True,
#             'v': '',
#             'm': 't',
#             'd': 'Ein Text'
#             },
#         # 'MultiText': {  's': 'T',
#         #         'l': ('mtext','mText'),
#         #         'o': True,
#         #         'M': True,
#         #         'm': 't',
#         #         'd': 'Multi Text'},
#         # 'Float': {  's': 'F',
#         #         'l': ('float','Float'),
#         #         'o': True,
#         #         'v': 10.47,
#         #         'm': 'F',
#         #         'L': 1,
#         #         'U': 100.2,
#         #         'd': 'Eine Gleitkommazahl zwischen 1 und 100.2'},
#         # 'File': {   's': 'f',
#         #         'l': 'file',
#         #         'o': True,
#         #         'm': 'f',
#         #         'd': 'Eine existierende Datei'},
#         # 'Dir': {    's': 'D',
#         #         'l': 'dir',
#         #         'o': True,
#         #         'm': 'd',
#         #         'd': 'Ein existierendes Verzeichnis'},
#         'Path': {
#                 's': 'p',
#                 'l': 'path',
#                 'r': 'true',
#                 'M': True,
#                 'o': True,
#                 'm': 'p',
#                 'd': 'Ein gültiger Path'},
#         # 'Counter': {
#         #         's': 'C',
#         #         'o': False,
#         #         'm': 'C',
#         #         'd': 'Mehrmals zum hochzählen'},
#         }
#     TestDef_Beta = {
#         'Float': {
#             's': 'F',
#             'l': ('float','Float'),
#             'o': True,
#             'v': 10.47,
#             'm': 'F',
#             'L': 1,
#             'U': 100.2,
#             'd': 'Eine Gleitkommazahl zwischen 1 und 100.2'
#             },
#         # 'Help': {
#         #         's': 'h',
#         #         'l': 'help',
#         #         'm': 'H',
#         #         'd': 'Diesen Hilfetext anzeigen und beenden'
#         #         },
#         # 'Verbose': {
#         #         's': 'v',
#         #         'l': 'verbose',
#         #         'r': False,
#         #         'm': 'C',
#         #         'd': 'Sei gesprächig'
#         #         },
#         }
#     TestDef_Gamma =     {
#         'Xy': {
#             's': 'b',
#             'm': 'b',
#             'o': True,
#             'd': 'Ein Switch'
#             },
#         # 'GlobalExport': {
#         #         'l': 'globexport',
#         #         'm': '>',
#         #         'd': 'Ausgabe aller Konfigurationen und Beenden'
#         #         },
# #         'GlobImport': {
# #                 's': 'g',
# #                 'l': 'globconfig',
# #                 'm': '<',
# #                 'o': True,
# #                 'd': '''Globale Config. Zuerst die Werte aus der Datei lesen,
# # danach erst die Komandozeilenparameter'''
# #                 },
#         }

#     import shlex

#     # def Trans(*,Type:str,Param:str, Path:str, FullPath:str, Msg:str, OptList:str) -> str:
#     #     """Translation Routine für Fehlermeldungen"""
#     #     if Type == "ImpFail":
#     #         return f"Fehler bei Import: {Path} bei Parameter {Param} ist keine gültige Datei"
#     #     if Type == "ErrMsg":
#     #         return f"Fehler '{Msg}' betreffend Datei {Path} ({FullPath}) von Parameter {Param}"
#     #     if Type == "NoFile":
#     #         return f"Der Pfad {Path} ({FullPath}) für Parameter {Param} ist keine Datei"
#     #     if Type == "NoPath":
#     #         return f"Der Pfad {Path} ({FullPath}) für Parameter {Param} existiert nicht"
#     #     if Type == "NoAct":
#     #         return f"Kein Inhalt für den Parameter {Param} angegeben"
#     #     if Type == "Required":
#     #         return f"Der Parameter {Param} ({OptList}) muss angegeben werden, ist aber nicht vorhanden"
#     #     return f"Unbekannter Fehler Type='{Type}', Param='{Param}', Path='{Path}', FullPath='{FullPath}', Msg='{Msg}', OptList='{OptList}'"


#     def main():
#         """Main"""
#         m = Param(Def=GlobalDef,
#                 Children = {
#                     'Alpha':
#                         {
#                         'Desc': "Description Alpha",
#                         'Def': TestDef_Alpha,
#                         },
#                     'Beta':
#                         {
#                         'Def': TestDef_Beta,
#                         'Desc': "Description Beta",
#                         }
#                     },
#                 # HelpType=3
#                 )
#         m.Child['alpha'].AddChild(Prefix='Gamma', Def=TestDef_Gamma, Description="Eine eingefügte Ebene")
#         m.SetTranslation(Translation_de_DE)
#         # m._PrintInitTranslation()                  # pylint: disable=protected-access
#         # m._PrintAktualTranslation()                  # pylint: disable=protected-access
#         # m.Child['alpha']._PrintAktualTranslation()                  # pylint: disable=protected-access
#         try:
#             # m.SetArgs(Args = shlex.split(__name__ + ' ' + '-vv -h --globexport --config=xyz.json'))
#             # m.SetArgs(Args = shlex.split(__name__ + ' ' + '--path=./xyz.json --globexport'))
#             # m.SetArgs(Args = shlex.split(__name__ + ' ' + '-g xyz.json'))
#             # m.SetArgs(Args = shlex.split(__name__ + ' ' + '-vv --globexport --config=xyz.json'))

#             m.SetArgs(Args = shlex.split(__name__ + ' ' + '--zzz -zz'))

#             Erg = m.Process()
#         except Exception as exc:                                    # pylint: disable=broad-except
#             print(exc)
#             Erg = True
#             # return
#         if Erg:         # Es war eine terminale Funktion in der Commandline (Help, Export, GlobalExport) -> Programmende
#             return

#         g =m.Child['alpha'].Child['gamma']
#         print(g.Parents)
#         print(g.FullPrefix)

#         m['TopLevel'] = 'Top'
#         m.Child['alpha']['AlphaLevel'] = 'Alpha'
#         m.Child['alpha'].Child['gamma']['GammaLevel'] = 'Gamma'

#         print(f"{'*' * 60}All Options ON\n")
#         print(m.ParamStr(dotted=True,parentopts=True))

#         print(f"{'*' * 60}Shortes\n")
#         print(m.ParamStr(dotted=False,parentopts=False,indent=0,header=False,cmdpar=False,allvalues=False))

#         print(f"{'*' * 60}Dotted\n")
#         print(m.ParamStr(indent=0,dotted=True,cmdpar=True))

#         print(f"{'*' * 60}Default\n")
#         print(m.ParamStr())

#         print(f"{'*' * 60}No header\n")
#         print(m.ParamStr(indent=2, header=False))

#         print(f"{'*' * 60}Not all\n")
#         print(m.ParamStr(indent=8,allvalues=False,parentopts=True))

#         print(f"{'*' * 60}Alpha Rec\n")
#         print(m.Child['alpha'].ParamStr(dotted = True, parentopts = True))

#         print(f"{'*' * 60}No Rec\n")
#         print(m.ParamStr(recursive=False))

#         print(f"{'*' * 60}\n")
#         print(f"{'-' * 60}\nGlobal\n{'-' * 60}")
#         for key,value in m.items():
#             print(f"Global -> {key}: {value}")

#         for Name, Par in m.Child.items():
#             print(f"{'-' * 60}\n{Name}\n{'-' * 60}")
#             for key,value in Par.items():
#                 print(f"{Name} -> {key}: {value}")
#         print(f"\n{'-' * 80}\n\n")
#         print(m.Usage())
#         print(f"\n{'#' * 80}\n\n")



#         a = Param(Def = TestDef_Alpha,
#             Desc = "Dies ist ein Test\ndas bedeutet hier steht nur\nnonsens",
#             AddPar = "File .... File",
#             # Translate = Trans,
#             AllParams = True
#             )
#         a.SetArgs(Args = shlex.split('Test -v -CCC -f /Mist --dir=/tmp'))
#         try:
#             a.Process()
#         except Exception as exc:                                    # pylint: disable=broad-except
#             dir(exc)
#             print(exc)
#             return
#         for key,value in a.items():
#             print(key,value)
#         # print(dir(a))
#         print(f"ExportDict = {a.GetExportDict}")
#         print(f"Ergebnis: {a}")
#         print(f"Rest: {a.GetRemainder()}")
#         print(a.GetCmdPar('Text'))
#         print(a.Definition)
#         print(a.Usage())
#         print('-'*60)
#         b = Param(Def = TestDef_Beta,
#             Desc = "Dies ist ein Test # 2",
# #            AddPar = "File .... File",
#             # Translate = Trans,
#             AllParams = True
#             )
# #        b.SetArgs(Args = shlex.split('Test --ignore.help -v -x'))
#         try:
#             b.Process()
#         except Exception as exc:                                    # pylint: disable=broad-except
#             dir(exc)
#             print(exc)
#             return
#         for key,value in b.items():
#             print(key,value)
#         # print(dir(a))
#         print(f"Ergebnis: {b}")
#         print(f"Rest: {b.GetRemainder()}")
#         print(b.GetCmdPar('Text'))
#         print(b.Definition)
#         print(b.Usage())
#         print('-'*60)

#     main()

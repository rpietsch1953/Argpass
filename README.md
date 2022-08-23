Module Param
============
Deals with command-line parameters

Copyright (c) 2022 Ing. Rainer Pietsch <r.pietsch@pcs-at.com>

Detailed docs at <https://argpass.readthedocs.io/en/latest/index.html>

Source at <https://github.com/rpietsch1953/Argpass>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

Classes
-------

`Param(*, Def: dict = {}, Args: Optional[list] = None, Chk=None, Desc: str = '', AddPar: str = '', AllParams: bool = True, UserPars: Optional[dict] = None, UserModes: Optional[dict] = None, ErrorOnUnknown: bool = True, HelpType: int = 0, Children: dict = {}, translation: dict = {}, Version: str = '', License: Union[str, tuple, list, dict, ForwardRef(None)] = None, ShowPrefixOnHelp: bool = True)`
:   Main class and also the result-dictionary.
    A member of this class acts like a dictionary. There are some special cases
    if you use nested childs. (Check out the :doc:`usage` section for further information)
    
        
    
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
                if 'L': all entries separated by a newline ('\n') are displayed.
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
                    License=('\nCopyright (c) <date> <your name>\n' + GPL_Preamble_DE,
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

    ### Class variables

    `DeclarationError`
    :   this exception is raised if there is an declaration error within the
        parameters of the class.
        
        .. note::
            This error messages are NEVER translated since they are not user
            initiated errors.

    `GetoptError`
    :   Own error-class for option-errors

    `ParamError`
    :   This exception is raised if there is an error within the runtime-parameters.
        This is only raised within the :func:`Param.Process`-function.
        
        .. note::
            This errors are translated with the 'translation' dictionary. There
            is the initial state of this dict using 'en_US' texts.
        
            This module also provide a 'Translation_de_DE' entry giving a german
            translation of the error-messages, and a 'Translation_en_US' table only vor completeness.
        
            If you can provide translations to other languages send me this
            declarations to <r.pietsch@pcs-at.com> and I will add them to this
            module.

    ### Instance variables

    `Child: Dict[str, object]`
    :   Child dict
        
        :return: return all the children of this instance
        :rtype: Dict[str, :py:class:`Param`]

    `Definition: dict`
    :   Returns s copy of the definition
        
        :return: a definition dictionary
        :rtype: dict

    `FreeShortCommandLineParameter: str`
    :   Helper for programmers. Can be used before "Process".
        Should not be used in production environment
        
        :return: A formatted, sorted list of all unused (free to use) short options broken to 68 characters a line.
        :rtype: str

    `FullPrefix: str`
    :   Returns the full qualified prefix of this instance
        e.g.: global.alpha.gamma
        if alpha is a child of global and gamma (this instance) is a child of alpha
        
        :return: full qualified prefix of this instance
        :rtype: str

    `GetExportDict`
    :   Return the dictionary for exporting all parameters
        
        Returns:
            dict: The complete parameter dictionary

    `LongOptsList: list`
    :   Return copied list of long options
        
        Returns:
            list: List of long options

    `OverviewCommandLineParameter: str`
    :   Helper for programmers. can be used before "Process".
        Should not be used in production environment. Give
        information about used long and short options and all
        unused (=availlable) short options.
        
        :return: A formatted string giving all information about command-line parameters, broken to 68 characters a line.
        :rtype: str

    `ParDict: dict`
    :   Return copied dict with references options -> parameter-names
        
        Returns:
            dict: {option: name, ...}

    `Parents: str`
    :   Returns the full qualified parents of this instance
        e.g.: global.alpha
        if alpha is a child of global and gamma (this instance) is a child of alpha
        
        :return: full qualified parents of this instance
        :rtype: str

    `PartPrefix: str`
    :   Returns the full qualified prefix without global of this instance
        e.g.: alpha.gamma
        if alpha is a child of global and gamma (this instance) is a child of alpha
        
        :return: full qualified prefix of this instance without root prefix
        :rtype: str

    `Prefix: str`
    :   Return the prefix of this class
        
        Returns:
            str: the prefix value

    `ShortOptsList: list`
    :   Return copied list of short options

    `TestCommandLineParameter: str`
    :   Helper for programmers. Can be used before "Process".
        Helps to find problems with the command-line interface.
        Prevent missunderstandig the interface by the user.
        Should not be used in production environment
        
        :return: A formatted sting giving all informations about errors
                 or possible problems within the definition(s).
        :rtype: str

    `UnusedArgs: list`
    :   Return list of not defined args from the commandline
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

    `UsedLongCommandLineParameter: str`
    :   Helper for programmers. Can be used before "Process".
        Should not be used in production environment
        
        :return: A formatted, sorted list of all used long options broken to 68 characters a line.
        :rtype: str

    `UsedShortCommandLineParameter: str`
    :   Helper for programmers. Can be used before "Process".
        Should not be used in production environment
        
        :return: A formatted string giving all information about short options used, broken to 68 characters a line.
        :rtype: str

    ### Methods

    `AddChild(self, Prefix: str, Def: dict = {}, Description: str = '', Children: dict = {}, Version: str = '', License: list = [''], AddPar: str = '') ‑> None`
    :   Add a child to a instance
        
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

    `GetCmdPar(self, Entry: str, dotted: bool = False, parents: bool = False) ‑> str`
    :   Return the commandline-options for one entry
        
        :param Entry: The entry we are looking for
        :type Entry: str
        :param dotted: show prefix for long params, defaults to False
        :type dotted: bool, optional
        :param parents: show also options from parents, defaults to False
        :type parents: bool, optional
        :return: the command-line options for this entry. E.g. "-h, --help"
        :rtype: str

    `GetRemainder(self) ‑> list`
    :   Return list of additionel arguments on command-line
        
        Returns:
            list: List of additional arguments within runtime-arguments

    `IsInherited(self, key: str) ‑> bool`
    :   Check if key is from parent
        
        :param key: Key to search for
        :type key: str
        :return: True if key is inherited from parent
        :rtype: bool

    `IsOwnKey(self, key: str) ‑> bool`
    :   Check if the key is from the own optionset
        
        :param key: Key to search for
        :type key: str
        :return: True if key is in the own optionset
        :rtype: bool

    `MyProgName(self) ‑> str`
    :   Return the program-name
        
        :return: Name of the executeable
        :rtype: str

    `MyProgPath(self) ‑> str`
    :   Return the program-path
        
        :return: Path of the directory where executeable resides
        :rtype: str

    `MyPwd(self) ‑> str`
    :   Return the directory at invocation of "Process"
        
        :return: Current directory at the time "Process" was called
        :rtype: str

    `ParamStr(self, indent: int = 4, header: bool = True, allvalues: bool = True, dotted: bool = False, cmdpar: bool = True, parentopts: bool = False, recursive: bool = True) ‑> str`
    :   Returns a string with formatted output of the
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

    `Process(self) ‑> bool`
    :   Process the runtime-arguments.
        After this call the values of the class are all set.
        
        .. note::
            You can not access the values bevore you call this function. The results
            are undefined.
        
        :raises RuntimeError: if an internal error occures. Should never occure!
        :raises ParamError: if an error occures within a parameter
        :return: True if a terminal function is requested. e.g this are "Help", all "License" and all "Export" options
        :rtype: bool

    `SetAddPar(self, AddPar: str = '') ‑> None`
    :   Description of additional parameters for usage-function.
        printed in first line after "OPTIONS"
        normally used if there are non-option parameters on command line.
        (e.g. file ... file)
        
        :param AddPar: The text or additional parameters. Defaults to "".
        :type AddPar: str, optional
        :raises TypeError: if AddPar is not a string

    `SetAllParams(self, AllParams: bool = True) ‑> None`
    :   Set the flag for All Params
        
        :param AllParams: If True, all params are initialized,
            at least with None. If False params with no default and no setting on
            the commandline are not defined within the dictionary, defaults to True
        :type AllParams: bool, optional

    `SetArgs(self, Args: Union[list, tuple, ForwardRef(None)] = None) ‑> None`
    :   Set the argument list to process
        
        :param Args: Runtime Arguments, if None: use sys.argv as the arguments , defaults to None
        :type Args: Optional[Union[list, tuple]], optional
        :raises TypeError: if Args is not a list or tuple

    `SetChk(self, Chk=None)`
    :   Set the check-function. Not implementet now
        
        :param Chk: The user check function
        :type Chk: callable
        :raises TypeError: if function is not of the proper type

    `SetDef(self, Def: dict = {}) ‑> None`
    :   Set the definition for processing arguments
        
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

    `SetDesc(self, Desc: str = '') ‑> None`
    :   Set the description of the program for usage-string.
        
        :param Desc: A descriptive string for the Program.
            printed bevore the parameters. Defaults to ''.
        :type Desc: str, optional
        :raises TypeError: if Desc is not a string.

    `SetTranslation(self, translation: dict, IsChild: bool = False) ‑> None`
    :   Seta net translation-table
        
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

    `SetUserKeys(self, UserPars: Optional[dict] = None, UserModes: Optional[dict] = None) ‑> None`
    :   _summary_
        
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

    `Usage(self, ShowPrefixHeader: bool = True) ‑> str`
    :   Return the helptext
        
        :return: The help-text as would be printet if a "Help" option is set on command-line
        :rtype: str

    `items(self) ‑> list`
    :   Return the items list including the items of all parents
        
        :return: return the items list
        :rtype: list

    `keys(self) ‑> list`
    :   Return the keys list including the keys of all parentsof
        
        :return: return the keys list
        :rtype: list

    `values(self) ‑> list`
    :   Return the values list including the values of all parents
        
        :return: return the values list
        :rtype: list

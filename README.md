<div class="wy-grid-for-nav">

<div class="wy-side-scroll">

<div class="wy-side-nav-search">

[pcs\_argpass](#)

<div class="version">

1.12.268.220829142221

</div>

</div>

<div class="wy-menu wy-menu-vertical" data-spy="affix" role="navigation" aria-label="Navigation menu">

  - [Usage](#document-usage)
  - [Param reference](#document-api)
  - [Examples](#document-examples)

</div>

</div>

<div class="section wy-nav-content-wrap" data-toggle="wy-nav-shift">

** [pcs\_argpass](#)

<div class="wy-nav-content">

<div class="rst-content">

<div role="navigation" aria-label="Page navigation">

  - [](#) »
  - pcs\_argpass 1.12 documentation
  - 

-----

</div>

<div class="document" role="main" itemscope="itemscope" itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="welcome-to-pcs-argpass-s-documentation" class="section">

# Welcome to pcs\_argpass’s documentation\!

Document version: 1.12.268.220829142221

<div class="admonition note">

Note

This project is under active development.

</div>

<div id="source" class="section">

## Source

> 
> 
> <div>
> 
> You can get the complete source-code from [GitHub
> repository](https://github.com/rpietsch1953/Argpass)
> 
> </div>

</div>

<div id="detailed-documentation" class="section">

## Detailed documentation

> 
> 
> <div>
> 
> The detailed documentation is on [Read the
> Docs](https://argpass.readthedocs.io/en/latest/index.html)
> 
> </div>

</div>

<div id="table-of-contents" class="section">

## Table of contents

<div class="toctree-wrapper compound">

<span id="document-usage"></span>

<div id="usage" class="section">

### Usage

<div id="installation" class="section">

<span id="id1"></span>

#### Installation

To use pcs\_argpass, first install it using pip:

<div class="highlight-console notranslate">

<div class="highlight">

    (.venv) $ pip install pcs_argpass

</div>

</div>

</div>

<div id="use-in-your-program" class="section">

#### Use in your program

  - This module handles the most often used command-line parameter
    types:
    
      - boolean switch
    
      - integer
    
      - float
    
      - file
    
      - dir
    
      - path
    
      - text
    
      - counter

additionally this module handles the generation and display of
help-messages and licence informations. Another functionallity is the
export of parameters and the import of settings.

normally imported as

<div class="highlight-python notranslate">

<div class="highlight">

    from pcs_argpass.Param import Param, Translation_de_DE

</div>

</div>

This class can be used to create recursive sub-parameter classes. All
children inherit the settings of their parents.

Check out
[<span class="doc">Examples</span>](#document-examples)

</div>

</div>

<span id="document-api"></span>

<div id="module-Param" class="section">

<span id="param-reference"></span>

### Param reference

Deals with command-line parameters

Copyright (c) 2022 Ing. Rainer Pietsch
\<[r<span>.</span>pietsch<span>@</span>pcs-at<span>.</span>com](mailto:r.pietsch%40pcs-at.com)\>

Detailed docs at
\<<https://argpass.readthedocs.io/en/latest/index.html>\>

Source at \<<https://github.com/rpietsch1953/Argpass>\>

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

  - *<span class="pre">class</span><span class="w">
    </span>*<span class="sig-prename descclassname"><span class="pre">Param.</span></span><span class="sig-name descname"><span class="pre">Param</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span>*,
    *<span class="n"><span class="pre">Def</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">dict</span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">{}</span></span>*,
    *<span class="n"><span class="pre">Args</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">Optional</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">None</span></span>*,
    *<span class="n"><span class="pre">Chk</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*,
    *<span class="n"><span class="pre">Desc</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">str</span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">''</span></span>*,
    *<span class="n"><span class="pre">AddPar</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">str</span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">''</span></span>*,
    *<span class="n"><span class="pre">AllParams</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">bool</span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">True</span></span>*,
    *<span class="n"><span class="pre">UserPars</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">Optional</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">None</span></span>*,
    *<span class="n"><span class="pre">UserModes</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">Optional</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">None</span></span>*,
    *<span class="n"><span class="pre">ErrorOnUnknown</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">bool</span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">True</span></span>*,
    *<span class="n"><span class="pre">HelpType</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">int</span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">0</span></span>*,
    *<span class="n"><span class="pre">Children</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">dict</span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">{}</span></span>*,
    *<span class="n"><span class="pre">translation</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">dict</span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">{}</span></span>*,
    *<span class="n"><span class="pre">Version</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">str</span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">''</span></span>*,
    *<span class="n"><span class="pre">License</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">Optional</span><span class="p"><span class="pre">\[</span></span><span class="pre">Union</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w">
    </span><span class="pre">tuple</span><span class="p"><span class="pre">,</span></span><span class="w">
    </span><span class="pre">list</span><span class="p"><span class="pre">,</span></span><span class="w">
    </span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">None</span></span>*,
    *<span class="n"><span class="pre">ShowPrefixOnHelp</span></span><span class="p"><span class="pre">:</span></span><span class="w">
    </span><span class="n"><span class="pre">bool</span></span><span class="w">
    </span><span class="o"><span class="pre">=</span></span><span class="w">
    </span><span class="default_value"><span class="pre">True</span></span>*,
    *<span class="n"><span class="pre">\_Child</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span>  
    Main class and also the result-dictionary. A member of this class
    acts like a dictionary. There are some special cases if you use
    nested childs. (Check out the
    [<span class="doc">Usage</span>](#document-usage) section
    for further information)
    
      - <span class="sig-name descname"><span class="pre">AddChild</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">Prefix</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">str</span></span>*,
        *<span class="n"><span class="pre">Def</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">dict</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">{}</span></span>*,
        *<span class="n"><span class="pre">Description</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">str</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">''</span></span>*,
        *<span class="n"><span class="pre">Children</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">dict</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">{}</span></span>*,
        *<span class="n"><span class="pre">Version</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">str</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">''</span></span>*,
        *<span class="n"><span class="pre">License</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">list</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">\[''\]</span></span>*,
        *<span class="n"><span class="pre">AddPar</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">str</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">''</span></span>*<span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">None</span></span></span>  
        Add a child to a instance
        
          - Parameters
            
              - **Def** (*dict,* *optional*) – Definition for this
                instance (look at
                [`SetDef()`](#Param.Param.SetDef "Param.Param.SetDef")
                for details), defaults to {}
            
              - **Description** (*str,* *optional*) – Description of
                this instance, defaults to ‘’
            
              - **Children** (*dict,* *optional*) – Dictionary of
                children to the new instance, defaults to {}
            
              - **Version** (*str,* *optional*) – A version string,
                defaults to ‘’
            
              - **AddPar** (*str,* *optional*) – Additional parameter
                string of this instance, defaults to ‘’
        
          - Raises  
            **self.DeclarationError** – If a parameter is invalid
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">Child</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">Dict</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w">
        </span><span class="pre">object</span><span class="p"><span class="pre">\]</span></span>*  
        Child dict
        
          - Returns  
            return all the children of this instance
        
          - Return type  
            Dict\[str, [`Param`](#module-Param "Param")\]
    
    <!-- end list -->
    
      - *<span class="pre">exception</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">DeclarationError</span></span>  
        this exception is raised if there is an declaration error within
        the parameters of the class.
        
        <div class="admonition note">
        
        Note
        
        This error messages are NEVER translated since they are not user
        initiated errors.
        
        </div>
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">Definition</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">dict</span>*  
        Returns s copy of the definition
        
          - Returns  
            a definition dictionary
        
          - Return type  
            dict
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">FreeShortCommandLineParameter</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">str</span>*  
        Helper for programmers. Can be used before “Process”. Should not
        be used in production environment
        
          - Returns  
            A formatted, sorted list of all unused (free to use) short
            options broken to 68 characters a line.
        
          - Return type  
            str
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">FullPrefix</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">str</span>*  
        Returns the full qualified prefix of this instance e.g.:
        global.alpha.gamma if alpha is a child of global and gamma (this
        instance) is a child of alpha
        
          - Returns  
            full qualified prefix of this instance
        
          - Return type  
            str
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">GetCmdPar</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">Entry</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">str</span></span>*,
        *<span class="n"><span class="pre">dotted</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">False</span></span>*,
        *<span class="n"><span class="pre">parents</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">str</span></span></span>  
        Return the commandline-options for one entry
        
          - Parameters
            
              - **Entry** (*str*) – The entry we are looking for
            
              - **dotted** (*bool,* *optional*) – show prefix for long
                params, defaults to False
            
              - **parents** (*bool,* *optional*) – show also options
                from parents, defaults to False
        
          - Returns  
            the command-line options for this entry. E.g. “-h, –help”
        
          - Return type  
            str
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">GetExportDict</span></span>  
        Return the dictionary for exporting all parameters
        
          - Returns:  
            dict: The complete parameter dictionary
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">GetRemainder</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">list</span></span></span>  
        Return list of additionel arguments on command-line
        
          - Returns:  
            list: List of additional arguments within runtime-arguments
    
    <!-- end list -->
    
      - *<span class="pre">exception</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">GetoptError</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">msg</span></span>*,
        *<span class="n"><span class="pre">opt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span>*<span class="sig-paren">)</span>  
        Own error-class for option-errors
        
          - <span class="sig-name descname"><span class="pre">\_\_init\_\_</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">msg</span></span>*,
            *<span class="n"><span class="pre">opt</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span>*<span class="sig-paren">)</span>
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">IsInherited</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">bool</span></span></span>  
        Check if key is from parent
        
          - Parameters  
            **key** (*str*) – Key to search for
        
          - Returns  
            True if key is inherited from parent
        
          - Return type  
            bool
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">IsOwnKey</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">str</span></span>*<span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">bool</span></span></span>  
        Check if the key is from the own optionset
        
          - Parameters  
            **key** (*str*) – Key to search for
        
          - Returns  
            True if key is in the own optionset
        
          - Return type  
            bool
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">LongOptsList</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">list</span>*  
        Return copied list of long options
        
          - Returns:  
            list: List of long options
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">MyProgName</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">str</span></span></span>  
        Return the program-name
        
          - Returns  
            Name of the executeable
        
          - Return type  
            str
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">MyProgPath</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">str</span></span></span>  
        Return the program-path
        
          - Returns  
            Path of the directory where executeable resides
        
          - Return type  
            str
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">MyPwd</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">str</span></span></span>  
        Return the directory at invocation of “Process”
        
          - Returns  
            Current directory at the time “Process” was called
        
          - Return type  
            str
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">OverviewCommandLineParameter</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">str</span>*  
        Helper for programmers. can be used before “Process”. Should not
        be used in production environment. Give information about used
        long and short options and all unused (=availlable) short
        options.
        
          - Returns  
            A formatted string giving all information about command-line
            parameters, broken to 68 characters a line.
        
          - Return type  
            str
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">ParDict</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">dict</span>*  
        Return copied dict with references options -\> parameter-names
        
          - Returns:  
            dict: {option: name, …}
    
    <!-- end list -->
    
      - *<span class="pre">exception</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">ParamError</span></span>  
        This exception is raised if there is an error within the
        runtime-parameters. This is only raised within the
        [`Param.Process()`](#Param.Param.Process "Param.Param.Process")-function.
        
        <div class="admonition note">
        
        Note
        
        This errors are translated with the ‘translation’ dictionary.
        There is the initial state of this dict using ‘en\_US’ texts.
        
        This module also provide a ‘Translation\_de\_DE’ entry giving a
        german translation of the error-messages, and a
        ‘Translation\_en\_US’ table only vor completeness.
        
        If you can provide translations to other languages send me this
        declarations to
        \<[r<span>.</span>pietsch<span>@</span>pcs-at<span>.</span>com](mailto:r.pietsch%40pcs-at.com)\>
        and I will add them to this module.
        
        </div>
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">ParamStr</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">indent</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">int</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">4</span></span>*,
        *<span class="n"><span class="pre">header</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">True</span></span>*,
        *<span class="n"><span class="pre">allvalues</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">True</span></span>*,
        *<span class="n"><span class="pre">dotted</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">False</span></span>*,
        *<span class="n"><span class="pre">cmdpar</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">True</span></span>*,
        *<span class="n"><span class="pre">parentopts</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">False</span></span>*,
        *<span class="n"><span class="pre">recursive</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">str</span></span></span>  
        Returns a string with formatted output of the processed
        parameters.
        
          - Parameters
            
              - **indent** (*int,* *optional*) – Number of leading
                spaces for children. Defaults to 4. this value is
                multiplied with the generation. So grandchildren have
                two times this number of leading spaces and children
                only one time this number of spaces.
            
              - **header** (*bool,* *optional*) – If True a header with
                the name of the object are added, defaults to True
            
              - **allvalues** (*bool,* *optional*) – Outputs all
                avallable options for this child, included the inherited
                options. Defaults to True
            
              - **dotted** (*bool,* *optional*) – If True the names of
                the parameters are prefixed with the names of their
                parents, defaults to False
            
              - **cmdpar** (*bool,* *optional*) – If True the
                commandline-options ere included in the output, defaults
                to True
            
              - **parentopts** (*bool,* *optional*) – If True and cmdpar
                is also True the commandline-options of the parents are
                anso included in the output, defaults to False
            
              - **recursive** (*bool,* *optional*) – If True all
                descendants are include in the output, else only the own
                parameters are included, defaults to True
        
          - Returns  
            The formated string of the processed parameters
        
          - Return type  
            str
        
        Examples:
        
        <div class="highlight-text notranslate">
        
        <div class="highlight">
        
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
        
        </div>
        
        </div>
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">Parents</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">str</span>*  
        Returns the full qualified parents of this instance e.g.:
        global.alpha if alpha is a child of global and gamma (this
        instance) is a child of alpha
        
          - Returns  
            full qualified parents of this instance
        
          - Return type  
            str
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">PartPrefix</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">str</span>*  
        Returns the full qualified prefix without global of this
        instance e.g.: alpha.gamma if alpha is a child of global and
        gamma (this instance) is a child of alpha
        
          - Returns  
            full qualified prefix of this instance without root prefix
        
          - Return type  
            str
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">Prefix</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">str</span>*  
        Return the prefix of this class
        
          - Returns:  
            str: the prefix value
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">Process</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">bool</span></span></span>  
        Process the runtime-arguments. After this call the values of the
        class are all set.
        
        <div class="admonition note">
        
        Note
        
        You can not access the values bevore you call this function. The
        results are undefined.
        
        </div>
        
          - Raises
            
              - **RuntimeError** – if an internal error occures. Should
                never occure\!
            
              - [**ParamError**](#Param.Param.ParamError "Param.Param.ParamError")
                – if an error occures within a parameter
        
          - Returns  
            True if a terminal function is requested. e.g this are
            “Help”, all “License” and all “Export” options
        
          - Return type  
            bool
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">SetAddPar</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">AddPar</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">str</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">''</span></span>*<span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">None</span></span></span>  
        Description of additional parameters for usage-function. printed
        in first line after “OPTIONS” normally used if there are
        non-option parameters on command line. (e.g. file … file)
        
          - Parameters  
            **AddPar** (*str,* *optional*) – The text or additional
            parameters. Defaults to “”.
        
          - Raises  
            **TypeError** – if AddPar is not a string
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">SetAllParams</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">AllParams</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">None</span></span></span>  
        Set the flag for All Params
        
          - Parameters  
            **AllParams** (*bool,* *optional*) – If True, all params are
            initialized, at least with None. If False params with no
            default and no setting on the commandline are not defined
            within the dictionary, defaults to True
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">SetArgs</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">Args</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">Optional</span><span class="p"><span class="pre">\[</span></span><span class="pre">Union</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">,</span></span><span class="w">
        </span><span class="pre">tuple</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">None</span></span></span>  
        Set the argument list to process
        
          - Parameters  
            **Args** (*Optional\[Union\[list,* *tuple\]\],* *optional*)
            – Runtime Arguments, if None: use sys.argv as the
            arguments , defaults to None
        
          - Raises  
            **TypeError** – if Args is not a list or tuple
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">SetChk</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">Chk</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span>  
        Set the check-function. Not implementet now
        
          - Parameters  
            **Chk** (*callable*) – The user check function
        
          - Raises  
            **TypeError** – if function is not of the proper type
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">SetDef</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">Def</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">dict</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">{}</span></span>*<span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">None</span></span></span>  
        Set the definition for processing arguments
        
          - Parameters  
            **Def** (*dict,* *optional*) – A definition-dict. Defaults
            to {}.
        
          - Raises  
            **TypeError** – on error within the definition
        
        Describes the definition for arg-parsing.
        
        Def-dict: a dictionary of dictionaries
        
        <div class="highlight-python notranslate">
        
        <div class="highlight">
        
            { 'Name1': {.. declaration ..},
            ...
            'Name2': {.. declaration ..}, }
        
        </div>
        
        </div>
        
        “NameN” is the key with which, at runtime, you get the values
        within the resulting dictionary.
        
        The individual definitions look like:
        
        <div class="highlight-python notranslate">
        
        <div class="highlight">
        
            {'s': 'a',
            'l': 'longval',
            'o': True,
            'v': "LuLu",
            'm': 't',
            'd': 'Description',
            'L': 'Low',
            'U': 'Up',
            'r': False },
        
        </div>
        
        </div>
        
        where:
        
        <div class="highlight-default notranslate">
        
        <div class="highlight">
        
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
        
        </div>
        
        </div>
        
        The entries “m” and (“s” or “l”) must be present, all others are
        optional.
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">SetDesc</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">Desc</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">str</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">''</span></span>*<span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">None</span></span></span>  
        Set the description of the program for usage-string.
        
          - Parameters  
            **Desc** (*str,* *optional*) – A descriptive string for the
            Program. printed bevore the parameters. Defaults to ‘’.
        
          - Raises  
            **TypeError** – if Desc is not a string.
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">SetTranslation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">translation</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">dict</span></span>*,
        *<span class="n"><span class="pre">IsChild</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">None</span></span></span>  
        Seta net translation-table
        
          - Parameters
            
              - **translation** (*dict*) – Dictionary with translated
                error-messages
            
              - **IsChild** (*bool,* *optional*) – True if we are the
                root-parent. You should only use this Option if you know
                what you do. If it is True the **translation** dict is
                ignored and the translation of the parent is used.
                Defaults to False
        
        There are 2 ‘Hidden’ function to help debug the translations:
        
        > 
        > 
        > <div>
        > 
        > [`_PrintInitTranslation()`](#Param.Param._PrintInitTranslation "Param.Param._PrintInitTranslation")
        > and
        > 
        > [`_PrintAktualTranslation()`](#Param.Param._PrintAktualTranslation "Param.Param._PrintAktualTranslation")
        > 
        > </div>
        
        Theses functions do exactly what they say: print the values out
        to stdout. You can use them to get the exact values used. The
        following default may not be accurate at all - do not rely on
        this info, print the dict yourselve.
        
        defaults to:
        
        <div class="highlight-python notranslate">
        
        <div class="highlight">
        
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
        
        </div>
        
        </div>
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">SetUserKeys</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">UserPars</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">Optional</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">None</span></span>*,
        *<span class="n"><span class="pre">UserModes</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">Optional</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">None</span></span></span>  
        \_summary\_
        
          - Parameters
            
              - **UserPars** (*Optional\[dict\],* *optional*) – ignored
                if None. Defaults to None. Dictionary of keys used
                within the definition-dictionary. All key-value pairs
                are optional. Only the keys from self.\_\_WorkPars are
                valid. The value has to be a string. This string
                replaces the keysting for this key. After all changes
                are made the values within self.\_\_WorkPars have to be
                unique\!, defaults to None
            
              - **UserModes** (*Optional\[dict\],* *optional*) – ignored
                if None. Defaults to None. Dictionary of modes used
                within the definition-dictionary. All key-value pairs
                are optional. Only the keys from self.\_\_WorkModes are
                valid. The value has to be a string. This string
                replaces the keysting for this key. After all changes
                are made the values within self.\_\_WorkModes have to be
                unique\!, defaults to None
        
          - Raises
            
              - **TypeError** – if invalid type
            
              - [**DeclarationError**](#Param.Param.DeclarationError "Param.Param.DeclarationError")
                – if declaration is invalid
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">ShortOptsList</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">list</span>*  
        Return copied list of short options
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">TestCommandLineParameter</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">str</span>*  
        Helper for programmers. Can be used before “Process”. Helps to
        find problems with the command-line interface. Prevent
        missunderstandig the interface by the user. Should not be used
        in production environment
        
          - Returns  
            A formatted sting giving all informations about errors or
            possible problems within the definition(s).
        
          - Return type  
            str
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">UnusedArgs</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">list</span>*  
        Return list of not defined args from the commandline This list
        is for the current Param-object and all of the children of this
        Param-object. So under normal conditions it makes only sense on
        the root of all Param-objects.
        
          - Example:  
            root defines ‘-z’ child defines ‘-a’ commandline is “-a -z
            –test”
            
            UnusedArgs of child is \[‘-z’,’–test’\] UnusedArgs of root =
            \[’–test’\] which is the correct list of undefined args.
        
          - Returns:  
            list: list of undefined args (str)
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">Usage</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">ShowPrefixHeader</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">str</span></span></span>  
        Return the helptext
        
          - Returns  
            The help-text as would be printet if a “Help” option is set
            on command-line
        
          - Return type  
            str
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">UsedLongCommandLineParameter</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">str</span>*  
        Helper for programmers. Can be used before “Process”. Should not
        be used in production environment
        
          - Returns  
            A formatted, sorted list of all used long options broken to
            68 characters a line.
        
          - Return type  
            str
    
    <!-- end list -->
    
      - *<span class="pre">property</span><span class="w">
        </span>*<span class="sig-name descname"><span class="pre">UsedShortCommandLineParameter</span></span>*<span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="pre">str</span>*  
        Helper for programmers. Can be used before “Process”. Should not
        be used in production environment
        
          - Returns  
            A formatted string giving all information about short
            options used, broken to 68 characters a line.
        
          - Return type  
            str
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">\_PrintAktualTranslation</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span>  
        Prints the actual translation dict to stdout.
        
        Only usefull during development\!
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">\_PrintInitTranslation</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span>  
        Prints the initial translation dict to stdout.
        
        Only usefull during development\!
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">\_\_init\_\_</span></span><span class="sig-paren">(</span>*<span class="o"><span class="pre">\*</span></span>*,
        *<span class="n"><span class="pre">Def</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">dict</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">{}</span></span>*,
        *<span class="n"><span class="pre">Args</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">Optional</span><span class="p"><span class="pre">\[</span></span><span class="pre">list</span><span class="p"><span class="pre">\]</span></span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">None</span></span>*,
        *<span class="n"><span class="pre">Chk</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*,
        *<span class="n"><span class="pre">Desc</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">str</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">''</span></span>*,
        *<span class="n"><span class="pre">AddPar</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">str</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">''</span></span>*,
        *<span class="n"><span class="pre">AllParams</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">True</span></span>*,
        *<span class="n"><span class="pre">UserPars</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">Optional</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">None</span></span>*,
        *<span class="n"><span class="pre">UserModes</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">Optional</span><span class="p"><span class="pre">\[</span></span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">None</span></span>*,
        *<span class="n"><span class="pre">ErrorOnUnknown</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">True</span></span>*,
        *<span class="n"><span class="pre">HelpType</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">int</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">0</span></span>*,
        *<span class="n"><span class="pre">Children</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">dict</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">{}</span></span>*,
        *<span class="n"><span class="pre">translation</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">dict</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">{}</span></span>*,
        *<span class="n"><span class="pre">Version</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">str</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">''</span></span>*,
        *<span class="n"><span class="pre">License</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">Optional</span><span class="p"><span class="pre">\[</span></span><span class="pre">Union</span><span class="p"><span class="pre">\[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w">
        </span><span class="pre">tuple</span><span class="p"><span class="pre">,</span></span><span class="w">
        </span><span class="pre">list</span><span class="p"><span class="pre">,</span></span><span class="w">
        </span><span class="pre">dict</span><span class="p"><span class="pre">\]</span></span><span class="p"><span class="pre">\]</span></span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">None</span></span>*,
        *<span class="n"><span class="pre">ShowPrefixOnHelp</span></span><span class="p"><span class="pre">:</span></span><span class="w">
        </span><span class="n"><span class="pre">bool</span></span><span class="w">
        </span><span class="o"><span class="pre">=</span></span><span class="w">
        </span><span class="default_value"><span class="pre">True</span></span>*,
        *<span class="n"><span class="pre">\_Child</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span>  
        This is the constructor of the Param-class.
        
        Most of the parameters can be set also later on (if nessasary)
        
        <div class="admonition note">
        
        Note
        
        all parameters are only by name and NOT positional\!
        
        </div>
        
          - Parameters
            
              - **Def** (*dict,* *optional*) – For details check out
                [`SetDef()`](#Param.Param.SetDef "Param.Param.SetDef"),
                defaults to None
            
              - **Args** (*list,* *optional*) – For details check out
                [`SetArgs()`](#Param.Param.SetArgs "Param.Param.SetArgs"),
                defaults to None
            
              - **Chk** (*callable,* *optional*) – For details check out
                [`SetChk()`](#Param.Param.SetChk "Param.Param.SetChk"),
                defaults to None
            
              - **Desc** (*str,* *optional*) – For details check out
                [`SetDesc()`](#Param.Param.SetDesc "Param.Param.SetDesc"),
                defaults to “”
            
              - **AddPar** (*str,* *optional*) – For details check out
                [`SetAddPar()`](#Param.Param.SetAddPar "Param.Param.SetAddPar"),
                defaults to “”
            
              - **AllParams** (*bool,* *optional*) – For details check
                out
                [`SetAllParams()`](#Param.Param.SetAllParams "Param.Param.SetAllParams"),
                defaults to True
            
              - **UserPars** (*Optional\[dict\],* *optional*) – For
                details check out
                [`SetUserKeys()`](#Param.Param.SetUserKeys "Param.Param.SetUserKeys"),
                defaults to None
            
              - **UserModes** (*Optional\[dict\],* *optional*) – For
                details check out
                [`SetUserKeys()`](#Param.Param.SetUserKeys "Param.Param.SetUserKeys"),
                defaults to None
            
              - **ErrorOnUnknown** (*bool,* *optional*) –
                
                If True an error is raised if there are undefined
                options on the commandline, if False: no error is
                raised.
                
                UnusedArgs is always populated with all undefined args
                from the commandline. This error is raised only on the
                topmost Param-object (not on children) Defaults to True.
                So if set to False you can test the ‘UnusedArgs’
                property after return of the ‘Process’-function to get
                the list of undefined args and process this situation on
                your own. Defaults to True
            
              - **HelpType** (*int,* *optional*) –
                
                Type of helptext.
                
                0: No Type, no standard defaults, 1: No Type, all
                defaults, 2: Type, no standard defaults, 3: Type and all
                defaults,
                
                defaults to 0
            
              - **Children** (*dict,* *optional*) –
                
                Dictionary of Child-definition for this class.
                
                <div class="highlight-python notranslate">
                
                <div class="highlight">
                
                    { 'Name': {'Def': {}, 'Desc': str, 'AddPar': str, 'Children': {} }, .... }
                
                </div>
                
                </div>
                
                  - Name = The name of this child. Must be unique.  
                    Is translated to lower case. Can not be “global”
                    (this is the name of the root-class)
                
                Def = A definition dictionary like our own “Def”
                parameter,
                
                  - Children (optional) = dict of type Children,
                    describes the grand-childer,  
                    this can be done to any level.
                
                  - Desc (optional) = A string that describes this
                    class  
                    (like our own “Desc”-parameter).
                
                  - AddPar (optional) = String used as additional info  
                    (like our own “AddPar”-parameter). Defaults to {}
            
              - **translation** (*dict,* *optional*) – For details check
                out
                [`SetTranslation()`](#Param.Param.SetTranslation "Param.Param.SetTranslation"),
                defaults to None
            
              - **License** (*list\[str\],* *optional*) –
                
                List of license-texts. Thie texts are displayed if a ‘§’
                or ‘L’ -type option is applied. If ‘§’: only the first
                entry within this list is displayed, if ‘L’: all entries
                separated by a newline (’n’) are displayed. To help
                there is a separate module “GPL3” which includes the
                folowing entries:
                
                > 
                > 
                > <div>
                > 
                > ”GPL\_Preamble” the suggested preamble (after the
                > copyright notice)
                > 
                > ”GPL\_Preamble\_DE” the same preamble in German
                > language.
                > 
                >   - ”LGPL\_Preamble” the suggested preamble for the
                >     LGPL  
                >     (use after the copyright notice)
                > 
                > ”LGPL\_Preamble\_DE” the same preamble in German
                > language.
                > 
                >   - ”LGPL3\_2007” the additional terms of the Lesser
                >     GPL Version 3 from  
                >     June, 29th 2007, you shold append also the
                >     following (GPL3\_2007) if you use this license.
                > 
                > ”GPL3\_2007” the complete text of the GPL Version 3
                > from June, 29th 2007
                > 
                > </div>
                
                you can use this by
                
                <div class="highlight-python notranslate">
                
                <div class="highlight">
                
                    from pcs_argpass.GPL3 import GPL_Preamble, LGPL3_2007, GPL3_2007
                
                </div>
                
                </div>
                
                and in the constructor of Param par example with:
                
                <div class="highlight-python notranslate">
                
                <div class="highlight">
                
                    MyParam = Param (
                        ....
                    License=('\nCopyright (c) <date> <your name>\n' + GPL_Preamble_DE,
                            GPL_Preamble,
                            LGPL3_2007,
                            GPL3_2007),
                        ....
                        )
                
                </div>
                
                </div>
                
                but, of course you can use every other license text you
                want, as long as this license is compatible with the
                license of this module, whitch IS LGPL3.
            
              - **Version** (*str,* *optional*) – Version string for
                help-display, defaults to ‘’
            
              - **ShowPrefixOnHelp** –
                
                if True a header block in the form
                
                <div class="highlight-text notranslate">
                
                <div class="highlight">
                
                    ------------------------------------------------------------
                    <child-name>
                    ------------------------------------------------------------
                
                </div>
                
                </div>
        
        is printed within the help-output to divide child help from each
        other
        
          - Parameters  
            **\_Child** (*bool,* *optional*) – True if this instance
            should be a child, defaults to False
        
        <div class="admonition note">
        
        Note
        
        All long options can be abbreviated to at least 2 characters or
        to the length making them unique within the defined long
        options.
        
        Example:
        
        > 
        > 
        > <div>
        > 
        > you define ‘automatic’, ‘autonom’ and ‘testopt’ at the
        > commandline this can be abbreviated to
        > 
        > <div class="highlight-default notranslate">
        > 
        > <div class="highlight">
        > 
        >     PROG --autom --auton --te
        > 
        > </div>
        > 
        > </div>
        > 
        > but not to
        > 
        > <div class="highlight-default notranslate">
        > 
        > <div class="highlight">
        > 
        >     PROG --au
        > 
        > </div>
        > 
        > </div>
        > 
        > because this is not unique within the optionlist.
        > 
        > </div>
        
        </div>
        
        <div class="admonition note">
        
        Note
        
        If children are used, the prefix-name is always optional, but if
        given, the option is ONLY recognized for this child. if there
        are the same long options for more then one child and NO prefix
        is given, this option is recognized by ALL children having this
        long option within their definition.
        
        Example:
        
        > 
        > 
        > <div>
        > 
        > you define ‘auto’ within the root as ‘MyOpt’ you define ‘auto’
        > within the child ‘alpha’ as ‘DoAuto’
        > 
        > the commandline should be
        > 
        > <div class="highlight-default notranslate">
        > 
        > <div class="highlight">
        > 
        >     PROG --auto=yes
        > 
        > </div>
        > 
        > </div>
        > 
        > then BOTH options are set to ‘yes’ e.g. MyParam\[‘MyOpt’\] ==
        > ‘yes’ AND MyParam\[‘DoAuto’\] == ‘yes’ with the commandline
        > 
        > <div class="highlight-default notranslate">
        > 
        > <div class="highlight">
        > 
        >     PROG --alpha.auto=yes
        > 
        > </div>
        > 
        > </div>
        > 
        > only MyParam\[‘DoAuto’\] == ‘yes’ and MyParam\[‘MyOpt’\] is
        > either the default or not set depending on the definition of
        > this option with the commandline
        > 
        > <div class="highlight-default notranslate">
        > 
        > <div class="highlight">
        > 
        >     PROG --alpha.auto=yes --global.auto=no
        > 
        > </div>
        > 
        > </div>
        > 
        > MyParam\[‘MyOpt’\] == ‘no’ AND MyParam\[‘DoAuto’\] == ‘yes’
        > REMEMBER: ‘global’ is ALWAYS the name of the root
        > Param-object\!
        > 
        > </div>
        
        please inform your users about this possibility if you use
        child-definitions\!
        
        </div>
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">items</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">list</span></span></span>  
        Return the items list including the items of all parents
        
          - Returns  
            return the items list
        
          - Return type  
            list
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">keys</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">list</span></span></span>  
        Return the keys list including the keys of all parentsof
        
          - Returns  
            return the keys list
        
          - Return type  
            list
    
    <!-- end list -->
    
      - <span class="sig-name descname"><span class="pre">values</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span>
        <span class="sig-return"><span class="sig-return-icon">→</span>
        <span class="sig-return-typehint"><span class="pre">list</span></span></span>  
        Return the values list including the values of all parents
        
          - Returns  
            return the values list
        
          - Return type  
            list

</div>

<span id="document-examples"></span>

<div id="examples" class="section">

### Examples

<div id="simple-example-one-file" class="section">

<span id="example-1"></span>

#### Simple example: One file

let’s view an example (my native language is German, so I use this with
translation):

Ex1.py:

<div class="highlight-default notranslate">

<div class="highlight">

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

</div>

</div>

Try start this program with “-h” and next time with “-§” or “-L”. Try
start it with illegal parameters and look what happens.

If you start the program without any parameters the result will be:

<div class="highlight-text notranslate">

<div class="highlight">

    ------------------------------------------------------------
    global
    ------------------------------------------------------------
    global -> MqttBroker (-m, --mqttbroker) : 'localhost'
    global -> MqttPort   (-p, --port)       : 1883
    global -> OutFile    (-f, --file)       : ''
    global -> Topic      (-t, --topic)      : ['#']

</div>

</div>

If you give “-h” or “–help” the result is:

<div class="highlight-text notranslate">

<div class="highlight">

    Version:: 1.0.0
    Usage:
    
        Ex1 [OPTIONS ...]
    
    dump MQTT-Topics to file
    Options:
    
    -h   --help                Show this text and quit.
    
    -m   --mqttbroker=value    Default: 'localhost'
                               Address of MQTT-Broker
    
    -p   --port=value          (1024 ... 32766), Default: 1883
                               Port of MQTT-Broker
    
    -t   --topic=value         Topic to dump
    
    -f   --file=value          Output path
    
    -§   --license             Show license and exit
    -l
    
    -g   --gpl                 Show complete license and exit
         --GPL
         --Gpl

</div>

</div>

The module will enshure that you get all requested parameter at least
initiated with the default values. All not requested options are found
in **UnusedArgs**. If you prefer to not having keys that are not on the
command-line set **AllParams** to False. An error will be raised in this
case if a “required” parameter (‘r’ is True) is not given.

It is up to you if you check yourselve for a default value (e.g. ‘’ at
OutFile) or let the module check if the parameter is given.

If you simply set the output to sys.stdout if not given you MUST set
**AllParams** to True and test the resultvalue yourselfe.

</div>

<div id="normal-but-still-simple-example-two-files" class="section">

<span id="example-2"></span>

#### Normal but still simple example: Two files

Normally you put the parameter definition in its own file to make the
program more readable:

1.) Ex2\_Args.py

<div class="highlight-default notranslate">

<div class="highlight">

    #!/usr/bin/env python3
    # vim: expandtab:ts=4:sw=4:noai
    """Example 2 Args"""
    Def_LogMqtt = {
        'Help':
            {
            's': 'h',
            'l': 'help',
            'm': 'H',
            'd': 'Show this text and quit.'
            },
        'MqttBroker':
            {
            's': 'm',
            'l': 'mqttbroker',
            'm': 't',
            'r': True,
            'o': True,
            'v': 'localhost',
            'd': 'Address of MQTT-Broker',
            },
        'MqttPort':
            {
            's': 'p',
            'l': 'port',
            'm': 'i',
            'L': 1024,
            'U': 32766,
            'r': True,
            'o': True,
            'v': 1883,
            'd': 'Port of MQTT-Broker',
            },
        'Topic':
            {
            's': 't',
            'l': 'topic',
            'm': 't',
            'o': True,
            'M': True,
            'v': [],
            'd': 'Topic to dump',
            },
        'OutFile':
            {
            's': 'f',
            'l': 'file',
            'm': 'p',
            'o': True,
            'd': 'Output path',
            },
        'License':
            {
            's': '§l',
            'l': 'license',
            'm': '§',
            'd': 'Show license and exit'
            },
        'GPL':
            {
            's': 'g',
            'l': ('gpl','GPL','Gpl'),
            'm': 'L',
            'd': 'Show complete license and exit'
            },
    }

</div>

</div>

2.) Ex2.py

<div class="highlight-default notranslate">

<div class="highlight">

    #!/usr/bin/env python3
    # vim: expandtab:ts=4:sw=4:noai
    """Example 2"""
    import sys
    from pcs_argpass.Param import Param #, Translation_de_DE
    from pcs_argpass.GPL3 import LGPL_Preamble_DE, GPL3_2007, LGPL_Preamble, LGPL3_2007
    from Ex2_Args import Def_LogMqtt
    
    MyParam:Param = None              # to produce an error if not initialized!
    Version = "1.0.0"
    
    def main():
        """ Do your work here """
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

</div>

</div>

Now we see that the program is very clear and short as long as it is
only for parameter handling.

</div>

<div id="more-complex-usage" class="section">

<span id="example-3"></span>

#### More complex usage

Let’s assume you write a program that uses some type of data handling.

Let’s say there is a part that adds a person to some datastructure
another part that send the data to an file and at least a possibility to
delete this person by an id returned at the time we add it.

We can define a switch for adding, another for printing and so on. The
definition will not be very clear to the user. Now we split this in to 4
parts.

1.) Ex3\_Args.py

<div class="highlight-default notranslate">

<div class="highlight">

    #!/usr/bin/env python3
    # vim: expandtab:ts=4:sw=4:noai
    """Example 2 Args"""
    Def_Main = {
        'Help':
            {
            's': 'h',
            'l': 'help',
            'm': 'H',
            'd': 'Show this text and quit.'
            },
        'License':
            {
            's': '§',
            'l': 'licence',
            'm': '§',
            'd': 'Show license text and quit.'
            },
        'GPL':
            {
            's': 'g',
            'l': 'gpl',
            'm': 'L',
            'd': 'Show full license text and quit.'
            },
        'Verbose': {
            's': 'v',
            'l': 'verbose',
            'r': False,
            'm': 'C',
            'd': "Be more verbose in logging"
            },
    }
    
    Def_Add = {
        'Help':
            {
            'l': 'help',
            'm': 'H',
            'd': 'Show this text and quit.'
            },
        'Add':
            {
            's': 'a',
            'l': 'add',
            'm': 't',
            'r': True,
            'o': True,
            'v': '',
            'd': 'Name to add',
            },
        'Department':
            {
            'l': 'department',
            'm': 't',
            'r': False,
            'o': True,
            'v': '',
            'd': 'Optional department',
            },
    }
    
    Def_Print = {
        'Print':
            {
            's': 'p',
            'l': 'print',
            'm': 'b',
            'v' : False,
            'd': 'Print values'
            },
    }
    
    Def_Del = {
        'Del':
            {
            's': 'd',
            'l': 'del',
            'm': 'i',
            'L': 1,
            'r': True,
            'o': True,
            'v': 0,
            'd': 'Id to delete',
            },
    }
    
    Child_Def = {
        'add':
            {
            'Desc': 'Add a new name with optional department',
            'Def': Def_Add,
            },
        'del':
            {
            'Desc': 'delete an Id',
            'Def': Def_Del,
            },
        'print':
            {
            'Desc': 'Print values',
            'Def': Def_Print,
            },
    }

</div>

</div>

2.) Ex3.py

<div class="highlight-default notranslate">

<div class="highlight">

    #!/usr/bin/env python3
    # vim: expandtab:ts=4:sw=4:noai
    """Example 3"""
    
    import sys
    from Ex3_Args import Def_Main, Child_Def
    from pcs_argpass.Param import Param
    from pcs_argpass.GPL3 import GPL3_2007, GPL_Preamble
    
    
    MyParam:Param = None              # to produce an error if not initialized!
    Version = "1.0.0"
    
    def main():
        """ Do your work here """
        print(MyParam.ParamStr())       # only to do something
    
        AddPar = MyParam.Child['add']   # you can get a sub-part of your definitions
        for key,value in AddPar.items():
            print(f"{key} -> {value}")
    
    if __name__ == '__main__':
        try:                                            # catch illegal definitions
            MyParam = Param(Def=Def_Main,
                            Desc="Manage names",
                            AllParams=True,
                            Children=Child_Def,
                            Version=Version,
                            ShowPrefixOnHelp=False,
    #                        translation=Translation_de_DE, # remove this line for english messages
                            License=('\nCopyright (c) 2022 <your name>\n' + GPL_Preamble, GPL3_2007))
            print(MyParam.TestCommandLineParameter)
            if not MyParam.Process():
                main()
        except Param.ParamError as RunExc:      # here we catch any parameter errors and inform the user
            print(f"{RunExc }",file=sys.stderr)
            sys.exit(1)
        sys.exit(0)

</div>

</div>

If you invoke this program with “-h” then the output look like this:

<div class="highlight-text notranslate">

<div class="highlight">

    Version:: 1.0.0
    Usage:
    
        Ex3 [OPTIONS ...]
    
    Manage names
    Options:
    
    -h   --help             Show this text and quit.
    
    -§   --licence          Show license text and quit.
    
    -g   --gpl              Show full license text and quit.
    
    -v   --verbose=value    Be more verbose in logging
    
    
        Add a new name with optional department
    
             --[add.]help                Show this text and quit.
    
        -a   --[add.]add=value           Name to add
    
             --[add.]department=value    Optional department
    
    
        delete an Id
    
        -d   --[del.]del=value    (1 ...)
                                    Id to delete
    
    
        Print values
    
        -p   --[print.]print          Print values

</div>

</div>

As you see the different options are grouped and (in this simple case
not relly necassary) vied as “function groups”. But all keys are
accessible by their names from the normal Param instance.

  - Look at **–\[add.\]help**:  
    this means there is a second help entry within this declaration. It
    only has a “long” option an can therefore be invoked by

<div class="highlight-text notranslate">

<div class="highlight">

    Ex3.py --add.help

</div>

</div>

in this case the folowing output is generated:

<div class="highlight-text notranslate">

<div class="highlight">

    #------------------------------------------------------------
    # add
    #------------------------------------------------------------
    
    
    Add a new name with optional department
    
         --[add.]help                Show this text and quit.
    
    -a   --[add.]add=value           Name to add
    
         --[add.]department=value    Optional department

</div>

</div>

I know this is not a great benefit for THIS application but if you have
a lot of parameters in an big cli it is helpfull. It is up to you if you
put a separate “help”-entry in your definition, but the rest is done by
the module.

It is possible to get the sub-instances by the “Child” property and work
with them exact the same way as with the main instance. It is also
possible to nest this system ad infinitum.

  - Remember:  
    All sub-instances inherit the keys of all of their parents\! A
    parent has also all keys of all of his children, grandchilden and so
    on.

If you run this program without any parameter the result is:

<div class="highlight-text notranslate">

<div class="highlight">

    ------------------------------------------------------------
    global
    ------------------------------------------------------------
    global    -> Verbose    (-v, --verbose) : 0
        ------------------------------------------------------------
        add
        ------------------------------------------------------------
        add   -> Add        (-a, --add)     : ''
        add   -> Department (--department)  : ''
        add   -> Verbose                    : 0
        ------------------------------------------------------------
        del
        ------------------------------------------------------------
        del   -> Del        (-d, --del)     : 0
        del   -> Verbose                    : 0
        ------------------------------------------------------------
        print
        ------------------------------------------------------------
        print -> Print      (-p, --print)   : False
        print -> Verbose                    : 0
    Add ->
    Department ->
    Verbose -> 0

</div>

</div>

Now we see that all children have the **Verbose** option of their parent
also within their keys, but that are no copies but only references to
their parent. So the key-linking is up and down the tree.

The last 3 lines is the result of the printing of the clild-instance in
the **main** function. It is exactly what we expect\!

</div>

</div>

</div>

</div>

</div>

</div>

</div>

-----

<div role="contentinfo">

© Copyright 2022, Ing. Rainer Pietsch.

</div>

Built with [Sphinx](https://www.sphinx-doc.org/) using a
[theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by
[Read the Docs](https://readthedocs.org).

</div>

</div>

</div>

</div>

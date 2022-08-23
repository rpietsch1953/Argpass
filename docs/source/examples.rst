Examples
========

.. _example_1:

Simple example: One file
------------------------

let's view an example
(my native language is German, so I use this with translation):

Ex1.py:

.. literalinclude:: Examples/Ex1.py


Try start this program with "-h" and next time with "-§" or "-L".
Try start it with illegal parameters and look what happens.

If you start the program without any parameters the result will be:

.. code-block:: text

    ------------------------------------------------------------
    global
    ------------------------------------------------------------
    global -> MqttBroker (-m, --mqttbroker) : 'localhost'
    global -> MqttPort   (-p, --port)       : 1883
    global -> OutFile    (-f, --file)       : ''
    global -> Topic      (-t, --topic)      : ['#']

If you give "-h" or "--help" the result is:

.. code-block:: text

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

The module will enshure that you get all requested parameter at least initiated with the default values. All not requested
options are found in **UnusedArgs**. If you prefer to not having keys that are not on the command-line set **AllParams**
to False. An error will be raised in this case if a "required" parameter ('r' is True) is not given.

It is up to you if you check yourselve for a default value (e.g. '' at OutFile) or let the module check if the parameter is given. 

If you simply set the output to sys.stdout if not given you MUST set **AllParams** to True and test the resultvalue yourselfe.



.. _example_2:

Normal but still simple example: Two files
------------------------------------------

Normally you put the parameter definition in its own file to make the program more readable:


1.) Ex2_Args.py

.. literalinclude:: Examples/Ex2_Args.py



2.) Ex2.py

.. literalinclude:: Examples/Ex2.py


Now we see that the program is very clear and short as long as it is only for parameter handling.



.. _example_3:

More complex usage
------------------

Let's assume you write a program that uses some type of data handling.

Let's say there is a part that adds a person to some datastructure
another part that send the data to an file and
at least a possibility to delete this person by an id returned at the time we add it. 

We can define a switch for adding, another for printing and so on. The definition will not be very clear to the user. 
Now we split this in to 4 parts.



1.) Ex3_Args.py

.. literalinclude:: Examples/Ex3_Args.py

2.) Ex3.py

.. literalinclude:: Examples/Ex3.py

If you invoke this program with "-h" then the output look like this:

.. code-block:: text

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

As you see the different options are grouped and (in this simple case not relly necassary) vied as "function groups". But
all keys are accessible by their names from the normal Param instance. 

Look at **--[add.]help**:
    this means there is a second help entry within this declaration. It only has a "long" option an can therefore be invoked by

.. code-block:: text

    Ex3.py --add.help

in this case the folowing output is generated:

.. code-block:: text

    #------------------------------------------------------------
    # add
    #------------------------------------------------------------


    Add a new name with optional department

         --[add.]help                Show this text and quit.

    -a   --[add.]add=value           Name to add

         --[add.]department=value    Optional department

I know this is not a great benefit for THIS application but if you have a lot of parameters in an big cli it is helpfull. It 
is up to you if you put a separate "help"-entry in your definition, but the rest is done by the module.


It is possible to get the sub-instances by the "Child" property and work with them exact the same way as with the main instance. It
is also possible to nest this system ad infinitum. 

Remember:
    All sub-instances inherit the keys of all of their parents!
    A parent has also all keys of all of his children, grandchilden and so on.

If you run this program without any parameter the result is:

.. code-block:: text

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

Now we see that all children have the **Verbose** option of their 
parent also within their keys, but that are no copies but only references to their parent. So 
the key-linking is up and down the tree.

The last 3 lines is the result of the printing of the clild-instance in the **main** function.
It is exactly what we expect!

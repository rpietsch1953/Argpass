Usage
=====

.. _installation:

Installation
------------

To use pcs_argpass, first install it using pip:

.. code-block:: console

   (.venv) $ pip install pcs_argpass

Use in your program
-------------------

This module handles the most often used command-line parameter types:
 - boolean switch
 - integer
 - float
 - file
 - dir
 - path
 - text
 - counter

additionally this module handles the generation and display of
help-messages and licence informations. Another functionallity is
the export of parameters and the import of settings.

normally imported as


.. code-block:: python

    from pcs_argpass.Param import Param, Translation_de_DE

This class can be used to create recursive sub-parameter classes.
All children inherit the settings of their parents.

Check out :doc:`examples`


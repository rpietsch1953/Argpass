#!/usr/bin/env python3
# vim: expandtab:ts=4:sw=4:noai

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

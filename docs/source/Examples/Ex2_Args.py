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

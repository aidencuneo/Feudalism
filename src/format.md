`FORMATTING FOR THIS PROJECT`
=============================

Hi, welcome to the formatting guide for this project!

Keep in mind that:
+ This project follows standard PEP-8 syntax.
+ This file may be updated at any time, so be sure to keep up to date with it.

## Built-in Imports
Built-in imports are in **alphabetical order.**

    import sys
    import time

    from os import getcwd, listdir, remove
    from random import choice, randint

## Local Imports
Local imports are also in **alphabetical order.**

    import ic
    import var

    from key import keycodes, Key

## From Imports
`from` imports come **after regular imports** in their respective areas,
and they are also in **alphabetical order.**


`CLASSES and FUNCTIONS come next`
=================================
One line between class definition and `__init__` method definition.

    class Key:

        def __init__(self):
            self.value = 0
            ...
            'code goes here'
        
        def anotherfunction(self, a, b):
            self.value += a + b


`VARIABLE DECLARATIONS`
=======================
There is no strict syntax for variables, although dictionaries, lists,
and tuples *should* be formatted on separate lines, as shown below:

    bobs = {
        'ross': Bob('Bob Ross'),
        'number two': Bob('Bob Number Two'),
    }

The rest of the variables simply follow this pattern:

    current_day = 1
    key = Key()
    bob = 'Bob'


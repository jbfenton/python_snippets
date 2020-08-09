"""
Different approaches to adding or modifying the behaviour of Python builtins.
"""

import builtins

# Defining a new builtin variable.
# This could be useful for defining custom application level exceptions, etc.
builtins.__unlucky__ = "unlucky"
print(builtins.__unlucky__)


# Monkey patching the builtin exec function to print the code prior to execution.
core_exec = builtins.exec


def new_exec(code, globals={}, locals={}):
    """
    builtin exec function wrapper.

    Prints the code to be executed prior to execution.

    :param code: Source code to be executed.
    :type code: str
    :param globals: Globals to add to execution context.
    :type globals: dict
    :param locals: Locals to add to execution context.
    :type locals: dict
    :return: None.
    :rtype: None
    """

    print("Executing code: {}".format(code))
    return core_exec(code, globals, locals)


builtins.exec = new_exec

exec('print("Hello World!")')

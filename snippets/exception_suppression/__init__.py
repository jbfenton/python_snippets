"""
Python 3.4 added the 'suppress' function to contextlib.
The suppress context manager will suppress specified exceptions.

This snippet is one potential approach to getting the same functionality out of Python 2.7.
"""


class SuppressException:
    """
    Exception suppression context.
    """

    def __init__(self, exc):
        """
        :param exc: Exception type to suppress.
        :type exc: type
        """

        self._exc = exc

    def __enter__(self):
        """
        Enter context.

        :return: None.
        :rtype: None
        """

        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit context.

        :param exc_type: Exception type.
        :type exc_type: type
        :param exc_val: Exception value.
        :type exc_val: exception
        :param exc_tb: Exception traceback.
        :type exc_tb: traceback
        :return:
        :rtype: bool
        """

        print(type(exc_tb))

        if exc_type == AttributeError:
            return True
        else:
            raise


with SuppressException(AttributeError):
    "".Count

print("Made it past the exception!")

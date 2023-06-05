import inspect


# how i can get result '13 >>> number = 123' instead '13 >>> variable = 123'


def print_line_number_name_and_value_of(variable: int | float | str | list | tuple | dict,
                            variable_name: str
                            ) -> None:
    """ for inspection of results
    >>> variable = 'test'
    >>> print_line_number_name_and_value_of(variable, 'variable')
    ***************************
    0 >>> variable =
    test
    """
    # frame = inspect.currentframe()
    # line_number = frame.f_back.f_lineno
    # text = f"***************************\n{~-line_number} >>> {variable_name} = \n{variable}"
    # print(text)
    print(f"***************************\n{~-inspect.currentframe().f_back.f_lineno} >>> {variable_name} = \n{variable}")


number: int = 123
print_line_number_name_and_value_of(number, 'number')

# Example usage

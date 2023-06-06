# def end_test_print_line_number_name_and_value_of(variable: int | float | str | list | set | tuple | dict,
#                                                  variable_name: str,
#                                                  test_mode: int | None = print_for_test
#                                                  ) -> None:
#     """ for inspection of results
#     >>> test = 'test'
#     >>> end_test_print_line_number_name_and_value_of(test, 'test', test_mode=1) if not git_hub else print('', end='')
#     """
#     print({
#               8: f"***************************\n{~-inspect.currentframe().f_back.f_lineno} >>> {variable_name} =\n{variable}\n{~-inspect.currentframe().f_back.f_lineno} >>> {variable_name} =\n***************************",
#               3: f"***************************\n{~-inspect.currentframe().f_back.f_lineno} >>> {variable_name} = {variable}\n***************************",
#               2: f"{~-inspect.currentframe().f_back.f_lineno} >>> {variable_name} = {variable}".splitlines()[0],
#               1: ''
#           }[test_mode], end='')
from Source.tools import filter_lines

text = """Nouns:\r\n\r\nBeneath - под (preposition), низ (noun)\r\nExample: "The treasure lies beneath the surface." - Сокровище находится под поверхностью.\r\nVerbs:\r\n\r\nNone\r\nAdjectives:\r\n\r\n"""
print([filter_lines(text)])

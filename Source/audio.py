import time
import keyboard
from typing import Unionabccv

def press_keys(*args: Union[float, str]) -> None:
    """
    Presses the given keys with optional time delays.

    Args:
        *args (float or str): The keys to press, with optional time delays between consecutive key presses.

    Raises:
        TypeError: If any argument in *args is not a float or string.

    Examples:
        >>> press_keys('a', 'b', 'c')
        >>> # Presses the keys 'a', 'b', and 'c' in sequence.
        >>>
        >>> press_keys('ctrl', 'c', 0.5, 'ctrl', 'v')
        >>> # Presses Ctrl+C, sleeps for 0.5 seconds, and then presses Ctrl+V.
    """
    for arg in args:
        if isinstance(arg, float):
            time.sleep(arg)
        elif isinstance(arg, str):
            keyboard.send(arg)
        else:
            raise TypeError(f"Invalid argument: {arg}")

# Additional test
def test_press_keys():
    press_keys('a', 'b', 'c')
    press_keys('ctrl', 'c', 0.5, 'ctrl', 'v')
    press_keys(1.5)  # Invalid argument, raises TypeError

test_press_keys()

import datetime
import traceback

txt = f'C:\\Users\\Я\\Desktop\\PythonProjectsFrom22_04_2023\\ANKI\\tests\\exceptions\\exceptions.txt'


def log_exception(module, function, data, traceback_info):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"Timestamp: {timestamp}\nModule: {module}\nFunction: {function}\nData: {data}\nTraceback:\n{traceback_info}\n\n"

    with open(txt, "a") as log_file:
        log_file.write(log_entry)


def tracebacker(func):
    def wrapped_function(*args, **kwargs):
        module = func.__module__
        function = func.__name__
        data = str(args) + str(kwargs)

        try:
            func(*args, **kwargs)

        except Exception as e:
            traceback_info = traceback.format_exc()
            print("An exception occurred!")
            log_exception(module, function, data, traceback_info)
            pass  # Optionally handle the exception or re-raise it

    return wrapped_function


# Example usage:

@tracebacker
def example_function(x, y):
    return x / y


# Test the wrapped function
result = example_function(10, 2)
print(result)  # Output: 5.0

result = example_function(10, 0)  # This will cause a ZeroDivisionError

import datetime

def logger(old_function):

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        text = f'{datetime.datetime.now()} | {old_function.__name__} | {args} - {kwargs} | {result}\n'
        with open('main.log', 'a') as log_file:
            log_file.write(text)
        return result

    return new_function
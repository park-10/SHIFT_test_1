# Логирование событий
import json
from datetime import datetime
from inspect import currentframe, getframeinfo
import inspect


def addLogging(log_dict: dict):
    loggings_file = 'loggings.json'
    log_dict['timestamp'] = currentTimeUTC()
    stack = inspect.stack()
    log_dict['lineno'] = getframeinfo(stack[1][0]).lineno
    try:
        data = json.load(open(loggings_file))
    except:
        data = []
    data.append(log_dict)
    with open(loggings_file, 'w') as f:
        json.dump(data, f, indent=2)


def currentTimeUTC():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')


addLogging({'level': 'debug', 'message': 'Сообщение'})

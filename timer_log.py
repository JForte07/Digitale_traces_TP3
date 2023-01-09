import logging
import time
from collections import Counter
from functools import wraps

 #Define a decorator function
 
logging.basicConfig()
logger = logging.getLogger("my-logger")
logger.setLevel(logging.DEBUG)


def timed(func):
    """This decorator prints the execution time for the decorated function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.debug("{} ran in {}s".format(func.__name__, round(end - start, 2)))
        a = "{} ran in {}s".format(func.__name__, round(end - start, 2))
        return a

    return wrapper

#count the number of appearances of each word in this text

#With dictionnary 
def count_dict(file):
    word_dict ={}
    with open(file , encoding = 'utf8') as f:
        for line in f:
            words_in_line = line.split(' ')
            for word in words_in_line:
                if word in word_dict:
                    word_dict[word] += 1
                else :
                    word_dict[word] = 1
    return word_dict

#using the Counter function
def count_function(file):
    with open(file, encoding = 'utf8') as f:
        content = f.read()
    return Counter(content.split())

#run this experiment 100 times
def time_dict():
    import time
    start = time.time()
    count_dict('t8.shakespeare.txt')
    time = time.time() - start
    return time

def time_func():
    import time
    start = time.time()
    count_function('t8.shakespeare.txt')
    time = time.time() - start
    return time

def run_100times(): 
    dictionary=[]
    function = []
    i = 0
    while i <= 99 : 
        dictionary.append(time_dict())
        function.append(time_func())
        i += 1
    return dictionary,function
                
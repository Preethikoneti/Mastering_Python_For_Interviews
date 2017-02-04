"""Most basic example of a decorator"""
"""I am talking about this because most interviewers ask about"""
"""the basic working principle of a decorator"""

"""A decorator in layman terms is a function/ class assigned to a variable,"""
"""passed to another function and returned from another function"""
"""Basic example:"""

def time_this(original_function):
    def new_function(*args, **kwargs):
        import datetime as dt
        before = dt.datetime.now()
        x = original_function(*args, **kwargs)
        after = dt.datetime.now()
        print("Elapsed time = {0}".format(after - before))
        return x
    return new_function()

@time_this      # '@' is used to define a decorator
def func_a(stuff):
    import time
    time.sleep(3)
# the above can also be written as
def func_a(stuff):
    import time
    time.sleep(3)
func_a = time_this(func_a)

"""func_a() is passed into time_this() as an argument and returned at the end."""
"""This is what decorators do!"""

"""Although this program will not execute right now"""
"""since no argument has been passed into func_a"""

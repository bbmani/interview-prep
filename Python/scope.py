'''
    LEGB - Local, Enclosed, Global, Built-ins
    function parameters are local to the function, they are not global or enclosed
'''
# GLOBAL SCOPE
# x = "global X"

def outer():
    # Enclosed Scope
    # X local to outer, enclosed to inner
    x = "outer x"
    
    def inner() :
        # Local Scope
        x = "inner x"
        print(x)
    
    inner()
    print(x)
    
outer()

def non_local_outer():
    
    y = "outer y"
    
    def non_local_inner():
        # Going to use the enclosed y
        # # not global, but outside of non_local_inner
        # nonlocal y
        y = "inner y"
        print(y)
    
    non_local_inner()
    print(y)

non_local_outer()
import functools
def collapse(L) :
    return (lambda x:" ".join(x))(functools.reduce(lambda x,y: x+y, L))

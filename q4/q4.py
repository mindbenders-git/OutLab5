import itertools as it
import operator as op
def myFunc(deg, vals, coeffs):
    x11=it.accumulate(it.repeat(deg,deg+1), lambda s, _:s-1)
    x1=it.starmap(op.pow,it.zip_longest(it.repeat(vals[0],deg+1),x11))
    y1=it.accumulate(it.repeat(1,deg+1), lambda s, _:vals[1] *s)
    xy=it.starmap(op.mul,it.zip_longest(x1,y1))
    out=b=it.starmap(op.mul,it.zip_longest(coeffs,xy))
    i=1
    j=deg
    x="x*"
    for l in out:
        yield str(x*(j-i if i<=1 else j-i+1)+"x"*(1 if i<=1 else 0)+"y*"*(i-2)+"y"*(1 if i>1 else 0)+" -> ")+str(l)
        i=i+1


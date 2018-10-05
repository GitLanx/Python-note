import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.  
    Return (total time, last result)  
    """
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.  
    Returns (best time, last result)  
    """
    best = 2 ** 32
    for i in range(reps):                       # range 在此处不被计时
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals:  
    (best of reps1 runs of (total of reps2 runs of func))  
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)# timer.py 文件
import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.  
    Return (total time, last result)  
    """
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last result)
    """
    best = 2 ** 32 
    for i in range(reps):                     # range 在这里不被计时
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start 
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals:  
    (best of reps1 runs of (total of reps2 runs of func))  
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)
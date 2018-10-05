"""
pybench.py: Test speed of one or more Pythons on a set of simple
code-string benchmarks. A function, to allow stmts to vary.
This system itself runs on both 2.X and 3.X, and may spawn both.
Uses timeit to test either the Python running this script by API
calls, or a set of Pythons by reading spawned command-line outputs
(os.popen) with Python's -m flag to find timeit on module search path.
Replaces $listif3 with a list() around generators for 3.X and an
empty string for 2.X, so 3.X does same work as 2.X. In command-line
mode only, must split multiline statements into one separate quoted
argument per line so all will be run (else might run/time first line
only), and replace all \t in indentation with 4 spaces for uniformity.
Caveats: command-line mode (only) may fail if test stmt embeds double
quotes, quoted stmt string is incompatible with shell in general, or
command-line exceeds a length limit on platform's shell--use API call
mode or homegrown timer; does not yet support a setup statement: as is,
time of all statements in the test stmt are charged to the total time.
"""

import sys, os, timeit
defnum, defrep = 1000, 5

def runner(stmts, pythons=None, tracecmd=False):
    """
    Main logic: run tests per input lists, caller handles usage modes.
    stmts: [(number?, repeat?, stmt-string)], replaces $listif3 in stmt
    pythons: None=this python only, or [(ispy3?, python-executable-path)]
    """
    print(sys.version)
    for (number, repeat, stmt) in stmts:
        number = number or defnum
        repeat = repeat or defrep
        
        if not pythons:
            # Run stmt on this python: API call
            # No need to split lines or quote here
            ispy3 = sys.version[0] == '3'
            stmt = stmt.replace('$listif3', 'list' if ispy3 else '')
            best = min(timeit.repeat(stmt=stmt, number=number, repeat=repeat))
            print('%.4f [%r]' % (best, stmt[:70]))
        
        else:
            # Run stmt on all pythons: command line
            # Split lines into quoted arguments
            print('-' * 80)
            print('[%r]' % stmt)
            for (ispy3, python) in pythons:
                stmt1 = stmt.replace('$listif3', 'list' if ispy3 else '')
                stmt1 = stmt1.replace('\t', ' ' * 4)
                lines = stmt1.split('\n')
                args = ' '.join('"%s"' % line for line in lines)
                cmd = '%s -m timeit -n %s -r %s %s' % (python, number, repeat, args)
                print(python)
                if tracecmd: print(cmd)
                print('\t' + os.popen(cmd).read().rstrip())
"""
pybench_cases.py: Run pybench on a set of pythons and statements.
Select modes by editing this script or using command-line arguments (in
sys.argv): e.g., run a "C:\python27\python pybench_cases.py" to test just
one specific version on stmts, "pybench_cases.py -a" to test all pythons
listed, or a "py −3 pybench_cases.py -a -t" to trace command lines too.
"""
import pybench, sys
pythons = [(1, 'E:\Anaconda')]            # (ispy3?, path)
stmts = [                                        # (num,rpt,stmt)
    (0, 0, "[x ** 2 for x in range(1000)]"),         # Iterations
    (0, 0, "res=[]\nfor x in range(1000): res.append(x ** 2)"),    # \n=multistmt
    (0, 0, "$listif3(map(lambda x: x ** 2, range(1000)))"),        # \n\t=indent
    (0, 0, "list(x ** 2 for x in range(1000))"),                   # $=list or ''
    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"), # String ops
    (0, 0, "s = '?'\nfor i in range(10000): s += '?'"),
]
tracecmd = '-t' in sys.argv                           # -t: trace command lines?
pythons = pythons if '-a' in sys.argv else None       # -a: all in list, else one?
pybench.runner(stmts, pythons, tracecmd)
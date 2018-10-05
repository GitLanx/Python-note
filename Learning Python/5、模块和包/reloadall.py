#!python
"""
reloadall.py: transitively reload nested modules (2.X + 3.X).
Call reload_all with one or more imported module module objects.
"""
import types
from imp import reload

def status(module):
    print('reloading ' + module.__name__)
    
def tryreload(module):
    try:
        reload(module)
    except:
        print('FAILED: %s' % module)
        
def transitive_reload(module, visited):
    if not module in visited:                     
        status(module)                            
        tryreload(module)                        
        visited[module] = True
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:        # 如果是模块就递归
                transitive_reload(attrobj, visited)
        
def reload_all(*args):
    visited = {}                                         
    for arg in args:                                    
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)
            
def tester(reloader, modname):                           # 自测试代码
    import importlib, sys                                # 仅在测试时导入
    if len(sys.argv) > 1: modname = sys.argv[1]
    module = importlib.import_module(modname)            # 通过名称字符串导入
    reloader(module)

if __name__ == '__main__':
    tester(reload_all, 'reloadall')
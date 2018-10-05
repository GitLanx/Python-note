# updatedb.py 文件

import shelve
db = shelve.open('persondb')

for key in sorted(db):
    print(key, '\t=>', db[key])
    
sue = db['Sue Jones']
sue.giveRaise(.10)
db['Sue Jones'] = sue
db.close()
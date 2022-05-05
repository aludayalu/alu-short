import json 
def get(dbname,query):
    try:
        path=dbname+"/"+query
        file=open(path)
        return file.read()
    except:
        return "False"

def add(dbname,path,to):
    import os.path
    pathtohash=dbname+"/"+path
    file_exists = os.path.exists(pathtohash)
    if file_exists==False:
        with open(pathtohash, 'x') as f:
            f.write(to)
        return True
    else:
        return False

def remove(dbname,path):
    import os.path
    pathtohash=dbname+"/"+path
    file_exists = os.path.exists(pathtohash)
    if file_exists==True:
        os.remove(pathtohash)
        return True
    else:
        return False
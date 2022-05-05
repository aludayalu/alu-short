from aludbms import query,makedb
makedb.fresh("redirs")
action=input("Choose one of the following\n1.Add Or Edit\n2.Remove\n3.Read\nSelected : ")
if action=="1":
    key=input("Input Path (without /) : ")
    value=input("Input Redirected Site URL : ")
    query.add("redirs", key, value)
if action=="2":
    key=input("Input Path (without /) : ")
    print(query.remove("redirs", key))
if action=="3":
    key=input("Input Path (without /) : ")
    print(query.get("redirs", key))

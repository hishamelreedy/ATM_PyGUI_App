def importclientsdb(id):
    import csv
    with open('clientsdb.csv',newline='')as csvfile:
        reader=csv.DictReader(csvfile)
        passofid=0
        nameofid=0
        balanceofid=0
        for column in reader:
            #print(column)
            if column['ID']==id and column['Type']=='Password':
                passofid=column['Data']
            if column['ID']==id and column['Type']=='Balance':
                balanceofid=column['Data']
            if column['ID']==id and column['Type']=='Name':
                nameofid=column['Data']
        print('id=',id)
        print('name=',nameofid)
        print('passofid=',passofid)
        print('balanceofid=',balanceofid)
        global client1
        client1 = client(id,nameofid,passofid,balanceofid)
def updateclientsdb(client1,newpass,newbalance):
    import csv
    reader=open("clientsdb.csv", "r")
    lines=list(reader)
    iterator=0
    with open('clientsdb.csv',newline='')as csvfile:
        reader=csv.DictReader(csvfile)
        for column in reader:
            if column['ID']==client1.cid and column['Type']=='Balance':
                break
            iterator=iterator+1    
    newpass=str(client1.cid)+',Password,'+str(newpass)+'\n'
    newbalance=str(client1.cid)+',Balance,'+str(newbalance)+'\n'
    print('oldpass=',lines[iterator])
    lines[iterator]=newpass
    lines[iterator+1]=newbalance
    #print('newpass=',lines[iterator])
    writer= open("clientsdb.csv","w") 
    writer.writelines(lines) 
    writer.close()

class client:
    def __init__(self,id,name,passw,balance):
        self.cid=id
        self.cname=name 
        self.cpassw=passw
        self.cbalance=int(balance)
    
    def getpass(self):
        return self.cpassw
    def getname(self):
        return self.cname
    def getbalance(self):
        return self.cbalance
    def reduceme(self,amount):
        newbalance=int(self.cbalance-int(amount))
        updateclientsdb(self,self.cpassw,newbalance)
    def changepass(self,newpass):
        updateclientsdb(self,newpass,self.cbalance)
#End of ClientDB Manager
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
def updateclientsdb(id,balanceupdate):
    import csv
    with open('clientsdb.csv',newline='')as csvfile:
        reader=csv.DictReader(csvfile)
        lines=list(reader)
        for column in lines:
            if column['ID']==id and column['Type']=='Balance':
                column['Data']=balanceupdate
                print('Balance updated:',column['Data'])
                #print(lines[column]['Data'])
        #writer=csv.writer(open(csvfile))
        #writer.writerows(reader)        
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
        self.cbalance=int(self.cbalance-int(amount))
        updateclientsdb(self.cid,self.cbalance)
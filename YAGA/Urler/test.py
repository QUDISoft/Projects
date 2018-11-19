#try:
    #f=open('exc.txt', 'a')
#except:
    #f=open('exc.txt', 'w')
#exceptions='hello', 'world', 'brave'

#for x in exceptions:
    #f.write(x + '\n')
    
f=open('exc.txt', 'r+')
excep=[]
for line in f:
    line=line[:-1]
    excep.append(line)
def delit(select):
    newExcep=[]
    for exception in excep:
        if exception!=select:
            newExcep.append(exception)    
        else:
            continue
    print(newExcep)
    
print(excep)    
delit('facebook')    

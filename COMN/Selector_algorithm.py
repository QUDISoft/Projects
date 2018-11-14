a = '#comment_126060840 > div.comment__body > div.comment__content > p:nth-child(2)'
q = 0
myList = []
print(a)
while q != len(a):
    if a[q] == '>':
        q += 2
    else:
        myList.append(a[q])
        q += 1

myString = ''.join(myList)
print("")
print(myString)

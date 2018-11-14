a = '#comment_126060840 > div.comment__body > div.comment__content > p:nth-child(2)'
q = 0
myList = []
while q != len(a):
    if a[q] == '>':
        print(a[q], 'MISS')
        q += 2
    else:
        myList.append(a[q])
        print(a[q], 'ADDED')
        q += 1

myString = ''.join(myList)
print(myString)

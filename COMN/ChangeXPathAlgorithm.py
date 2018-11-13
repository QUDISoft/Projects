a = '//*[@id="dle-content"]/div[1]/div[1]/h2/a'
nums = '1234567890'
myList = []
print(a)
q = 0

while q != len(a):
    if a[q] == '[':
        q += 1
        if a[q] in nums:
            print(a[q], 'MISS', q)
            while a[q] != ']':
                q += 1
                print(a[q], 'MISS', q)
            q += 1
        else:
            myList.append(a[q])
            print(a[q], 'ADDED', q)
            q += 1
    else:
        myList.append(a[q])
        print(a[q], 'ADDED', q)
        q += 1
myString = ''.join(myList)
print(myString)
print("")

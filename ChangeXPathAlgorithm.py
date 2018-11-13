a = '//*[@id="dle-content"]/div[1]/div[1]/h2/a'
q = 0
nums = '1234567890'
myList = []
print(a)
try:
    for x in a:
        if a[q] == '[':
            if a[q+1] in nums:
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
except:
    myString = ''.join(myList)
    print(myString)

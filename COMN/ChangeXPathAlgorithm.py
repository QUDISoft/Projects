a = '//*[@id="dle-content"]/div[1]/div[1]/h2/a'
nums = '1234567890'
print(a)
my_list = []


def xpath():
    q = 0
    while q != len(a):
        if a[q] == '[':
            q += 1
            if a[q] in nums:
                while a[q] != ']':
                    q += 1
                q += 1
            else:
                my_list.append(a[q])
                q += 1
        else:
            my_list.append(a[q])
            q += 1
    my_string = ''.join(my_list)
    print("")
    print(my_string)


xpath()

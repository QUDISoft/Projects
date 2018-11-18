# -*- coding: utf-8 -*-

exceptions='instagram', 'vk.com', 'facebook', 'twitter'
links='https://ru.wikipedia.org/vk.com/wiki/PyQt', 'https://ru.wikipedia.org/wiki/PyQt', 'https://ru.wikipedia.org/vk.com/'
a=len(exceptions)
for link in links:
    f=0
    tempLinks=[]
    for exception in exceptions:
        if exception in link:
            break
        else:
            f+=1
        
    if f==len(exceptions):
        print(link)
        
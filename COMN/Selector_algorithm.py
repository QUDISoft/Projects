a = '#container > div > div.l-gradient-wrapper > div > div > div.news-content.js-scrolling-area > div.news-wrapper > div > div > div > div > div.news-grid__part.news-grid__part_1 > div.news-tidings > div > div > div:nth-child(1) > div.news-tidings__clamping > div.news-tidings__speech.news-helpers_hide_mobile-small'
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

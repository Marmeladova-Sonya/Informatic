file = open('xml.txt', 'r')
json = open('json1.txt', 'w')
xml = file.read().split('\n')
k = len(xml)
print('{', file=json)

for i in xml:
    if i.count('<') == 1:
        if i.count('/') == 0:
            i = i.replace('<', '"')
            i = i.replace('>', '": {')
        else:
            i = ''

    if i.count('<') == 2:
        a = i[i.find('</'):]
        i = i.replace(a, '",')

    if i.count('<') == 1:
        i = i.replace('<', '"')
        i = i.replace('>', '": "')

    print(i, end="\n", file=json)
print('\t\t\t\t }  \n \t\t\t }  \n \t\t } \n \t } \n } ', file=json)

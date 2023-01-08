import re

smile = '8-P'
strs = [' .', 'afserfres8-Pqe', ' s', 'cvwmeojfnearjsgnkefjnvkjdr', '8-P']
for str1 in strs:
    if re.findall(r'[8][-][P]', str1):
        print('смайлик 8-P в строке', str1, ' встречается ', len(re.findall(r'[8][-][P]', str1)), 'раз(а)')
    else:
        print('смайлик 8-P не встречается в строке', str1)

# s = input()
# 
# for i in s:
#    m = re.search((r" ВТ "), s)
#    k = re.search((r"ИТМО"), s)
#    if m == None or k == None:
#        break
#    else:
#        m = (m.start())
#        k = (k.start())
#        z = s[m:k]
#        n = len(re.findall(" ", z))
#        if n <= 5:
#            print(s[m:k] + "ИТМО")
#            s = re.sub(r"ИТМО", "1111", s, 1)
#            s = re.sub(r"ВТ", "11", s, 1)
#        else:
#            s = re.sub(r"ИТМО", "1111",s, 1)
#            s = re.sub(r"ВТ", "11", s, 1)


# s = input()
# k = str(input())
# j = re.findall("[А-Яа-я]+-*[А-Я]*[а-я]* [А-Я]\.[А-Я]\. [A-Z][0-9]+", s)
# print(j)
# for i in range(len(j)):
#     if len(re.findall(k, j[i])) != 0:
#         x = str(j[i])
#         m = re.search("\s", x)
#         m = (m.start())
#         m2 = re.search((r"\."), x)
#         m2 = (m2.start())
#         m1 = re.search((r"-"), x)
#         if m1 != None:
#             m1 = (m1.start())
#             if x[0] != x[m + 1] or x[0] != x[m1 + 1] or x[0] != x[m2 + 1] or x[m + 1] != x[m1 + 1] or x[m + 1] != \
#                     x[m2 + 1] or x[m1 + 1] != x[m2 + 1]:
#                 print(x)
#         else:
#             if x[0] != x[m + 1] or x[0] != x[m2 + 1] or x[m + 1] != x[m2 + 1]:
#                 print(x)
#     else:
#         print(j[i])

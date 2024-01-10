str1 = 'hello, world!'
print('字符串的长度是:', len(str1))
print('单词首字母大写: ', str1.title())
print('字符串变大写: ', str1.upper())
# str1 = str1.upper()
print('字符串是不是大写: ', str1.isupper())
print('字符串是不是以hello开头: ', str1.startswith('hello'))
print('字符串是不是以hello结尾: ', str1.endswith('hello'))
print('字符串是不是以感叹号开头: ', str1.startswith('!'))
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
str2 = '- \u9a84\u6602'
str3 = str1.title() + ' ' + str2.lower()
print(str3)


'''
docker exec -it python380_c python3 python100days/day02/strings.py
'''

"""
1. 字符串常用操作
title 将字符串首字母大写
upper 将字符串所有字母大写
isupper 判断是不是所有字母大写
startswith 判断是不是以hello开头，大小写敏感
endswith 判断是不是以hello结尾，大小写敏感
2. 字符串拼接用 + 号
3. 字符串单引号、双引号都可以
"""
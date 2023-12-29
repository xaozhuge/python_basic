
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
# 
# 4 * 3 * 2 = 24
 
num = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print (i,j,k)
                num += 1

print(num)


'''
docker exec python380_c python3 demo/runoob/demo001.py
'''

'''
1. range 包含起始位置，不包含结束位置
2. if 多个条件 if () and () and ()
3. python 没有 ++，只有 +=
'''
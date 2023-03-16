# @Time    : 2023/3/16 14:08
'''
找数2
　　【问题描述】在一个小到大的有序序列中（不存在重复数字），查找某个数所在的位置。如果该数不在该数列中，输出其应插入点的位置。
输入说明
　　第一行输入N表示有N个数据（N<=1000)
　　第二行N个小到大非重复的数字（<=10000)
　　第三行数字X，查找X
输出说明
　　若X在序列中则输出其相应的位置，若不在序列中输出其应插入的位置。
样例输入
10
12 34 56 78 88 99 101 134 145 233
88
样例输出
5
样例输入
10
23 34 56 78 99 123 143 155 167 178
128
样例输出
7
'''
n = int(input())
nums = [int(i) for i in input().split()]
x = int(input())


def check(num):
    if num >= x:
        return 1
    else:
        return 0


l = 0
r = n
# 逐渐逼近，一定能找到这个数
while l < r:
    mid = (l + r) // 2
    if check(nums[mid]) == 1:
        r = mid
    else:
        l = mid + 1

print(l + 1)

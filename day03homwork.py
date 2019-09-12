#1.
# def getPentagona1number(n):
#     count = 0
#     for i in range(1,n + 1):
#         num = i * (3 * i - 1) / 2
#         print("%d"%num,end = ' ')
#         count += 1
#         if count % 10 == 0:
#             print('\n')

# getPentagona1number(100)

#2.
# def sumDigits(n):
#     ge = int(n) % 10
#     c = 0
#     for i in range(len(str(n))):
#         bai = int(n) // (10 * (10 ** i)) % 10
#         c += bai
#     sum = c + ge
#     print("这个整数之和是:%d"%sum)

# sumDigits(12345)

#3.
# def display(num1,num2,num3):
#     list = [num1,num2,num3]
#     s = sorted(list)
#     print("给三位数字排序得{}".format(s))
# if __name__ == "__main__":
#     a,b,c = map(int,input("请输入三个数字："))

#     display(a,b,c)

#5.
# def printChars():
#     for i in range(73,91):
#         print(chr(i),end=" ")
#         if i% 10 == 0:
#             print("\n")
# printChars()

#6.
# def numberOfDaysInAYear(year):
#     for count in range(year,year+11):
#         if count % 4 == 0 and count % 100 != 0 or count % 400 == 0:
#             print("{}年有366天".format(count))
#         else:
#             print("{}年有365天".format(count))
# numberOfDaysInAYear(2010)


#7.
# def distance(x1,x2,y1,y2):
#     dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     print("这两个点的距离是：%f"%dis)
# distance(1,4,4,2)


#8.
# from prettytable import PrettyTable
# def mei(p):
#     c = []
#     b = []
#     for p in range(2,32):
#         if p>1:
#             for i in range(2,p):
#                 if (p % i) == 0:
#                     break
#                 else:
#                     d = 2**(p-1)
#                     c.append([p,d])
#     for x in c:
#         if x not in b:
#             b.append(x)
#             table = PrettyTable(['p','2**(p-1)'])
#     for row in b:
#         table.add_row(row)
#     print(table)
# mei(5)

#9.
# import time
# def main():
#     localtime = time.asctime(time.localtime(time.time()))
#     print("本地时间为 :", localtime)
# main()

#10.
# import random
# def shaizi():
#     a=random.choice([1,2,3,4,5,6])
#     b=random.choice([1,2,3,4,5,6])
#     if a+b==2 or  a+b==3 or a+b==12:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('你输了')
#     elif a+b==7 or a+b==11:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('你赢了')
#     else:
#         print('%d + %d = %d' %(a,b,a+b))
#         c=random.choice([1,2,3,4,5,6])
#         d=random.choice([1,2,3,4,5,6])
#         if c+d==7:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('你输了')
#         elif c+d==a+b:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('你赢了')
# shaizi()
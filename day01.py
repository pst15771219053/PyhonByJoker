#print('hello word')
# num1=float (input("请输入数字"))
# num2=float (input("请输入另外一个数字"))
# print(num1 * num2)


# #
# a = int (input('a = '))
# b = int (input('b = '))
# print('%d + %d = %d' %(a, b, a + b))
# print('%d - %d = %d' %(a, b, a - b))
# print('%d * %d = %d' %(a, b, a * b))
# print('%d / %d = %d' %(a, b, a / b))
# print('%d // %d = %d' %(a, b, a // b))


# email = '493347685@qq.com'
# for e in email:
#     o = ord(e) - 10
#     print(chr(o),end="")


#输入一个年份，判断是否是闰年
# year = int (input('请输入一个年份：>>'))
# if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
#     print('%d 是闰年' %year)
# else:
#     print('%d 不是闰年' %year)


#将华氏度变成摄氏度
# f = float(input('请输入华氏温度'))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f,c))


#水仙花数
# Number = input('请输入一个数字：')

# bai = int (Number[0])
# shi = int (Number[1])
# ge = int (Number[2])
# if bai **3 + shi **3 + ge **3 == int(Number):
#     print('shuixianhua')
# else:
#     print('bushi shuixianhua')


#1.
c = float(input('请输入摄氏温度'))
f = (c*(9/5))+32
print('%.1f摄氏度 = %.1f华氏度' % (c,f))


#2.
import math
radius = float(input('请输入圆的半径:'))
length = float(input('请输入圆的高:'))
area = radius * radius * math.pi
volume = area * length
print('圆柱体的底面积为:%.2f'%area)
print('圆柱体的体积为:%.2f'%volume)


#3.
feet = float(input('请输入一个数字为:'))
meter = feet * 0.305
print('%.3f英尺数 对应的米数为 %.4f '%(feet,meter))


#4.
km = float(input('请输入水量:'))
inittem = float(input('输入初始温度:'))
finaltem = float(input('输入最终温度:'))
Q = km * (finaltem - inittem) * 4184
print('所需要的能量为: %.1f'%Q)


#5.
c = float(input('输入一个差额:'))
n = float(input('请输入一个百分比的年利率:'))
l = c * (n/1200)
print('所赚的利息为：%.5f'%l)


#6.
v0,v1,t = eval(input('初始速度为,末速度为,时间为：'))
a = (v1 - v0) / t
print('平均速度为：%.4f'%a)


#7.
amount = input('请输入存钱金额:')
sum = 0
for i in range(6):
    sum = (sum+float(amount)) * (1 + 0.00417)
print('6个月之后，账户值为： %.2f'%sum)


#8.
num = int(input("请输入0-1000之间任意整数："))
if num < 0 and num > 1000:
    print('输入有误')
else:
    a = int(num % 100)
    b = a % 10 
    c = int(a / 10) 
    d = int(num / 100) 
    sum = b + c + d
print('数字的和为： %d'%sum)
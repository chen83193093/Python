# i1 = 70
# i2 = 3
# i3 = 0.5
#
#
# if(i3  i1):
#     print(i3)
# elif(i1 > i2): #70 > 3
#     print(i1)  # 70
# elif(i2 > i1):
#     print(i2)

# i1 = 33
# i2 = 33
# #如果i1=i2,就输出“太好了！”，否则就输出”滚！“
#
# if(i1 == i2):
#     print("太好了！")
# else:
#     print("滚！")

#降序
# i = [10, 20, 30, 22, 5.2]
# #30 22 20 10
# # print(i[0] + i[1] + i[2] + i[3])
# print(i[0]+i[1]-i[2]+i[3]-i[4])

# 7 5 6
# 5 6 7


i = [7, 5, 6]
#i = [14, 10, 12]
# # x = i[2]  #x = 6[
# # i[2]=i[0]
# # i[0]=x
# t = i[0] # t = 7
# y = i[2] #y = 6
# z = i[1] # z = 5
# i[2] = t  #7 5 7
# i[0] = z
# i[1] = y
i[0] = i[0] * 2
i[1]=i[1]*2
i[2]=i[2]*2
print(i[0]*2+i[1]*2+i[2]*2)
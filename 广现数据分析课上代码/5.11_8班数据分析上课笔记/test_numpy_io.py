import numpy as np

a = np.array([1, 2, 3, 4, 5])

# 保存到 outfile.npy 文件上
# np.save('outfile.npy', a)

# 保存到 outfile2.npy 文件上，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上
# np.save('outfile2', a)   # 写进文件

# b = np.load('outfile.npy')     # 读取文件
# print (b)



# ---------------------------------------------
# a = np.array([[1,2,3],[4,5,6]])
# b = np.arange(0, 1.0, 0.1)
# c = np.sin(b)
# c 使用了关键字参数 sin_array
# np.savez("runoob.npz", a, b, sin_array = c)

# r = np.load("runoob.npz")  # 读
# print(r.files) # 查看各个数组名称
# print(r["arr_0"]) # 数组 a
# print(r["arr_1"]) # 数组 b
# print(r["sin_array"]) # 数组 c


# savetxt() 函数是以简单的文本文件格式存储数据，对应的使用 loadtxt() 函数来获取数据。
# a = np.array([1, 2, 3, 4, 5])
# np.savetxt('out.txt', a)
b = np.loadtxt('out.txt')
print(b)
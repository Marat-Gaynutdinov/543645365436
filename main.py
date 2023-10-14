# 1
# a = int(input("Введите число: "))
# k = 0
# for i in range(2, a // 2+1):
#     if (a % i == 0):
#         k = k+1
# if (k <= 0):
#     print("Число простое")
# else:
#     print("Число не является простым")


# 2
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
#
# array = [64, 34, 25, 12, 22, 11, 90]
# sorted_array = bubble_sort(array)
# print(sorted_array)


# 3
# def find_max(arr):
#     max_element = arr[0]
#
#     for num in arr:
#         if num > max_element:
#            max_element = num
#
#   return max_element
#
#
# array = [5, 2, 9, 3, 1, 4]
# max_num = find_max(array)
# print("Наибольший элемент масива:", max_num)


# 4
# x = int(input())
#
# def fibonacci(n):
#     if n in (1, 2):
#        return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(x))


# 5
s = ['привет', 'привет', 'привет', 'привет', 'пока', 'досвидание', 'прощай', 'здарова', 'довстречи']
di = {}
for word in s:
    if word in di.keys():
        di[word] += 1
    else:
        di[word] = 1
key = max(di, key=di.get)
print(key, di[key])
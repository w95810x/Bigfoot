#
# def bubbleSort(arr):
#     for i in range(1, len(arr)):
#         for j in range(0, len(arr)-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
# if __name__ == '__main__':
#     list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
#     print("List source is:", list)
#     result = bubbleSort(list)
#     print("List sort is:", result)
#
# list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
# for i in range(1,len(list)):
#
#     for j in range(0,len(list)-i):
#
#         if list[j]>list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
# print(list[::-1])
list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
for i in range(len(list)-1):
    print(i)
    minindex=i
    for j in range(i+1,len(list)):
        if list[j]<list[minindex]:
            minindex=j
    if i !=minindex:
        list[i],list[minindex]=list[minindex],list[i]
print(list)

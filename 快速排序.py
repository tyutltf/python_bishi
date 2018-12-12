#coding:utf-8
#author:徐卜灵
#交换排序.快速排序
# 虽然快速排序称为分治法，但分治法这三个字显然无法很好的概括快速排序的全部步骤。因此我的对快速排序作了进一步的说明：挖坑填数+分治法：
# import sys
# sys.setrecursionlimit(150000)
L = [6, 3, 2, 32, 5, 4]

def Fast_sort(L, left,right):
    if left >= right:
        return L
    key = L[left]
    low = left
    high = right
    while left < right:
        # if L[right] > key:
        #     right-=1
        # else:
        #     L[left] = L[right]
        # if L[left] <= key:
        #     left += 1
        # else:
        #     L[right] = L[left]
        # L[left] = key
        while left < right and L[right] >= key:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= key:
            left += 1
        L[right] = L[left]
    L[left] = key
    Fast_sort(L, low, left - 1)
    Fast_sort(L,left + 1,high)
    return L
print (Fast_sort(L,0,5))

#1.高质量代码
def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[left] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists
print (quick_sort(L,0,5))


#2.高质量代码
# # 设置最低位和最高位
# def quickSort(nums, low, high):
#     # 设置一个比较基准key
#     key = nums[low]
#     while low<high:
#         # 如果最高位的数 大于等于 key则向前走
#         while low<high and nums[high] >= key:
#             high -= 1
#         # 如果最低位的数 小于等于 key则向后走
#         while low<high and nums[low] <= key:
#             low += 1
#         # 交换值
#         nums[low], nums[high] = nums[high], nums[low]
#
#     #最后low=high, 此时交换key和high位上的值, 使小于key的值在key左边, 大的在key右边
#     nums[nums.index(key)], nums[low] = nums[low], nums[nums.index(key)]
#     # 返回最低位的位置
#     return low
#
#
# # 进行重复操作
# def interval(nums, low, high):
#     if low<high:
#         # 进行排序并得到最低位位置以循环操作
#         key_index = quickSort(nums, low, high)
#         interval(nums, low, key_index)
#         interval(nums, key_index+1, high)
#
#
# nums = [64,3,9,2,4,7,0,12,45,]
# interval(nums, 0, len(nums)-1)
# print nums
#

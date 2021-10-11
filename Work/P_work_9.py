def square(lst):
    return [i ** 2 for i in lst]

def sort_l(nums):

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


list_of_nums = [5, 2, 1, 7, 4]

sort_l(list_of_nums)
print(square(list_of_nums))
def insertion_sort(nums):
    for i in range(1, len(nums)):
        val_to_ins = nums[i]
        j = i
        while j > 0 and val_to_ins < nums[j - 1]:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = val_to_ins

    return nums


nums = [int(elem) for elem in input('enter numbers: ').split()]
print(insertion_sort(nums))

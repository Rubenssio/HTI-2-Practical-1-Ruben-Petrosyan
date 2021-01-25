def insertion_sort(nums):
    for i in range(1, len(nums)):
        val_to_ins = nums[i]
        move = 0
        j = i
        while j != 0:
            if val_to_ins < nums[j - 1]:
                nums[j] = nums[j - 1]
                move += 1
            else:
                break
            j -= 1
        nums[i - move] = val_to_ins

    return nums


nums = [int(elem) for elem in input('enter numbers: ').split()]
print(insertion_sort(nums))

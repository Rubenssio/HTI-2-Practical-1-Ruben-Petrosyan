def selection_sort(nums):
    for i in range(len(nums)):
        min_num_ind = i
        for j in range(i + 1, len(nums)):
            if nums[min_num_ind] > nums[j]:
                min_num_ind = j

        nums[i], nums[min_num_ind] = nums[min_num_ind], nums[i]

    return nums


nums = [int(elem) for elem in input('enter numbers: ').split()]
print(selection_sort(nums))

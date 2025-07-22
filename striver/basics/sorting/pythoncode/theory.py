class Sorting1:
    """
    Selection Sort:
    Find the minimum and swap with the current index and go on till n - 2
    """

    def selection_sort(self, numbers: list[int]):
        i = 0
        length = len(numbers)
        while i <= length - 2:
            j = i
            min_idx = i
            while j <= length - 1:
                if numbers[j] < numbers[min_idx]:
                    min_idx = j
                j += 1
            temp = numbers[i]
            numbers[i] = numbers[min_idx]
            numbers[min_idx] = temp
            i += 1
        return numbers

    def selection_sort_improved(self, nums: list[int]):
        n = len(nums)

        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            if min_idx != i:
                nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums

    def bubble_sort(self, nums: list[int]):
        length = len(nums)
        for passes in range(length):
            swapped = False
            for j in range(length - passes - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums
    def insertion_sort(self, nums: list[int]):
        for idx in range(1, len(nums)):
            temp = nums[idx]
            jdx = idx - 1
            has_shifted = False
            while jdx >= 0 and temp < nums[jdx]:
                print(f"JDX {jdx}")
                nums[jdx + 1] = nums[jdx]
                has_shifted = True
                jdx-=1
            if has_shifted:
                nums[jdx + 1] = temp
        return nums


def test_sorting1():
    sorting1 = Sorting1()
    nums = [13, 46, 24, 52, 20, 9]
    # print("Before sorting")
    # print(nums)
    # sorted_nums = sorting1.selection_sort([13, 46, 24, 52, 20, 9])
    # print("After sorting")
    # print(sorted_nums)
    # print("Selection sort improved", sorting1.selection_sort_improved(nums))
    # print("Bubble Sort ", sorting1.bubble_sort(nums))
    print("Unsorted", nums)
    print("Insertion sort ", sorting1.insertion_sort(nums))


test_sorting1()

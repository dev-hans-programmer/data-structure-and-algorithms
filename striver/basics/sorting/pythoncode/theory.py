class Sorting1():
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
                j+= 1
            temp = numbers[i]
            numbers[i] = numbers[min_idx]
            numbers[min_idx] = temp
            i+= 1
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



            


def test_sorting1():
    sorting1 = Sorting1()
    nums = [13, 46, 24, 52, 20, 9]
    print("Before sorting")
    print(nums)
    sorted_nums = sorting1.selection_sort([13, 46, 24, 52, 20, 9])
    print("After sorting")
    print(sorted_nums)
    print("Selection sort improved", sorting1.selection_sort_improved(nums))

test_sorting1()


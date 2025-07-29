import copy


class EasyArrayProblems:
    def test(self):
        print("Hello Array Test")

    def get_largest_element(self, nums: list[int]):
        largest = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > largest:
                largest = nums[i]
        return largest

    def get_second_largest_brute(self, nums: list[int]):
        largest = self.get_largest_element(nums)
        new_list = copy.copy(nums)
        new_list.remove(largest)
        second_largest = self.get_largest_element(new_list)
        return second_largest

    def get_second_largest_better(self, nums: list[int]):
        """
        Write a program to find the second largest element in an array
        """
        largest = nums[0]
        second_largest = 0
        for num in nums:
            if num > largest:
                largest = num
        for num in nums:
            if num > second_largest and num != largest:
                second_largest = num
        return second_largest

    def get_second_largest_optimal(self, nums: list[int]) -> int:
        largest = second_largest = float("-inf")

        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num

        return int(second_largest)

    def check_array_sorted_or_rotated(self, nums: list[int]) -> bool:
        """
                    Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

        There may be duplicates in the original array.

        Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.
        """
        count = 0
        length = len(nums)

        for i in range(length):
            prev = (i + 1) % length
            if nums[i] > nums[prev]:
                count += 1
                if count >= 2:
                    return False
        return True

    def r_duplicates_brute(self, nums):
        return len(list(set(nums)))

    def r_duplicates_better(self, nums: list[int]):
        freq = {}
        idx = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for f in freq:
            nums[idx] = f
            idx += 1
            # we can put anything on the remaining values after duplicates, not necessarily zero
        for i in range(idx, len(nums)):
            nums[i] = 0
        return (idx, nums)

    def r_ruplicates_best(self, nums: list[int]):
        """
        this is a 2 pointer approach
        where we place 2 pointers at the first and second place.
        Whenever we find a mismatch in values between i and j means we find an unique element hence we increment i and replace that nums[i] with nums[j].
        EVentually after iterating, i + 1 will be my total unique elements

        """
        i = 0
        j = i + 1
        while j < len(nums) - 1:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

    def remove_duplicates_from_sorted_array(self, nums: list[int]):
        """
                Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

        Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

        Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
        Return k.

        """
        # return self.r_duplicates_brute(nums)
        # return self.r_duplicates_better(nums)
        return self.r_ruplicates_best(nums)


def test_easy_array_problems():
    nums = [1, 4, 2, 3, 10]
    sorted_nums = [3, 4, 5, 1, 2]
    duplicated = [1, 1, 3, 2, 2, 10]
    p = EasyArrayProblems()
    p.test()
    print(p.get_largest_element(nums))
    print(p.get_second_largest_brute(nums))
    print(p.get_second_largest_better(nums))
    print(p.get_second_largest_optimal(nums))
    print(p.check_array_sorted_or_rotated(sorted_nums))
    print(p.remove_duplicates_from_sorted_array(duplicated))


if __name__ == "__main__":
    test_easy_array_problems()

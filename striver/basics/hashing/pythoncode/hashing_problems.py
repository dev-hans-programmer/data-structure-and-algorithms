class HashingProblems:
    def check_anagram(self, str1: str, str2: str) -> bool:
        """
        Two strings are anagrams if they contain same chars in the same frequency but order doesn’t matter
        """
        if len(str1) != len(str2):
            return False
        freq: list[int] = [0] * 26

        for ch1, ch2 in zip(str1, str2):
            freq[ord(ch1) - ord("a")] += 1
            freq[ord(ch2) - ord("a")] -= 1

        return all(f == 0 for f in freq)

    def get_idx_of_first_non_repeating_char(self, s: str):
        """
                Given a string s, return the index of the first non-repeating (unique) character in it.
        If no such character exists, return -1."""
        freq: list[int] = [0] * 26
        for char in s:
            freq[ord(char) - ord("a")] += 1
        for idx, ch in enumerate(s):
            if freq[ord(ch) - ord("a")] == 1:
                return idx

        return -1

    def most_frequent_element(self, nums: list[int]) -> int:
        """
                Given an array of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, find the smallest of them.

                Input: arr = [4, 4, 5, 5, 6]

        Output: 4

        Explanation: Both 4 and 5 appear twice, but 4 is smaller. So, 4 is the most frequent element.
        """
        
        hash_arr: list[int] = [0] * (max(nums) + 1)
        for num in nums:
            hash_arr[num] += 1
        max_freq = max(hash_arr)

        for idx, freq in enumerate(hash_arr):
            if freq == max_freq:
                return idx
        return nums[0]
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        """
            Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
        """
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        freq_list = [(num, freq) for num, freq in freq_map.items()]
        print(freq_list)
        freq_list.sort(key=lambda x: x[1], reverse=True)
        print(freq_list)
        

        return [freq_list[i][0] for i in range(k)]



def test_hashing_problems():
    h = HashingProblems()
    print(h.check_anagram("listen", "silent"))
    print(h.get_idx_of_first_non_repeating_char("aabb"))
    print(h.most_frequent_element([1, 2, 2, 3, 3, 3]))
    print(h.most_frequent_element([4, 4, 5, 5, 6]))
    # print(h.top_k_frequent([1,1,1,2,2,3], 2))
    # print(h.top_k_frequent([3,1,1,1,2,2,2,3], 2))
    print(h.top_k_frequent([3,0,1,0], 1))

print("Hello")

test_hashing_problems()


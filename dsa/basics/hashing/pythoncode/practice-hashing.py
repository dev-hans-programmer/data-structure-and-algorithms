from collections import defaultdict
class PracticeHashing:
    def count_frquency(self, nums: list[int]):
        freqMap:dict[int, int] = dict()
        frequencies: list[list[int]] = []

        for num in nums:
            print(f"Key {num} {freqMap.get(num)}")
            freqMap[num] = freqMap.get(num, 0) + 1
        for key in freqMap:
            frequencies.append([key, freqMap[key]])
        return frequencies
    def count_freq_native(self, nums: list[int]):
        max_num = max(nums)
        has_table: list[int] = [0] * (max_num + 1)

        for num in nums:
            has_table[num] += 1
        return has_table
    def count_char_frequency(self, chars: str, desired_char: str):
        freq_map: dict[str, int] = dict()

        for char in chars:
            freq_map[char] = freq_map.get(char, 0) + 1
        return freq_map.get(desired_char)
    def count_case_sensitive_freq(self, chars: str, desired_char: str):
        hash_table: list[int] = [0] * 52

        for char in chars:
            if 'a' <= char <= 'z':
                idx = ord(char) - ord('a') # 0 to 25
            elif 'A' <= char <= 'Z':
                idx = ord(char) - ord('A') + 26 # 26 to 51
            else:
                continue # non alphabet chars
            hash_table[idx] += 1
        if 'a' <= desired_char <= 'z':
            desired_idx = ord(desired_char) - ord('a')
        elif 'A' <= desired_char <= 'Z':
            desired_idx = ord(desired_char) - ord('A') + 26
        else:
            desired_idx = 0
        return hash_table[desired_idx]
    
    def count_char_freq_native(self, chars: str, desired_char: str):
        hash_table: list[int] = [0] * 26
        for char in chars:
            hash_table[ord(char) - ord('a')] += 1
        return hash_table[ord(desired_char) - ord('a')]
    
    def count_freq_pythonic(self, nums: list[int]):
        freqMap = defaultdict(int)

        for num in nums:
            freqMap[num] +=1
        return [[num, freq] for num, freq in freqMap.items()]
    

def test_practice_hashing():

    p = PracticeHashing()
    print("Hello")
    print(p.count_frquency([1, 2, 2, 1, 3]))
    print(p.count_freq_pythonic([1, 2, 2, 1, 3]))
    print(p.count_char_frequency("abcecd", 'c'))
    print(p.count_char_freq_native("abcecd", 'c'))
    print(p.count_case_sensitive_freq("abCeCd", 'C'))
    # print(p.count_freq_native([1, 2, 2, 1, 3]))

test_practice_hashing()


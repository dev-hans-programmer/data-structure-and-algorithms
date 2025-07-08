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


def test_hashing_problems():
    h = HashingProblems()
    print(h.check_anagram("listen", "silent"))
    print(h.get_idx_of_first_non_repeating_char("aabb"))


test_hashing_problems()

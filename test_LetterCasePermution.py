from LetterCasePermutation import Solution

class Test:
    def test_letterCasePermutation(self):
        expected = ["a1b2","a1B2","A1b2","A1B2"]
        s = Solution()
        assert expected == s.letterCasePermutation("a1b2")[::-1]
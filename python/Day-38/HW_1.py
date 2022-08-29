DIGIT_MAP = {
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
    "0": ["0"],
}


class Solution:
    # @param A : string
    # @return a list of strings
    def generate(self, cur_idx, cur_str):
        # print(cur_idx, cur_str)
        if cur_idx == self.N:
            self.ans.append("".join(cur_str))
            return
        for ch in DIGIT_MAP.get(self.A[cur_idx], ""):
            cur_str[cur_idx] = ch
            self.generate(cur_idx + 1, cur_str)

    def letterCombinations(self, A):
        self.N = len(A)
        self.A = A
        self.ans = []

        self.generate(0, [""] * self.N)

        return self.ans

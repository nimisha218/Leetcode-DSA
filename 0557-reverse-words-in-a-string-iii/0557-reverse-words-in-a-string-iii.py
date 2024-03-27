class Solution:
    def reverseWords(self, s: str) -> str:

        s_list = s.split(" ")
        result = []

        for word in s_list:
            for i in range(len(word) - 1, -1, -1):
                result.append(word[i])
            result.append(" ")

        return "".join(result)[:-1]

        
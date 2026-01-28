from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_len = 201
        for s in strs:
            shortest_len = min(shortest_len, len(s))

        res = []
        for i in range(shortest_len):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if char != strs[j][i]:
                    return "".join(res)
            res.append(char)

        return "".join(res)

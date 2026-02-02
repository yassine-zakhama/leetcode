from typing import List


class Solution:

    # O(m)
    def encode(self, strs: List[str]) -> str:
        for i, s in enumerate(strs):
            strs[i] = str(len(s)) + "#" + s
        return "".join(strs)

    # O(m + n)
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            len_end = i + 1
            while s[len_end] != "#":
                len_end += 1

            s_len = int(s[i:len_end])
            end_s = len_end + s_len + 1
            res.append(s[len_end + 1 : end_s])
            i = end_s

        return res

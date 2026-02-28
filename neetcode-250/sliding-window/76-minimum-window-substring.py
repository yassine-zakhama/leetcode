from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count, remaining = defaultdict(int), 0
        for c in t:
            remaining += 1
            count[c] += 1

        left, res, res_len = 0, None, float("inf")
        for right, right_c in enumerate(s):
            if right_c not in count:
                continue

            count[right_c] -= 1
            if count[right_c] >= 0:
                remaining -= 1

            if remaining > 0:
                continue

            while remaining == 0:
                if s[left] not in count:
                    left += 1
                    continue
                count[s[left]] += 1
                if count[s[left]] > 0:
                    remaining += 1
                left += 1

            candidate_len = right - left + 2
            if not res or candidate_len < res_len:
                res_len = candidate_len
                res = [left - 1, right + 1]

        return s[res[0] : res[1]] if res_len != float("inf") else ""

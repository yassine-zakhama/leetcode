from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_out = defaultdict(int)
        trust_in = defaultdict(int)

        for trusting, trusted in trust:
            trust_out[trusting] += 1
            trust_in[trusted] += 1

        for candidate_judge in range(1, n + 1):
            if trust_in[candidate_judge] == n - 1 and not trust_out[candidate_judge]:
                return candidate_judge
        return -1

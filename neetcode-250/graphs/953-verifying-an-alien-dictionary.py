from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord = {}
        for i in range(len(order)):
            ord[order[i]] = i

        def areWordsSorted(w1, w2):
            for i in range(len(w1)):
                if i == len(w2):
                    return False

                ord1, ord2 = ord[w1[i]], ord[w2[i]]
                if ord1 < ord2:
                    return True
                elif ord1 > ord2:
                    return False
            return True

        for i in range(len(words) - 1):
            if not areWordsSorted(words[i], words[i + 1]):
                return False

        return True

from collections import defaultdict, deque


# O(n^2 * len(beginWord))
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordList.append(beginWord)

        def differ_by_one(i1, i2):
            joker = True
            for j in range(len(wordList[i1])):
                if wordList[i1][j] == wordList[i2][j]:
                    continue
                if not joker:
                    return False
                joker = False
            return True

        adj = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if differ_by_one(i, j):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])

        visited, queue, shortest = set([beginWord]), deque([beginWord]), 1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == endWord:
                    return shortest
                for nei in adj[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            shortest += 1
        return 0

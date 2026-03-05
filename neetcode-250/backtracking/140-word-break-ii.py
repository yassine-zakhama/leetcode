class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        words, cache = set(wordDict), {}

        def backtrack(i):
            if i in cache:
                return cache[i]
            if i == len(s):
                return [""]

            sentences = []
            for word in words:
                if s.startswith(word, i):
                    suffixes = backtrack(i + len(word))
                    for suf in suffixes:
                        if suf:
                            sentences.append(word + " " + suf)
                        else:
                            sentences.append(word)
            cache[i] = sentences
            return sentences

        return backtrack(0)

from collections import defaultdict, deque
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0
        self.follows = {i: set([i]) for i in range(1, 501)}
        self.tweets = defaultdict(deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        if len(self.tweets[userId]) == 11:
            self.tweets[userId].popleft()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for followee in self.follows[userId]:
            if self.tweets[followee]:
                heap.append(
                    (
                        self.tweets[followee][-1][0],
                        len(self.tweets[followee]) - 1,
                        followee,
                    )
                )
        heapq.heapify(heap)

        res = []
        while heap and len(res) < 10:
            _, tweet_idx, user_id = heapq.heappop(heap)
            res.append(self.tweets[user_id][tweet_idx][1])
            if tweet_idx > 0:
                tweet_idx -= 1
                heapq.heappush(
                    heap, (self.tweets[user_id][tweet_idx][0], tweet_idx, user_id)
                )
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId] and followerId != followeeId:
            self.follows[followerId].remove(followeeId)


class Twitter2:

    def __init__(self):
        self.time = 0
        self.follows = defaultdict(set)
        self.tweets = defaultdict(deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        if len(self.tweets[userId]) == 11:
            self.tweets[userId].popleft()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [tweet for tweet in self.tweets[userId]]
        for followee in self.follows[userId]:
            for tweet in self.tweets[followee]:
                heap.append(tweet)
        heapq.heapify(heap)
        res = []
        for _ in range(10):
            if not heap:
                break
            res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

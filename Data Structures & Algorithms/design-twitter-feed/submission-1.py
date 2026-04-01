from collections import defaultdict
class Twitter:

    def __init__(self):
        self.twitter = defaultdict(lambda: [set(), []])
        self.postNum = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.twitter[userId][1], (self.postNum, tweetId))
        self.postNum += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for tweet in self.twitter[userId][1]:
            heapq.heappush(heap, tweet)

        for user in self.twitter[userId][0]:
            for tweet in self.twitter[user][1]:
                heapq.heappush(heap, tweet)

        amount = min(10, len(heap))
        tweets = heapq.nlargest(amount, heap)
        res = []

        for i in range(amount):
            res.append(tweets[i][1])
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.twitter[followerId][0].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.twitter[followerId][0] or followerId == followeeId:
            return
        self.twitter[followerId][0].remove(followeeId)
        

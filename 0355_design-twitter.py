class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = defaultdict(set)
        
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        followers = self.follows[userId]
        for i in range(len(self.tweets) - 1, -1, -1):
            if self.tweets[i][1] != userId and self.tweets[i][1] not in followers:
                continue
            res.append(self.tweets[i][0])
            if len(res) == 10:
                break
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

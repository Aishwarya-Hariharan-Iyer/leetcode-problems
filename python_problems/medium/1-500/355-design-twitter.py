from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time = 1
        self.user_feeds = defaultdict(list)  # user -> their 10 most recent posts
        self.user_following = defaultdict(list) # user -> who they follow
        
    def postTweet(self, userId: int, tweetId: int) -> None:

        # Add post to self user feeds (make sure only 10 most recent are stored)
        post = (self.time, tweetId)
        self.user_feeds[userId].append(post)
        self.user_feeds[userId] = self.user_feeds[userId][-10:]
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        # We get our own feeds
        own = self.user_feeds[userId]
        feed.extend(own)

        # We get our followees' feeds
        for followee in self.user_following[userId]:
            feed.extend(self.user_feeds[followee])

        # Sort by time stamp, return top 10
        feed.sort(key=lambda x: -x[0])

        if len(feed) > 10:
            feed = feed[:10]

        feed = list(map(lambda x: x[1], feed))
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.user_following[followerId]:
            self.user_following[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if len(self.user_following[followerId]) != 0:
            self.user_following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
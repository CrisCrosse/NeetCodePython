import heapq
from collections import deque, defaultdict
from typing import List


class BruteForceTwitter:
    def __init__(self):
        self.users = set()
        # userId to list of tuples (tweetIds, time) with oldest first
        self.tweets = {}
        # userId to list of userIds
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = deque()

        tweets = self.tweets[userId]
        tweets.append((tweetId, self.time))
        if len(tweets) > 10:
            # remove oldest tweet
            tweets.popleft()

        self.tweets[userId] = tweets
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        print(f"getting news feed for {userId}")
        all_followed_tweets = []

        if userId in self.tweets:
            this_users_tweets = self.tweets[userId]
            all_followed_tweets += list(this_users_tweets)

        if userId in self.following:
            following = self.following[userId]
            print(f"user follows {following}")
            for follower in following:
                all_followed_tweets += list(self.tweets[follower])
                print(f"this follower has tweets {list(self.tweets[follower])}")

        print(all_followed_tweets)

        all_followed_tweets.sort(key=lambda tweet: tweet[1])
        return [tweet[0] for tweet in all_followed_tweets[:-11:-1]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        following = self.following.get(followerId, [])
        if followeeId not in following:
            following.append(followeeId)
        self.following[followerId] = following
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        following = self.following.get(followerId, [])
        if followeeId in following:
            following.remove(followeeId)
        self.following[followerId] = following
        return

# This solution runs in O(n) for unfollow --> list.remove,
# O(1) follow --> list.append(),
# O(m * n log m * n) get News Feed --> m is number of following accounts and n is number of tweets per account, due to
# sorting the whole list of tweets

# Improvements:
# use tweet class to improve readability
# use user class
# getNewsfeed is currently most expensive operation due to calculating feed in real time
# feed could be updated by the follow, unfollow and post actions with a push model
# feed held against user
# when follow, adds new following user, merges last 10 tweets of all following and updated feed
# when unfollow, removes following user, merges last 10 tweets of all following and updated feed
# when getNewsFeed we just return feed O(1) time complexity
# when post tweet we update user feed, create a new followed by dict, for each person following user makes new post
# go through and update their feeds

# to improve speed of recalculating feed do not sert, just merge the already time sorted user tweets using heapify.merge
# this reduces time complexity from O(n log n) to O(log n)


class OptimalHeapTwitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])

        # limit to 10 to reduce memory usage and increase speed
        if len(self.tweetMap[userId]) > 10:
            # popping from a list at 0 index is O(n) can use deque here for O(1)
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)

        # if user follows more than 10 people
        if len(self.followMap[userId]) >= 10:
            maxHeap = []
            for followeeId in self.followMap[userId]:
                # if user has tweeted
                if followeeId in self.tweetMap:
                    tweets = self.tweetMap[followeeId]
                    most_recent_tweet_index = len(tweets) - 1
                    count, tweetId = tweets[most_recent_tweet_index]
                    # this is a max heap because we use a negative to inverse the default min heap implementation
                    # the heap sorts based on the count which is our time variable

                    # for each follower push a data item with a reference to their last published tweet
                    heapq.heappush(maxHeap, [-count, tweetId, followeeId, most_recent_tweet_index - 1])
                    # remove max element which is item with highest count, so lowest abs value and therefore oldest
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)

            while maxHeap:
                # switch back to minHeap and make count postive again, so we have oldest at the end
                count, tweetId, followeeId, most_recent_tweet_index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, followeeId, most_recent_tweet_index])
        else:
            # don't do maxHeap first?
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    most_recent_tweet_index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][most_recent_tweet_index]
                    heapq.heappush(minHeap, [count, tweetId, followeeId, most_recent_tweet_index - 1])

        while minHeap and len(res) < 10:
            # get the most recently tweeted tweet using count and minHeap pop
            count, tweetId, followeeId, previous_tweet_index = heapq.heappop(minHeap)
            res.append(tweetId)
            # if a user had more than one tweet
            if previous_tweet_index >= 0:
                # get users tweet before this one
                count, tweetId = self.tweetMap[followeeId][previous_tweet_index]
                # push previous tweet and ref to one before that onto heap
                heapq.heappush(minHeap, [count, tweetId, followeeId, previous_tweet_index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
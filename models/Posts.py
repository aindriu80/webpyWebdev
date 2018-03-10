import pymongo, bcrypt
from pymongo import MongoClient
import datetime
import humanize


class Posts:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users
        self.Post = self.db.posts

    def insert_post(self, data):
        inserted = self.Posts.insert({"username": data.username, "content": data.content})
        post = self.Posts.find.one({"_id": inserted})
        new_post = {}
        new_post["name"]  = self.Users.find_one({"username": post["username"]})["name"]
        new_post["content"] = post["content"]
        return post

    def get_all_posts(self):
        all_posts = self.Posts.find()
        new_posts = []

        for post in all_posts:
            post["user"] = self.Users.find_one({"username": post["username"]})
            post["timestamp"] = humanize.naturaltime(datetime.datetime.now() -post["date_added"])
            new_posts.append(post)

        return all_posts

    def get_user_posts(self, user):
        all_posts = self.Posts.find({"username": user}).sort("data_added", -1)
        new_posts = []

        for post in all_posts:
            print(post)
            post["user"] = self.Users.find_one({"username": post["username"]})
            new_posts.append(post)

        return new_posts
import praw
import sys
import json

class RedditCollect:

	def __init__(self, config):
		with open(config, 'r') as config_file:
			content_config = [line.strip() for line in config_file.readlines()]
			self.user = content_config[0]
			self.password = content_config[1]
			self.user_agent = content_config[2]	
			self.reddit_obj = praw.Reddit(user_agent=self.user_agent)
			self.reddit_obj.login(self.user, self.password, disable_warning=True)
			
			
	def top_from_subreddit(self, limit_num, subreddit_name):
		submissions = self.reddit_obj.get_subreddit(subreddit_name, fetch=True).get_top(limit=limit_num)
		for s in submissions:
			print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
			print "======================================================="
			print "Title: " + str(s)
			print "======================================================="
			print s.selftext.lower()
			print "======================================================="
			comment_counter = 0
			for comment in praw.helpers.flatten_tree(s.comments):
				print "Comment " + str(comment_counter) + ": " + str(comment.body)
				comment_counter += 1
			print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"


if __name__ == "__main__":
	r = RedditCollect(sys.argv[1])
	r.top_from_subreddit(10, 'dating')


import praw

WRONG_SPELLING = "medhi"
SPELLING_REPLY = "It's spelled MEHDI"
USERNAME = "mehdi_not_medhi_bot"

def main():
    
    reddit = praw.Reddit(client_id="",
                         client_secret="",
                         user_agent="<console:MehdiBot:1.0>",
                         username=USERNAME,
                         password="")

    electroboom_sub = reddit.subreddit("test_for_my_bot")

    for post in electroboom_sub.new(limit=10):
        process_post(post)

def process_post(post):
    post.comments.replace_more(limit=0)
    for top_level_comment in post.comments.list():
        process_comment(top_level_comment)

    if WRONG_SPELLING in post.title.lower():
        for reply in post.comments:
            if USERNAME == reply.author:
                return
        post.reply(SPELLING_REPLY)
        print("Processing: " + post.title)

def process_comment(comment):
    if WRONG_SPELLING in comment.body:
        # Ignore this comment if it has already been replied to
        for reply in comment.replies:
            if USERNAME == reply.author:
                return
        comment.reply(SPELLING_REPLY)
        print("Processing: " + comment.body.lower())

if __name__ == "__main__":
    main()

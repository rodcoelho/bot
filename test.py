import praw
import config

WORD = 'dreamsmall'


def bot_login():
    print("Logging in...")
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "YouCannotSayThat's bot responder v0.1")
    print("Logged in...")

    return r

def run_bot(r):
    print("Fetching 25 comments...")
    for comment in r.subreddit('test').comments(limit = 25):
        if WORD in comment.body:
            print("String with '{}' found ".format(WORD) + comment.id)
            comment.reply("OMG YOU CANNOT SAY THAT - dream big")
            print("Replied to comment " + comment.id)

r = bot_login()
run_bot(r)

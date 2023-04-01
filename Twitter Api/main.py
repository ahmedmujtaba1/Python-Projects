import twint
import asyncio
import re
import nest_asyncio

# Updated list of slang words
slang_words = [
    'OMG', 'plz', 'cuz', 'yaru', 'Wdym', 'abt', 'tmr', 'pov', 'b4', 'rlly'
]

def is_valid(tweet):
    if re.search(r'[A-Z]{4,}', tweet):
        return False
    if re.search(r'[^\x00-\x7F]', tweet):
        return False
    if not (8 <= len(tweet.split()) <= 20):
        return False
    return True

async def collect_tweets_with_slang(word, tweets_with_slang, limit):
    c = twint.Config()
    c.Search = word
    c.Lang = 'en'
    c.Limit = limit
    c.Store_object = True
    c.Hide_output = True

    twint.run.Search(c)
    tweets = twint.output.tweets_list

    for tweet in tweets:
        full_text = tweet.tweet.replace('\n', ' ')
        if is_valid(full_text):
            tweets_with_slang.append(full_text)

    await asyncio.sleep(0)  # give control back to the event loop to run other tasks

    for word in slang_words:
        await collect_tweets_with_slang(word, tweets_with_slang, 150000)
        if len(tweets_with_slang) >= 600000:
            break

    # Save the collected tweets to a file
    with open('tweets_with_slang.txt', 'w', encoding='utf-8') as f:
        for tweet in tweets_with_slang:
            f.write(f'{tweet}\n')

async def main():
    nest_asyncio.apply() # apply the nest_asyncio patch
    tweets_with_slang = []
    await collect_tweets_with_slang('', tweets_with_slang, 150000)

asyncio.run(main())

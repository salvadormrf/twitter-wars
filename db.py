import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)

# hardcoded for now
mc.set("london_valid_words", 0)
mc.set("london_invalid_words", 0)
mc.set("london_tweets", 0)

mc.set("exeter_valid_words", 0)
mc.set("exeter_invalid_words", 0)
mc.set("exeter_tweets", 0)

def increment(key, val):
    mc.incr(key, val)


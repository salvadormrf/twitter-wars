from flask import Flask, jsonify

app = Flask(__name__)

import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)

@app.route("/")
def home():
    res = {}
    
    for city in ["london", "exeter"]:
        tweets = mc.get("%s_tweets" % city)
        invalid = mc.get("%s_invalid_words" % city)
        error_per_tweet = float(invalid)/float(tweets) if tweets > 0 else 0
        
        res[city] = {
                     "city": city.upper(),
                     "tweets": tweets,
                     "invalid_words": invalid,
                     "errors_per_tweet": error_per_tweet
                     }
        
    return jsonify(res)
    
if __name__ == "__main__":
    app.run(debug=True)


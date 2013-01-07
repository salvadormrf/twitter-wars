##Task 1: Twitter Wars!

XYZCompany has two offices in the UK, the first in Exeter and the second in London. As avid and curious Twitter users we'd like to find out whether the population of Exeter or London are better at spelling. By using the Twitter API, aggregate and analyse tweets from Exeter and London.


__Assumptions__
  + Hashtags and @ replies contained in tweets can be ignored and should not have an impact on the overall spelling quality of a tweet.
  + Decisions about how you classify what a tweet from London is and what a tweet from Exeter is are for you to make.
  + Decisions about the scoring of individual tweets are for you to make.

__Deliverables__
  + Full source code in PHP, Ruby or Python, along with instructions about how to run it for ourselves.
  + Results of the analysis along with any comments you wish to make, and short description of the decisions you made whilst programming your solution, written in either Markdown or Textile
  + Upload the source and description as a Gists on GitHub


###### Setup

<pre>
Make sure you have memcached and virtualenv installed
sudo apt-get install memcached
sudo apt-get install python-virtualenv

mkdir company_xyz
cd company_xyz
virtualenv env
source env/bin/activate

pip install tweepy
pip install pyenchant
pip install celery
pip install python-memcached
pip install Flask

git clone https://github.com/salvadormrf/twitter-wars.git

</pre>


###### Runnning

<pre>
Start Celery (on a new terminal)

cd company_xyz
source env/bin/activate
cd twitter-wars
celery -A tasks worker --loglevel=info
</pre>

<pre>
Start Tweet Listener agent (on a new terminal)

cd company_xyz
source env/bin/activate
cd twitter-wars
python tweet_scanner.py
</pre>


<pre>
Start Web app (on a new terminal)

cd company_xyz
source env/bin/activate
cd twitter-wars
python views.py
</pre>


<pre>
http://127.0.0.1:5000/

Example result:

{
  "london": {
    "tweets": 667, 
    "city": "LONDON", 
    "invalid_words": 863, 
    "errors_per_tweet": 1.2938530734632683
  }, 
  "exeter": {
    "tweets": 8, 
    "city": "EXETER", 
    "invalid_words": 7, 
    "errors_per_tweet": 0.875
  }
}
</pre>


#### Comments 
  - Hashtags and Mentions are cleaned using enchant tokenizer Filters
  - I use only tweets with geo information given by Twitter Streaming API, others are ignored
  - 
  - tweet_scanner.py listens for tweets from London and Exeter and creates a task
  - analyser.py utility functions to check how many invalid words exists in a tweet
  - views.py simple Flask application to show collected information
  - tasks.py Celery tasks
  - 
  - Workflow: When a tweet is received, it is automatically created an assynchronous task to analyse the tweet.
  - When the task to analyse starts, the analyser removes hashtags and mentions and checks if all words exists in english dictionary
  - Then it saves the results to a central place (in a memecache database)
  - 
  - 
  - --- Tweet ----> Analyser -----> DB results <---- Web APP
  - 
  - 
  - Next iterations
  - check in what language the tweet is (some tweets are not in English...)
  - Use a dictionary of people name's. (some tweets words are about famous people...)





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

mkdir -p idio/twitter_wars
cd idio
virtualenv env
source env/bin/activate

pip install tweepy
pip install pyenchant
pip install celery
pip install python-memcached
pip install Flask
</pre>


###### Runnning

<pre>
Start Celery

cd idio
source env/bin/activate
cd twitter_wars
celery -A tasks worker --loglevel=info
</pre>

<pre>
Start Tweet Listener agent

cd idio
source env/bin/activate
cd twitter_wars
python tweet_scanner.py
</pre>


<pre>
Start Web app

cd idio
source env/bin/activate
cd twitter_wars
python views.py
</pre>



#### Comments 
  - Hashtags and Mentions are cleaned using enchant tokenizer Filters
  - I use only tweets with geo information given by Twitter Streaming API, others are ignored
  - 
  - Workflow: we remove hashtags and mentions and we check if the word exists in english dictionary
  - 
  - Next iterations
  - check in what language the tweet is (some tweets are not not in English...)
  - Use a dictionary of people name's. (some tweets words are about famous people...)





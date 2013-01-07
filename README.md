mkdir -p idio/twitter_wars
cd idio
virtualenv env
source env/bin/activate

pip install tweepy
pip install pyenchant
pip install celery
pip install python-memcached
pip install Flask


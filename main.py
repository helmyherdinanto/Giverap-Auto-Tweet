import os
import random
import time
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

if not all([API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
    raise ValueError("Token tidak lengkap. Pastikan semua token ada di file .env")

# OAuth1 session
auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Fungsi untuk mendapatkan User ID
def get_my_user_id():
    url = "https://api.twitter.com/2/users/me"
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        user_id = response.json()['data']['id']
        print(f"User ID kamu: {user_id}")
        return user_id
    else:
        print(f"Gagal ambil user ID: {response.text}")
        return None

# Fungsi untuk post tweet
def post_tweet(content):
    url = "https://api.twitter.com/2/tweets"
    payload = {"text": content}
    response = requests.post(url, json=payload, auth=auth)
    if response.status_code == 201:
        tweet_id = response.json()['data']['id']
        print(f"Berhasil post tweet! Tweet ID: {tweet_id}")
        return tweet_id
    else:
        print(f"Gagal post tweet: {response.text}")
        return None

# Fungsi untuk like tweet
def like_tweet(user_id, tweet_id):
    url = f"https://api.twitter.com/2/users/{user_id}/likes"
    payload = {"tweet_id": tweet_id}
    response = requests.post(url, json=payload, auth=auth)
    print(f"Like status: {response.status_code} - {response.text}")

# Fungsi untuk retweet
def retweet_tweet(user_id, tweet_id):
    url = f"https://api.twitter.com/2/users/{user_id}/retweets"
    payload = {"tweet_id": tweet_id}
    response = requests.post(url, json=payload, auth=auth)
    print(f"Retweet status: {response.status_code} - {response.text}")

if __name__ == "__main__":
    user_id = get_my_user_id()
    if user_id:
        tweet_templates = [
            "Just joined an awesome giveaway from @GiveRep! Big thanks to @gagukpurnotow and @guyub20 for the heads-up! 🚀💸 #Giveaway #Crypto #Giverep",
            "Feeling lucky today? I just entered @GiveRep's giveaway! Shoutout to @gagukpurnotow & @guyub20 🙌🔥 #Airdrop #CryptoCommunity",
            "Let’s win some free crypto with @GiveRep 💰 Huge thanks to @gagukpurnotow and @guyub20 for sharing this! #Crypto #Giveaway",
            "Another chance to win with @GiveRep 👀💎 Grateful for the tag from @gagukpurnotow & @guyub20! #Web3 #AirdropSeason",
            "Daily giveaway hunt continues! Joined @GiveRep with my buddies @gagukpurnotow & @guyub20 🌟 Don’t miss out! #Giverep #CryptoLife"
        ]

        tweet_content = random.choice(tweet_templates)
        tweet_id = post_tweet(tweet_content)
        if tweet_id:
            time.sleep(2)
            like_tweet(user_id, tweet_id)
            time.sleep(2)
            retweet_tweet(user_id, tweet_id)

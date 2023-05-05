import os
import openai
import tweepy
import requests
import json
import time

# Tweet API
api_key =""
api_key_secret = ""
access_token = ""
access_token_secret = ""
bearer_token =""
consumer_key = api_key
consumer_secret = api_key_secret
clinet_id =""
client_secret =""

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)


# Set up the OpenAI API client
openai.api_key = ""
openai.organization = ""

# Define the prompt to start the conversation
prompt = "Hello, let's chat!"

# Define a function to send a message to ChatGPT and get its response
def send_message(message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt + message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Start the conversation
print("Tweeting with ChatGPT. Type 'exit' to end the tweet.")
message = input("> ")

while message.lower() != "exit":
    response = send_message(message)
    print(response)
    response_tweet = client.create_tweet(text=response[0:279])
    message = input("> ")
    time.sleep(1) # wait 1 second to avoid hitting OpenAI API rate limits

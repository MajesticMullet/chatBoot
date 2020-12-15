# chatBoot

How to write a chat bot?? This is motivated by me wanting to talk to myself when I was in year 10. Ideally I would train my chatbot on my conversations in 2013. First, I need to understand the theory and what I even need to do.

### Goal ###
Write a chatbot that has learnt off my FaceBook messaging data. If this yeilds sensitive information, write a scraper to scrape things off twitter (?) - however this may pose issues as twitter is not a conversation but rather random posts. 

- Learn how to write a chatbot
- Implement it

Finish date: 17/2/2021 (Week 1 of Uni 2021)


### Notes

wit.ai seems like a good option seeing as it is developed by FaceBook and since I'll be using my FaceBook data - I will not have to worry about some third party using possibly sensitive data. Upon further investigation, this seems boring. There is a nice web interface and it seems like you just click buttons.
I want something that requires more coding.
https://discover.bot/bot-talk/guide-to-bot-buiding-frameworks/wit-ai/

Chatbots can be categorised into two types:
1. Rule based - when you train a chatbot to answer questions based on a set of predetermiend rules on which it was trained. These fail with more complicated queries and requests.
2. Self learning - learn on their own. These can be futher categorised into retrieval based or generative. 

Rule based seems more suitable for my requirements. 

It is likely that i'll have to perform significant amounts of data sanitizing, however I want to first realise what kind of data is requried and if my FaceBook data is appropriate. 

USE A PYTHON VIRTUAL ENVIRONMENT FOR INSTALLATION.

# virtualenv setup:
(also make sure to use `python3` instead of `python`)

Creating virtual environment:
```
virtualenv <name of environment>
virtualenv chatBootMate
```
Activating virtual environment:
```
source <name of environment>/bin/activate
```
Deactivating virtual environment:
```
deactivate
```
Make sure you deactivate mate!

To check if the terminal is indeed running in the virtual environment, use: 
`echo $VIRTUAL_ENV` or `pip -V` or `which python3`

This second one should show the path to the env's location

## Terminology

_Utterance_ is something that the user would say to the bot.
_Intent_ represents what ther users utterance means or what they intend to get from the chatbot
_Entity_ is a keyword that makes the user's intent more clear.
_Tokenise_ helps separate the text data into fragments into smaller readable chunks. 

_corpus_ in linguistics this is a large and structured set of texts used to do statistical analysis and hypothesis testing, checking occurrences or validating linguistic rules within a specific language territory.

## Possible frameworks / APIs

Chatterbot: a type of generating self learning framework?
Follow up with this link: https://www.upgrad.com/blog/how-to-make-chatbot-in-python/

## Useful links:
https://chatbotsmagazine.com/how-to-make-a-chatbot-intelligent-a232dc367aed

link dump since last research:
https://www.upgrad.com/blog/how-to-make-chatbot-in-python/
https://analyticsindiamag.com/top-python-libraries-for-chatbot-development/
https://techstunt.com/top-6-python-libraries-for-chatbot-development/

Nice:
https://github.com/adeshpande3/Facebook-Messenger-Bot/blob/master/README.md
https://www.kdnuggets.com/2017/08/deep-learning-train-chatbot-talk-like-me.html
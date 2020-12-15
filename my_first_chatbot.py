'''
Following this tutorial for now:
https://www.upgrad.com/blog/how-to-make-chatbot-in-python/#How_To_Make_A_Chatbot_In_Python
'''

# importing classes 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# chat bot we are creating will be instance of class 'ChatBot'
# read_only: disables bot's ability to learn after training
# logic_adapters: list of adaptors used to train chatbot
my_bot = ChatBot(
    name='VirginMary',
    read_only=True,
    logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])


# some example response you can train your chatbot using python to learn
small_talk = [
    'sup',
    'ni how',
    'doin',
    'suhh dude',
    'ye wot m9'
]

math_bants_1 = [
    'pythag', 'a^2 + b^2 = c^2'
]

math_bant_2 = [
    'pussy', 'me + u = 69'
]

# training bot using 'ListTrainer'
list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_bants_1, math_bant_2):
    list_trainer.train(item)

print("sup")
print(my_bot.get_response("sup"))
print("\n what's your name?")
print(my_bot.get_response("what's your name?"))
print("\n show me pussy")
print(my_bot.get_response("show me pussy"))
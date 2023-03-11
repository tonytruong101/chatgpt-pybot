from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
bot = ChatBot('MyChatBot')

# Train the chatbot on some sample data
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')

# Define a function to handle user inputs
def chat(input_text):
    response = bot.get_response(input_text)
    return str(response)

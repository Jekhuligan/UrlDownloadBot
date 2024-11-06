import telebot
from telebot import types
import os
from pywebcopy import save_webpage

# Initialize bot with your token
bot = telebot.TeleBot('7741671258:AAEE5aKeN0CP_ygO0yyOxKxOYPxx_4ZDjgA')

# Handle /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Download webpage")
    markup.add(btn1)
    
    bot.reply_to(message, 
                 "Welcome! I can help you download webpages.\n"
                 "Use the button below or just send me a URL.",
                 reply_markup=markup)

# Handle URLs
@bot.message_handler(func=lambda message: message.text.startswith('http'))
def handle_url(message):
    url = message.text
    try:
        # Create folder for downloads if it doesn't exist
        folder = f"downloads/{message.chat.id}/"
        if not os.path.exists(folder):
            os.makedirs(folder)
            
        # Download webpage
        save_webpage(
            url=url,
            project_folder=folder,
            project_name="webpage",
            bypass_robots=True,
            debug=False,
            open_in_browser=False,
            delay=None,
            threaded=False,
        )
        
        # Create zip archive
        import shutil
        zip_path = f"{folder}webpage.zip"
        shutil.make_archive(f"{folder}webpage", 'zip', f"{folder}webpage")
        
        # Find all index.html files
        index_paths = []
        for root, dirs, files in os.walk(f"{folder}webpage"):
            if "index.html" in files:
                path = os.path.join(root, "index.html")
                path = path.replace(f"{folder}webpage/", "")
                index_paths.append(path)
        
        # Send zip file to user
        with open(zip_path, 'rb') as zip_file:
            bot.send_document(message.chat.id, zip_file)
            
        # Cleanup
        shutil.rmtree(folder)
        
        # Send response with index file paths
        if index_paths:
            paths_str = "\n".join(index_paths)
            bot.reply_to(message, f"Webpage downloaded and sent successfully!\nPossible main file paths in archive:\n{paths_str}")
        else:
            bot.reply_to(message, "Webpage downloaded and sent successfully!")
        
    except Exception as e:
        bot.reply_to(message, f"Error downloading webpage: {str(e)}")

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Download webpage":
        bot.reply_to(message, "Please send me the URL you want to download")
    else:
        bot.reply_to(message, "Please send me a valid URL starting with http:// or https://")

# Start the bot
bot.polling(none_stop=True)


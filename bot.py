from pyrogram import Client, filters
from pymongo import MongoClient
import os

# Get environment variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URI = os.getenv("DATABASE_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
LOG_CHANNEL = os.getenv("LOG_CHANNEL")

# Initialize the bot
bot = Client(
    "movie_search_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Initialize MongoDB client
client = MongoClient(DATABASE_URI)
db = client[DATABASE_NAME]

# Log the start
@bot.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    await message.reply_text(f"Hello {message.from_user.first_name}, I am a Movie Search Bot. Use /search <movie name> to find a movie.")

# Search command
@bot.on_message(filters.command(["search"]) & filters.private)
async def search(client, message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text("Please provide a movie name to search.")
        return

    results = db.movies.find({"title": {"$regex": query, "$options": "i"}})

    if results.count() == 0:
        await message.reply_text("No movies found matching your query.")
    else:
        response = ""
        for movie in results:
            response += f"Title: {movie['title']}\nYear: {movie['year']}\nRating: {movie['rating']}\n\n"

        await message.reply_text(response)

# Log any errors
@bot.on_message(filters.private)
async def log_errors(client, message):
    try:
        # Process message
        pass
    except Exception as e:
        await client.send_message(LOG_CHANNEL, f"Error: {e}")

# Run the bot
bot.run()

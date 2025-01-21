import asyncio
import logging
import discord
from pprint import pprint
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DISCORD_DEV_BOT_TOKEN = os.getenv('DISCORD_DEV_BOT_TOKEN')
TARGET_SERVER_ID = int(os.getenv('TARGET_SERVER_ID'))

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Discord client
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
client = discord.Client(intents=intents)

async def scrape_server(target_server):
    logger.info(f'Successfully connected to the guild: {target_server.name} (ID: {target_server.id})')
    server_data = target_server

    return server_data

def print_server_data(server_data):
    print(f"Server: {server_data['name']} (ID: {server_data['id']})")
    for category in server_data['categories']:
        print(f"  Category: {category['name']} (ID: {category['id']})")
        for channel in category['channels']:
            print(f"    Channel: {channel['name']} (ID: {channel['id']})")
            for message in channel['messages']:
                print(f"      msg: {message}")

# Modify the existing function to use the new print function
async def get_and_print_server_data():
    await client.wait_until_ready()
    target_server = discord.utils.get(client.guilds, id=TARGET_SERVER_ID)

    if not target_server:
        logger.error(f"Could not find server with ID: {TARGET_SERVER_ID}")
        return

    server_data = await scrape_server(target_server)
    print_server_data(server_data)  # Use the new function to print server data
    await client.close()

@client.event
async def on_ready():
    logger.info(f'Logged in as {client.user}')
    await get_and_print_server_data()

def main():
    client.run(DISCORD_DEV_BOT_TOKEN)

if __name__ == "__main__":
    main()

## works! demonstrates what we should be seeing.
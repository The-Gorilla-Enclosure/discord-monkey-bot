import os    
import discord
from dotenv import load_dotenv

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = discord.Client()
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if '!monke' in message.content.lower():
            if 'new' in message.content.lower():
                await message.channel.send('https://tenor.com/view/cool-shades-on-wink-banana-gif-15443150')
            else:
                await message.channel.send('gorilla need mo bananas')
    client.run(TOKEN)

if __name__ == "__main__":
    main()

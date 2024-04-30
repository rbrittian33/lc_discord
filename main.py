import os

from itertools import cycle
import asyncio
import discord
from discord.ext import commands, tasks

# Set up the bot
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

bot_status = cycle(
    ['Jumping Jacks', 'Push Ups', 'Praying', 'At a Meeting', 'Step Work', 'Self Care'])
# Define a function to get a random response from the bot
@tasks.loop(seconds=5)
async def change_status():
	await client.change_presence(activity=discord.Game(next(bot_status)))
	pass


@client.event
async def on_ready():
	print("Bot is ready")
	# change_status.start()

async def load():
	for filename in os.listdir('./cogs'):
		if filename.endswith('.py'):
			await client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_message(message):
	# Process commands first
	await client.process_commands(message)

	# Then, your existing mention handling
	if message.author == client.user:
		return
	if client.user in message.mentions:
		username = str(message.author)
		user_message = str(message.content)
		channel = str(message.channel)
		print(f'{username} said: "{user_message}" ({channel})')
		await send_message(message, user_message)





async def main():
	async with client:
		await load()
		await client.start(os.getenv("DISCORD_TOKEN"))
	
asyncio.run(main())
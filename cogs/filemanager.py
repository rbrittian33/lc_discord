import json

import aiofiles
from discord.ext import commands


class FileManager(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"FileManager Cog is ready")
	
	async def save_data(self, filename, data):
		async with aiofiles.open(databases.json, 'w') as f:
			await f.write(json.dumps(data))

	async def load_data(self, filename):
		try:
			async with aiofiles.open(databases.json, 'r') as f:
				data = await f.read()
				return json.loads(data)
		except FileNotFoundError:
			return {}

# Setup function to add this cog to the bot
def setup(bot):
	bot.add_cog(FileManager(bot))


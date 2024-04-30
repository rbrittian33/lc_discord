import random
import discord
from discord.ext import commands

class Commands(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("Commands Cog is ready")

	@commands.command()
	async def embed(self, ctx):
		embed_message = discord.Embed(title="This is an embed", description="description", color=discord.Color.blue())

		# Fixed method name and added a conditional check for guild icon
		guild_icon_url = ctx.guild.icon.url if ctx.guild.icon else None
		embed_message.set_author(name=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar.url)

		if guild_icon_url:
			embed_message.set_image(url=guild_icon_url)
			embed_message.set_thumbnail(url=guild_icon_url)

		embed_message.add_field(name="Field 1", value="Value 1", inline=False)
		embed_message.set_footer(text="This is a footer")  # Corrected method name

		await ctx.send(embed=embed_message)

	
	
	@commands.command()
	async def gm(self, ctx):
		with open("good_morning.txt", "r") as f:
			random_responses = f.readlines()
		response = random.choice(random_responses)
		await ctx.send(response)


async def setup(client):
	await client.add_cog(Commands(client))
import asyncio
import os
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
from notion_client import AsyncClient

# Correctly use the asynchronous client from notion_client
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
notion = AsyncClient(auth=NOTION_TOKEN)

class Notion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file_manager = bot.get_cog('FileManager')

    @commands.Cog.listener()
    async def on_ready(self):
        print("Notion Cog is ready")

    async def list_databases(self):
        # Using the async search method provided by notion_client
        response = await notion.search(filter={"object": "database"}, sort={"direction": "ascending", "timestamp": "last_edited_time"})
        databases = []
        for db in response['results']:
            # Ensuring that the database has a title before appending to avoid errors
            if 'title' in db and db['title']:
                databases.append({"name": db["title"][0]["plain_text"], "id": db["id"]})
        return databases

    async def database_properties(self, database_id):
        # Using the async retrieve method provided by notion_client
        properties = await notion.databases.retrieve(database_id=database_id)
        return properties

    @commands.command()
    async def get_databases(self, ctx):
        """ Command to fetch and display databases """
        databases = await self.list_databases()
        await ctx.send("\n".join([f"{db['name']} - {db['id']}" for db in databases]))

    @commands.command()
    async def get_properties(self, ctx, database_id):
        """ Command to fetch and display properties of a specific database """
        properties = await self.database_properties(database_id)
        # Formatting properties output in a simple way, could be improved based on your needs
        await ctx.send(str(properties))

# Setup function to add this cog to the bot
def setup(bot):
    bot.add_cog(Notion(bot))

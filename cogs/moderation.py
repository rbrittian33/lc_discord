import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation Cog is ready")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Cleared {amount} messages.")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, modreason):
        await member.kick(reason=modreason)
        await ctx.send(f"Kicked {member} for reason: {modreason}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, modreason):
        await member.ban(reason=modreason)
        await ctx.send(f"Banned {member} for reason: {modreason}")

    @commands.command(name="unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userId):
        banned_users = await ctx.guild.bans()
        member_to_unban = discord.utils.get(banned_users, user__id=userId)
        await ctx.guild.unban(member_to_unban)

async def setup(client):
	await client.add_cog(Moderation(client))
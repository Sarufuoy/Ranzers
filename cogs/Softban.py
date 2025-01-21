import json
import discord
from discord.ext import commands
from discord.ext.commands import command, Cog, has_permissions
import psutil
import asyncio

class Sb(Cog):
  def _init_(self, client):
    self.bot = client


  @commands.command(
      description='Softban a user! \n(Basically just kicks and deletes all messages of a user, 5 second ban)',
      aliases=['sb'])
  @commands.guild_only()
  @commands.has_permissions(ban_members=True)
  async def softban(self, ctx, user_mention: discord.Member):
      try:
          await ctx.guild.ban(user_mention)
          sbmsg = await ctx.send(f"```{user_mention} has now been softbanned!```")
          await asyncio.sleep(4.8)
          await ctx.guild.unban(user_mention)
          await sbmsg.edit(content=f"```{user_mention} has now been softbanned! he may now join this server again```")

      except discord.Forbidden:
          await ctx.error(
              f"```Cannot softban {user_mention}.\nReason: User is higher than the/as high as the bot to softban.```")
    


def setup(client):
  client.add_cog(Sb(client))
import discord
from discord.ext.commands import Cog, is_owner, command
from discord.ext import commands
import json

class Blacklistsys(Cog):
  def _init_(self, client):
    self.bot = client

  @command()
  @is_owner()
  async def ackill(self, ctx, member: discord.Member, torf):
    with open ("blusers.json", "r") as f:
      bl = json.load(f)

    if torf == "true":
      bl[str(member.id)] = {}
      bl[str(member.id)]["blacklist"] = True
      await ctx.send("Blacklist process on sir", delete_after=5)
    elif torf == "false":
      bl[str(member.id)] = {}
      bl[str(member.id)]["blacklist"] = False
      await ctx.send("Unblacklisted process on sir", delete_after=5)
    
    with open("blusers.json", "w") as f:
      json.dump(bl, f)
    
    self.em = discord.Embed(title = f"{member.name} Has been blacklisted", description = f"BY {ctx.author.send}", color = member.color)

    await ctx.author.send(embed = self.em)
  
  @Cog.listener()
  async def on_message(self, msg):
    with open("blusers.json", "r") as f:
      user = json.load(f)
    
    if str(msg.author.id) in user:
      chk = user[str(msg.author.id)]["blacklist"]
      if chk == True:
        return
      else:
        pass
    else:
      pass

def setup(client):
  client.add_cog(Blacklistsys(client))
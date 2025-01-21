import json
import discord
from discord.ext import commands
from discord.ext.commands import command, Cog

class Helperconfig(Cog):
  def _init_(self, client):
    self.bot = client
    self.msjn = "```yaml\nHey {member.name} Welcome to {member.guild.name}\n```"
    self.mslv = "```yaml\nHey {member.name} Welcome to {member.guild.name}\n``"

  @Cog.listener()
  async def on_message(self, message):
    with open("lv.json", "r") as f:
      help1 = json.load(f)
    with open("wl.json", "r") as a:
      help2 = json.load(a)
    
    if str(message.guild.id) in help1:
      return False
    else:
      help1[str(message.guild.id)] = {}
      help1[str(message.guild.id)]["leave"] = False
      with open("lv.json", "w") as f:
        json.dump(help1, f)
      help2[str(message.guild.id)] = {}
      help2[str(message.guild.id)]["join"] = False
      with open("wl.json", "w") as f:
        json.dump(help2, f)



def setup(client):
  client.add_cog(Helperconfig(client))
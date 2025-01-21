import discord
from discord.ext.commands import Cog
from discord.ext import commands
import json
import asyncio

class On_Ready(Cog):
  def _init_(self, client):
    self.bot = client

  @Cog.listener()
  async def on_ready(self):
    print("ONLINE")

  @Cog.listener()
  async def on_guild_join(self, guild):
      await asyncio.sleep(2)
      with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

      pre = prefixes[str(guild.id)] = ">"

      for channel in guild.text_channels:
          if channel.permissions_for(guild.me).send_messages:
            self.em = discord.Embed(title="Hi server this is Ranzers thanks for adding me to the server", description = f"TYPE : {pre}help to get started", color = 0x2C3E50)
            self.em.add_field(name = f"prefix {pre}", value = "prefix", inline = False)
            self.em.set_footer(text = "THANKS TO INVITE RANZERS")  
            await channel.send(embed = self.em)
          break
  
def setup(client):
  client.add_cog(On_Ready(client))
import discord
from discord.ext import commands
import asyncio
import aiohttp


class Asktrump(commands.Cog):

    def __init__(self, client):
        self.bot = client


    @commands.command(aliases=['trump', 'trumpquote'])
    async def asktrump(self, ctx, *, question):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.whatdoestrumpthink.com/api/v1/quotes/personalized?q={question}') as resp:
                file = await resp.json()
        quote = file['message']
        em = discord.Embed(color=discord.Color.green())
        em.title = "What does Trump say?"
        em.description = quote
        await ctx.send(embed=em)

def setup(client):
  client.add_cog(Asktrump(client))
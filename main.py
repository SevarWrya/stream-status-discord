import discord, os , alive , asyncio , datetime ,pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='!',
  self_bot=True
)



# name = for your status and url = for your twitch link
@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = 
  "status", url = "https://twitch.tv/paogah"))



alive.alive()
client.run(os.getenv("MTA4NTYxOTAzNDM2NTYzNjY5OQ.G70Shu.ZWUbtRIaKcMmpXYNOCRsGJtMSipvUT6F_kcWww"), bot=True)

import discord
from discord import app_commands
from dotenv import load_dotenv
import os
from typing import Optional

load_dotenv()
MY_GUILD = discord.Object(os.environ['GUILD'])
# subclasss of discord client used to implement command tree
class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.current_voice_channel = None

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.tree.command()
async def hello(interaction: discord.Interaction):
    """ Says hello """ 
    await interaction.response.send_message(f"Hi, {interaction.user.mention}")

@client.tree.command()
async def join(interaction: discord.Interaction):
    """ Joins the current voice channel"""
    if(interaction.user.voice):
        await interaction.response.send_message(f"Joining....")
        client.current_voice_channel = await interaction.user.voice.channel.connect()
    else:
        await interaction.response.send_message("Not currently in a channel!")

@client.tree.command()
async def stop(interaction: discord.Interaction):
    """ Leaves the current voice channel"""
    if(client.current_voice_channel):
        await client.current_voice_channel.disconnect()
        await interaction.response.send_message("Bye bye")
        client.current_voice_channel = None
    else:
        await interaction.response.send_message("Not currently in a voice channel")



client.run(os.environ['BOT_TOKEN'])
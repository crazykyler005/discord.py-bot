import discord
import re #regex library
#import time
#import asyncio

token = ''
regions = ["USW","USE","CAN-WEST","RUE","RU","KR","ASIA","AU","CAE","EU","IN","JP","SA"]

with open('token.txt') as f:
	token = f.read()

client = discord.Client()
#discord.ext.Bot(command_prefix='!')

@client.event
async def on_ready():
    #changes playing status of bot
    await client.change_presence(activity=discord.Game("Invisigun Reloaded"))
    print(f"We have logged in as {client.user}")

def create_cadet(message):
    #member = message.author
    role = discord.utils.get(message.guild.roles, name="cadets")
    message.author.add_roles(role)

def remove_cadet(message):
    role = discord.utils.get(message.guild.roles, name="cadets")
    message.author.remove_roles(role)

#@client.event
async def validate_gif():
    #grab the name of an image name, confirm it's a .gif and check if it has 
    # "invisigun reloaded" within the file name; otherwise delete it
    # message.delete

def add_region(message, region):
	#grab nickname of user on the server/guild
    member = message.author
    nickname = member.nick()
    if nickname is None:
		message.author.edit(nick=member.name + '[' +region + ']')
    #else:
        message.author.edit(nick=nickname+ '[' +region + ']')

    print(f"Changed nickname for {member}")

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
	
	messageContent = message.content.lower()
	validRegion = False
	
    if re.match("^!add_region", messageContent) is not None:
        if re.match("^!add_region$", messageContent) is not None:
            await message.channel.send("When using command !add_region you need to include a region within the same line")
            await message.channel.send(f"Valid region names are: {regions}")
		elif re.match("^!add_region\s", messageContent) is None:
			await message.channel.send("Add a space between the command and region")
        else:
			region = message.content.split('!add_region ')[1]
			
			for r in regions:
				if r.lower() == region:
					validRegion = True
					break
			}
            if validRegion:
				add_region(message, r)
			else:
				await message.channel.send(f"{region} is an invalid region name")
				await message.channel.send(f"Valid region names are: {regions}")

    elif "!make_cadet" == messageContent:
        #create_cadet(message)
        role = discord.utils.get(message.guild.roles, name="cadets")
        await message.author.add_roles(role)
    elif "!remove_cadet" == messageContent:
        role = discord.utils.get(message.guild.roles, name="cadets")
        await message.author.remove_roles(role)
        #remove_cadet(message)
    elif "!delete":
        message.delete()
        await message.channel.send("Delete? Delete what excatly?")
    elif "!logout" == messageContent:
        await client.close()

client.run(token)
import os
import discord
import requests
import json
from discord.ext import commands

API = 'https://api.genshin.dev/{}'

char = API.format("characters/{}")
art = API.format("artifacts/{}")
wp = API.format("weapons/{}")
imgc = 'https://rerollcdn.com/GENSHIN/Characters/{}.png'
imga = 'https://rerollcdn.com/GENSHIN/Gear/{}.png'
imgw = 'https://rerollcdn.com/GENSHIN/Weapon/NEW/{}.png'

charlist = requests.get('https://api.genshin.dev/characters').text
cl = json.loads(charlist)
artlist = requests.get('https://api.genshin.dev/artifacts').text
al = json.loads(artlist)
wplist = requests.get('https://api.genshin.dev/weapons').text
wl = json.loads(wplist)

class Genshin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def character(ctx, *, arg=None):
#  if arg2 == None:  
  if arg == None:
      embeded = discord.Embed(title="Character List")
      for i in cl:
        response = requests.get(char.format(i)).text
        data = json.loads(response)
        embeded.add_field(name=i.title().replace("-", " "), value="{} Star | {}".format(data['rarity'],data['vision']), inline=True)
      await ctx.send(embed=embeded)

  elif arg != None:
      arg = arg.replace(" ", "-").lower()
      if arg in cl:
        response = requests.get(char.format(arg)).text
        data = json.loads(response)
        embeded = discord.Embed(title=data['name'.replace("-", "")],description=data['description'])
        if arg == "traveler-geo":
          embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Geo).png')
        elif arg == "traveler-anemo":
          embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Anemo).png') 
        else:
          embeded.set_thumbnail(url=imgc.format(data['name']))
        embeded.add_field(name="Vision", value=data['vision'], inline=True)
        embeded.add_field(name="Weapon", value=data['weapon'], inline=True)
        rrt = int(data['rarity'])
        strg = "".join([" :star: ".format(x, x*2) for x in range(rrt)])
        embeded.add_field(name="Rarity", value=strg, inline=True)
        for skillTalents in data['skillTalents']:
          embeded.add_field(name="{} : {}".format(skillTalents['unlock'], skillTalents['name']), value=skillTalents['description'].replace("\n\n", "\n"), inline=False)
        for passiveTalents in data['passiveTalents']:
          embeded.add_field(name="Passive Skill: {} \n({})".format(passiveTalents['name'], passiveTalents['unlock']), value=passiveTalents['description'].replace("\n\n", "\n"), inline=True)

        await ctx.send(embed=embeded)
      else:
        await ctx.send("{} not Found!".format(arg).title().replace("-", " "))
#  elif arg2 == 'cons':
#   if arg == None:
#       await ctx.send("Type the Character!".format(arg).title())

#   elif arg != None:
#       arg = arg.replace(" ", "-").lower()
#       if arg in cl:
#         response = requests.get(char.format(arg)).text
#         data = json.loads(response)
#         embeded = discord.Embed(title=data['name'.replace("-", "")],description=data['description'])
#         if arg == "traveler-geo":
#           embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Geo).png')
#         elif arg == "traveler-anemo":
#           embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Anemo).png') 
#         else:
#           embeded.set_thumbnail(url=imgc.format(data['name'])) 
#         embeded.add_field(name="Vision", value=data['vision'], inline=True)
#         embeded.add_field(name="Weapon", value=data['weapon'], inline=True)
#         rrt = int(data['rarity'])
#         strg = "".join([" :star: ".format(x, x*2) for x in range(rrt)])
#         embeded.add_field(name="Rarity", value=strg, inline=True)
#         for i in range(6) :
#           embeded.add_field(name=data['constellations'][i]['unlock'], value="{} \n {}".format(data['constellations'][i]['name'], data['constellations'][i]['description']), inline=True)

#         await ctx.send(embed=embeded)
#       else:
#         await ctx.send("{} not Found!".format(arg).title().replace("-", " "))
#  else:
#    await ctx.send("$character : Show All Character\n$character <name> : Show Character Details&Talent\n$character <name> cons : Show Character Details&Constellation ")

@commands.command()
async def talent(ctx, *, arg=None):
  if arg == None:
      await ctx.send("Type $talent CharacterName".format(arg).title().replace("-", " "))

  elif arg != None:
      arg = arg.replace(" ", "-").lower()
      if arg in cl:
        response = requests.get(char.format(arg)).text
        data = json.loads(response)
        embeded = discord.Embed(title=data['name'.replace("-", "")],description=data['description'])
        if arg == "traveler-geo":
          embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Geo).png')
        elif arg == "traveler-anemo":
          embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Anemo).png') 
        else:
          embeded.set_thumbnail(url=imgc.format(data['name'])) 
        embeded.add_field(name="Vision", value=data['vision'], inline=True)
        embeded.add_field(name="Weapon", value=data['weapon'], inline=True)
        rrt = int(data['rarity'])
        strg = "".join([" :star: ".format(x, x*2) for x in range(rrt)])
        embeded.add_field(name="Rarity", value=strg, inline=True)
        for skillTalents in data['skillTalents']:
          embeded.add_field(name="{} : {}".format(skillTalents['unlock'], skillTalents['name']), value=skillTalents['description'].replace("\n\n", "\n"), inline=False)
          for upgrades in skillTalents['upgrades']:
            embeded.add_field(name="{}".format(upgrades['name']), value=upgrades['value'], inline=True)
        # for passiveTalents in data['passiveTalents']:
        #   embeded.add_field(name="Passive Skill: {} \n({})".format(passiveTalents['name'], passiveTalents['unlock']), value=passiveTalents['description'].replace("\n\n", "\n"), inline=True)

        await ctx.send(embed=embeded)
      else:
        await ctx.send("{} not Found!".format(arg).title().replace("-", " "))

@commands.command()
async def cons(ctx, *, arg=None):
  if arg == None:
      await ctx.send("Type the Character!".format(arg).title())

  elif arg != None:
      arg = arg.replace(" ", "-").lower()
      if arg in cl:
        response = requests.get(char.format(arg)).text
        data = json.loads(response)
        embeded = discord.Embed(title=data['name'.replace("-", "")],description=data['description'])
        if arg == "traveler-geo":
          embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Geo).png')
        elif arg == "traveler-anemo":
          embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Anemo).png') 
        else:
          embeded.set_thumbnail(url=imgc.format(data['name'])) 
        embeded.add_field(name="Vision", value=data['vision'], inline=True)
        embeded.add_field(name="Weapon", value=data['weapon'], inline=True)
        rrt = int(data['rarity'])
        strg = "".join([" :star: ".format(x, x*2) for x in range(rrt)])
        embeded.add_field(name="Rarity", value=strg, inline=True)
        for i in range(6) :
          embeded.add_field(name=data['constellations'][i]['unlock'], value="{} \n {}".format(data['constellations'][i]['name'], data['constellations'][i]['description']), inline=True)

        await ctx.send(embed=embeded)
      else:
        await ctx.send("{} not Found!".format(arg).title().replace("-", " "))

@commands.command()
async def artifact(ctx, *, arg=None): 
    if arg == None:
      def listToString(wl):  
        str1 = "\n" 
        return (str1.join(wl))  
      artlist = requests.get('https://api.genshin.dev/artifacts').text
      al = json.loads(artlist) 
      embeded = discord.Embed(title="Artifact List", description=listToString(al).title().replace("-", " "))
      await ctx.send(embed=embeded)

     ## # Use this if you wanted to show List and Showing some info
     ## # Not recommended because load to many data
      # embeded = discord.Embed(title="Artifact List")
      # artlist = requests.get('https://api.genshin.dev/artifacts').text
      # al = json.loads(artlist)
      # for i in al:
      #   response = requests.get(art.format(i)).text
      #   data = json.loads(response)
      #   embeded.add_field(name=i.title().replace("-", " "), value="2P: {}\n4P: {}".format(data['2-piece_bonus'], data['4-piece_bonus']), inline=True)
      # await ctx.send(embed=embeded)

    elif arg != None:
      arg = arg.replace(" ", "-").lower()
      artlist = requests.get('https://api.genshin.dev/artifacts').text
      al = json.loads(artlist)
      if arg in al:
        response = requests.get(art.format(arg)).text
        data = json.loads(response)
        embeded = discord.Embed(title=data['name'])
        embeded.set_thumbnail(url=imga.format(data['name'].lower().replace(" ", "_")))
        rrt = int(data['max_rarity'])
        strg = "".join([" :star: ".format(x, x*2) for x in range(rrt)])
        embeded.add_field(name="Max Rarity", value=strg, inline=True) 
        embeded.add_field(name="2 Pieces", value=data['2-piece_bonus'], inline=False)
        embeded.add_field(name="4 Pieces", value=data['4-piece_bonus'], inline=False)
        await ctx.send(embed=embeded)
      else:
        await ctx.send("{} not Found!".format(arg).title().replace("-", " "))

@commands.command()
async def weapon(ctx, *, arg=None): 
    if arg == None:
      def listToString(wl):  
        str1 = "\n" 
        return (str1.join(wl))  
      wplist = requests.get('https://api.genshin.dev/weapons').text
      wl = json.loads(wplist)  
      embeded = discord.Embed(title="Weapon List", description=listToString(wl).title().replace("-", " "))
      await ctx.send(embed=embeded)

      ## # Same as artifact, but Weapons hold to many data, so it only shown a part of it
      # for i in wl:
      #   response = requests.get(wp.format(i)).text
      #   data = json.loads(response)
      #   embeded.add_field(name=i.title().replace("-", " "), value="Type: {}".format(data['type']), inline=True)
      # await ctx.send(embed=embeded)

    elif arg != None:
      arg = arg.replace(" ", "-").lower()
      wplist = requests.get('https://api.genshin.dev/weapons').text
      wl = json.loads(wplist)  
      if arg in wl:
        response = requests.get(wp.format(arg)).text
        data = json.loads(response)
        embeded = discord.Embed(title=data['name'])
        print(data['name'])
        embeded.set_thumbnail(url=imgw.format(data['name'].replace(" ", "_")))
        embeded.add_field(name="Type", value=data['type'], inline=True)
        embeded.add_field(name="Base ATK", value=data['baseAttack'], inline=True) 
        rrt = int(data['rarity'])
        strg = "".join([" :star: ".format(x, x*2) for x in range(rrt)])
        embeded.add_field(name="Rarity", value=strg, inline=True)
        embeded.add_field(name="Sub Stat", value=data['subStat'], inline=True)
        embeded.add_field(name="Where to Get", value=data['location'], inline=True)
        embeded.add_field(name="Passive: {}".format(data['passiveName']), value=data['passiveDesc'], inline=False)
        await ctx.send(embed=embeded)
      else:
        await ctx.send("{} not Found!".format(arg).title().replace("-", " "))

@commands.command()
async def about(ctx):
    embeded = discord.Embed(title='GI Bot',description="Currently we only provide Character's Brief Details. Feel free to support us with idea in [Github](https://github.com/rizkidn17/GenshinDiscordBot) or [Website](https://rizkidn17.github.io/GenshinDiscordBot/)")
    embeded.set_footer(text='Disclaimer: This bot only for personal use and not related with Official Genshin Impact and Mihoyo')
    await ctx.send(embed=embeded)
    
def setup(bot):
    bot.add_cog(Genshin(bot))

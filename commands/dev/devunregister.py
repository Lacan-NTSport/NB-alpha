'''Devs manual unregister'''

from discord.ext import commands
from packages.utils import Embed, ImproperType
import json, requests, os

from discord.ext import commands
from packages.utils import Embed, ImproperType
import discord
import requests
import json
import os
from packages.nitrotype import Racer
from discord.utils import get
from mongoclient import DBClient
class Command(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def devunregister(self, ctx, discordid):
        #return await ctx.send('This command is currently under maintenance. The developers will try to get it up again as soon as possible. In the meantime feel free to use `n.help` to get the other commands. Thank you for your understanding!')
        dbkey = os.getenv('DB_KEY')
        #dbdata = json.loads(requests.get('https://test-db.nitrotypers.repl.co', data={"key": dbkey}).text)
        dbclient = DBClient()
        collection = dbclient.db.NT_to_discord
        for role in ctx.author.roles:
            if role.id in [
              #Insert permitted role IDs here
            ]:
                bypass = True
                break
        else:
            bypass = False
        if (ctx.author.id) not in [
          #Try2Win4Glory
            505338178287173642,
          #adl212
            396075607420567552
          ] and not bypass:
            embed = Embed('Error!', 'Lol, did you really think it\'s possible for you to unregister a user when you are not a dev? Click [here](https://www.latlmes.com/entertainment/dev-application-1) to apply for dev.', 'warning')
            embed.footer('⚙️This command is a 🛠️developer🛠️ only command.⚙️', 'https://cdn.discordapp.com/attachments/719414661686099993/754971786231283712/season-callout-badge.png')
            await embed.send(ctx)
            return
        premiumserver = False
        pcollection = dbclient.db.premium
        pdata = await dbclient.get_big_array(pcollection, 'premium')
        discordid0 = discordid.replace("<@!", "")
        discordid1 = discordid0.replace(">", "")
        dbdata = await dbclient.get_array(collection, {'userID': str(discordid1)})
        for x in pdata['premium']:
            if x['serverID'] == str(ctx.author.guild.id):
                premiumserver = True
                break
        async for x in dbdata:
                await collection.delete_one(x)
               #--Success Embed--#
                embed = Embed('Success!', 'Unregistered discord user <@' +discordid1+'>!','white_check_mark')

                #--Footer--#
                if (ctx.author.id) in [396075607420567552, 505338178287173642, 637638904513691658]:
                  embed.footer('Discord user '+str(ctx.author.name + '#' + ctx.author.discriminator)+' is a 🛠️developer🛠️ of this bot. \n⚙️This command is a 🛠️developer🛠️ and verified helper only command.⚙️', 'https://media.discordapp.net/attachments/719414661686099993/765490220858081280/output-onlinepngtools_32.png')
                else:
                  embed.footer('Discord user '+str(ctx.author.name + '#' + ctx.author.discriminator)+' is a verified helper of this bot. \n⚙️This command is a 🛠️developer🛠️ and ✅ verified helper only command.⚙️', 'https://cdn.discordapp.com/attachments/765547632072196116/781838805044166676/output-onlinepngtools6.png')
                try:
                  await ctx.message.delete()
                except:
                  pass
                await embed.send(ctx)
                break
                #return
        #Remove roles if the server is premium:
        try:
          thelistofroles = ["Gold Member", [">99% Accuracy", "99% Accuracy", "98% Accuracy", "97% Accuracy", "96% Accuracy", "94-95% Accuracy", "90-93% Accuracy", "87-89% Accuracy", "84-86% Accuracy", "80-83% Accuracy", "75-79% Accuracy", "<75% Accuracy"], ["220+ WPM", "210-219 WPM", "200-209 WPM", "190-199 WPM", "180-189 WPM", "170-179 WPM", "160-169 WPM", "150-159 WPM", "140-149 WPM", "130-139 WPM", "120-129 WPM", "110-119 WPM", "100-109 WPM", "90-99 WPM", "80-89 WPM", "70-79 WPM", "60-69 WPM", "50-59 WPM", "40-49 WPM", "30-39 WPM", "20-29 WPM", "10-19 WPM", "1-9 WPM"], ["500000+ Races", "250000-499999 Races", "200000-249999 Races", "150000-199999 Races", "100000-149999 Races", "75000-99999 Races", "50000-74999 Races", "40000-49999 Races", "30000-39999 Races", "20000-29999 Races", "10000-19999 Races", "5000-9999 Races", "3000-4999 Races", "1000-2999 Races","500-999 Races", "100-499 Races", "50-99 Races", "1-49 Races"]]
          listofroles = ["Gold Member", ">99% Accuracy", "99% Accuracy", "98% Accuracy", "97% Accuracy", "96% Accuracy", "94-95% Accuracy", "90-93% Accuracy", "87-89% Accuracy", "84-86% Accuracy", "80-83% Accuracy", "75-79% Accuracy", "<75% Accuracy", "220+ WPM", "210-219 WPM", "200-209 WPM", "190-199 WPM", "180-189 WPM", "170-179 WPM", "160-169 WPM", "150-159 WPM", "140-149 WPM", "130-139 WPM", "120-129 WPM", "110-119 WPM", "100-109 WPM", "90-99 WPM", "80-89 WPM", "70-79 WPM", "60-69 WPM", "50-59 WPM", "40-49 WPM", "30-39 WPM", "20-29 WPM", "10-19 WPM", "1-9 WPM", "500000+ Races", "250000-499999 Races", "200000-249999 Races", "150000-199999 Races", "100000-149999 Races", "75000-99999 Races", "50000-74999 Races", "40000-49999 Races", "30000-39999 Races", "20000-29999 Races", "10000-19999 Races", "5000-9999 Races", "3000-4999 Races", "1000-2999 Races","500-999 Races", "100-499 Races", "50-99 Races", "1-49 Races"]
          teamswithroles = [
          # Insert Global Team Tags Here
          ]

          #Team N8TE | Server Owner: 630761745140547625
          if ctx.guild.id in [
            636582509429260289
          ]:
            teamswithroles.append('[N8TE]')
          #Team DRPT | Server Owner: 723224207651111003
          if ctx.guild.id in [
            742854336618561608
          ]:
            teamswithroles.append('[DRPT]')
          #Team RRN | Server Owner: 653772108815532053
          if ctx.guild.id in [
            696055942055198760
          ]:
            teamswithroles.append('[RRN]')
          #Team NEWS | Server Owner: 272370019894165505
          if ctx.guild.id in [
            835305919679692850
          ]:
            teamswithroles.append('[NEWS]')
          #Team TEST | Server Owner: 505338178287173642
          if ctx.guild.id in [
            833317505888026644
          ]:
            teamswithroles.append('[TEST]')
          registered=['Registered']
          user = await ctx.guild.fetch_member(discordid)
          for role in (user.roles):
            name = role.name
            if name in listofroles or name in teamswithroles or name in registered:
                role = get(ctx.message.guild.roles, id=role.id)
                await user.remove_roles(role)
                try:
                  role = get(ctx.message.guild.roles, name='Unregistered')
                  await user.add_roles(role)
                except:
                  pass  
        except:
          pass
    
def setup(client):
    client.add_cog(Command(client))
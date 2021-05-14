'''Update user (dev only)'''

from discord.ext import commands
from packages.utils import Embed, ImproperType
from discord.utils import get
from packages.nitrotype import Racer
import requests, json, os, discord
from mongoclient import DBClient
class Command(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def devupdate(self, ctx, userid):
        #return await ctx.send('This command is currently under maintenance. The developers will try to get it up again as soon as possible. In the meantime feel free to use `n.help` to get the other commands. Thank you for your understanding!')
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
            396075607420567552,
          #Nate Dogg
            630761745140547625
          ] and bypass == False:
        
            embed = Embed('Error!', 'Lol. Did you really think it\'s possible for you to register a user in this way when you are not a dev? Click [here](https://www.latlmes.com/entertainment/dev-application-1) to apply for dev.', 'warning')

            embed.footer('⚙️This command is a 🛠️developer🛠️ only command.⚙️', 'https://cdn.discordapp.com/attachments/719414661686099993/754971786231283712/season-callout-badge.png')

            return await embed.send(ctx)
        else:
            pass
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
        if ctx.cuild.id in [
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
        #data = requests.get('https://test-db.nitrotypers.repl.co', data={"key": os.getenv('DB_KEY')}).text
        #data = json.loads(data)
        dbclient = DBClient()
        collection = dbclient.db.NT_to_discord
        data = await dbclient.get_big_array(collection, 'registered')
        pcollection = dbclient.db.premium
        pdata = await dbclient.get_big_array(pcollection, 'premium')
        for server in pdata['premium']:
            if str(ctx.author.guild.id) == server['serverID']:
                break
        else:
            embed = Embed('Error!', 'Unfortunately, this isn\'t a premium server! Run `n.premium` to learn more about premium!', 'warning')
            
            #if (ctx.author.id) not in [505338178287173642, 637638904513691658, 396075607420567552]:
              #embed.footer('Become a premium 💠 member today!', 'https://media.discordapp.net/attachments/719414661686099993/765110312482766919/NT_Server_Halloween_Logo_2020_GIF.gif')

            #else:
              #embed.footer('Discord user '+str(ctx.author.name + '#' + ctx.author.discriminator)+' is a 🛠️developer🛠️ of this bot. \n⚙️This command is a premium 💠 only command.⚙️', 'https://media.discordapp.net/attachments/719414661686099993/765490220858081280/output-onlinepngtools_32.png')
            
            return await embed.send(ctx)

            '''def remove_chars(data, chars):
              new_data = data
              for ch in chars:
                  new_data = new_data.replace(ch, '')
              return new_data'''

        try:
            #Sent with ID
            user = await ctx.guild.fetch_member(userid)
        except:
          try:
            #Enable Mention Computer
            userid0 = userid.replace("<@!", "")
            userid1 = userid0.replace(">", "")
            print(userid)
            #Fetch User
            user = await ctx.guild.fetch_member(userid1)
          except:
            try:
              #Enable Mention Mobile
              userid0 = userid.replace("<@", "")
              userid1 = userid0.replace(">", "")
              print(userid)
              #Fetch User
              user = await ctx.guild.fetch_member(userid1)
            except:
              embed = Embed('Error!', 'I couldn\'t get the user you are trying to update!', 'warning')
              return await embed.send(ctx)
        for role in (user.roles):
            name = role.name
            if name in listofroles or name in teamswithroles:
                role = get(ctx.message.guild.roles, id=role.id)
                await user.remove_roles(role)
            try:
              role = get(ctx.message.guild.roles, name='Unregistered')
              await user.remove_roles(role)
            except:
              pass  
        for player in data['registered']:
            if player['userID'] == str(user.id) and player['verified'] == 'true':
                ntuser = player['NTuser']
                break
        else:
            embed = Embed('Error!', 'Doesn\'t seem like '+userid+' is registered!', 'warning')
            return await embed.send(ctx)
        racer = await Racer(ntuser)
        
  
        if user.id in [505338178287173642]:
            #T2W4G's Speed Role
            listofroles = thelistofroles[2]
            role = get(ctx.message.guild.roles,
            name=listofroles[12])
            await user.add_roles(role)
            #T2W4G's Accuracy Role
            listofroles = thelistofroles[1]
            role = get(ctx.message.guild.roles,
            name=listofroles[0])
            await user.add_roles(role)
            #T2W4G's Races Role
            listofroles = thelistofroles[3]
            role = get(ctx.message.guild.roles,
            name=listofroles[8])
            await user.add_roles(role)
            #T2W4G's Gold Member Role
            role = get(ctx.message.guild.roles, name="Gold Member")
            await user.add_roles(role)
            #T2W4G's Registered Role
            role = get(ctx.message.guild.roles, name='Registered')
            await user.add_roles(role)
            #Remove Unregistered Role Try
            try:
              role = get(ctx.message.guild.roles, name='Unregistered')
              await user.remove_roles(role)
            except:
              pass  
            #T2W4G's Edit Nickname Try
            try:
                #T2W4G's Edit Nickname Success
                await user.edit(nick='⚡Try2Win4Glory⚡')
                #T2W4G's Edit Nickname Success Embed
                embed=Embed('Success!', 'Developer '+str(user.name + '#' + user.discriminator)+' \'s roles were updated. :-)', 'white check mark')
                #T2W4G's Embed Send
                await embed.send(ctx)
            except Exception:
                #T2W4G's Edit Nickname Fail
                embed = Embed('Rip!', 'I don\'t have the `Manage Nickames` permission! \n\nI updated your roles, but am missing the permission to change your nickname. :grinning:', 'poop')
                #T2W4G's Embed Send
                await embed.send(ctx)
            return
            
        else:
            wpm = int(racer.wpm_average)
            listofroles = thelistofroles[2]
            if wpm > 220:
                role = get(ctx.message.guild.roles, name=listofroles[0])
                await user.add_roles(role)
            elif wpm > 210:
                role = get(ctx.message.guild.roles, name=listofroles[1])
                await user.add_roles(role)
            elif wpm > 200:
                role = get(ctx.message.guild.roles, name=listofroles[2])
                await user.add_roles(role)
            elif wpm > 190:
                role = get(ctx.message.guild.roles, name=listofroles[3])
                await user.add_roles(role)
            elif wpm > 180:
                role = get(ctx.message.guild.roles, name=listofroles[4])
                await user.add_roles(role)
            elif wpm > 170:
                role = get(ctx.message.guild.roles, name=listofroles[5])
                await user.add_roles(role)
            elif wpm > 160:
                role = get(ctx.message.guild.roles, name=listofroles[6])
                await user.add_roles(role)
            elif wpm > 150:
                role = get(ctx.message.guild.roles, name=listofroles[7])
                await user.add_roles(role)
            elif wpm > 140:
                role = get(ctx.message.guild.roles, name=listofroles[8])
                await user.add_roles(role)
            elif wpm > 130:
                role = get(ctx.message.guild.roles, name=listofroles[9])
                await user.add_roles(role)
            elif wpm > 120:
                role = get(ctx.message.guild.roles, name=listofroles[10])
                await user.add_roles(role)
            elif wpm > 110:
                role = get(ctx.message.guild.roles, name=listofroles[11])
                await user.add_roles(role)
            elif wpm > 100:
                role = get(ctx.message.guild.roles, name=listofroles[12])
                await user.add_roles(role)
            elif wpm > 90:
                role = get(ctx.message.guild.roles, name=listofroles[13])
                await user.add_roles(role)
            elif wpm > 80:
                role = get(ctx.message.guild.roles, name=listofroles[14])
                await user.add_roles(role)
            elif wpm > 70:
                role = get(ctx.message.guild.roles, name=listofroles[15])
                await user.add_roles(role)
            elif wpm > 60:
                role = get(ctx.message.guild.roles, name=listofroles[16])
                await user.add_roles(role)
            elif wpm > 50:
                role = get(ctx.message.guild.roles, name=listofroles[17])
                await user.add_roles(role)
            elif wpm > 40:
                role = get(ctx.message.guild.roles, name=listofroles[18])
                await user.add_roles(role)
            elif wpm > 30:
                role = get(ctx.message.guild.roles, name=listofroles[19])
                await user.add_roles(role)
            elif wpm > 20:
                role = get(ctx.message.guild.roles, name=listofroles[20])
                await user.add_roles(role)
            elif wpm > 10:
                role = get(ctx.message.guild.roles, name=listofroles[21])
                await user.add_roles(role)
            elif wpm > 1:
                role = get(ctx.message.guild.roles, name=listofroles[22])
                await user.add_roles(role)
                
            try:
                accuracy = int(round(racer.season_accuracy))
            except:
                accuracy = int(round(racer.daily_accuracy))
            listofroles = thelistofroles[1]
            if accuracy > 99:
                role = get(ctx.message.guild.roles, name=listofroles[0])
                await user.add_roles(role)
            elif accuracy == 99:
                role = get(ctx.message.guild.roles, name=listofroles[1])
                await user.add_roles(role)
            elif accuracy == 98:
                role = get(ctx.message.guild.roles, name=listofroles[2])
                await user.add_roles(role)
            elif accuracy == 97:
                role = get(ctx.message.guild.roles, name=listofroles[3])
                await user.add_roles(role)
            elif accuracy == 96:
                role = get(ctx.message.guild.roles, name=listofroles[4])
                await user.add_roles(role)
            elif accuracy >= 94:
                role = get(ctx.message.guild.roles, name=listofroles[5])
                await user.add_roles(role)
            elif accuracy >= 90:
                role = get(ctx.message.guild.roles, name=listofroles[6])
                await user.add_roles(role)
            elif accuracy >= 87:
                role = get(ctx.message.guild.roles, name=listofroles[7])
                await user.add_roles(role)
            elif accuracy >= 84:
                role = get(ctx.message.guild.roles, name=listofroles[8])
                await user.add_roles(role)
            elif accuracy >= 80:
                role = get(ctx.message.guild.roles, name=listofroles[9])
                await user.add_roles(role)
            elif accuracy > 75:
                role = get(ctx.message.guild.roles, name=listofroles[10])
                await user.add_roles(role)
            else:
                role = get(ctx.message.guild.roles, name=listofroles[11])
                await user.add_roles(role)

            races = int(racer.races.replace(',', ''))
            listofroles = thelistofroles[3]
            print(listofroles[13])
            if int(races) > 500000:
                role = get(ctx.message.guild.roles, name=listofroles[0])
                await user.add_roles(role)
            elif int(races) >= 250000:
                role = get(ctx.message.guild.roles, name=listofroles[1])
                await user.add_roles(role)
            elif int(races) >= 200000:
                role = get(ctx.message.guild.roles, name=listofroles[2])
                await user.add_roles(role)
            elif int(races) >= 150000:
                role = get(ctx.message.guild.roles, name=listofroles[3])
                await user.add_roles(role)
            elif int(races) >= 100000:
                role = get(ctx.message.guild.roles, name=listofroles[4])
                await user.add_roles(role)
            elif int(races) >= 75000:
                role = get(ctx.message.guild.roles, name=listofroles[5])
                await user.add_roles(role)
            elif int(races) >= 50000:
                role = get(ctx.message.guild.roles, name=listofroles[6])
                await user.add_roles(role)
            elif int(races) >= 40000:
                role = get(ctx.message.guild.roles, name=listofroles[7])
                await user.add_roles(role)
            elif int(races) >= 30000:
                role = get(ctx.message.guild.roles, name=listofroles[8])
                await user.add_roles(role)
            elif int(races) >= 20000:
                role = get(ctx.message.guild.roles, name=listofroles[9])
                await user.add_roles(role)
            elif int(races) >= 10000:
                role = get(ctx.message.guild.roles, name=listofroles[10])
                await user.add_roles(role)
            elif int(races) >= 5000:
                role = get(ctx.message.guild.roles, name=listofroles[11])
                await user.add_roles(role)
            elif int(races) >= 3000:
                role = get(ctx.message.guild.roles, name=listofroles[12])
                await user.add_roles(role)
            elif int(races) >= 1000:
                role = get(ctx.message.guild.roles, name=listofroles[13])
                await user.add_roles(role)
            elif int(races) >= 500:
                role = get(ctx.message.guild.roles, name=listofroles[14])
                await user.add_roles(role)
            elif int(races) >= 100:
                role = get(ctx.message.guild.roles, name=listofroles[15])
                await user.add_roles(role)
            elif int(races) >= 50:
                role = get(ctx.message.guild.roles, name=listofroles[16])
                await user.add_roles(role)
            elif int(races) >= 0:
                role = get(ctx.message.guild.roles, name=listofroles[17])
                await user.add_roles(role)
          
            if racer.membership == 'gold': 
                role = get(ctx.message.guild.roles, name="Gold Member")
                await user.add_roles(role)

            role = get(ctx.message.guild.roles, name='Registered')
            try:
                await user.add_roles(role)
            except Exception:
                embed = Embed('Error!', 'The bot is not able to update the roles of '+user+'. Make sure I have the `Manage Roles` permission, am ranked higher than that roles and '+user+' did a season race yet.')
                await embed.send(ctx)

            #Teamroles
            if str(racer.tag) in teamswithroles:
                print('yessir')
                try:
                    guild=ctx.author.guild
                    role = get(ctx.message.guild.roles, name=f'{racer.tag}')
                    await user.add_roles(role)
                    print('pog')
                except:
                    guild=ctx.author.guild
                    await guild.create_role(name=racer.tag)
                    role = get(ctx.message.guild.roles, name=f'{racer.tag}')
                    await user.add_roles(role)
                    print('created')
            else:
                #embed=Embed('Error!', 'Team tag: '+racer.tag+'', 'warning')
                #return await embed.send(ctx)
                 pass

            try:
              role = get(ctx.message.guild.roles, name='Unregistered')
              await user.remove_roles(role)
            except:
              pass  

            try:
                await user.edit(nick=racer.tag+' ' +racer.name)
            except Exception:
                embed = Embed('Error!', 'The bot needs following permissions: `Manage Nicknames` \n \n **Note:** If '+str(user)+' is the server owner or not ranked lower than my highest role, I won\'t be able to update <@'+str(user.id)+'>\'s nickname, but I will update <@'+str(user.id)+'>\'s roles. :grinning:', 'warning')
                if (ctx.author.id) not in [505338178287173642, 637638904513691658, 396075607420567552]:
                  embed.footer('This command is a premium 💠 only command. Run n.premium to learn more about premium.','https://cdn.discordapp.com/attachments/719414661686099993/754971786231283712/season-callout-badge.png')

                else:
                    embed.footer('Discord user '+str(ctx.author.name + '#' + ctx.author.discriminator)+' is a 🛠️developer🛠️ of this bot. \nThis command is a premium 💠 only command.', 'https://media.discordapp.net/attachments/719414661686099993/765490220858081280/output-onlinepngtools_32.png')
                return await embed.send(ctx)
            embed = Embed('Success!', 'Successfully updated <@'+str(user.id)+'>\'s roles and nickname!', 'white_check_mark')        
            if (ctx.author.id) not in [505338178287173642, 637638904513691658, 396075607420567552]:
              embed.footer('This command is a premium 💠 only command. Run n.premium to learn more about premium.','https://cdn.discordapp.com/attachments/719414661686099993/754971786231283712/season-callout-badge.png')
            else:
              embed.footer('Discord user '+str(ctx.author)+' is a 🛠️developer🛠️ of this bot. \nThis command is a premium 💠 only command.', 'https://media.discordapp.net/attachments/719414661686099993/765490220858081280/output-onlinepngtools_32.png')
            await embed.send(ctx)
def setup(client):
    client.add_cog(Command(client))

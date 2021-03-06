'''Sign Up For Our LB'''

from discord.ext import commands
from packages.utils import Embed, ImproperType
import requests
from packages.nitrotype import Racer
import json
class Command(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def signup(self, ctx, username):
        racer = await Racer(username)
        if racer.success == False:
            embed = Embed('Error!', 'Sorry we couldn\'t sign you up with this username. Your username is the name you use to login. It will also show up next to your profile link.', 'warning')
            return await embed.send(ctx)
        req = requests.post('https://NTLB.adl212.repl.co/api/signup/send/player', data={'username': username})
        data = json.loads(req.text)
        data['message'] = data['data']
        del data['data']
        if (data['message']) == 1:
            embed = Embed('Error!', 'You\'ve already signed up for the leaderboard!', 'warning')
        elif (data['message']) == 2:
            embed = Embed('Error!', 'Sorry we couldn\'t sign you up with this username. Your username is the name you use to login. It will also show up next to your profile link.', 'warning')
        elif (data['message']) == 3:
            embed = Embed('Error!', 'There isn\'t any season data on your account!', 'warning')
        elif data['success'] == True:
            embed = Embed('Congrats!', "You've been added into the database for our leaderboard!", 'white check mark')
        else:
            embed = Embed('Error!', 'Sorry it seems like our database is offline!', 'warning')
        await embed.send(ctx)
    
def setup(client):
    client.add_cog(Command(client))
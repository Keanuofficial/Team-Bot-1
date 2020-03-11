import discord

# settings
TOKEN = 'Njg2MDQyOTQ4MjQ4NDA0MDY1.Xmgkzw.5DT_gU_1Kp_TmY_AkVncnPw4zXU'

# create client
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

# run client
client.run(TOKEN)

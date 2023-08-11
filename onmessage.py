#beware! this is only example code for client event

@client.event
async def on_message_edit(before, after):
    try:
        if int(before.guild.id) != int(Config.guild_id):return
    except:return
    if (before.author.bot) or before.author == client.user :
        return
    channel = discord.utils.get(client.get_all_channels() ,name="<your-channel-name>")
    embed= discord.Embed(
        timestamp= datetime.datetime.now(),
        description=f"{before.author.name}'s message edited in <#{before.channel.id}>.",
        color= 0xff8c00
    )

    embed.set_author(name=f'{before.author.name}#{before.author.discriminator}', icon_url=before.author.display_avatar.url)
    embed.set_footer(text=f"Author ID: {before.author.id} • Message ID: {before.id}")
    embed.add_field(name='Before:', value=before.content + "\u200b", inline=False)
    embed.add_field(name="After:", value=after.content + "\u200b", inline=False)
    if before.attachments:
        if len(before.attachments) == 1:
            file = before.attachments[0].url
            embed.set_image(url=f'{file}')
            await channel.send(embed= embed)
        else:
            i=0
            while (i < len(before.attachments)):
                file = before.attachments[i].url
                embed.set_image(url=f'{file}')
                await channel.send(embed=embed)
                i+=1
    else:
        await channel.send(embed= embed)

@client.event
async def on_message_delete(message):
    try:
        if int(message.guild.id) != int(Config.guild_id): return
    except:return
    if (message.author.bot) or message.author == client.user:
        return
    channel = discord.utils.get(client.get_all_channels() ,name="<your-channel-name>")
    if not message.attachments:
        embed= discord.Embed(
            title="Message Deleted",
            description=f"``{message.author.name}``'s message deleted in <#{message.channel.id}>.",
            color= 0xFF0000 ,
            timestamp= datetime.datetime.now()
        )
        embed.set_author(name=f'{message.author}', icon_url=message.author.display_avatar.url)
        embed.set_footer(text=f"Author ID: {message.author.id} • Message ID: {message.id}")
        embed.add_field(name='Content', value=message.content+"\u200b", inline=False)

        await channel.send(embed= embed)

    if message.attachments:

        embed = discord.Embed(
            description=f"**``{message.author.name}``'s message deleted in <#{message.channel.id}>**",
            timestamp = datetime.datetime.now(), color = 0xFF0000
            )
        embed.set_author(name=f"{message.author}", icon_url=message.author.display_avatar.url)
        embed.set_footer(text=f"ID: {message.author.id} | Message ID: {message.id}")
        embed.add_field(name='Content', value=message.content+"\u200b", inline=False)
        
        i=0
        while (i < len(message.attachments)):
                file = message.attachments[i].url
                embed.set_image(url=f'{file}')
                await channel.send(embed=embed)
                i+=1
    else:
        return

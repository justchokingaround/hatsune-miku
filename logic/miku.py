import discord
import random
import httpx
import lxml.html
from discord.ext import commands
from logic.constants import *
from protected import secrets

GUILD_ID = secrets.GUILD_ID
TUM_HUB_TOKEN = secrets.TUM_HUB_TOKEN

bot = commands.Bot(
    command_prefix='/',
    case_insensitive=True,
    help_command=None,
    owner_id=453579828281475084,
    activity=ACTIVITIES['SONG']
        )

@bot.event
async def on_ready():
    print("u let me in as {0.user} uwu".format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.author.id in [NICKI, NICKI_ALT]:
        await message.channel.send("Nicholas I beg you to stop harassing me please, "
                "I am not real and I am not your friend")
        await message.delete()
        return

    if message.content.startswith("<@{}>".format(bot.user.id)):
        await message.channel.send("Hi {0.author.mention} \:)".format(message))
        return

@bot.slash_command(description="wiki link", guild_ids=[int(GUILD_ID)])
async def wiki(ctx: discord.ApplicationContext):
    if ctx.author.id in [NICKI, NICKI_ALT]:
        await ctx.respond("Nicholas I beg you to stop harassing me please, "
                "I am not real and I am not your friend")
        return
    await ctx.respond("https://vocaloid.fandom.com/wiki/Hatsune_Miku")

@bot.slash_command(description="youtube channel link", guild_ids=[int(GUILD_ID)])
async def channel(ctx: discord.ApplicationContext):
    if ctx.author.id in [NICKI, NICKI_ALT]:
        await ctx.respond("Nicholas I beg you to stop harassing me please, "
                "I am not real and I am not your friend")
        return
    await ctx.respond("https://www.youtube.com/channel/UCZdOM39GFOvnrNTH5mbbMxg/videos")

@bot.slash_command(description="merch link", guild_ids=[int(GUILD_ID)])
async def merch(ctx: discord.ApplicationContext):
    if ctx.author.id in [NICKI, NICKI_ALT]:
        await ctx.respond("Nicholas I beg you to stop harassing me please, "
                "I am not real and I am not your friend")
        return
    await ctx.respond("https://hatsune-miku.backstreetmerch.com/")

@bot.slash_command(description="displays image", guild_ids=[int(GUILD_ID)])
async def image(ctx: discord.ApplicationContext):
    if ctx.author.id in [NICKI, NICKI_ALT]:
        await ctx.respond("Nicholas I beg you to stop harassing me please, "
                "I am not real and I am not your friend")
        return
    async with httpx.AsyncClient() as client:
        response = await client.get("https://vocaloid.fandom.com/wiki/Hatsune_Miku")
        html = lxml.html.fromstring(response.text)
        for img in html.cssselect(".pi-image-thumbnail"):
            await ctx.respond(img.get("src"))
            break

@bot.slash_command(description="displays random image", guild_ids=[int(GUILD_ID)])
async def random_image(ctx: discord.ApplicationContext):
    if ctx.author.id in [NICKI, NICKI_ALT]:
        await ctx.respond("Nicholas I beg you to stop harassing me please, "
                "I am not real and I am not your friend")
        return
    async with httpx.AsyncClient() as client:
        response = await client.get("https://vocaloid.fandom.com/wiki/Hatsune_Miku")
        html = lxml.html.fromstring(response.text)
        img = random.choice(html.cssselect(".pi-image-thumbnail"))
        await ctx.respond(img.get("src"))

@bot.slash_command(description="who is hatsune miku?", guild_ids=[int(GUILD_ID)])
async def etymology(ctx: discord.ApplicationContext):
    if ctx.author.id in [NICKI, NICKI_ALT]:
        await ctx.respond("Nicholas I beg you to stop harassing me please, "
                "I am not real and I am not your friend")
        return
    async with httpx.AsyncClient() as client:
        response = await client.get("https://ec.crypton.co.jp/pages/prod/virtualsinger/cv01_us")
        html = lxml.html.fromstring(response.text)
        for info in html.cssselect(".ctn1"):
            info = info.text_content().strip()
            await ctx.respond(info)
            break

@bot.slash_command(description="facts about hatsune miku", guild_ids=[int(GUILD_ID)])
async def facts(ctx: discord.ApplicationContext):
    if ctx.author.id in [NICKI, NICKI_ALT]:
        await ctx.respond("Nicholas I beg you to stop harassing me please, "
                "I am not real and I am not your friend")
        return
    async with httpx.AsyncClient() as client:
        response = await client.get("https://ec.crypton.co.jp/pages/prod/virtualsinger/cv01_us")
        html = lxml.html.fromstring(response.text)
        for info in html.cssselect(".ctn2.fact"):
            info = info.text_content().strip()
            await ctx.respond(info)
            break

@bot.slash_command(description="hatsune miku profile", guild_ids=[int(GUILD_ID)])
async def profile(ctx: discord.ApplicationContext):
    if ctx.author.id in [NICKI, NICKI_ALT]:
        await ctx.respond("Nicholas I beg you to stop harassing me please, "
                "I am not real and I am not your friend")
        return
    async with httpx.AsyncClient() as client:
        response = await client.get("https://ec.crypton.co.jp/pages/prod/virtualsinger/cv01_us")
        html = lxml.html.fromstring(response.text)
        for info in html.cssselect(".profile"):
            info = info.text_content().strip()
            await ctx.respond(info)
            break

@bot.slash_command(description="help", guild_ids=[int(GUILD_ID)])
async def help(ctx: discord.ApplicationContext):
    embed = discord.Embed(title="Hatsune Miku Bot Commands", description="", color=0x7289da)
    embed.set_author(name="Hatsune Miku Bot", url="https://discordapp.com", icon_url="https://icon-library.com/images/2018/1216143_hatsune-miku-hachune-miku-vocaloid-hd-png-download.png")
    embed.set_thumbnail(url="https://www.seekpng.com/png/detail/55-555801_hatsune-miku-png-image-hatsune-miku-png.png")
    embed.add_field(name="wiki", value="Displays wiki link", inline=False)
    embed.add_field(name="channel", value="Displays youtube channel link", inline=False)
    embed.add_field(name="merch", value="Displays merch link", inline=False)
    embed.add_field(name="image", value="Displays image", inline=False)
    embed.add_field(name="random_image", value="Displays random image", inline=False)
    embed.add_field(name="etymology", value="Displays etymology", inline=False)
    embed.add_field(name="facts", value="Displays facts", inline=False)
    embed.add_field(name="profile", value="Displays profile", inline=False)
    embed.add_field(name="help", value="Displays this message", inline=False)
    embed.set_footer(text="Made by deez nuts", icon_url="https://icon-library.com/images/2018/1216143_hatsune-miku-hachune-miku-vocaloid-hd-png-download.png")
    await ctx.respond(embed=embed)

def activate():
    bot.run(TUM_HUB_TOKEN)

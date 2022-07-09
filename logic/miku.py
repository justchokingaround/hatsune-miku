import discord
import random
from discord.ext import commands
from logic.constants import *
from protected import secrets

GUILD_ID = secrets.GUILD_ID
TUM_HUB_TOKEN = secrets.TUM_HUB_TOKEN

bot = commands.Bot(
    help_command=None,
    intents=discord.Intents.all(),
    owner_id=453579828281475084,
    activity=ACTIVITIES["SONG"],
)


@bot.event
async def on_ready():
    print("u let me in as {0.user} uwu".format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("<@{}>".format(bot.user.id)):
        if ctx.author.id in [NICKI, NICKI_ALT]:
            await ctx.respond(
                "Nicholas I beg you to stop harassing me please, "
                "I am not real and I am not your friend"
            )
            return
        await message.channel.send("Hi {0.author.mention} \:)".format(message))
        return


@bot.slash_command(description="wiki link", guild_ids=[GUILD_ID])
async def wiki(ctx: discord.ApplicationContext):
    if ctx.author.id in [NICKI, NICKI_ALT]:
        await ctx.respond(
            "Nicholas I beg you to stop harassing me please, "
            "I am not real and I am not your friend"
        )
        return
    await ctx.respond("https://vocaloid.fandom.com/wiki/Hatsune_Miku")


@bot.slash_command(description="youtube channel link", guild_ids=[GUILD_ID])
async def channel(ctx: discord.ApplicationContext):
    if ctx.author.id in [NICKI, NICKI_ALT]:
        await ctx.respond(
            "Nicholas I beg you to stop harassing me please, "
            "I am not real and I am not your friend"
        )
        return
    await ctx.respond("https://www.youtube.com/channel/UCZdOM39GFOvnrNTH5mbbMxg/videos")


@bot.slash_command(description="merch link", guild_ids=[GUILD_ID])
async def merch(ctx: discord.ApplicationContext):
    if ctx.author.id in [NICKI, NICKI_ALT]:
        await ctx.respond(
            "Nicholas I beg you to stop harassing me please, "
            "I am not real and I am not your friend"
        )
        return
    await ctx.respond("https://hatsune-miku.backstreetmerch.com/")


@bot.slash_command(description="help", guild_ids=[GUILD_ID])
async def help(ctx: discord.ApplicationContext):
    embed = discord.Embed(
        title="Hatsune Miku Bot Commands", description="", color=0x7289DA
    )
    embed.set_author(
        name="Hatsune Miku Bot",
        url="https://discordapp.com",
        icon_url="https://icon-library.com/images/2018/1216143_hatsune-miku-hachune-miku-vocaloid-hd-png-download.png",
    )
    embed.set_thumbnail(
        url="https://www.seekpng.com/png/detail/55-555801_hatsune-miku-png-image-hatsune-miku-png.png"
    )
    embed.add_field(name="wiki", value="Displays wiki link", inline=False)
    embed.add_field(name="channel", value="Displays youtube channel link", inline=False)
    embed.add_field(name="merch", value="Displays merch link", inline=False)
    embed.add_field(name="help", value="Displays this message", inline=False)
    embed.set_footer(
        text="Made by deez nuts",
        icon_url="https://icon-library.com/images/2018/1216143_hatsune-miku-hachune-miku-vocaloid-hd-png-download.png",
    )
    await ctx.respond(embed=embed)


def activate():
    bot.run(TUM_HUB_TOKEN)

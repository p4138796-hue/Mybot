import os
import discord
from discord.ext import commands

WELCOME_CHANNEL_ID = 1522905666224787606
HELP_CHANNEL_ID = 1522905899553787964

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"تم تشغيل البوت: {bot.user}")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if channel is None:
        return

    message = (
        f"مرحبًا {member.mention}\n\n"
        f"أنت العضو رقم **{member.guild.member_count}**\n\n"
        f"نرحب بك في سيرفر **الطاعون**\n"
        f"من تطوير **Migoo**\n\n"
        f"انتقل إلى <#{HELP_CHANNEL_ID}> للسؤال عن أهداف القنوات.\n\n"
        f"نتمنى زيارة سعيدة.\n\n"
        f"↩️ التالي"
    )

    await channel.send(message)


TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)

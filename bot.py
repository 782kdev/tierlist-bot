import discord
from discord.ext import commands
from keep_alive import keep_alive
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

class PanelView(discord.ui.View):
    @discord.ui.button(label="Verify Account", style=discord.ButtonStyle.primary)
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = discord.ui.Modal(title="Account Verification")
        modal.add_item(discord.ui.TextInput(label="IGN", custom_id="ign"))
        modal.add_item(discord.ui.TextInput(label="Region (AS/AU/NA/EU)", custom_id="region"))
        modal.add_item(discord.ui.TextInput(label="Server", custom_id="server"))
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="Enter Waitlist", style=discord.ButtonStyle.secondary)
    async def waitlist(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You've been added to the waitlist channel!", ephemeral=True)

@bot.command()
async def panel(ctx):
    await ctx.send("**Evaluation Testing Waitlist**\nClick below to verify or join the waitlist:", view=PanelView())

@bot.event
async def on_modal_submit(interaction: discord.Interaction):
    region = interaction.data['components'][1]['components'][0]['value'].lower()

    role_map = {
        'as': 1378112895946194971,
        'au': 1378112895946194971,
        'na': 1378112895946194973,
        'eu': 1378112895983812659
    }

    role_id = role_map.get(region)
    if role_id:
        role = interaction.guild.get_role(role_id)
        await interaction.user.add_roles(role)

    await interaction.response.send_message("✅ Verification complete! Role assigned.", ephemeral=True)

keep_alive()
bot.run(os.getenv("MTQxMjEzMTUwMjMwNDY1NzUwOQ.G6fvBo.st2EN9mJNATLiYB1a1nDmVfZ-lFgyIwxLP0Fv0"))

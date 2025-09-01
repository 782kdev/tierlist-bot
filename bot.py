import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Role IDs by region
ROLE_MAP = {
    'as': 1378112895946194971,
    'au': 1378112895946194971,
    'na': 1378112895946194973,
    'eu': 1378112895983812659
}

class PanelView(discord.ui.View):
    @discord.ui.button(label="Verify Account", style=discord.ButtonStyle.primary)
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = discord.ui.Modal(title="Zali TierList Verification")

        modal.add_item(discord.ui.TextInput(label="IGN", custom_id="ign"))
        modal.add_item(discord.ui.TextInput(label="Region (AS/AU/NA/EU)", custom_id="region"))
        modal.add_item(discord.ui.TextInput(label="Server", custom_id="server"))

        await interaction.response.send_modal(modal)

    @discord.ui.button(label="Enter Waitlist", style=discord.ButtonStyle.secondary)
    async def waitlist(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Ask for region via DM or default to a role (optional enhancement)
        await interaction.response.send_message("You've been added to the Zali TierList waitlist channel!", ephemeral=True)

        # Example: assign default role or prompt for region
        # For demo, let's assume region is NA (you can customize this)
        region = 'na'  # You can change this logic to ask for region if needed
        role_id = ROLE_MAP.get(region)

        if role_id:
            role = interaction.guild.get_role(role_id)
            await interaction.user.add_roles(role)

@bot.command()
async def panel(ctx):
    await ctx.send(
        "**Zali TierList Evaluation Panel**\nClick below to verify your account or join the waitlist:",
        view=PanelView()
    )

@bot.event
async def on_modal_submit(interaction: discord.Interaction):
    # Modal is just for collecting info now, not assigning roles
    await interaction.response.send_message("✅ Info received! You’ll be pinged when a tester is available.", ephemeral=True)

keep_alive()
bot.run(os.getenv("MTQxMjEzMTUwMjMwNDY1NzUwOQ.G6fvBo.st2EN9mJNATLiYB1a1nDmVfZ-lFgyIwxLP0Fv0"))

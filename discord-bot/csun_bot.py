import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

load_dotenv()

# Set your SendGrid API key
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
TOKEN = os.environ.get('DISCORD_TOKEN')
FROM_EMAIL=os.environ.get('FROM_EMAIL')
DOMAIN=os.environ.get('DOMAIN')


# Verification Code Storage
verification_codes = {}

def generate_verification_code():
    return str(random.randint(1000, 9999))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    try: 
        sync= await bot.tree.sync()
        print(f"Synced {len(sync) } commands")
    except Exception as f:
        print(f)
@bot.event
async def on_member_join(member):
    await member.send("Welcome! Please verify your email by using the command `!verify verification_code`")        
        
@bot.tree.command(name="verification", description="verify as CSUN student with your email") 
@app_commands.describe(email="Enter your CSUN email")
async def verification(interaction: discord.Integration,email:str):
    verification_code = generate_verification_code()
    print(verification_code)
    verification_codes[interaction.user.id] = verification_code
    await submit_email(interaction,email)  

@bot.tree.command(name="token",description="Please enter the token given in your email")
@app_commands.describe(verification_code="Enter the token to be a verified CSUN student")
async def token(interaction: discord.Integration, verification_code:str):
    user_id = interaction.user.id
    if user_id in verification_codes and verification_codes[user_id] == verification_code:
        await interaction.response.send_message("Email verified successfully!\nThank you for verifying your email.",ephemeral=True)
        del verification_codes[user_id]  # Remove the verification code after successful verification
        role = discord.utils.get(interaction.user.guild.roles, name="yeah")
        await interaction.user.add_roles(role)
    else:
        await interaction.response.send_message("Invalid verification code. Please check and try again.",ephemeral=True)

async def submit_email(interaction: discord.Integration, email):
    if email.endswith("my.csun.edu"):  # Validate email domain
        verification_code = verification_codes.get(interaction.user.id)
        print(verification_code)
        if verification_code:
            message =  send_verification_email(email, verification_code)
            try:
                sg = SendGridAPIClient(api_key=SENDGRID_API_KEY)
                sg.send(message)
                await interaction.response.send_message("Verification email sent. Please check your inbox.",ephemeral=True)
            except Exception as e:
                await interaction.response.send_message("Failed to send verification email. Please try again later.",ephemeral=True)
        else:
            await interaction.response.send_message("Please join the server first before submitting your email.",ephemeral=True)
    else:
        await interaction.response.send_message("Invalid email format. Please provide a valid CSUN email.",ephemeral=True)

def send_verification_email(email, verification_code):
    subject = "Discord Verification"
    content = f"Welcome to the server! Please verify your email by using the command !verify {verification_code}"
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=email,
        subject=subject,
        html_content=content)
    return message

bot.run(TOKEN)

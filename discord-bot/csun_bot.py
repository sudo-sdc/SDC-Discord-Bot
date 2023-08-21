import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands
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


# Verification Code Storage
verification_codes = {}

def generate_verification_code():
    return str(random.randint(1000, 9999))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    verification_code = generate_verification_code()
    verification_codes[member.id] = verification_code
    await member.send(f"Welcome! Please verify your email by using the command `!verify verification_code`")

@bot.command()
async def verify(ctx, verification_code):
    user_id = ctx.author.id
    if user_id in verification_codes and verification_codes[user_id] == verification_code:
        await ctx.send("Email verified successfully!")
        await ctx.author.send("Thank you for verifying your email.")
        del verification_codes[user_id]  # Remove the verification code after successful verification
    else:
        await ctx.send("Invalid verification code. Please check and try again.")

@bot.command()
async def submit_email(ctx, email):
    if email.endswith("csun.edu"):  # Validate email domain
        verification_code = verification_codes.get(ctx.author.id)
        if verification_code:
            await send_verification_email(email, ctx.author, verification_code)
            await ctx.send("Verification email sent. Please check your inbox.")
        else:
            await ctx.send("Please join the server first before submitting your email.")
    else:
        await ctx.send("Invalid email format. Please provide a valid CSUN email.")

async def send_verification_email(email, user, verification_code):
    subject = "Discord Verification"
    content = f"Welcome to the server! Please verify your email by using the command !verify {verification_code}"
    message = Mail(
        from_email='csunsdc@gmail.com',
        to_emails=email,
        subject=subject,
        html_content=content)
   
    try:
        sg = SendGridAPIClient(api_key=SENDGRID_API_KEY)
        response = sg.send(message)
    except Exception as e:
        await user.send("Failed to send verification email. Please try again later.")

bot.run(TOKEN)

import discord
import random
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

# Discord Bot Token
TOKEN = 'MTE0MTE3OTIyMzc0MzE1NjMzNQ.Gp6e2Q.uBZWyCqN8pUq5S3QFQDnrJu07JhhLcXak21pl8'

# Email Configurations
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'SDCdiscordbot@gmail.com'
EMAIL_PASSWORD = '@SDCdiscordbot'

# Verification Code Storage
verification_codes = {}

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_member_join(member):
    verification_code = generate_verification_code()
    verification_codes[member.id] = verification_code

    email_subject = "Discord Verification Code"
    email_body = f"Your verification code: {verification_code}"

    send_email(member, email_subject, email_body)

    await member.send("Check your email for the verification code.")

def generate_verification_code():
    return str(random.randint(1000, 9999))

def send_email(member, subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = member.email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, member.email, msg.as_string())
    server.quit()

client.run(TOKEN)


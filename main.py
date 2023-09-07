#instagram posting library 
#https://www.tutorialspoint.com/post-a-picture-automatically-on-instagram-using-python
import os
os.popen("rm -rf config")


from instabot import Bot
from decouple import config


API_USERNAME = config('USERNAME')
API_PASSWORD = config('PASSWORD')

# Initialize the bot
bot = Bot()

# Login to your Instagram account
bot.login(username=API_USERNAME, password=API_PASSWORD)

# # Upload a picture
bot.upload_photo('photo.png', caption='Our First Auto POST! :)')

# # Logout from your account
bot.logout()


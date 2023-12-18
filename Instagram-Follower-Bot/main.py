from InstaFollower import InstaFollower
# Note, Instagram will update it's website. So the CSS Selectors and XPATH may change.#
# Update `InstaFollower.py` with your Instagram account details
      
bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()  
""" Automatically open the browser and the Social media sites 
    Facebook, Messenger, Twitter, Instagram, """

import webbrowser

facebook = 'https://www.facebook.com/'
messenger = 'https://www.messenger.com/'
twitter = 'https://twitter.com/home'
insta = 'https://www.instagram.com/'

socmed = [facebook, messenger, twitter, insta]

for site in socmed:
  webbrowser.open(site)

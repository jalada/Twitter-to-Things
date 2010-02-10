# How to use

  1. Set up a Twitter account that's sole purpose is to receive DMs from you (in the future this could parse DMs on your actual account, but not for now). Follow it with your main account, and make sure it follows you.
  2. Edit twitter-to-things.py to include the username and password of this account.
  3. The default action is to add the todo to 'Today' with a tag of 'Twitter'. If you feel comfortable with Applescript, you can change this in the .scpt file. There's more you can do with Things and Applescript, Cultured Code have [reference documentation](http://culturedcode.com/things/download/ThingsAppleScriptGuide.pdf).
  4. Add it to your crontab (`crontab -e`). Something like:

  		*/5 * * * * python ~/Downloads/Twitter-to-things/twitter-to-things.py

  5. Enjoy!

# Bugs

Probably millions.

# Crontab mail

You will get a mail (internally on your Mac) whenever Twitter has a problem. I think you can fix this by piping the output of stderr and stdin to /dev/null, but I haven't tried it myself (yet).

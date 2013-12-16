#!/usr/bin/env python
"""
gifts_cfg.py: Getters for configuration data for giftswithfriends program.

Replace the return values in these functions with your specific
configuration details.
"""
__author__ = "Steven Gomez"


kids = {'Steve': 'steve@somewhere', 'Laura': 'laura@somewhere', 'Brian': 'brian@somewhere', 'Greg': 'greg@somewhere'}
"""
A dict mapping of names and emails. For example:
    {'Steve': 'steve@somewhere',
    'Laura': 'laura@somewhere',
    'Brian': 'brian@somewhere',
    'Greg': 'greg@somewhere'}
"""
        
price = 40
"""
A number representing the price limit in USD for the gift exchange.
For example:
    40
"""

date = '12/25'
"""
A string representing the date of the gift exchange.
For example:
    'December 25'
"""

gmail_usr = 'giftswithfriends@gmail.com'
"""
A gmail user email to authenticate with Google's SMTP server.
For example:
    'giftswithfriends@gmail.com'
"""

gmail_pwd = 'imnotgivingyoumypassword'
"""
A gmail user pwd (paired with the user account) to authenticate
with Google's SMTP server.
For example:
    'imnotgivingyoumypassword'
"""

def usage():
    print '\nWarning: gifts_cfg.py defines configurations for gifts_with_friends.py and ' + \
        'is not intended to be called as a script.\n'

if __name__ == '__main__':
    usage()

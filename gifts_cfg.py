#!/usr/bin/env python
"""
gifts_cfg.py: Getters for configuration data for giftswithfriends program.

Replace the return values in these functions with your specific
configuration details.
"""

__author__ = "Steven Gomez"
      
def kids():
    """
    Returns:
        A dict mapping of names and emails. For example:
        {'Steve': 'steve@somewhere',
        'Laura': 'laura@somewhere',
        'Brian': 'brian@somewhere',
        'Greg': 'greg@somewhere'}
    """
    
    return {'Steve': 'steve@somewhere',
        'Laura': 'laura@somewhere',
        'Brian': 'brian@somewhere',
        'Greg': 'greg@somewhere'}
        
def price():
    """
    Returns:
        A number representing the price limit in USD for the gift exchange.
        For example:
            40
    """
     
    return 40

def date():
    """
    Returns:
        A string representing the date of the gift exchange.
        For example:
            'December 25'
    """
    
    return 'December 25'

def gmail_usr():
    """
    Returns:
        A gmail user email to authenticate with Google's SMTP server.
        For example:
            'giftswithfriends@gmail.com'
    """
    
    return 'giftswithfriends@gmail.com'
    
def gmail_pwd():
    """
    Returns:
        A gmail user pwd (paired with the user account) to authenticate
        with Google's SMTP server. For example:
            'imnotgivingyoumypassword
    """

    return 'imnotgivingyoumypassword'

def usage():
    print 'santa_cfg.py defines configurations for santa.py and ' + \
        'is not intended to be called as a script.'

if __name__ == '__main__':
    usage()

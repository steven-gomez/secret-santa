#!/usr/bin/env python
"""
gifts_with_friends.py: Match up friends randomly for secret shopping.
"""
__author__ = "Steven Gomez"


import smtplib
from random import shuffle
from email.mime.text import MIMEText
import gifts_cfg

def verify_no_fixed_points(list_a, list_b, debug=False):
    """Return whether two lists have no fixed points.
    
    Iterate through lists; return whether the ith entry in list_a does not
    equal the ith entry in list_b, for all i.
    """
    assert(len(list_a) == len(list_b))
    for i in range(len(list_a)):
        if list_a[i] == list_b[i]:
            print 'Found fixed point at position '+str(i)
            if debug:
                print list_a, list_b
            return False
            
    print 'No fixed points'
    if debug:
        print list_a, list_b       
    return True
    
def send_gift_mail(to_email, shop_for, price, date, gmail_usr, gmail_pwd):
    """Send email with match/shopping details.
    
    Notify a person who his match is, what price to spend, the date. Use Google's
    mail server to send the email.
    """
    text_body = "You are " + shop_for + "\'s secret santa. " + \
                "Please get them something nice for around $"+str(price)+". " + \
                "Gifts will be exchanged on "+date+".\n\nHo Ho Ho!"
    msg = MIMEText(text_body)
    reply_email = 'Santa Claus <giftswithfriends@gmail.com>'

    msg['Subject'] = 'Randomized Secret Santa results'
    msg['From'] = reply_email
    msg['To'] = to_email

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(gmail_usr, gmail_pwd)
    server.sendmail(reply_email, [to_email], msg.as_string())
    server.quit()

def shuffle_and_notify(kids, gmail_usr, gmail_pwd, price, date):
    """Notify friends about gift match-ups.
    
    Duplicate and shuffle the list of kids. Keep shuffling until no one is
    matched up with herself, i.e., the ith person in the kids list does not match
    the ith person in the shuffled list, for all i. Then email each person their
    match. 
    """
    print '\n--- Gifts With Friends! ---'
    shuffled = kids.keys()
    shuffle(shuffled)
    tries = 1
    while not verify_no_fixed_points(kids.keys(), shuffled):
        shuffle(shuffled)
        tries = tries + 1
        print 'Shuffle succeeded after ' + str(tries) + ' tries'

    # Loop through kids and look up paired person in shuffled list at
    # corresponding index.
    for i in range(len(kids.keys())):
        shopper_email = kids.values()[i]
        receiver_name = shuffled[i]
        send_gift_mail(shopper_email, receiver_name, price, date, gmail_usr, gmail_pwd)
        print 'Email sent to ' + shopper_email

    print 'All emails sent. Ho Ho Ho!\n'
    
def main():
    """Load configuration and run shuffle_and_notify."""
    kids = gifts_cfg.kids
    price = gifts_cfg.price
    date = gifts_cfg.date
    gmail_usr = gifts_cfg.gmail_usr
    gmail_pwd = gifts_cfg.gmail_pwd
    
    shuffle_and_notify(kids, gmail_usr, gmail_pwd, price, date)

if __name__ == '__main__':
    main()

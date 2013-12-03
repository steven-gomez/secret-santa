secret-santa
============

Set up a "Secret Santa" style gift exchange between remote friends through email.

This repository includes simple python scripts that help you set up a gift exchange:
- **gifts_cfg.py**: Edit the return values of getters in this script to configure your gift exchange (e.g., people involved, their email addresses, date of the exchange, gift price limit). Note that credentials from a valid gmail account are needed to send email notifications with this program. If you use your personal gmail account, *do not peek* at the sent messages or you'll ruin the surprise!
- **gifts_with_friends.py**: Run this script with no arguments (*after editing gifts_cfg.py*) to start the exchange. It will match up people in the exchange and prevent anyone from shopping for herself. Then, it will notify each individual by email with *who* he is shopping for, *when* the exchange will happen, and *how much* he can spend on a gift.

This code has been tested with python 2.7. It is released under the terms of the MIT license. 

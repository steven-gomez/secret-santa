Gifts With Friends
============

Set up a "Secret Santa" style gift exchange between remote friends through email. When you can't draw names out of a hat, this is the next best solution. No need to enlist a third party to pick names.

## Table of Contents
* [Configure](#configure)
* [Run](#run)
* [Have fun](#havefun)

## <a name="configure"></a>Configure
After cloning this project, first configure `gifts_cfg.py`. This is a python module that defines getter functions for parameters needed by `gifts_with_friends.py`. Edit the return values of getters in this script to configure your gift exchange (e.g., people involved, their email addresses, date of the exchange, gift price limit). Note that credentials from a valid gmail account are needed to send email notifications with this program. If you use your personal gmail account, *do not peek* at the sent messages or you'll ruin the surprise!

## <a name="run"></a>Run
Next, run `gifts_with_friends.py` from the same directory containing `gifts_cfg.py`.
Run this script with no arguments (*after editing gifts_cfg.py*) to start the gift exchange. The script will match up people participating in the exchange and prevent anyone from shopping for herself. Then, it will notify each individual by email with *who* he is shopping for, *when* the exchange will happen, and *how much* he can spend on a gift.

```bash
cd <local repository>
python gifts_with_friends.py
```

## <a name="havefun"></a>Have fun
This code was written by [Steven Gomez](http://steveg.name "Steve's Homepage"). It has been tested with python 2.7. It is released under the terms of the MIT license.

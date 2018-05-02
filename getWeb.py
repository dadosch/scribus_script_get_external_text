#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Based on File: replacetext.py by Gregory Pittman, © 2014.06.06
# File: getWeb.py by dadosch
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
"""
USAGE

Place a URL in a text box, click on that text box and then run the script. The text should be replaced by the content of the link.
You might want to update your python stuff, so that cryptography and requests are up to date.


"""
import scribus
import random
import requests

if scribus.haveDoc():
    c = 0
        
else:
    scribus.messageBox('Usage Error', 'You need a Document open', scribus.ICON_WARNING, scribus.BUTTON_OK)
    sys.exit(2)

if scribus.selectionCount() == 0:
    scribus.messageBox('Scribus - Usage Error',
        "There is no object selected.\nPlease select a text frame and try again.",
        scribus.ICON_WARNING, scribus.BUTTON_OK)
    sys.exit(2)
if scribus.selectionCount() > 1:
    scribus.messageBox('Scribus - Usage Error',
        "You have more than one object selected.\nPlease select one text frame and try again.", scribus.ICON_WARNING, scribus.BUTTON_OK)
    sys.exit(2)

textbox = scribus.getSelectedObject()
pageitems = scribus.getPageItems()
boxcount = 1
for item in pageitems:
    if (item[0] == textbox):
        if (item[1] != 4):
            scribus.messageBox('Scribus - Usage Error', "This is not a textframe. Try again.", scribus.ICON_WARNING, scribus.BUTTON_OK)
            sys.exit(2)
contents = scribus.getTextLength(textbox)


probably_url = scribus.getAllText(textbox)
button= scribus.messageBox('url is',  probably_url, scribus.ICON_NONE,scribus.BUTTON_OK,scribus.BUTTON_CANCEL)
if button==scribus.BUTTON_CANCEL:
        sys.exit(2)

r = requests.get(probably_url)
scribus.setText(r.text, textbox)


scribus.setRedraw(1)
scribus.docChanged(1)
# TODO: save in a new doc
# TODO: Check for a valid url
# TODO: make it possible to do all text boxes in a document
# TODO: Format the text, make it possible to use basic markdown, basic wiki formatting
scribus.messageBox("Finished", "That should do it!",scribus.ICON_NONE,scribus.BUTTON_OK)

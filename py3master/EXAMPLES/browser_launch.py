#!/usr/bin/env python
"""

@author: jstrick
Created on Mon Mar 18 23:35:31 2013

"""
import webbrowser

webbrowser.open('http://xkcd.com/327')

browsers = ('firefox', 'windows-default',
    'safari', 'mozilla', 'lynx')

for browser in browsers:
    try:
        browser_controller = webbrowser.get(browser)
        browser_controller.open('http://xkcd.com/327')
    except Exception as e:
        print("Sorry, {0} not available: {1}".format(browser, e))

#!/usr/bin/env python
import urllib.request, urllib.error, urllib.parse

# note: fill in local proxy server
proxy = urllib.request.ProxyHandler({'http': '127.0.0.1'})

opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)
google_url = urllib.request.urlopen('http://www.google.com')

google_source = google_url.read()
print(google_source)
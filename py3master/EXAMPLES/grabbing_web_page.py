#!/usr/bin/env pythonimport urllib.request

response = urllib.request.urlopen("http://www.reddit.com")
print(response.info())
print("-" * 60)

for line in response:
    print(line.decode())

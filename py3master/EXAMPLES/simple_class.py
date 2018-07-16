#!/usr/bin/env python

class Simple:
    def __init__(self, message):
        self._message = message

    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = message

if __name__ == "__main__":
    s = Simple('hello')
print(s.get_message())

    s.set_message('howdy')
print(s.get_message())

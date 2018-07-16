#!/usr/bin/env python

import calendar

def main():
    print_text_calendar()
    print()
    print_html_calendar()

def print_text_calendar():
    tcal = calendar.TextCalendar()
    print(tcal.formatmonth(2015, 8))

def print_html_calendar():
    hcal = calendar.HTMLCalendar()
    print(hcal.formatmonth(2015, 8))

if __name__ == '__main__':
    main()

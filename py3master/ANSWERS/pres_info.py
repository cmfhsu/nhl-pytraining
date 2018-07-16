#!/usr/bin/env python
import datetime

while True:
    pres_lname = input("Enter president's last name: ")

    if pres_lname == 'q':
        break

    if pres_lname == '':
        continue

    with open("../DATA/presidents.txt") as pres_file:

        for rec in pres_file:
            flds = rec.split(":")
            if flds[1] == pres_lname:
                byear, bmonth, bday = flds[3].split('-')
                byear = int(byear)
                bmonth = int(bmonth)
                bday = int(bday)

                if flds[4] == 'NONE':
                    alive = '*'
                    dyear = datetime.date.today().year
                    dmonth = datetime.date.today().month
                    dday = datetime.date.today().day
                else:
                    alive = ''
                    dyear, dmonth, dday = flds[4].split('-')
                    dyear = int(dyear)
                    dmonth = int(dmonth)
                    dday = int(dday)

                birthdate = datetime.date(byear,bmonth,bday)
                deathdate = datetime.date(dyear,dmonth,dday)

                print("NAME: {0} {1}".format( flds[2],flds[1] ))
                print("BIRTH: {0:02d}/{1:02d}/{2:02d}".format(bmonth, bday, byear))
                if not alive:
                    print("DEATH: {0:02d}/{1:02d}/{2:02d}".format(dmonth, dday, dyear))

                lifespan = deathdate - birthdate
                age = lifespan.days/365.25

                print("AGE {0:.2f}{1}".format(age, alive))
                print()


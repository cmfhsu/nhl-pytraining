#!/usr/bin/env python

with open("../DATA/alt.txt") as f_in:
    with open("a.txt","w") as a_out:
        with open("b.txt","w") as b_out:
            for line in f_in:
                if line.lower().startswith('a'):
                    a_out.write(line)
                else:
                    b_out.write(line)

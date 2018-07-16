#!/usr/bin/env python
"""
@author: jstrick
Created on Thu Mar 14 14:16:29 2013

"""
import tarfile

for tar_file in ('pres.tar', 'NOT_A.tar', 'potus.tar.gz'):
    filename = '../DATA/' + tar_file
    is_valid = tarfile.is_tarfile(filename)
    print(filename, end=' ')
    print('IS' if is_valid else 'IS NOT', end=' ')
    print('a tarfile')
print()

with tarfile.open('../DATA/pres.tar') as TAR_READ:
    for member in TAR_READ:
        print(member.name, member.size)
    print()

with tarfile.open('../DATA/pres.tar') as TAR_READ:
    TAR_READ.extract('presidents.txt', path='../TEMP')

with tarfile.open('../DATA/potus.tar.gz') as TAR_READ:
    TAR_READ.extract('presidents.csv', path='../TEMP')

with tarfile.open('../TEMP/text_files.tar','w') as TAR_WRITE:
    TAR_WRITE.add('../DATA/parrot.txt')
    TAR_WRITE.add('../DATA/alice.txt')

with tarfile.open('../TEMP/more_text_files.tar.gz','w:gz') as TAR_GZ_WRITE:
    TAR_GZ_WRITE.add('../DATA/parrot.txt')
    TAR_GZ_WRITE.add('../DATA/alice.txt')


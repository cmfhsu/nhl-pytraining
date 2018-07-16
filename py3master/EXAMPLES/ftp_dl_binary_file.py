#!/usr/bin/env python
# (c)2015 John Strickler
from ftplib import FTP
FTP_SERVER = 'speedtest.tele2.net'

def main():
    ftp_conn = FTP(FTP_SERVER)

    ftp_conn.login('anonymous','guest')

    get_binary_file(ftp_conn, '5MB.zip')

    ftp_conn.close()


def get_binary_file(ftp_client, file_name, dest=None):
    if not dest:
        dest = file_name

    ftp_cmd = 'RETR {}'.format(file_name)

    with open(dest,'wb') as dest_in:
        ftp_client.retrbinary(
            ftp_cmd,
            dest_in.write
        )

if __name__ == '__main__':
    main()

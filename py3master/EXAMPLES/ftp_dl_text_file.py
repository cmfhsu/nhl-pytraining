#!/usr/bin/env python
# (c)2015 John Strickler
from ftplib import FTP
FTP_SERVER = 'ftp.cs.unc.edu'
FILE_TO_DOWNLOAD = 'welcome.msg'

def main():
    ftp_conn = FTP(FTP_SERVER)

    ftp_conn.login('anonymous','-guest')

    get_text_file(ftp_conn, FILE_TO_DOWNLOAD)

    ftp_conn.close()

    with open(FILE_TO_DOWNLOAD) as ftd_in:
        print(ftd_in.read())


def get_text_file(ftp_client, file_name, dest=None):
    if not dest:
        dest = file_name

    ftp_cmd = 'RETR {}'.format(file_name)

    with open(dest,'w') as dest_out:
        ftp_client.retrlines(
            ftp_cmd,
            lambda line, writer=dest_out.write: writer(line + '\n')
        )

if __name__ == '__main__':
    main()

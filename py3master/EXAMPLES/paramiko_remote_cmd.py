#!/usr/bin/env python

import time
import paramiko

USER = 'student'
PASSWORD = 'l3@rn3r'
PORT = 22
HOST = 'www.cja-tech.com'

transport = paramiko.Transport((HOST, PORT))    
transport.connect(username = USER, password = PASSWORD)    

def execute_cmd(transport, cmd):
    channel = transport.open_channel(kind = "session")
    channel.exec_command(cmd)

    while not channel.exit_status_ready():
        time.sleep(1)
    output = channel.recv(99999)
    err_output = channel.recv_stderr(99999)
    return channel.exit_status,output, err_output

status, output, err = execute_cmd(transport, 'whoami')
print('status is:', status)
print('output is:', output.decode().rstrip())
print('err is:', err.decode())
print()

status, output, err = execute_cmd(transport, 'ls -l /Users/{0}'.format(USER))
print('status is:', status)
print('output is:', output.decode().rstrip())
print('err is:', err.decode())
print()

status, output, err = execute_cmd(
    transport, 'ls -l /Users/{0}'.format('CARDINALBIGGLES')
)

print('status is:', status)
print('output is:', output.decode().rstrip())
print('err is:', err.decode())
print()

transport.close()

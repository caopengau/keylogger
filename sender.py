import paramiko
from scp import SCPClient


def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client
    
server = "SERVER_ADDRESS"
port = 22
user = "USERNAME"
password = "PASSWORD"

ssh = createSSHClient(server, port, user, password)
# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())

# :location
scp.put('logs.txt', 'remote_logs.txt')
scp.get('remote_logs.txt')
scp.close()
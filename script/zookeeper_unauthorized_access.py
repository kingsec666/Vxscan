import socket
from lib.verify import verify

vuln = ['2181', 'Zookeeper']


def check(url, ip, ports, apps):
    if verify(vuln, ports, apps):
        try:
            socket.setdefaulttimeout(1.5)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, 2181))
            s.send(b'success')
            data = s.recv(1024)
            if b'Environment' in data:
                return 'zookeeper://%s:2181' % ip
        except Exception as e:
            pass

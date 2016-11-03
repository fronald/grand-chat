import socket

import sys


class TCPClient:
    def __init__(self):
        self.is_connected = False
        self.socket = None

    def connect_socket(self, addr):
        """Connect to a server given an address of IP and port"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect(addr)
            self.is_connected = True
        except ConnectionError:
            self.is_connected = False

    def disconnect_socket(self):
        """Close the socket if is open"""
        if self.is_connected():
            self.socket.close()
        else:
            print('The socket is not connected', file=sys.stderr)

    def send_message(self, msg):
        """Sends a message through the open socket"""
        if self.is_connected():
            self.socket.write(msg)
        else:
            print('The socket is not connected', file=sys.stderr)

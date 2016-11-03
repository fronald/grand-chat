import socket

import sys


class TCPServer:
    def __init__(self):
        self.is_server_open = False
        self.socket = None

    def open_server(self):
        """This method opens the server"""
        if not self.is_server_open:
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.bind(('localhost', 8080))
                self.socket.listen(5)
                self.is_server_open = True
            except ConnectionError:
                print('Connection error', file=sys.stderr)
        else:
            print('The server has already opened', file=sys.stderr)

    def close_server(self):
        """This method closes the server if it is open"""
        if self.is_server_open:
            try:
                self.socket.close()
                self.is_server_open = False
            except ConnectionError:
                print('Connection error', file=sys.stderr)
        else:
            print('The server is not open', file=sys.stderr)

    def receive_message(self):
        """This method receives message if the server is open"""
        if self.is_server_open:
            return self.socket.recv(2048)
        else:
            return []

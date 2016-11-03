import unittest
from unittest.mock import MagicMock

from src.server.tcp_server import TCPServer


class TCPServerTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_openServerSuccessfully(self):
        tcp_server = TCPServer()
        tcp_server.open_server()
        self.assertTrue(tcp_server.is_server_open)

    def test_serverDontOpenIfAlreadyOpened(self):
        tcp_server = TCPServer()
        tcp_server.is_server_open = True
        tcp_server.socket = MagicMock()
        tcp_server.socket.assert_not_called()

    def test_serverCloses(self):
        tcp_server = TCPServer()
        tcp_server.is_server_open = True
        tcp_server.socket = MagicMock()
        tcp_server.close_server()
        tcp_server.socket.close.assert_called_with()

    def test_serverDontClosesIfNotOpen(self):
        tcp_server = TCPServer()
        tcp_server.is_server_open = False
        tcp_server.socket = MagicMock()
        tcp_server.close_server()
        tcp_server.socket.close.assert_not_called()

    def test_serverDontReceiveMsgIfClosed(self):
        tcp_server = TCPServer()
        tcp_server.is_server_open = False
        tcp_server.socket = MagicMock()
        self.assertEquals(tcp_server.receive_message(), [])
        tcp_server.socket.recv.assert_not_called()

    def test_serverReceiveMsgIfOpened(self):
        tcp_server = TCPServer()
        tcp_server.is_server_open = True
        tcp_server.socket = MagicMock()
        tcp_server.receive_message()
        self.assertTrue(tcp_server.socket.recv.called)

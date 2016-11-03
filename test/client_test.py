import socket
import unittest

from mock.mock import MagicMock

from gc.client.tcp_client import TCPClient


class TCPClientTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_socketConnectionSuccessful(self):
        """Test whether the TCPClient can successfully connect to an open socket"""
        client = TCPClient()
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('localhost', 8080))
        serversocket.listen()
        client.connect_socket(('localhost', 8080))
        self.assertTrue(client.is_connected)

    def test_socketConnectionFailure(self):
        """Test whether the TCPClient cannot successfully connect to an closed socket"""
        client = TCPClient()
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('localhost', 8080))
        self.assertFalse(client.connect_socket(('localhost', 8080)))

    def test_socketSendMessageSuccessfully(self):
        """Test whether the TCPClient is capable of sending a message or not"""
        client = TCPClient()
        client.is_connected = MagicMock(return_value=True)
        client.socket = MagicMock()
        client.send_message('Test')
        client.socket.write.assert_called_with('Test')

    def test_socketDoesntSendMessageIfNotConnected(self):
        """Test wheter the TCPClient tries to send a message without having a open socket or not"""
        client = TCPClient()
        client.is_connected = MagicMock(return_value=False)
        client.socket = MagicMock()
        client.send_message('Test')
        client.socket.write.assert_not_called()

    def test_socketSuccessfullyCloses(self):
        """Test whether the TCPClient is capable of closing its socket"""
        client = TCPClient()
        client.is_connected = MagicMock(return_value=True)
        client.socket = MagicMock()
        client.disconnect_socket()
        client.socket.close.assert_called()

    def test_socketDontCloseIfNotOpen(self):
        """Test whether the TCPClient is capable of closing its socket"""
        client = TCPClient()
        client.is_connected = MagicMock(return_value=False)
        client.socket = MagicMock()
        client.disconnect_socket()
        client.socket.close.assert_not_called()

#!/usr/bin/env python


"""
Simple IRC bot
It has no goal, only to be there

doc:
https://tools.ietf.org/html/rfc1459
https://docs.python.org/3/howto/
"""


import sys
from getopt import getopt, GetoptError
import socket
import ssl

VERBOSE = False


def usage():
    """
    usage
    """
    print("usage:")
    print("  ./birc.py -s/--server server -p/--port port -n/--nick \
-c/--channels channels -d/--description desc")
    print()
    print("`channels` should be a file containing desired channels following this format:")
    print("channel1\\n")
    print("channel2\\n")
    print("...")
    print()
    print("ex:")
    print('  ./birc.py -s chat.freenode.net -p 6667 -n blipblop -c channel_file -d "blip blop"')
    print("with channel_file:")
    print("#archlinux\\n")
    print("#arch-fr-off\\n")


def connect(server, port):
    """
    Socket creation and connection
    """
    print(f"creating socket to server: {server} using port: {port}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server, port))
    return sock


def register(sock, nick, description):
    """
    registration (nick + description)
    """
    print(f"registrating with nick: {nick}")
    send(sock, f"NICK {nick}\r\n")
    send(sock, f"USER {nick} * 8 :{description}\r\n")


def join(sock, channels_file):
    """
    joining desired channels
    """
    if channels_file is None:
        return
    with open(channels_file, "r") as channels:
        channels_list = ','.join(channels.read().split('\n'))
        if channels_list[-1] == ',':
            channels_list = channels_list[:-1]

        print(f"joining channels: {channels_list}")
        send(sock, f"JOIN {channels_list}" + "\r\n")


def loop(sock):
    """
    main loop, simple read/write
    """
    while True:
        data = receive(sock)
        if VERBOSE:
            print(data)
        data = data.split(' ')
        # server ping
        if data[0] == 'PING':
            send(sock, "PONG " + data[1] + "\r\n")
        # user ping
        try:
            if data[1] == 'PRIVMSG' and data[3][:6] == ':@ping':
                send(sock, "PRIVMSG " + data[2] + " :@pong\r\n")
        except IndexError:
            pass


def send(sock, msg):
    """
    wrapper to send messages through socket
    """
    if not msg.endswith("\r\n"):
        # arf, don't forget it please
        msg += "\r\n"

    total_sent = 0
    while total_sent < len(msg):
        sent = sock.send(msg[total_sent:].encode('utf-8'))
        if sent == 0:
            raise RuntimeError("socket connection broken")
        total_sent += sent


def receive(sock):
    """
    wrappter to receive messages through socket
    """
    string_received = ""
    total_received = 0
    while True:
        chunk = sock.recv(2048)
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        string_received += chunk.decode('utf-8')
        total_received += len(chunk)
        if string_received.endswith("\r\n"):
            return string_received


def main(argv):
    """
    main function
    arg parse + calls loop
    """
    try:
        opts, _ = getopt(argv, "s:p:n:c:hvd:",
                         ["server=", "port=", "nick=", "channels=",
                          "help", "verbose", "description="])
    except GetoptError:
        usage()
        sys.exit(1)

    # defaults
    server = "chat.freenode.net"
    port = 6697
    nick = "bitbatbot"
    channels = None # by default, doesn't connect to any channel
    description = "blip blop, I'm a bot"

    for opt, arg in opts:
        if opt in ["-s", "--server"]:
            server = arg
        elif opt in ["-p", "--port"]:
            try:
                port = int(arg)
            except ValueError:
                usage()
                sys.exit(1)
        elif opt in ["-n", "--nick"]:
            nick = arg
        elif opt in ["-c", "--channels"]:
            channels = arg
        elif opt in ["-h", "--help"]:
            usage()
            sys.exit(0)
        elif opt in ["-d", "--description"]:
            description = arg
        elif opt in ["-v", "--verbose"]:
            global VERBOSE
            VERBOSE = True
        else:
            assert False, "unhandled option"

    sock = connect(server, port)
    sock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_SSLv23)
    register(sock, nick, description)
    join(sock, channels)
    loop(sock)


if __name__ == "__main__":
    main(sys.argv[1:])

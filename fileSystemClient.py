import socket
from logger import Logger


class FileSystemClient:
    @Logger("111", "log")
    def __init__(self, lock_ip, name_ip, file_ip):
        self.lock_ip = lock_ip
        self.name_ip = name_ip
        self.file_ip = file_ip
        pass

    @Logger("111", "log")
    def list(self, path):
        pass

    @Logger("111", "log")
    def recv(self, path):
        pass

    @Logger("111", "log")
    def remv(self, path):
        pass

    @Logger("111", "log")
    def sent(self, path):
        pass

    @Logger("111", "log")
    def crte(self, path):
        pass

    @Logger("111", "log")
    def aloc(self):
        pass

    @Logger("111", "log")
    def rnme(self, path, string):
        pass

    def isDr(self, path):
        pass

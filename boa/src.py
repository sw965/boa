import json
import pickle
import re
import socket

def dump_pickle(obj, file_path):
    with open(file_path, 'wb') as file_obj:
        pickle.dump(obj, file_obj)

def load_pickle(file_path):
    with open(file_path, "rb") as file_obj:
        return pickle.load(file_obj)

def dump_json(d, file_path):
    with open(file_path, "w") as file_obj:
        json.dump(d, file_obj, ensure_ascii=False, indent=4, separators=(",", ":"))

def load_json(file_path, encoding="utf-8"):
    with open(file_path, "rt", encoding=encoding) as file_obj:
        return json.load(file_obj)

def read_txt(file_path):
    with open(file_path, "rt", encoding="utf-8") as file_obj:
        return file_obj.read()

def readlines_txt(file_path, del_new_line):
    with open(file_path, "rt", encoding="utf-8") as file_obj:
        lines = file_obj.readlines()
        if del_new_line:
            return [re.sub("\n", "", line) for line in lines]
        return lines

def write_txt(file_path, data):
    with open(file_path, "wt", encoding="utf-8") as file_obj:
        file_obj.write(data)


class SimpleLocalSocketServer:
    def __init__(self, port):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind(("127.0.0.1", port))
        self.__server.listen(1)
        self.__conn, _ = self.__server.accept()

    def recv(self, byte_size):
        return self.__conn.recv(byte_size).decode("utf-8")

    def send(self, msg):
        self.__conn.sendall(msg.encode("utf-8"))

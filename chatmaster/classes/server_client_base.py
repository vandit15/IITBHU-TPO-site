from abc import ABCMeta

import Queue as queue


class ServerClientBase:
    __metaclass__ = ABCMeta
    def __init__(self):
        self._msg_queue = queue.Queue()

    def get_new_msgs(self):
        msgs = []
        while not self._msg_queue.empty():
            try:
                msg = self._msg_queue.get(block=False)
                msgs.append(msg)
            except queue.Empty():
                return msgs
        return msgs

    def recv_handler(self, sock):
        raise NotImplemented()

    def send_msg(self, msg):
        raise NotImplemented()

    def destroy(self):
        raise NotImplemented()

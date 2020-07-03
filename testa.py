第一版本
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/14 上午11:08
# @Author  : linqikai
# @Site    : 
# @File    : repeatSendGift.py
# @Software: PyCharm Community Edition

import json
import random
import threading
import time
import unittest

import tf.automation.backend
from tf.automation.backend.websocket import ChatRoom, send_request


class repeatSendGift(tf.automation.backend.LoggedTestCase):
    def setUp(self):
        self.sending_threads = []

    def tearDown(self):
        self.chat.close()

    def send_gift(self, roomId, giftId):
        # self.room_id = roomId
        P_sck = 'QjYbazx0AqOQK2fPyUqpNJ4Le%2BJfhuiYm3pIPqYExSRPAuNO2f87afK684OYVG7b58rbuun7ubYbhToF3%2FDaMVzKfErBqE1lycVH1EiAqaBG3b7qBUHfUbgKfGOnvrtYlTW%2BaTCbqjBN0oAa5uO2qw%3D%3D'
        chat = ChatRoom(P_sck=P_sck, logger=self.logger)
        self.chat = chat
        chat.create_chat(roomId)
        send_gift = json.dumps({"name": "SendGift", "args": [
            {
                "g": giftId,  # 礼物ID
                "q": random.randrange(1, 10, 3),  # 礼物数量
                # "ti":"926380764",         #被送礼用户ID
                "r": roomId,  # 房间ID
                "_sid": "SendGift{}".format(str(time.time()).split(".")[0])  # SID
            }
        ]})

        t = threading.Thread(target=send_request, name='thread-{}'.format('LiveTaskInit'), args=(chat,
                                                                                                 send_gift
                                                                                                 ))

        self.sending_threads.append(t)
        self.logger.info("===========send_gift_start==========")
        t.start()
        self.logger.debug("===========sleep 2 seconds==============\r\n")
        time.sleep(2)
        self.logger.info("sending_threads:{}".format(len(self.sending_threads)))

    def test_send(self):
        gift_id = 858
        room_ids = ['96232','96233','95625','503474','96251','96221','96256','503475','503452','503446','95641','95536','95664','95532','96218','95677','95534','96255','96203','95669','95643','101554','503421','503420','95529','95640','503417','503422','96212','95547','95548','95561','95572','95569','95570','95565','95564','95668','503384','95543','95662','95582','95670','95663','96273','96271','503412','503391','96226','503476','96184','95623','503390','95630','95583','96230','503408','503394','503378','503450','95661','503385','503419','503461','95580','503454','96243','96242','503457','95628','96244','96241','503398','95545','503409','96229','95581','96245','96137','96179','503379','96139','503403','503381','96183','96148','96185','503400','96250','96191','503392','95678','503402','503406','503401','503389','503405','503410','101557','503445',
                    '95587','95629','95571','95646','503414','96227','96220','503451','96187','96228','95976','503411']

        for roomId in room_ids:
            self.send_gift(roomId, gift_id)

        print "\r\n============send_gift_end========\r\n"
        self.chat.close()


if __name__ == '__main__':
    unittest.main()

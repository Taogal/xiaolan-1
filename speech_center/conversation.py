# -*- coding: utf-8 -*-
# 小蓝对话系统

# description:
# author: xiaoland
# create_time: 2018/7/9

"""
    desc:pass
"""

import sys
import os
import re
import time
import threading
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase


class Dialogue(xiaolanBase):

    def __init__(self):

        super(Dialogue, self).__init__()
    
    def conversation(self):

        """
        小蓝对话处理
        :return:
        """
        self.speaker('ding')
        if self.set['main_setting']['talk_mode'] == 'voice':

            self.recorder('normal', 0)
            self.stt('./voice.wav')
            f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r');text = f.read();f.close()
        elif self.set['main_setting']['talk_mode'] == 'gesture':

            self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
            self.display('TextDisplay', {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认', 'RemindWord': [], 'BackgroundImage': ''})
            while 1 == 1:
                os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                if self.gesture('normal', {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'}) == 'ok':
                    os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                    text = self.text_recognition('normal', {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'})
                    break
                else:
                    self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                    self.display('TextDisplay', {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认', 'RemindWord': [], 'BackgroundImage': ''})

        else:

            self.recorder('normal', 0)
            self.stt('./voice.wav')
            f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r');text = f.read();f.close()

        self.speaker('dong')

        intentdict = self.client_to_server('NluReq', {'Text': text})
        self.client_to_server('SkillReq', {'Intent': intentdict['Intent'], 'Slots': intentdict['Slots'], 'IntentDict': intentdict})

    def wait_answer(self, recordtype):

        """
        等待答案处理
        :param recordtype: 录制类型
        :return:
        """
        self.speaker('ding')
        if recordtype == 'ex':

            if self.set['main_setting']['talk_mode'] == 'voice':

                self.recorder('express', 0)
                self.stt('./voice.wav')
                f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                text = f.read()
                f.close()
            elif self.set['main_setting']['talk_mode'] == 'gesture':

                self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                self.display('TextDisplay', {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                             'RemindWord': [], 'BackgroundImage': ''})
                while 1 == 1:
                    os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                    if self.gesture('normal', {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'}) == 'ok':
                        os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                        text = self.text_recognition('normal',
                                                     {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'})
                        break
                    else:
                        self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                        self.display('TextDisplay',
                                     {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                      'RemindWord': [], 'BackgroundImage': ''})

            else:

                self.recorder('express', 0)
                self.stt('./voice.wav')
                f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                text = f.read()
                f.close()
        elif recordtype == 'normal':

            if self.set['main_setting']['talk_mode'] == 'voice':

                self.recorder('normal', 0)
                self.stt('./voice.wav')
                f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                text = f.read()
                f.close()
            elif self.set['main_setting']['talk_mode'] == 'gesture':

                self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                self.display('TextDisplay', {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                             'RemindWord': [], 'BackgroundImage': ''})
                while 1 == 1:
                    os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                    if self.gesture('normal', {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'}) == 'ok':
                        os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                        text = self.text_recognition('normal',
                                                     {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'})
                        break
                    else:
                        self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                        self.display('TextDisplay',
                                     {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                      'RemindWord': [], 'BackgroundImage': ''})

            else:

                self.recorder('normal', 0)
                self.stt('./voice.wav')
                f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                text = f.read()
                f.close()
        elif recordtype == 'ts':

            if self.set['main_setting']['talk_mode'] == 'voice':

                self.recorder('translate', 0)
                self.stt('./voice.wav')
                f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                text = f.read()
                f.close()
            elif self.set['main_setting']['talk_mode'] == 'gesture':

                self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                self.display('TextDisplay', {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                             'RemindWord': [], 'BackgroundImage': ''})
                while 1 == 1:
                    os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                    if self.gesture('normal', {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'}) == 'ok':
                        os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                        text = self.text_recognition('normal',
                                                     {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'})
                        break
                    else:
                        self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                        self.display('TextDisplay',
                                     {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                      'RemindWord': [], 'BackgroundImage': ''})

            else:

                self.recorder('translate', 0)
                self.stt('./voice.wav')
                f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                text = f.read()
                f.close()
        elif recordtype == 's':

            if self.set['main_setting']['talk_mode'] == 'voice':

                self.recorder('less_time', 0)
                self.stt('./voice.wav')
                f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                text = f.read()
                f.close()
            elif self.set['main_setting']['talk_mode'] == 'gesture':

                self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                self.display('TextDisplay', {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                             'RemindWord': [], 'BackgroundImage': ''})
                while 1 == 1:
                    os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                    if self.gesture('normal', {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'}) == 'ok':
                        os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                        text = self.text_recognition('normal',
                                                     {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'})
                        break
                    else:
                        self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                        self.display('TextDisplay',
                                     {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                      'RemindWord': [], 'BackgroundImage': ''})

            else:

                self.recorder('less_time', 0)
                self.stt('./voice.wav')
                f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                text = f.read()
                f.close()
        else:
            if self.set['main_setting']['talk_mode'] == 'voice':

                self.recorder('normal', 0)
                self.stt('./voice.wav')
                f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                text = f.read()
                f.close()
            elif self.set['main_setting']['talk_mode'] == 'gesture':

                self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                self.display('TextDisplay', {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                             'RemindWord': [], 'BackgroundImage': ''})
                while 1 == 1:
                    os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                    if self.gesture('normal', {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'}) == 'ok':
                        os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                        text = self.text_recognition('normal',
                                                     {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'})
                        break
                    else:
                        self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                        self.display('TextDisplay',
                                     {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                      'RemindWord': [], 'BackgroundImage': ''})

            else:

                self.recorder('normal', 0)
                self.stt('./voice.wav')
                f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                text = f.read()
                f.close()
        self.speaker('dong')

        intentdict = self.client_to_server('NluReq', {'Text': text})
        self.client_to_server('SkillResForWaitAnswer', {'Intent': intentdict['intent'], 'Slots': intentdict['slots'], 'IntentDict': intentdict})

    def ask_slots(self, slotname, slotdicts, slotask, recordtype):

        """
        询问槽位信息处理
        :param slotname: 槽位名称
        :param slotdicts: 槽位字典
        :param recordtype: 录制类型
        :param slotask: 槽位询问语句
        :return:
        """
        text = ''
        a = 0
        slotturn = []
        while 1 == 1:
            if a < len(slotname) + 1:
                self.tts(slotask[a])
                if recordtype == 'ex':

                    if self.set['main_setting']['talk_mode'] == 'voice':

                        self.recorder('express', 0)
                        f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                        self.stt('./voice.wav')
                        text = f.read()
                        f.close()
                    elif self.set['main_setting']['talk_mode'] == 'gesture':

                        self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                        self.display('TextDisplay',
                                     {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                      'RemindWord': [], 'BackgroundImage': ''})
                        while 1 == 1:
                            os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                            if self.gesture('normal',
                                            {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'}) == 'ok':
                                os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                                text = self.text_recognition('normal',
                                                             {
                                                                 'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'})
                                break
                            else:
                                self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                                self.display('TextDisplay',
                                             {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                              'RemindWord': [], 'BackgroundImage': ''})

                    else:

                        self.recorder('express', 0)
                        self.stt('./voice.wav')
                        f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                        text = f.read()
                        f.close()
                elif recordtype == 'normal':

                    if self.set['main_setting']['talk_mode'] == 'voice':

                        self.recorder('normal', 0)
                        self.stt('./voice.wav')
                        f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                        text = f.read()
                        f.close()
                    elif self.set['main_setting']['talk_mode'] == 'gesture':

                        self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                        self.display('TextDisplay',
                                     {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                      'RemindWord': [], 'BackgroundImage': ''})
                        while 1 == 1:
                            os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                            if self.gesture('normal',
                                            {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'}) == 'ok':
                                os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                                text = self.text_recognition('normal',
                                                             {
                                                                 'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'})
                                break
                            else:
                                self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                                self.display('TextDisplay',
                                             {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                              'RemindWord': [], 'BackgroundImage': ''})

                    else:

                        self.recorder('normal', 0)
                        self.stt('./voice.wav')
                        f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                        text = f.read()
                        f.close()
                elif recordtype == 'ts':

                    if self.set['main_setting']['talk_mode'] == 'voice':

                        self.recorder('translate', 0)
                        self.stt('./voice.wav')
                        f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                        text = f.read()
                        f.close()
                    elif self.set['main_setting']['talk_mode'] == 'gesture':

                        self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                        self.display('TextDisplay',
                                     {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                      'RemindWord': [], 'BackgroundImage': ''})
                        while 1 == 1:
                            os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                            if self.gesture('normal',
                                            {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'}) == 'ok':
                                os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                                text = self.text_recognition('normal',
                                                             {
                                                                 'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'})
                                break
                            else:
                                self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                                self.display('TextDisplay',
                                             {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                              'RemindWord': [], 'BackgroundImage': ''})

                    else:

                        self.recorder('translate', 0)
                        self.stt('./voice.wav')
                        f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                        text = f.read()
                        f.close()
                elif recordtype == 's':

                    if self.set['main_setting']['talk_mode'] == 'voice':

                        self.recorder('less_time', 0)
                        self.stt('./voice.wav')
                        f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                        text = f.read()
                        f.close()
                    elif self.set['main_setting']['talk_mode'] == 'gesture':

                        self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                        self.display('TextDisplay',
                                     {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                      'RemindWord': [], 'BackgroundImage': ''})
                        while 1 == 1:
                            os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                            if self.gesture('normal',
                                            {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'}) == 'ok':
                                os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                                text = self.text_recognition('normal',
                                                             {
                                                                 'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'})
                                break
                            else:
                                self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                                self.display('TextDisplay',
                                             {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                              'RemindWord': [], 'BackgroundImage': ''})

                    else:

                        self.recorder('less_time', 0)
                        self.stt('./voice.wav')
                        f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                        text = f.read()
                        f.close()
                else:
                    if self.set['main_setting']['talk_mode'] == 'voice':

                        self.recorder('normal', 0)
                        self.stt('./voice.wav')
                    elif self.set['main_setting']['talk_mode'] == 'gesture':

                        self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                        self.display('TextDisplay',
                                     {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                      'RemindWord': [], 'BackgroundImage': ''})
                        while 1 == 1:
                            os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                            if self.gesture('normal',
                                            {'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'}) == 'ok':
                                os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                                text = self.text_recognition('normal',
                                                             {
                                                                 'Image': '/home/pi/xiaolan/memory_center/face_img/face.jpg'})
                                break
                            else:
                                self.tts('请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别')
                                self.display('TextDisplay',
                                             {'Text': '请将您写好的文字放置在摄像头之前，放置完毕以后请做出ok的手势，将会自动开始识别', 'Title': '小蓝文字识别交互确认',
                                              'RemindWord': [], 'BackgroundImage': ''})

                    else:

                        self.recorder('normal', 0)
                        self.stt('./voice.wav')
                        f = open('/home/pi/xiaolan/memory_center/more/text.txt', 'r')
                        text = f.read()
                        f.close()
                slotturn.append(self.client_nlu('get_slots', {'Text': text, 'SlotsList': [slotname[a], slotdicts[a]]}))
                a = a + 1
            else:
                break
        return slotturn

            
            
            
            
        

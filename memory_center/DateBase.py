# -*- coding: utf-8 -*-
# Datebase: memcache

import memcache
import json
import os
import sys
from Log import Log
sys.path.append('/home/pi/xiaolan/')
import setting
from Base import xiaolanBase

class Datebase(xiaolanBase):

    def __init__(self):

        super(Datebase, self).__init__()
        self.dburl = self.set['main_setting']['DatebaseUrl']

    def SetDate(self, date, db):

        url = self.dburl[db]
        try:
            dbc = memcache.Client([url + ':11211'], debug=True)
        except:
            print "Error: datebaseRequestsError"
            self.log('write', {'log': 'Error:BatebaseCanNotConnect', 'level': 'error'})
        else:
            dbc.set(date[0], date[1])

    def GetDate(self, key, db):

        turn = 0
        while 0 == 0:
            if db == self.dburl[turn]:
                url = self.dburl[turn + 1]
            else:
                try:
                    test = self.dburl[turn + 2]
                except IndexError:
                    break
                else:
                    turn = turn + 2
        else:
            pass
        try:
            dbc = memcache.Client([url + ':11211'], debug=True)
        except:
            print "Error: datebaseCE"
            self.log.addLog("Error: BatebaseCanNotConnect", "error")
        else:
            return dbc.get(key)

    def ReplaceDate(self, date, db):

        turn = 0
        while 0 == 0:
            if db == self.dburl[turn]:
                url = self.dburl[turn + 1]
            else:
                try:
                    test = self.dburl[turn + 2]
                except IndexError:
                    break
                else:
                    turn = turn + 2
        else:
            pass
        try:
            dbc = memcache.Client([url + ':11211'], debug=True)
        except:
            print "Error: datebaseCE"
            self.log.addLog("Error: BatebaseCanNotConnect", "error")
        else:
            satates = dbc.replace(date[0], date[1])
            if satates == False or satates == 'False':
                print "Waring: NoThisKeyInThisDateBase"
                self.log("Waring: NoThisKeyInThisDateBase", "waring")
            else:
                print "Info: DatebaseReplaceComplete"

    def DeleteDate(self, key, db):

        turn = 0
        while 0 == 0:
            if db == self.dburl[turn]:
                url = self.dburl[turn + 1]
            else:
                try:
                    test = self.dburl[turn + 2]
                except IndexError:
                    break
                else:
                    turn = turn + 2
        else:
            pass
        try:
            dbc = memcache.Client([url + ':11211'], debug=True)
        except:
            print "Error: datebaseCE"
            self.log.addLog("Error: BatebaseCanNotConnect", "error")
        else:
            return dbc.delete(key)







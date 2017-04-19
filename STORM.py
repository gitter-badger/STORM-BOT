#! /usr/bin/env python
# -*- coding: utf-8 -*-
#  version 5.2.3
#  DEV BY ALI .B .OTH

import Kernal
import multiprocessing
import platform
import time

if __name__ == "__main__":

      try:
            np = multiprocessing.cpu_count()
            print 'You have {0:0} CPUs'.format(np)
            
            print
            print 'system   :', platform.system()
            print 'node     :', platform.node()
            print 'release  :', platform.release()
            print 'version  :', platform.version()
            print 'machine  :', platform.machine()
            print 'processor:', platform.processor()
            
            time.sleep(1)
            print '\nSTARTING ',
            
            for i in range(1, 6) :
                  time.sleep(1)
                  print '.', 
            if platform.python_version() < '2.7' or platform.python_version() >= '3.0':
                  print'\nYour python version is ', platform.python_version()
                  print '\nPlease install python 2.7'
                  print '\nEXITING ',
                  for i in range(1, 11) :
                        time.sleep(1)
                        print '.',                  
            else:
                  Kernal.start()

      except KeyboardInterrupt:
            print '\nKeyboard INTERUPT (Ctrl+C)\nFIX ERROR AND TRY AGIN ! '
      except:
            print '\n\nERROR !!\nDISCONNECTED'
            if platform.system() != 'Windows' :
                  print '\nNot tested on ', platform.system()
            print '\nPlease feedback: https://github.com/alosh55/STORM-BOT'
            time.sleep(100000)
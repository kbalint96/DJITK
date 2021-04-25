import socket
import threading
import time
from datetime import datetime


"""
def __str__(self):
        return self.firstName + " " + self.lastName
"""
class Tello:

    def __init__(self, name):
        self.name = name

    def doInit(self):

        self.response = "No response yet"

        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))

        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.tello_ip = '192.168.10.1'
        self.tello_port = 8889
        self.tello_adderss = (self.tello_ip, self.tello_port)
        self.log = []
        self.MAX_TIME_OUT = 10
        print (">> Name:    " + self.name)
        self.do("command")
        if (self.response == "No response yet"):
            print (">> Inicializalas nem sikerult!")
            exit()
        else:
            print (">> Inicializalas sikeres!")

    def do(self, command):
        self.log.append(Stats(command, len(self.log)))

        self.socket.sendto(command.encode('utf-8'), self.tello_adderss)
        #print "Command '" + command + "' is being processed by " + self.name

        start = time.time()
        while not self.log[-1].got_response():
            now = time.time()
            diff = now - start
            if diff > self.MAX_TIME_OUT:
                print 'Max timeout exceeded... command %s' % command
                return

        #print "Command '" + command + "' is processed by " + self.name

    def _do_not_sleep_thread(self):
        while True:
            self.do("command")

    def _receive_thread(self):
        while True:
            try:
                self.response, ip = self.socket.recvfrom(1024)
                print('from %s: %s' % (ip, self.response))
                self.log[-1].add_response(self.response)
            except socket.error, exc:
                print "Caught exception socket.error : %s" % exc


    def on_close(self):
        pass

    def get_log(self):
        return self.log

    def getActualResponse(self):
        print self.response
        return self.response

    def getBattery(self):
        self.do("battery?")
        print ">> Battery:      " + self.response
        return self.response

    def getSpeed(self):
        self.do("speed?")
        print ">> Speed:        " + self.response
        return self.response

    def getTime(self):
        self.do("time?")
        print ">> Flight time:  " + self.response
        return self.response

    def getWifiSNR(self):
        self.do("wifi?")
        print ">> WIFI SNR:     " + self.response
        return self.response

    def getSdk(self):
        self.do("sdk?")
        print ">> SDK version:  " + self.response

    def getSn(self):
        self.do("sn?")
        print ">> Serial number: " + self.response

    def takeOff(self):
        self.do("takeoff")

    def stop(self):
        self.do("stop")

    def land(self):
        self.do("land")

    def move(self, direction, x):
        self.do(direction + " " + str(x))

    def rotate(self, direction, x):
        command = ""
        if direction == "left":
            command = "cw"
        elif direction == "right":
            command = "ccw"
        self.do(command + " " + str(x))
        print command

    def flip(self, direction):
        command = "flip"
        if direction == "left" or "l":
            command += " l"
        elif direction == "right" or "r":
            command += " r"
        elif direction == "forward" or "f":
            command += " f"
        elif direction == "back" or "b":
            command += " b"
        self.do(command)
        print command

    def setSpeed(self, speed):
        self.do("speed " + str(speed))

class Stats:
    def __init__(self, command, id):
        self.command = command
        self.response = None
        self.id = id

        self.start_time = datetime.now()
        self.end_time = None
        self.duration = None

    def add_response(self, response):
        self.response = response
        self.end_time = datetime.now()
        self.duration = self.get_duration()
        #self.print_stats()

    def get_duration(self):
        diff = self.end_time - self.start_time
        return diff.total_seconds()

    def print_stats(self):
        print '\nid: %s' % self.id
        print 'command: %s' % self.command
        print 'response: %s' % self.response
        print 'start time: %s' % self.start_time
        print 'end_time: %s' % self.end_time
        print 'duration: %s\n' % self.duration

    def got_response(self):
        if self.response is None:
            return False
        else:
            return True

    def return_stats(self):
        str = ''
        str +=  '\nid: %s\n' % self.id
        str += 'command: %s\n' % self.command
        str += 'response: %s\n' % self.response
        str += 'start time: %s\n' % self.start_time
        str += 'end_time: %s\n' % self.end_time
        str += 'duration: %s\n' % self.duration
        return str
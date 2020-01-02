import os
clear = lambda: os.system('cls')

class TimeErrorControl:
    '''
    It calculates unexpected time errors'''
    def __init__(self,timeNow) :
        '''
        TimeErrors(timeNow)'''
        self.now = timeNow
        self.before = timeNow
        self.innerLoops = 0

    def checkTimeError(self,timeNow,frame,mustPrint=False):
        '''
        It checks any time errors each frame.fps frames
        TimeError.checkErrors(timeNow,Frame)'''
        self.innerLoops += 1

        if frame.newSecond :
            frame.timeOveralError = 0
            self.before = self.now
            self.now = timeNow
            frame.timeOveralError += frame.correctionFactor * ( self.now - self.before - 1 - frame.timeOveralError )
            if frame.timeOveralError<0 :
                frame.timeOveralError = 0

            if mustPrint :
                clear()
                print(f'''      Main loop -- It should be 1: {self.now-self.before}
                timeNow = {timeNow}, frame.timeNext = {frame.timeNext}
                frame.timeError         = {frame.timeError}
                frame.timeOveralError   = {frame.timeOveralError}
                frame.apfTimeError      = {frame.apfTimeError}
                frame.fpsCounter    = {frame.fpsCounter}
                frame.apsCounter    = {frame.apsCounter}
                innerLoops      = {self.innerLoops}''')

            self.innerLoops = 0

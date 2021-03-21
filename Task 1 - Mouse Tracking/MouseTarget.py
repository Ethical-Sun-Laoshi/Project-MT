#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on February 03, 2021, at 21:08
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, monitors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # hanTy system and path functions
import sys  # to get file system encoding
import pandas as pd

from psychopy.hardware import keyboard

# Importing library
import csv




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'mouseANDtarget'  # from the Builder filename that created this script
expInfo = {'participant': 'sun', 'session': '01A'}
#dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
#if dlg.OK == False:
#    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

## Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
##filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
mousefilename = 'mousePosition_' + expInfo['participant'] + '_' + expInfo['session']+'_' + expInfo['date'];
mousefile = mousefilename + '.csv'
targetfilename ='targetPosition_' + expInfo['participant'] + '_' + expInfo['session'] +'_' + expInfo['date'];
targetfile = targetfilename + '.csv'


# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\melis\\Desktop\\untitled.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
for mon in monitors.getAllMonitors():
    print('#######################    MONITOR    #################', mon, monitors.Monitor(mon).getSizePix())
win = visual.Window(
    fullscr=False, screen=0, size=(900, 900),
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix') ################################################### size : 1024,769  // 3840,2160 & FullScreen=True // units='height'
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()

# --------- AREA TARGET components
targetBG = visual.Rect(
    win=win, name='targetBG', size=(700, 700), units='pix',
    ori=0, pos=(0,0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='blue', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)



# --------- MOUSE components
mouse = event.Mouse(win=win)
win.setMouseType(name='crosshair') #the MOUSE cursor is a cross +
Mx, My = [None, None] # MOUSE positions in a list
mouse.mouseClock = core.Clock()
MposList=[] #initializing the list for the MOUSE positions

#--------- TARGET components
target = visual.Rect(
    win=win, name='target', size=(250, 150), units='pix',
    #width=(150, 150)[0], height=(150, 150)[1],#
    ori=0, pos=(-50,-50),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
#TposList=[[],[]]#initializing the list for the TARGET positions
Tx = -200 # x position of the TARGET
Ty = 50 # y position of the TARGET   <<<<<<<<<<<<--------------I'm trying to do like the mouse
Txspeed = 10
Tyspeed = 10
# * * * * boucing components * * * *
#ranTx = 0 # initializing the random x position for the target
#ranTy = 0 # initializing the random x position for the target
TposList=[] #initializing the list for the MOUSE positions

#--------- TOOLS FOR CONDITIONS components
mIOt=[] # MOUSE in/out TARGET    in list

xFloor = - targetBG.size[0]/2 #the center of the TARGET is located at the half of TARGET's width
xCeiling = targetBG.size[0]/2 ## if the center of the TARGET is positioned at the window's width-half of the TARGET
yFloor = - targetBG.size[1]/2 #the center of the TARGET is located at the half of TARGET's height
yCeiling = targetBG.size[1]/2 #if the center of the TARGET is positioned at the window's width-half of the TARGET
print('the window is ',win.units,' and the target is ',target.units) #TODO : remove
print('window "X" largeur ====',win.size[0],'xfloor ====== ',xFloor,'xceiling ==== ', xCeiling, 'size of the TARGET width ====', target.width)
print('window Y hauteur ====',win.size[1],'yfloor ====== ',yFloor,'yceiling ==== ', yCeiling, 'size of the TARGET height ====', target.height)


# Create some hanTy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine
##--------- TIMER TEXT component TODO : add
#timer : 2 minutes, 120 seconds : the participants can see how seconds left
timer = visual.TextStim(win=win, name='timer', text='default', font='Arial', pos=(-400,-400), height=20,colorSpace='rgb', opacity=1)

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(125.000000)  #____________ in seconds, default 10 = we had 125 seconds for the experiment lifetime
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
sameCount = 0
sameThresh = 300
sameWarning = 200
thisCol = "green"
# keep track of which components have finished
trialComponents = [mouse, target, timer,targetBG]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:

    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

    # update/draw components on each frame
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down alreaTy this ISN'T a new click
    if mouse.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mouse.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            mouse.tStop = t  # not accounting for scr refresh
            mouse.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mouse, 'tStopRefresh')  # time at next scr refresh
            mouse.status = FINISHED
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    MposList.append(mouse.getPos())

# --------> we can record if the user doesn't move their mouse for some frame (reminder : 1 second = 60 frames)
    if len(MposList) > 2:
        if MposList[-1][0] == MposList[-2][0]:
            if MposList[-1][1] == MposList[-2][1]:
                #print('same')
                sameCount += 1
        else:
            thisCol = "green"
            sameCount = 0

    if sameCount >= sameWarning:
        thisCol = "red"
    if sameCount >= sameThresh:
        #continueRoutine = False
        print(" mouse not moved for " + str(sameCount)+ " frames.")

   
   # *timer* updates
    if timer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        timer.frameNStart = frameN  # exact frame index
        timer.tStart = t  # local t and not account for scr refresh
        timer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(timer, 'tStartRefresh')  # time at next scr refresh
        timer.setAutoDraw(True)
    if timer.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > timer.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            timer.tStop = t  # not accounting for scr refresh
            timer.frameNStop = frameN  # exact frame index
            win.timeOnFlip(timer, 'tStopRefresh')  # time at next scr refresh
            timer.setAutoDraw(False)
    if timer.status == STARTED:  # only update if drawing
        timer.setColor("black", colorSpace='rgb')
        timer.setText("T I M E   L E F T : " + str(round(routineTimer.getTime(),2)) + " seconds")
        
        # *target background* updates
    if targetBG.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        targetBG.frameNStart = frameN  # exact frame index
        targetBG.tStart = t  # local t and not account for scr refresh
        targetBG.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
        targetBG.setAutoDraw(True)
    if targetBG.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > targetBG.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            targetBG.tStop = t  # not accounting for scr refresh
            targetBG.frameNStop = frameN  # exact frame index
            win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
            targetBG.setAutoDraw(False)
    
    # *target* updates
    if target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        target.frameNStart = frameN  # exact frame index
        target.tStart = t  # local t and not account for scr refresh
        target.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
        target.setAutoDraw(True)
    if target.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > target.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            target.tStop = t  # not accounting for scr refresh
            target.frameNStop = frameN  # exact frame index
            win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
            target.setAutoDraw(False)
    TposList.append(target.pos)

    
    if frameN % 6 == 0:
        print('frameN = ', frameN)
        
        
        Tx = Tx + Txspeed
        Ty = Ty + Tyspeed
        
        Tleft = Tx - (target.width/2)
        Tright = Tx + (target.width/2)
        Tbottom = Ty - (target.height/2)
        Ttop = Ty + (target.height/2)
        
        print ('Ttop =', Ttop,' ||| Tleft =',Tleft, '||| Tbottom = ', Tbottom, '||| Tright = ', Tright)
        
        if Tright >= xCeiling or Tleft <= xFloor:
            Txspeed = Txspeed * (-1)
        if Ttop >= yCeiling or Tbottom <= yFloor:
            Tyspeed = Tyspeed * (-1)        


        target.pos = [Tx, Ty]

    #check if the mouse is in the target
    if target.contains(mouse):
#        print('in')
        mIOt.append('in')
        target.fillColor='green'
    else:
#        print("out")
        mIOt.append('out')
        target.fillColor='red'

################### count(mouse x) pour compter le nombre de ligne (pour la moyenne)






    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)





###############################################################
x, y = mouse.getPos()
buttons = mouse.getPressed()
thisExp.addData('last x', x)
thisExp.addData('last y', y)
#thisExp.addData('mouse.leftButton', buttons[0])
#thisExp.addData('mouse.midButton', buttons[1])
#thisExp.addData('mouse.rightButton', buttons[2])
#thisExp.addData('mouse.started', mouse.tStart)
#thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.addData('x', MposList)
thisExp.nextEntry()
#print('MOUSE LIST', MposList)
#print('MOUSE ARRAY', MposArr)
#print('last mouse position', MposList[-1][0],  MposList[-1][1])
#print('TARGET LIST', TposList)
#print('TARGET ARRAY', TposArr)
thisExp.addData('target.started', target.tStartRefresh)
thisExp.addData('target.stopped', target.tStopRefresh)
###################################################################################################


########### FILE 2 ###########
## data to be written row-wise in csv fil
#data = MposList
##data  = MposArr   #######_csv.Error: iterable expected, not numpy.float64
#
## opening the csv file in 'a+' mode
#file = open(mousefile, 'a+', newline ='') ;
#
## writing the data into the file
#with file:
#    # identifying header
#    header = ['Mouse at x', 'Mouse at Y']
#    writer = csv.DictWriter(file, fieldnames = header)
#    writer.writeheader()
#    write = csv.writer(file)
#    write.writerows(data)
#
########### FILE 3 ###########
## data to be written row-wise in csv fil
##Tdata = TposArr
Tdata = TposList
del Tdata[0]
del Tdata[0]
# opening the csv file in 'a+' mode
#file = open(targetfile, 'a+', newline ='') ;
#
## writing the data into the file
#with file:
#    # identifying header
#    Theader = ['target at x', 'target at y']
#    writer = csv.DictWriter(file, fieldnames = Theader)
#    writer.writeheader()
#    write = csv.writer(file)
#    write.writerows(Tdata)
#
########## FILE 4 ###########
# data to be written row-wise in csv file
dataF = [[i[0],i[1],j[0],j[1],k,abs(i[0]-j[0]),abs(i[1]-j[1])] for i,j,k in zip(MposList,Tdata,mIOt)]
## opening the csv file in 'a+' mode
file = open("MouseTarget.csv", 'a+', newline ='') ;
# writing the data into the file
with file:
    # identifying header
    Fheader = ['Mouse at x', 'Mouse at Y', 'target at x', 'target at y', 'in or out', 'x difference', 'y difference']
    writer = csv.DictWriter(file, fieldnames = Fheader)
    writer.writeheader()
    write = csv.writer(file)
    write.writerows(dataF)



# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText('filename'+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

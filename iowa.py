#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on 十二月 17, 2020, at 20:01
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import random
random.seed(10)



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'Iowa Gambling Task'  # from the Builder filename that created this script
expInfo = {'被试编号': '', '性别': '', '驾龄': '', '实验类型': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['被试编号'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\workspace\\Python\\iowa\\iowa.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "inst"
instClock = core.Clock()
instruction = visual.TextStim(win=win, name='instruction',
    text='欢迎您参与本次实验！\n在实验中，屏幕上会呈现四张不同的纸牌，\n每次您可以从四张纸牌中任意选择一张(用鼠标点击即可)，\n每选一张，你会赢一些钱，但同时也可能会输一些钱。\n屏幕下方显示着你的初始钱数(你有2000元的本金)。\n这四张纸牌中有几张是好牌，如果您能尽量避免差的\n纸牌，从好牌中选的次数越多，您就可以赢得更多。\n您一共有100次选择的机会，可以通过点击扑克牌\n找到规律，以获得更多的奖励。',
    font='Microsoft YaHei UI',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_hint = visual.TextStim(win=win, name='key_hint',
    text='如果您看懂了以上内容，请点击空格键开始实验。',
    font='Microsoft YaHei UI',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
A = visual.ImageStim(
    win=win,
    name='A', 
    image='.\\image\\button.png', mask=None,
    ori=0, pos=[-0.6,0], size=[0.3,0.42],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
B = visual.ImageStim(
    win=win,
    name='B', 
    image='.\\image\\button.png', mask=None,
    ori=0, pos=[-0.2,0], size=[0.3,0.42],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
C = visual.ImageStim(
    win=win,
    name='C', 
    image='.\\image\\button.png', mask=None,
    ori=0, pos=[0.2,0], size=[0.3,0.42],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
D = visual.ImageStim(
    win=win,
    name='D', 
    image='.\\image\\button.png', mask=None,
    ori=0, pos=[0.6,0], size=[0.3,0.42],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "choose"
chooseClock = core.Clock()
state_Score = visual.TextStim(win=win, name='state_Score',
    text=None,
    font='Microsoft YaHei UI',
    pos=(0, -0.3), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
state_Gain = visual.TextStim(win=win, name='state_Gain',
    text=None,
    font='Microsoft YaHei UI',
    pos=(0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
# Set experiment start values for variable component Forfeit
Forfeit = ''
ForfeitContainer = []
# Set experiment start values for variable component Gain
Gain = ''
GainContainer = []
if str(expInfo['实验类型'])!='1':
    bgm = sound.Sound('./sound/'+str(expInfo['实验类型'])+'.wav')
    bgm.play(loops=-1)
# Set experiment start values for variable component Atimes
Atimes = 0
AtimesContainer = []
# Set experiment start values for variable component Btimes
Btimes = 0
BtimesContainer = []
# Set experiment start values for variable component Ctimes
Ctimes = 0
CtimesContainer = []
# Set experiment start values for variable component Dtimes
Dtimes = 0
DtimesContainer = []
# Set experiment start values for variable component Score
Score = 2000
ScoreContainer = []

# Initialize components for Routine "end"
endClock = core.Clock()
thank = visual.TextStim(win=win, name='thank',
    text=None,
    font='Microsoft YaHei UI',
    pos=(0, 0.1), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_score = visual.TextStim(win=win, name='end_score',
    text=None,
    font='Microsoft YaHei UI',
    pos=(0, -0.4), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
end_input = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "inst"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
instruction.wrapWidth = 1.3
# keep track of which components have finished
instComponents = [instruction, key_hint, key_resp]
for thisComponent in instComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inst"-------
while continueRoutine:
    # get current time
    t = instClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction* updates
    if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction.frameNStart = frameN  # exact frame index
        instruction.tStart = t  # local t and not account for scr refresh
        instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
        instruction.setAutoDraw(True)
    
    # *key_hint* updates
    if key_hint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_hint.frameNStart = frameN  # exact frame index
        key_hint.tStart = t  # local t and not account for scr refresh
        key_hint.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_hint, 'tStartRefresh')  # time at next scr refresh
        key_hint.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst"-------
for thisComponent in instComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "inst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=100, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trialComponents = [A, B, C, D, mouse]
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
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *A* updates
        if A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A.frameNStart = frameN  # exact frame index
            A.tStart = t  # local t and not account for scr refresh
            A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A, 'tStartRefresh')  # time at next scr refresh
            A.setAutoDraw(True)
        
        # *B* updates
        if B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B.frameNStart = frameN  # exact frame index
            B.tStart = t  # local t and not account for scr refresh
            B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B, 'tStartRefresh')  # time at next scr refresh
            B.setAutoDraw(True)
        
        # *C* updates
        if C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            C.frameNStart = frameN  # exact frame index
            C.tStart = t  # local t and not account for scr refresh
            C.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C, 'tStartRefresh')  # time at next scr refresh
            C.setAutoDraw(True)
        
        # *D* updates
        if D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            D.frameNStart = frameN  # exact frame index
            D.tStart = t  # local t and not account for scr refresh
            D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(D, 'tStartRefresh')  # time at next scr refresh
            D.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [A,B,C,D]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
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
    # store data for trials (TrialHandler)
    if len(mouse.clicked_name): trials.addData('mouse.clicked_name', mouse.clicked_name[0])
    cur_deck = mouse.clicked_name[0]
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "choose"-------
    continueRoutine = True
    # update component parameters for each repeat
    state_Score.setText('')
    state_Gain.setText('')
    Forfeit = 0  # Set routine start values for Forfeit
    Gain = 0  # Set routine start values for Gain
    ran = random.random()
    rate = 0
    if cur_deck == "A":
        Atimes += 1
        rate = 0.5
        if ran <= rate:
            Forfeit = -250
        Gain = 100
    elif cur_deck == "B":
        Btimes += 1
        rate = 0.1
        if ran <= rate:
            Forfeit = -1250
        Gain = 100
    elif cur_deck == "C":
        Ctimes += 1
        rate = 0.5
        if ran <= rate:
            Forfeit = -50
        Gain = 50
    elif cur_deck == "D":
        Dtimes += 1
        rate = 0.1
        if ran <= rate:
            Forfeit = -250
        Gain = 50
    Current = Gain + Forfeit
    Score += Current
    state_Score.setText('您的余额：'+str(Score)+'元')
    if Current == 0:
        state_Gain.setText('输赢相抵！')
        state_Gain.setColor('white')
    elif Current > 0:
        state_Gain.setText('恭喜您赢了'+str(Current)+'元')
        state_Gain.setColor('green')
    else :
        state_Gain.setText('抱歉，您输了'+str(abs(Current))+'元')
        state_Gain.setColor('red')
    # keep track of which components have finished
    chooseComponents = [state_Score, state_Gain]
    for thisComponent in chooseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    chooseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choose"-------
    while continueRoutine:
        # get current time
        t = chooseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=chooseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *state_Score* updates
        if state_Score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            state_Score.frameNStart = frameN  # exact frame index
            state_Score.tStart = t  # local t and not account for scr refresh
            state_Score.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(state_Score, 'tStartRefresh')  # time at next scr refresh
            state_Score.setAutoDraw(True)
        if state_Score.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > state_Score.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                state_Score.tStop = t  # not accounting for scr refresh
                state_Score.frameNStop = frameN  # exact frame index
                win.timeOnFlip(state_Score, 'tStopRefresh')  # time at next scr refresh
                state_Score.setAutoDraw(False)
        
        # *state_Gain* updates
        if state_Gain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            state_Gain.frameNStart = frameN  # exact frame index
            state_Gain.tStart = t  # local t and not account for scr refresh
            state_Gain.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(state_Gain, 'tStartRefresh')  # time at next scr refresh
            state_Gain.setAutoDraw(True)
        if state_Gain.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > state_Gain.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                state_Gain.tStop = t  # not accounting for scr refresh
                state_Gain.frameNStop = frameN  # exact frame index
                win.timeOnFlip(state_Gain, 'tStopRefresh')  # time at next scr refresh
                state_Gain.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in chooseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choose"-------
    for thisComponent in chooseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Atimes',Atimes)
    trials.addData('Btimes',Btimes)
    trials.addData('Ctimes',Ctimes)
    trials.addData('Dtimes',Dtimes)
    trials.addData('Score',Score)
    # the Routine "choose" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 100 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
end_score.setText('您最后拥有'+str(Score)+'元')
thank.setText('感谢您参与本次实验！\n您的被试编号为:'+str(expInfo['被试编号'])+\
'\n请您以此编号完成后续的\n《一般决策风格问卷》\n谢谢！')
bgm.stop()
end_input.keys = []
end_input.rt = []
_end_input_allKeys = []
# keep track of which components have finished
endComponents = [thank, end_score, end_input]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank* updates
    if thank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank.frameNStart = frameN  # exact frame index
        thank.tStart = t  # local t and not account for scr refresh
        thank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank, 'tStartRefresh')  # time at next scr refresh
        thank.setAutoDraw(True)
    
    # *end_score* updates
    if end_score.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_score.frameNStart = frameN  # exact frame index
        end_score.tStart = t  # local t and not account for scr refresh
        end_score.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_score, 'tStartRefresh')  # time at next scr refresh
        end_score.setAutoDraw(True)
    
    # *end_input* updates
    waitOnFlip = False
    if end_input.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_input.frameNStart = frameN  # exact frame index
        end_input.tStart = t  # local t and not account for scr refresh
        end_input.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_input, 'tStartRefresh')  # time at next scr refresh
        end_input.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_input.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_input.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_input.status == STARTED and not waitOnFlip:
        theseKeys = end_input.getKeys(keyList=None, waitRelease=False)
        _end_input_allKeys.extend(theseKeys)
        if len(_end_input_allKeys):
            end_input.keys = _end_input_allKeys[-1].name  # just the last key pressed
            end_input.rt = _end_input_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
trials.addData('C+D-A-B', Ctimes+Dtimes-Atimes-Btimes)
trials.addData('Atimes',Atimes)
trials.addData('Btimes',Btimes)
trials.addData('Ctimes',Ctimes)
trials.addData('Dtimes',Dtimes)
trials.addData('Score',Score)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

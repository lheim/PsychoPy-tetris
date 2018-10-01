#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on Mon Oct  1 13:34:49 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Tetris-Workload'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/nope/ownCloud/work/uka/code/psychoPy/psychoPy-tetris/Tetris-Workload-PsychoPy.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1422, 800], fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "IntroText"
IntroTextClock = core.Clock()
Intro1_text1 = visual.TextStim(win=win, name='Intro1_text1',
    text=u'In diesem Experiment lassen wir sie Tetris spielen und werden Ihnen dabei die Ger\xfcche Banane, Orange, Ledern Holz sowie einen Leerduft pr\xe4sentieren.\n\nIhre Aufgabe ist es, nach Ablauf der Spielzeit die Intensit\xe4t des Geruchs zu bewerten.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
Intro1_text2 = visual.TextStim(win=win, name='Intro1_text2',
    text=u'Weiter durch dr\xfccken der Leertaste.',
    font='Arial',
    pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "IntroText2"
IntroText2Clock = core.Clock()
Intro2_text = visual.TextStim(win=win, name='Intro2_text',
    text=u'Der Geruch wird Ihnen w\xe4hrend des Spielens in Bl\xf6cken pr\xe4sentiert. Atmen sie ruhig und normal.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
intro2_text2 = visual.TextStim(win=win, name='intro2_text2',
    text=u'Weiter durch dr\xfccken der Leertaste.',
    font='Arial',
    pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "IntroText3"
IntroText3Clock = core.Clock()
Intro3_text = visual.TextStim(win=win, name='Intro3_text',
    text=u'Nach jedem Duftstoff stoppt das Spiel und sie werden gebeten den Duftstoff auf einer Skala von 1-10 hinsichtlich seiner Intensit\xe4t zu bewerten.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
Intro3_text2 = visual.TextStim(win=win, name='Intro3_text2',
    text=u'Start des Experiments durch dr\xfccken der Leertaste.',
    font='Arial',
    pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Spacer"
SpacerClock = core.Clock()
spacer_text = visual.TextStim(win=win, name='spacer_text',
    text='Eine neue Runde Tetris startet bald...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Tetris"
TetrisClock = core.Clock()
import tetris
import serial

port = 'none' # when testing withOUT OLF
# port = serial.Serial('COM4', 19200, timeout=0.5) # when testing WITH OLF

text = visual.TextStim(win=win, name='text',
    text='Tetris finished\nit returned',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_val = visual.TextStim(win=win, name='text_val',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "rating_intensity"
rating_intensityClock = core.Clock()
intensity = visual.RatingScale(win=win, name='intensity', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=[''], scale=u'Bitte bewerten sie nun die Intensit\xe4t des vorangegangenen Duftstoffs. Dabei steht 1 f\xfcr eine niedrige Intensit\xe4t und 10 f\xfcr eine hohe Intensit\xe4t.', markerStart='5')

# Initialize components for Routine "rating_difficulty"
rating_difficultyClock = core.Clock()
difficulty = visual.RatingScale(win=win, name='difficulty', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=[''], scale=u'Bitte bewerten sie nun die Schwierigkeit der Runde, die sie gerade gespielt haben. 1 steht f\xfcr eine sehr einfache, 10 f\xfcr eine sehr schwere Runde.', markerStart='5')

# Initialize components for Routine "EndText"
EndTextClock = core.Clock()
EndText1 = visual.TextStim(win=win, name='EndText1',
    text='Byee...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "IntroText"-------
t = 0
IntroTextClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
IntroTextComponents = [Intro1_text1, Intro1_text2, key_resp_2]
for thisComponent in IntroTextComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "IntroText"-------
while continueRoutine:
    # get current time
    t = IntroTextClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro1_text1* updates
    if t >= 0.0 and Intro1_text1.status == NOT_STARTED:
        # keep track of start time/frame for later
        Intro1_text1.tStart = t
        Intro1_text1.frameNStart = frameN  # exact frame index
        Intro1_text1.setAutoDraw(True)
    
    # *Intro1_text2* updates
    if t >= 3.0 and Intro1_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Intro1_text2.tStart = t
        Intro1_text2.frameNStart = frameN  # exact frame index
        Intro1_text2.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "IntroText"-------
for thisComponent in IntroTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "IntroText" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "IntroText2"-------
t = 0
IntroText2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
IntroText2Components = [Intro2_text, intro2_text2, key_resp_3]
for thisComponent in IntroText2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "IntroText2"-------
while continueRoutine:
    # get current time
    t = IntroText2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro2_text* updates
    if t >= 0.0 and Intro2_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Intro2_text.tStart = t
        Intro2_text.frameNStart = frameN  # exact frame index
        Intro2_text.setAutoDraw(True)
    
    # *intro2_text2* updates
    if t >= 3.0 and intro2_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        intro2_text2.tStart = t
        intro2_text2.frameNStart = frameN  # exact frame index
        intro2_text2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroText2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "IntroText2"-------
for thisComponent in IntroText2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "IntroText2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "IntroText3"-------
t = 0
IntroText3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
IntroText3Components = [Intro3_text, Intro3_text2, key_resp_4]
for thisComponent in IntroText3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "IntroText3"-------
while continueRoutine:
    # get current time
    t = IntroText3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro3_text* updates
    if t >= 0.0 and Intro3_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Intro3_text.tStart = t
        Intro3_text.frameNStart = frameN  # exact frame index
        Intro3_text.setAutoDraw(True)
    
    # *Intro3_text2* updates
    if t >= 3.0 and Intro3_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Intro3_text2.tStart = t
        Intro3_text2.frameNStart = frameN  # exact frame index
        Intro3_text2.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroText3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "IntroText3"-------
for thisComponent in IntroText3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "IntroText3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
repeats = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('workload_data.xlsx'),
    seed=None, name='repeats')
thisExp.addLoop(repeats)  # add the loop to the experiment
thisRepeat = repeats.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
if thisRepeat != None:
    for paramName in thisRepeat:
        exec('{} = thisRepeat[paramName]'.format(paramName))

for thisRepeat in repeats:
    currentLoop = repeats
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
    if thisRepeat != None:
        for paramName in thisRepeat:
            exec('{} = thisRepeat[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Spacer"-------
    t = 0
    SpacerClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    SpacerComponents = [spacer_text]
    for thisComponent in SpacerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Spacer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = SpacerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *spacer_text* updates
        if t >= 0.0 and spacer_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            spacer_text.tStart = t
            spacer_text.frameNStart = frameN  # exact frame index
            spacer_text.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if spacer_text.status == STARTED and t >= frameRemains:
            spacer_text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SpacerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Spacer"-------
    for thisComponent in SpacerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Tetris"-------
    t = 0
    TetrisClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # to decrease runtime to speed up testing
    runtime = 5 # usualy runtime = 56
    
    logging.log(level=logging.EXP, msg='Starting Tetris ...')
    returnval = tetris.main(difficulty_level-1, runtime, thisExp, port, channel, logging)
    logging.log(level=logging.EXP, msg= 'Tetris returned: %d' %returnval)
    
    # to remove
    print('Tetris returned: %d' %returnval)
    
    key_resp_5 = event.BuilderKeyResponse()
    # keep track of which components have finished
    TetrisComponents = [text, key_resp_5, text_val]
    for thisComponent in TetrisComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Tetris"-------
    while continueRoutine:
        # get current time
        t = TetrisClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_5.keys = theseKeys[-1]  # just the last key pressed
                key_resp_5.rt = key_resp_5.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_val* updates
        if t >= 0.0 and text_val.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_val.tStart = t
            text_val.frameNStart = frameN  # exact frame index
            text_val.setAutoDraw(True)
        if text_val.status == STARTED:  # only update if drawing
            text_val.setText(returnval, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TetrisComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Tetris"-------
    for thisComponent in TetrisComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys=None
    repeats.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        repeats.addData('key_resp_5.rt', key_resp_5.rt)
    # the Routine "Tetris" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rating_intensity"-------
    t = 0
    rating_intensityClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    intensity.reset()
    # keep track of which components have finished
    rating_intensityComponents = [intensity]
    for thisComponent in rating_intensityComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "rating_intensity"-------
    while continueRoutine:
        # get current time
        t = rating_intensityClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *intensity* updates
        if t >= 0.0 and intensity.status == NOT_STARTED:
            # keep track of start time/frame for later
            intensity.tStart = t
            intensity.frameNStart = frameN  # exact frame index
            intensity.setAutoDraw(True)
        continueRoutine &= intensity.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rating_intensityComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rating_intensity"-------
    for thisComponent in rating_intensityComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for repeats (TrialHandler)
    repeats.addData('intensity.response', intensity.getRating())
    repeats.addData('intensity.rt', intensity.getRT())
    # the Routine "rating_intensity" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rating_difficulty"-------
    t = 0
    rating_difficultyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    difficulty.reset()
    # keep track of which components have finished
    rating_difficultyComponents = [difficulty]
    for thisComponent in rating_difficultyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "rating_difficulty"-------
    while continueRoutine:
        # get current time
        t = rating_difficultyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *difficulty* updates
        if t >= 0.0 and difficulty.status == NOT_STARTED:
            # keep track of start time/frame for later
            difficulty.tStart = t
            difficulty.frameNStart = frameN  # exact frame index
            difficulty.setAutoDraw(True)
        continueRoutine &= difficulty.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rating_difficultyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rating_difficulty"-------
    for thisComponent in rating_difficultyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for repeats (TrialHandler)
    repeats.addData('difficulty.response', difficulty.getRating())
    repeats.addData('difficulty.rt', difficulty.getRT())
    # the Routine "rating_difficulty" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'repeats'

# get names of stimulus parameters
if repeats.trialList in ([], [None], None):
    params = []
else:
    params = repeats.trialList[0].keys()
# save data for this loop
repeats.saveAsExcel(filename + '.xlsx', sheetName='repeats',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "EndText"-------
t = 0
EndTextClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndTextComponents = [EndText1]
for thisComponent in EndTextComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "EndText"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndTextClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndText1* updates
    if t >= 0.0 and EndText1.status == NOT_STARTED:
        # keep track of start time/frame for later
        EndText1.tStart = t
        EndText1.frameNStart = frameN  # exact frame index
        EndText1.setAutoDraw(True)
    frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if EndText1.status == STARTED and t >= frameRemains:
        EndText1.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndText"-------
for thisComponent in EndTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if port != 'none':
    serial.close()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

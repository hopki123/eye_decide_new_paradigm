from psychopy import core, visual, gui, data, event
import numpy, random
import clock as c
import trial as t
from config import *
from psychopy.iohub import launchHubServer
from psychopy.data import ExperimentHandler
from psychopy import gui

# Get user input for saving the data

myDlg = gui.Dlg(title="Experiment")
myDlg.addText('Subject info')
myDlg.addField('Name:')
myDlg.addField('Age:', 21)
myDlg.addText('Experiment Info')
myDlg.addField('Grating Ori:',45)
myDlg.addField('Group:', choices=["Test", "Control"])
ok_data = myDlg.show()  # show dialog and wait for OK or Cancel
if myDlg.OK:  # or if ok_data is not None
    print(ok_data)
else:
    print('user cancelled')

#if DUMMY == True:
#    iohub_config = {'eyetracker.hw.sr_research.eyelink.EyeTracker':
#                    {'name': 'tracker',
#                     'model_name': 'EYELINK 1000 DESKTOP',
#                     'runtime_settings': {'sampling_rate': 500,
#                                          'track_eyes': 'RIGHT'},
#                     'enable_interface_without_connection': True,
#                     'simulation_mode': True}
#                    }
#else:
#    iohub_config = {'eyetracker.hw.sr_research.eyelink.EyeTracker':
#                {'name': 'tracker',
#                 'model_name': 'EYELINK 1000 DESKTOP',
#                 'runtime_settings': {'sampling_rate': 500,
#                                      'track_eyes': 'RIGHT'},
#                 'default_native_data_file_name': str(ok_data[0])
#                }
#                }
#
#io = launchHubServer(**iohub_config)
#
## Get the eye tracker device.
#tracker = io.devices.tracker
#
## run eyetracker calibration
#r = tracker.runSetupProcedure()

# Create experiment handler to record user inputs
exp = ExperimentHandler(dataFileName='test')

# create window and stimuli
win = visual.Window([1920,1080],allowGUI=True,
                    monitor='testMonitor', units='deg')

# Create mouse
mouse = event.Mouse(win=win)
mouse.setVisible(visible=0)

# foil = visual.GratingStim(win, sf=1, size=4, mask='gauss',
#                           ori=expInfo['refOrientation'])
# target = visual.GratingStim(win, sf=1, size=4, mask='gauss',
#                             ori=expInfo['refOrientation'])
fixation = visual.GratingStim(win, color=-1, colorSpace='rgb',
                              tex=None, mask='circle', size=0.2)
# and some handy clocks to keep track of time
globalClock = core.Clock()
trialClock = core.Clock()

# display instructions and wait
message1 = visual.TextStim(win, pos=[0,+3],text='Hit a key when ready.')
message2 = visual.TextStim(win, pos=[0,-3],
    text="The experiment is about to start!")
message1.draw()
message2.draw()
fixation.draw()
win.flip()#to show our newly drawn 'stimuli'
#pause until there's a keypress
event.waitKeys()

test_trial = t.Trial(experiment_type='w')

#test_trial.run(win, mouse, event, tracker, report=True, exp=None, block_type=None, block_id=None, trial_number=None)

# Test the program without the eye-tracker
test_trial.run(win, mouse, event, report=True, exp=exp, block_type='w', block_id=1, trial_number=1)

exp.saveAsWideText(fileName='test.csv', delim=',')

win.close()
core.quit()

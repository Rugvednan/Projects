from vcScript import *
from vcMatrix import *
def OnSignal (signal ):
global triggerSignals, tasks
try:
if signal in triggerSignals:
task = signal.Name, signal.Value
tasks.append(task)
except:
pass
def OnRun():
global triggerSignals, tasks, Shuttle1_HomePositionValue, Shuttle1_WorkingPositionValue,
Shuttle2_WorkingPositionValue, Shuttle2_HomePositionValue, Piston_UpValue,
Piston_DownValue, Fixer_UpValue, Fixer_DownValue
global targets
Shuttle1_HomePositionValue = comp.getProperty('Shuttle1_HomePosition').Value
Shuttle1_WorkingPositionValue = comp.getProperty('Shuttle1_WorkingPosition').Value
Shuttle2_WorkingPositionValue = comp.getProperty('Shuttle2_WorkingPosition').Value
Shuttle2_HomePositionValue = comp.getProperty('Shuttle2_HomePosition').Value
Piston_UpValue = comp.getProperty('Piston_Up').Value
Piston_DownValue = comp.getProperty('Piston_Down').Value
Fixer_UpValue = comp.getProperty('Fixer_Up').Value
Fixer_DownValue = comp.getProperty('Fixer_Down').Value
tasks = []
triggerNames = ['From_PLC_Shuttle1HomePosition', 'From_PLC_Shuttle1WorkingPosition',
'From_PLC_Shuttle2HomePosition','From_PLC_Shuttle2WorkingPosition','From_PLC_PistonUp
, 'From_PLC_PistonDown', 'From_PLC_FixerUp','From_PLC_FixerDown', 'task']
triggerSignals = map (comp.findBehaviour, triggerNames)
# MAIN LOOP
while True:
condition (lambda: tasks)
stats.State = "Idle"
#triggerCondition (lambda: getTrigger() == task)
if tasks:
signal_name, signal_val = tasks.pop(0)
stats.State = "Busy"
## Connectivity events
if signal_name == "From_PLC_Shuttle1HomePosition" and signal_val:
MoveShuttle1(False)
elif signal_name == "From_PLC_Shuttle1WorkingPosition" and signal_val:
MoveShuttle1(True)
elif signal_name == "From_PLC_Shuttle2HomePosition" and signal_val:
MoveShuttle2(False)
elif signal_name == "From_PLC_Shuttle2WorkingPosition" and signal_val:
MoveShuttle2(True)
elif signal_name == "From_PLC_FixerUp" and signal_val:MoveFixer(False)
elif signal_name == "From_PLC_FixerDown" and signal_val:
MoveFixer(True)
elif signal_name == "From_PLC_PistonUp" and signal_val:
MovePiston(False)
elif signal_name == "From_PLC_PistonDown" and signal_val:
MovePiston(True)
#Works process
elif signal_name == "task":
worksProcess()
def MoveShuttle1(Back):
if Back:
Shuttle1servo.setJointTarget(0, Shuttle1_WorkingPositionValue)
Shuttle1servo.move()
else:
Shuttle1servo.setJointTarget(0, Shuttle1_HomePositionValue)
Shuttle1servo.move()
def MoveShuttle2(Back):
if Back:
Shuttle2servo.setJointTarget(0, Shuttle2_WorkingPositionValue)
Shuttle2servo.move()
else:
Shuttle2servo.setJointTarget(0, Shuttle2_HomePositionValue)
Shuttle2servo.move()
def MoveFixer(Down):
if Down:
Fixerservo.setJointTarget(0, Fixer_DownValue)
Fixerservo.move()
else:
Fixerservo.setJointTarget(0, Fixer_UpValue)
Fixerservo.move()
def MovePiston(Down):
if Down:
Pistonservo.setJointTarget(0, Piston_DownValue)
Pistonservo.move()
else:
Pistonservo.setJointTarget(0, Piston_UpValue)
Pistonservo.move()
comp = getComponent()
app = getApplication()
Shuttle1servo = comp.findBehaviour('Servo_Controller_Shuttle1')
Shuttle2servo = comp.findBehaviour('Servo_Controller_Shuttle2')
Fixerservo = comp.findBehaviour('Servo Controller_Fixer')
Pistonservo = comp.findBehaviour('Servo Controller_Piston')
stats = comp.getBehaviour('Statistics')
Shuttle1Front = comp.findBehaviour('From_PLC_Shuttle1HomePosition')
Shuttle1Back = comp.findBehaviour('From_PLC_Shuttle1WorkingPosition')
Shuttle2Front = comp.findBehaviour('From_PLC_Shuttle2HomePosition')
Shuttle2Back = comp.findBehaviour('From_PLC_Shuttle2WorkingPosition')
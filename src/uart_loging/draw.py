import matplotlib.pyplot as plt
import random


max_delay = 1.8
max_error = 0.1
max_time_error = 0.1
roll = []
pitch = []
roll_after = []
pitch_after = []
time = []
time_delay_roll = []
time_delay_pitch = []
count = 0
#read_log
f = open("logging.txt", "r")
for line in f:
    if(line == "\n"):
        continue 
    line = line.strip() 
    my_split = line.split(" ")
    roll.append(float(my_split[2]))
    pitch.append(float(my_split[8]))
    roll_after.append(  (float(my_split[2]) / 15) + random.uniform(-max_error, max_error))
    pitch_after.append( (float(my_split[8]) / 15) + random.uniform(-max_error, max_error))
    time.append(count)
    time_delay_roll.append(  count + (float(my_split[2]) / 50.0) + random.uniform(-max_time_error, max_time_error))
    time_delay_pitch.append( count + (float(my_split[8]) / 50.0) + random.uniform(-max_time_error, max_time_error))
    count = count + 1
start = 0
stop = 2000
plt.plot(time[start:stop], roll[start:stop], '-', label='roll')
plt.plot(time[start:stop], pitch[start:stop], '-', label='pitch')
plt.plot(time_delay_roll[start:stop], roll_after[start:stop], '-', label='roll after')
plt.plot(time_delay_pitch[start:stop], pitch_after[start:stop], '-', label='pitch after')
plt.legend(loc='best')

#plt.plot(x,y)
plt.xlabel('time (ms)')
plt.ylabel('angle')
#plt.title("PID Test (P = 12, i = 10, D = 0.1 Setpoint = 100)")
plt.grid(True)
plt.show()
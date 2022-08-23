from datetime import datetime
from playsound import playsound

now = datetime.now()
c_h = now.strftime("%I")
c_m = now.strftime("%M")
c_s = now.strftime("%S")
    
alarm_time = input("Enter alarm time in: HH:MM:SS\n")
h = alarm_time[0:2]
m = alarm_time[4:5]
s = alarm_time[7:8]
p = alarm_time[10:11].upper()

print("setting alarm.....")


while True:
    now = datetime.now()
    c_h = now.strftime("%I")
    c_m = now.strftime("%M")
    c_s = now.strftime("%S")
    c_p = now.strftime("%p")
    if(p == c_p):
        if(h== c_h):
            if(m == c_m):
                if(s == c_s):
                    print("wake up......")
                    playsound('audio.mp3')
                    break


    

import pygame
import datetime
import time

def Set_time(Alarm_time):
    print(f"Alarm set for {Alarm_time}")
    sound_file=".\sound.mp3"
    is_running=True

    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time==Alarm_time:
            print("Wake up !")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running=False

        time.sleep(1)



if __name__=="__main__":
    Alarm_time=input("Set the time for Alarm : ")
    Set_time(Alarm_time)


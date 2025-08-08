import time
from plyer import notification

is_running=True

while is_running:
    print("sip some water !")
    notification.notify(title="Please drink some water !",
                        message="hey you need to drink water !",)
    time.sleep(5)
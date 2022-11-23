from threading import Timer
# from datetime import datetime
import datetime
import schedule
import time
import character_misspellings


def scheduled_events():
    print("Here I am")


schedule.every(4).seconds.do(scheduled_events)
while True:
    schedule.run_pending()



# for i in range(0, 99999999999999):
#     x = datetime.datetime.now()
#     time.sleep(1)

#     d1 = x.strftime("%d/%m/%Y")
#     # print(d1)

#     now = datetime.datetime.now()
#     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#     seconds = now.strftime("%S")
#     print(seconds)




# now = datetime.datetime.now()
# seconds = now.strftime("%S")

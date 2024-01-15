from datetime import datetime
from dateutil import tz

time = str(datetime.now())
timeb = datetime.now()
print(time[11:19])

time_reunion = timeb.astimezone(tz.gettz('Indian/Reunion')).time()
time_paris = timeb.astimezone(tz.gettz('Europe/Paris')).time()

print(time_paris, time_reunion)

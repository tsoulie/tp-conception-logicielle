from datetime import datetime
from dateutil import tz
import logging

timezone = 0

logging.basicConfig(filename=None, encoding='utf-8', level=logging.DEBUG)

logging.info(f"Lancement du traitement")
logging.debug(f"Demande d'heure sur le timezone : {timezone}")

if timezone is None:
    logging.error("aucune timezone n'a été renseignée")
    raise ValueError("aucune timezone n'a été renseignée")

def get_date_formatted(timezeone):
    date= datetime.now(timezeone)
    return date.strftime("%H:%M:%S")


time = str(datetime.now())
timeb = datetime.now()
print(time[11:19])

time_reunion = timeb.astimezone(tz.gettz('Indian/Reunion')).time()
time_paris = timeb.astimezone(tz.gettz('Europe/Paris')).time()

print(time_paris, time_reunion)


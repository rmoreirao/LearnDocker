from datetime import datetime
import pytz

tz = pytz.timezone('US/Pacific')
datetime_1 = datetime.now(tz)
print(str(datetime_1))
import datetime

import pytz


_tz = pytz.timezone("America/New_York")


def now():
    "Return tz-aware version of current time."
    return _tz.localize(datetime.datetime.now())


def year_ago():
    "Return tz-aware version of time at 12:01 AM a year ago."
    d = datetime.date.today()
    d = d.replace(year=d.year - 1)
    t = datetime.time(hour=12, minute=1, second=0)
    dt = datetime.datetime.combine(d, t)
    return _tz.localize(dt)

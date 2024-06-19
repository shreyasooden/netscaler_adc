from datetime import datetime

def compare_datetimes(datetime1, datetime2, format="%Y-%m-%d %H:%M:%S"):
    dt1 = datetime.strptime(datetime1, format)
    dt2 = datetime.strptime(datetime2, format)
    return dt1 < dt2

class FilterModule(object):
    def filters(self):
        return {
            'compare_datetimes': compare_datetimes
        }

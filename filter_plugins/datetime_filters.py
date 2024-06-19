from datetime import datetime

def compare_datetimes(datetime1, datetime2, datetime3, format="%Y-%m-%d %H:%M:%S"):
    dt1 = datetime.strptime(datetime1, format)
    dt2 = datetime.strptime(datetime2, format)
    dt3 = datetime.strptime(datetime3, format)
    return dt1 < dt3 < dt2

class FilterModule(object):
    def filters(self):
        return {
            'compare_datetimes': compare_datetimes
        }

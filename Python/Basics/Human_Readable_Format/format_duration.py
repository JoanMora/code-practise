class Switcher(object):
    def indirect(self,i,value):
        self.value = value
        method_name=str(i)
        method=getattr(self,method_name,lambda :'Invalid')
        return method()

    def year(self):
        year = 'year' if(self.value == 1) else 'years'
        return f"{self.value} {year}"

    def day(self):
        day = 'day' if(self.value == 1) else 'days'
        return f"{self.value} {day}"

    def hour(self):
        hour = 'hour' if(self.value == 1) else 'hours'
        return f"{self.value} {hour}"

    def min(self):
        mins = 'minute' if(self.value == 1) else 'minutes'
        return f"{self.value} {mins}"

    def sec(self):
        sec = 'second' if(self.value == 1) else 'seconds'
        return f"{self.value} {sec}"



def compute_time(seconds):
    years = int(seconds / 31536000)
    seconds -= years * 31536000
    days = int(seconds / 86400)
    seconds -= days * 86400
    hours = int(seconds / 3600)
    seconds -= hours * 3600
    minutes = int(seconds / 60)
    seconds -= minutes * 60
    return (years, days, hours, minutes, seconds)



def format_duration(seconds):
    if(seconds == 0): return 'now'
    time = zip(('year','day','hour','min','sec'),compute_time(seconds))
    s=Switcher()
    l = []
    for unit,value in time:
        if(value):
            l.append(s.indirect(unit,value))

    if(len(l)==1): result = l[0]
    elif(len(l)==2): result = ' and '.join(l)
    else:
        last = l.pop()
        result = l.pop(0)
        for item in l:
            result = f"{result}, {item}"
        result = f"{result} and {last}"

    return result



def test_format_duration():
    assert format_duration(1) == "1 second"
    assert format_duration(62) == "1 minute and 2 seconds"
    assert format_duration(120) == "2 minutes"
    assert format_duration(3600) == "1 hour"
    assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"
    assert format_duration(0) == "now"
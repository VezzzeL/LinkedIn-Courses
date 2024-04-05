import calendar

show_expected_result = False
show_hints = False

def count_days(year, month, whichday):
    count = 0
    wlist = calendar.monthcalendar(year, month)
    for w in wlist:
        if(w[whichday] != 0):
            count += 1
    return count
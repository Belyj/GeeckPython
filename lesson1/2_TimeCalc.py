seconds = input('vvedi secundy:\n')
minutes = 0
hours = 0
delimetr = 60

fstr = '{}:{}:{}'

if seconds.isdigit():
    seconds = int(seconds)
    minutes = seconds // delimetr
    seconds -= minutes * delimetr
    hours = minutes // delimetr
    minutes -= hours * delimetr
    print(fstr.format(hours, minutes, seconds))
else:
    print('Eto bylo ne chislo')

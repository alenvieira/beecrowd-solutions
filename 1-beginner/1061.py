from datetime import timedelta

days_start=int(input().split(' ')[1])
hours_start, minutes_start, seconds_start =[int(value) for value in input().split(':')]
days_end=int(input().split(' ')[1])
hours_end, minutes_end, seconds_end =[int(value) for value in input().split(':')]
d_start = timedelta(days=days_start, hours=hours_start, minutes=minutes_start, seconds=seconds_start)
d_end = timedelta(days=days_end, hours=hours_end, minutes=minutes_end, seconds=seconds_end)
delta = d_end - d_start
total_minute, second = divmod(delta.seconds, 60)
hour, minute = divmod(total_minute, 60)
print('{} dia(s)'.format(delta.days))
print('{} hora(s)'.format(hour))
print('{} minuto(s)'.format(minute))
print('{} segundo(s)'.format(second))

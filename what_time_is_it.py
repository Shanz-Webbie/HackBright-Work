what_time_is_it = input("What time is it currently in hours?")
how_many_hours_to_wait = input("How many hours would you like to wait for the alarm?")

current_time = int(what_time_is_it)
hours_waited = int(how_many_hours_to_wait)

total_hours = current_time + hours_waited

hours_in_day = total_hours % 24

print(hours_in_day)
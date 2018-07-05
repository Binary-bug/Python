import time
print('process_time\t\t\t\t',time.get_clock_info("process_time"))
print('perf_counter\t\t\t\t',time.get_clock_info('perf_counter'))
print('time\t\t\t\t',time.get_clock_info('time'))
print('monotonic\t\t\t\t',time.get_clock_info('monotonic'))
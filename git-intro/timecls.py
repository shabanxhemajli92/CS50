class Time:
    """Represents the time of day"""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)   

    # def print_time(Time):
    #     print('%.2d:%.2d:%.2d' % (time.hour,time.minute,time.second))

    # def increment(self,seconds):
    #     seconds += self.time_to_int()
    #     return int_to_time(seconds)    
start =Time(9,45)
start.hour = 9
start.minute = 45
start.second = 00
start.Time() 

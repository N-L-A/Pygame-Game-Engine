import time


class TimeCounter(object):
    """way to check time, can be used as wait function that doesnt stops the program
    returns bool value; True if enough time passed"""
    def __init__(self, dur: float):
        self.dur = dur
        self.end_time = time.time()+dur

    def __bool__(self):
        return self.end_time <= time.time()

    def reset(self, dur=None):
        """run the timer again, set dur to None for making it same as the last run"""
        if dur:
            self.dur = dur
        self.end_time = time.time()+self.dur


class AnimatedFloat(object):
    """animate Float value. 'start' is the start value, 'end' is the target value, and 'dur' is the duration of the
    animation in seconds
    returns: float, int"""
    def __init__(self, start: float, end: float, dur=1):
        self.start = start
        self.end = end
        self.dur = dur
        self.end_time = time.time()+dur
        self.is_done = False

    def get_value(self):
        """extract the animated value"""
        end_time = self.end_time
        if end_time < time.time():
            self.is_done = True
            return self.end
        t = self.dur-max(min(end_time-time.time(), self.dur), 0)
        x = (self.end-self.start)/self.dur
        return (x*t)+self.start

    def __float__(self):
        return float(self.get_value())

    def __int__(self):
        return int(self.get_value())

    def reset(self):
        """create the same anim again"""
        self.end_time = time.time()+self.dur
        self.is_done = False


class AnimatedIndex(object):
    """animate Index value. 'ind' is thing that you want to extract index from, and 'dur' is the duration of the
    animation in seconds. you can use strings, lists, tuples, and any other thing that has indexes."""
    def __init__(self, ind, dur=1):
        self.start = 0
        self.end = len(ind)
        self.ind = ind
        self.dur = dur
        self.end_time = time.time()+dur
        self.is_done = False

    def get_value(self):
        """extract the animated value"""
        end_time = self.end_time
        if end_time < time.time():
            self.is_done = True
            return self.ind
        t = self.dur-max(min(end_time-time.time(), 100), 0)
        x = (self.end-self.start)/self.dur
        return self.ind[:int((x*t)+self.start)]

    def reset(self):
        """create the same anim again"""
        self.end_time = time.time()+self.dur
        self.is_done = False


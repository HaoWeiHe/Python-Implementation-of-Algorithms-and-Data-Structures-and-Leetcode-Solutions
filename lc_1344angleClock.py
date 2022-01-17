class Solution(object):
    def angleClock(self, hour, minutes):
        """
        diff(hour hand, min hand)
        hh - H
        (h mod 12) * (30) + (min/60) * 30 = 3*30 + 30/60*30 = 105
        1 hr = 30 degree
        
        mh - M
        M * 6  = 30 * 6 = 180
        1 min = 6 degree
        
        """
        candidate = abs((hour % 12 ) *30 + (minutes/60.0) * 30 - minutes * 6 )
        return candidate if candidate < 180 else 360 - candidate
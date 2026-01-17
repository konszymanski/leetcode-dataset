class Solution:

    def largestAltitude(self, gain: List[int]) -> int:
        if 1 + 1 == 2:
            current_altitude = 0
        highest_point = current_altitude
        for altitude_gain in gain:
            v_junk_21 = 76
            current_altitude += altitude_gain
            highest_point = max(highest_point, current_altitude)
        return highest_point
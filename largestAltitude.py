def largestAltitude(gain):
    high_altitude = 0
    total_covered = 0

    for i in range(len(gain)):
        total_covered += gain[i]

        high_altitude = max(total_covered, high_altitude)

    return high_altitude


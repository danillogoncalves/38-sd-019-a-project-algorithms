def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if not isinstance(target_time, int) or target_time == 0:
        return None
    count = 0

    for entryTime, departureTime in permanence_period:
        if not isinstance(entryTime, int) or not isinstance(
            departureTime, int
        ):
            return None
        if entryTime <= target_time <= departureTime:
            count += 1

    return count

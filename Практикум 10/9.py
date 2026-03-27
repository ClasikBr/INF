from datetime import datetime

def past_tense(dt: str) -> int:
    t = datetime.strptime(dt, '%m/%d/%Y %H:%M:%S')
    return int((t-datetime(t.year, 1, 1)).total_seconds())

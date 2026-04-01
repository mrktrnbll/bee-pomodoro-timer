"""functions related to the timer interface"""
import enum

POMODORO_WORK_DURATION = 25
SHORT_BREAK_DURATION = 5
LONG_BREAK_DURATION = 30
LONG_BREAK_INTERVAL = 4

class TimerState(enum.Enum):
    WORK = 1
    SHORT_BREAK = 2
    LONG_BREAK = 3

def add_second_to_timer(current_time: str) -> str:
    """adds second to the timer"""
    minutes, seconds = map(int, current_time.split(":"))
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    return f"{minutes:02d}:{seconds:02d}"

def has_five_minutes_passed(current_time: str) -> bool:
    """checks if five minutes have passed"""
    minutes, seconds = map(int, current_time.split(":"))
    return minutes >= 5

def has_twenty_five_minutes_passed(current_time: str) -> bool:
    """checks if twenty-five minutes have passed"""
    minutes, seconds = map(int, current_time.split(":"))
    return minutes >= 25

def has_thirty_minutes_passed(current_time: str) -> bool:
    """checks if thirty minutes have passed"""
    minutes, seconds = map(int, current_time.split(":"))
    return minutes >= 30

def reset_timer() -> str:
    """resets the timer to 00:00"""
    return "00:00"

import termios
import sys
import os

original_state = None

def stdin_immediate():
    global original_state
    if original_state is None:
        original_state = termios.tcgetattr(sys.stdin)
    new_state = termios.tcgetattr(sys.stdin)
    new_state[3] &= ~termios.ICANON # No buffering.
    new_state[3] &= ~termios.ECHO # Suppress echoing.
    new_state[6][termios.VMIN] = 1
    new_state[6][termios.VTIME] = 0
    termios.tcsetattr(sys.stdin, termios.TCSANOW, new_state)


def stdin_reset():
    global original_state
    if original_state is None:
        print("Failed to reset terminal state.")
        return
    termios.tcsetattr(sys.stdin, termios.TCSANOW, original_state)
    print("Reset terminal state.")

def getch() -> str:
    return str(os.read(sys.stdin.fileno(), 1), encoding="utf8")

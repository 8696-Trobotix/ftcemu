import atexit

import terminal
import launch

@atexit.register
def reset_term_state():
    print("Cleaning up terminal state.")
    terminal.stdin_reset()

def main():
    terminal.stdin_immediate()

    print("""
Daemon started.

0 - Extract, Embed, and Run
1 - Extract
2 - Embed
3 - Run
q - Quit
""")

    while (option := terminal.getch()) != 'q':
        match option:
            case '0':
                launch.extract()
                launch.embed()
                launch.run()
            case '1':
                launch.extract()
            case '2':
                launch.embed()
            case '3':
                launch.run()

if __name__ == "__main__":
    main()

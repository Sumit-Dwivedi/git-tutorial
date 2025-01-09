import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_CYAN)
    curses.init_pair(2,curses.COLOR_MAGENTA,curses.COLOR_YELLOW)
    BLUE_AND_CYAN= curses.color_pair(1)
    MAGNETA_AND_YELLOW= curses.color_pair(2)
    stdscr.clear()
    stdscr.addstr("Welcome to the Terminal games",curses.A_BOLD | MAGNETA_AND_YELLOW)
    stdscr.addstr(4,0,"Which game you want to play?",curses.A_STANDOUT)
    stdscr.addstr(5,10,"1] X or O")
    stdscr.addstr(6,10,"2] Chess")
    stdscr.refresh()
    # wind=curses.newwin(1,20,15,50)
    # for i in range(100):
    #     wind.clear()
    #     try:
    #         wind.addstr(f"Loading {i}% ---", BLUE_AND_CYAN)
    #         wind.refresh()
    #         time.sleep(0.01)
    #     except curses.error:
    #         pass
    pad=curses.newpad(100,100)
    for i in range(100):
        for j in range(26):
            k=chr(j+65)
            pad.addstr(k,MAGNETA_AND_YELLOW)
    
    for i in range(50):
        pad.refresh(0,0,7,5,20,50)
        time.sleep(0.2)
    stdscr.getch()
wrapper(main)
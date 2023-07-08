#Process strings to print to terminal with margins and stuff

#imports
import os

def left_margin(string: str, margin: int = 1):
    display_width = os.get_terminal_size()[0]
    processed_string = []
    for i in range(0, len(string), display_width - margin):
        processed_string.append(' '*margin + string[i:i+display_width - margin])

    return processed_string
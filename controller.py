import os


class Controller:
    def __init__(self):
        self.COMMANDS = {
            'Closed_Fist': self.__scroll_down,
            'Open_Palm': self.__view_windows,
            'Pointing_Up': self.__space_bar,
            'Thumb_Down': self.__switch_desktop_left,
            'Thumb_Up': self.__switch_desktop_right,
            'Victory': self.__zoom_out,
            'ILoveYou': self.__zoom_in
        }

    def issue_command(self, gesture):
        self.COMMANDS[gesture]()

    def __switch_desktop_left(self):
        os.system("osascript -e 'tell application \"System Events\" to key code  123  using control down'")

    def __switch_desktop_right(self):
        os.system("osascript -e 'tell application \"System Events\" to key code  124  using control down'")

    def __view_windows(self):
        os.system("osascript -e 'tell application \"System Events\" to key code  160  '")

    def __space_bar(self):
        os.system("osascript -e 'tell application \"System Events\" to key code  49  '")

    def __scroll_down(self):
        return

    def __scroll_up(self):
        return

    def __zoom_out(self):
        return

    def __zoom_in(self):
        return

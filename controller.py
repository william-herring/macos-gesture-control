import os


class Controller:
    def switch_desktop_left(self):
        pass

    def switch_desktop_right(self):
        pass

    def space_bar(self):
        pass

    def scroll_down(self):
        pass

    def scroll_up(self):
        pass

    def zoom_out(self):
        pass

    def zoom_in(self):
        pass

    COMMANDS = {
        'wave_right': switch_desktop_left,
        'wave_left': switch_desktop_right,
        'stop_gesture': space_bar,
        'two_fingers_up': scroll_up,
        'two_fingers_down': scroll_down,
        'pinch': zoom_out,
        'release_pinch': zoom_in
    }

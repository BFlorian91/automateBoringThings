import time
import threading
from pynput.keyboard import KeyCode, Listener, Controller

# REPEAT TIME
delay = 1
toggle_key = KeyCode(char='=')
exit_key = KeyCode(char='p')

# List of KEYPRESS
spell_1 = KeyCode(char='h')
spell_2 = KeyCode(char='j')
spell_3 = KeyCode(char='k')
spell_4 = KeyCode(char='l')

class KeyGenerator(threading.Thread):
    def __init__(self, delay, spell_1, spell_2, spell_3, spell_4):
        super(KeyGenerator, self).__init__()
        self.delay = delay
        self.spell_1 = spell_1
        self.spell_2 = spell_2
        self.spell_3 = spell_3
        self.spell_4 = spell_4
        self.running = False
        self.program_running = True

    def start_keysend(self):
        self.running = True

    def stop_keysend(self):
        self.running = False

    def exit(self):
        self.stop_keysend()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                keyboard.press(self.spell_1)
                keyboard.press(self.spell_2)
                keyboard.press(self.spell_3)
                keyboard.press(self.spell_4)
                time.sleep(self.delay)

keyboard = Controller()
keypress_thread = KeyGenerator(delay, spell_1, spell_2, spell_3, spell_4)
keypress_thread.start()

def on_press(key):
    if key == toggle_key:
        if keypress_thread.running:
            keypress_thread.stop_keysend()
        else:
            keypress_thread.start_keysend()
    elif key == exit_key:
        keypress_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()    
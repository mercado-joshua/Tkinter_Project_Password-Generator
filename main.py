#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd

import string
import random

class Password:
    """Creates Password."""
    def __init__(self, adjectives, nouns):
        self._adjectives = adjectives
        self._nouns = nouns

        self._adjective = random.choice(self._adjectives)
        self._noun = random.choice(self._nouns)
        self._number = random.randrange(0, 100)
        self._special_char = random.choice(string.punctuation)

    # ------------------------------------------
    def generate(self):
        password = f'{self._adjective}{self._noun}{str(self._number)}{self._special_char}'
        return password

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""

    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self._init_config()
        self._init_vars()
        self._init_widgets()

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def _init_config(self):
        self.resizable(False, False)
        self.title('Password Generator Version 1.0')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #------------------------------------------
    # Instance Variables
    #------------------------------------------
    def _init_vars(self):
        self._adjectives = [
            'sleepy', 'slow', 'smelly', 'wet', 'fat',
            'red', 'orange', 'yellow', 'green', 'blue',
            'purple', 'fluffy', 'white', 'proud', 'brave'
            ]

        self._nouns = [
            'apple', 'dinosaur', 'ball', 'toaster', 'goat',
            'dragon', 'hammer', 'duck', 'panda', 'cobra'
            ]

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def _init_widgets(self):

        frame = self._create_frame(self,
            side=tk.TOP, fill=tk.BOTH, expand=True)

        fieldset = self._create_fieldset(frame, 'Create Password',
            side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.password = tk.StringVar()
        self._create_entry(fieldset, '', self.password, 'Helvetica 20 bold',
            fill=tk.X, padx=10, pady=10, ipady=10)

        self._create_button(fieldset, 'Generate', self._create_password,
            pady=(0, 10))

    # INSTANCE ---------------------------------
    def _create_frame(self, parent, **kwargs):
        frame = ttk.Frame(parent)
        frame.pack(**kwargs)
        return frame

    def _create_fieldset(self, parent, title, **kwargs):
        fieldset = ttk.LabelFrame(parent, text=title)
        fieldset.pack(**kwargs)
        return fieldset

    def _create_button(self, parent, title, method, **kwargs):
        button = ttk.Button(parent, text=title, command=lambda: method())
        button.pack(**kwargs)
        return button

    def _create_entry(self, parent, title, var_, font, **kwargs):
        entry = ttk.Entry(parent, text=title, textvariable=var_, font=font)
        entry.pack(**kwargs)
        return entry

    def _create_password(self):
        password = Password(self._adjectives, self._nouns)
        self.password.set(password.generate())


#===========================
# Start GUI
#===========================

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()
from typing import Any

from ..views.home_menu_view import HomeMenuView


class ApplicationController:
    """???"""

    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = MainMenuController()
        while self.controller:
            self.controller = self.controller()


class MainMenuController:
    """Main Menu."""
    def __init__(self):
        self.view = HomeMenuView()

    def __call__(self):
        #appelle models vues
        choice = None
        return choice
import rumps
import yaml
import os


class ShortcutsApp(rumps.App):
    def __init__(self):
        super().__init__("ShellQuick", icon="icon.png")
        self.config_path = os.path.expanduser(
            "~/.config/shellquick/config.yml")
        self.load_shortcuts(first_time=True)
        self.menu.add(rumps.MenuItem("Update Config",
                      callback=self.load_shortcuts_from_file))

    def load_shortcuts(self, first_time=False):
        try:
            with open(self.config_path, 'r') as f:
                config = yaml.safe_load(f)
                shortcuts = config.get('shortcuts', [])
                self.menu.clear()
                self.build_menu(shortcuts, self.menu)
                if not first_time:
                    self.menu.add(rumps.MenuItem("Update Config",
                                  callback=self.load_shortcuts_from_file))
                    # Add Quit item back
                    self.menu.add(rumps.MenuItem(
                        "Quit", callback=rumps.quit_application))
        except Exception as e:
            rumps.alert(f"Failed to load shortcuts: {e}")

    def load_shortcuts_from_file(self, sender):
        file_dialog = rumps.Window(
            title="Load Shortcuts",
            message="Enter the path to your YAML config file:",
            default_text=self.config_path,
            dimensions=(320, 40)
        )
        response = file_dialog.run()
        if response.clicked:
            self.config_path = response.text
            self.load_shortcuts()

    def build_menu(self, items, menu):
        for item in items:
            if 'submenu' in item:
                submenu = rumps.MenuItem(item['label'])
                menu.add(submenu)
                self.build_menu(item['submenu'], submenu)
            else:
                menu.add(rumps.MenuItem(
                    item['label'], callback=self.run_command(item['command'])))

    def run_command(self, command):
        def callback(sender):
            os.system(command)
        return callback


if __name__ == "__main__":
    ShortcutsApp().run()

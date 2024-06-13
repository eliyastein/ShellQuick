# ShellQuick

ShellQuick is a macOS menu bar application that provides quick access to custom shell commands defined in a YAML configuration file. The application supports hierarchical submenus for better organization of commands.

## Features

- Quickly access and run shell commands from the macOS menu bar
- Supports hierarchical submenus for organizing commands
- Ability to update the configuration file on the fly

## Installation

### Prerequisites

- macOS
- Python 3.6 or later
- `pip` (Python package installer)

### Steps

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd ShellQuick
    ```

2. **Install the application:**

    ```bash
    make all
    ```

    This will set up a virtual environment, install the necessary dependencies, create a configuration directory, copy the default configuration file, and place the run script in `/usr/local/bin`.

## Usage

1. **Run the application:**

    The application should automatically run in the background after installation. You can access it from the macOS menu bar.

2. **Update the configuration:**

    To update the shortcuts configuration, click on "Update Config" in the menu bar app. Enter the path to your YAML configuration file to load new shortcuts.

3. **Create your own configuration:**

    You can create your own configuration file in YAML format. The default location for the configuration file is `~/.config/shellquick/config.yml`.

    Example configuration:

    ```
    shortcuts:
        - label: "This is a menu item"
        command: osascript -e 'tell app "System Events" to display dialog "Hello World"'
        - label: "This is a collection of menu items"
        submenu:
            - label: "This is a submenu item"
            command: osascript -e 'tell app "System Events" to display dialog "Hello World"'

    ```

## Uninstallation

To uninstall ShellQuick, run:

```bash
make uninstall


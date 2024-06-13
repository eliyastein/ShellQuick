.PHONY: all install venv config bin uninstall

APP_NAME = ShellQuick
CONFIG_DIR = $(HOME)/.config/shellquick
CONFIG_FILE = $(CONFIG_DIR)/config.yml
INSTALL_DIR = /usr/local/bin
RUN_SCRIPT = $(INSTALL_DIR)/$(APP_NAME)
VENV_DIR := venv


all: install

install: venv config bin

venv:
	@echo "Setting up virtual environment..."
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

config:
	@echo "Creating configuration directory and copying default config..."
	mkdir -p $(CONFIG_DIR)
	cp config.yml $(CONFIG_FILE)

bin:
	@echo "Creating run script and place in /usr/local/bin..."
	echo "#!/bin/bash\nsource $(PWD)/venv/bin/activate\npython $(PWD)/app.py 2>&1 2>/dev/null &" > shellquick_run.sh
	chmod +x shellquick_run.sh
	sudo cp shellquick_run.sh $(RUN_SCRIPT)

uninstall:
	@echo "Stopping and unloading the ShellQuick service..."
	sudo rm -f $(RUN_SCRIPT)
	rm -rf $(CONFIG_DIR)
	rm -rf $(VENV_DIR)
	rm -rf shellquick_run.sh

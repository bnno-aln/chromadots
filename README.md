# Chroma Dots

https://github.com/user-attachments/assets/6de4b280-9d36-4346-a6d7-0382c54ba26b

---
## Screenshots
**Example palette 1 (Dark)**
![palette_1_dark](https://github.com/user-attachments/assets/6ee49ae0-df57-476d-aa66-77e2a8dc73ac)

**Example palette 1 (Light)**
![palette_1_light](https://github.com/user-attachments/assets/1ca6a134-be29-4b08-8afa-639cf3d083fa)

**Example palette 2 (Dark)**
![palette_2_dark](https://github.com/user-attachments/assets/ebc04ebe-c32e-487a-a1c9-2c66825525a8)

**Example palette 2 (Light)**
![palette_2_light](https://github.com/user-attachments/assets/b473c484-0f23-4f0a-9480-d588c5cc9d2c)

---
## Used programs
- Hyprland
- Hyprlock - Hyprland lock screen
- Hypridle - Hyprland idle handler
- Clipse - Clipboard manager
- Waybar - Navbar at the top of the screen
- Waypaper - Wallpaper manager, responsible for executing the palette switch script
- Swaync - Notification Center
- Rofi - App Launcher
- Wlogout - Logout, Shutdown, Restart and Lock dialog
- Kitty - Terminal emulator

Spotify and discord are next on the list

---
## Installation process
**The files and folder names are important, changing the name of any might break the automatic palette change**

1. **Backup your files**
	1. **Make sure your .config folder have a backup, or at the very least the config for the programs above**
2. Install all used programs
3. Create a Python Virtual environment for the scripts to work
	1. Go to your waybar config folder in ~/.config/waybar
	2. In your terminal use the command `python -m venv waybar-venv`
	3. Inside the venv go in the bin folder and use `source activate` to install the necessary modules
		1. `pip install pylette`
		2. `pip install configparser`
4. Download repository
	1. Get the files, either:
		1. Download the repository as a zip file in **Code<>**
		2. Git clone to your PC and move its contents to the .config folder in home
5. Copy the files to the .config folder
	1. Make sure you have made a backup first
	2. Copy the folders inside the dotfiles folder to your .config folder in `/home/username/.config`
6. Use the palette
	1. Restart waybar to use the theme with `killall -SIGUSR2 waybar`
	2. Apply a wallpaper with waypaper
	3. Done

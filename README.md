[![Static Badge](https://img.shields.io/badge/lang-pt--BR-green)](https://github.com/bnno-aln/chromadots/blob/main/README.pt-br.md)


### Description
Project for archlinux using waypaper as a mediator to perform a palette exchange script using the wallpaper used.
Supports all formats used by the waypaper


![](Assets/chromadots.mp4)

### What is Chromadots
This project came about as a simple script to change the colors of the waybar, but as I perfected, the project grew in scope. Seeing programs that use CSS to control interface colors 

- Programs used
- Hyprland
- Hyprlock
- Hypridle
- Waypaper
- Waybar
- Kitty
- Rofi
- Clips of Clip
- Swaync
- Wlogout


### Examples
#### The Palette example 1

![](Assets/Palette1_dark.png)
![](Assets/Palette1_light.png)

#### Palette example 2
![](Assets/Palette2_dark.png)
![](Assets/Palette2_light.png)

### Installation method
1. **Backup your data and .config folder**
	1. **This step is extremely important due to the nature of the project**
2. Install the necessary programs
	2. Chromadots uses AURs, it is recommended to use an AUR Helper like yay or paru
		1. If you have yay installed use: `yay -S hyprlock hyprlock hypridle waybar waypaper rofi-wayland swaync wlogout python-pywal16 python-haishoku pythonon-configargparse clipse`
	3. To add the colors of the palette to your terminal follow the [pywal tutorial](https://github.com/eylles/pywal16/wiki/Getting-Started#applying-the-theme-to-new-terminals)
3. Create a virtual python environment for installing the necessary packages
	1. **It is important to keep the name of files and folders in order not to occur problems in the execution of the script**
	2. Go to the waybar folder, create a folder called scripts
	3. Inside the scripts folder use the command `python -m venv waybar-venv`
	4. Activate the venv with the command `source waybar-venv/bin/activate`
		1. Use `pip install -r requirements.txt` to install the packages necessary for the operation of the waybar modules and the palette script
4. Acquire Chromadots
	1. Choose from:
		1. `git clone https://github.com/bnno-aln/chromadots`
		2. Click code and download ZIP file
		3. Use the script (WIP)
	2. Extract/Move content to your .config

import re
import os


def update_hyprlock(hyprlock_path, colors, wallpaper):
    # Reads the file
    with open(hyprlock_path, "r") as file:
        config = file.readlines()

    lookup = r"(\$\w*|\$\w*-\w*|\$\w*-\w*-\w*)\s*=\s*(\w*)\((.*)\)"

    old_colors = dict()

    for num, line in enumerate(config):
        if line == "\n":
            continue
        try:
            search = re.findall(lookup, line)
            old_colors.update({f"{search[0][0]}": [search[0][1], search[0][2]]})
        except IndexError:
            continue

    # Replaces the old colors with the new ones
    for num, line in enumerate(config):
        for key, value in old_colors.items():
            if line.startswith(key) and line.endswith(f"{value[1]})\n"):
                config[num] = f"{key} = {colors[key]}\n"

            if "path=" in line.strip():
                config[num] = re.sub(
                    r"(?!path\s=|path=)\$HOME\/(.*(?:\.jpg|\.png|\.jpeg|\.webp))",
                    f"path = {os.path.expanduser('~')}{get_wallpaper(waypaper_config_path).strip('~')}\n",
                    line,
                )

    # Updates the file
    with open(hyprlock_path, "w") as file:
        file.writelines(config)
        file.close()


colors = {
    "$background": "rgb(67, 45, 39)",
    "$background-alt": "rgb(101, 57, 44)",
    "$accent": "rgb(141, 70, 46)",
    "$accent-alt": "rgb(208, 104, 41)",
    "$text-color": "rgb(245, 140, 51)",
    "$background-alpha": "rgba(67, 45, 39, 0.5)",
    "$background-alt-alpha": "rgba(101, 57, 44, 0.5)",
    "$accent-alpha": "rgba(141, 70, 46, 0.5)",
    "$accent-alt-alpha": "rgba(208, 104, 41, 0.5)",
    "$text-color-alpha": "rgba(245, 140, 51, 0.5)",
}

# adicionar $ ao nome da cor e adicionar variações alpha

update_hyprlock(os.path.expanduser("~") + "/.config/hypr/hyprlock.conf", colors)

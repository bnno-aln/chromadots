[![Static Badge](https://img.shields.io/badge/lang-en--US-green)](https://github.com/bnno-aln/chromadots/blob/main/README.md)

### Descrição

Projeto para archlinux utilizando waypaper como mediador para executar um script de troca de paleta utilizando o papel de parede utilizado.
Suporta todos os formatos utilizados pelo waypaper

<https://github.com/user-attachments/assets/c708cfef-df16-41c1-879e-384afe0ace1c>

### O que é Chromadots

Esse projeto surgiu como um simples script para trocar as cores do waybar, mas conforme eu aperfeiçoava, o projeto crescia em escopo. Vendo os programas que utilizam CSS para controlar as cores da interface

### Programas utilizados

- Hyprland
- Hyprlock
- Hypridle
- Waypaper
- Waybar
- Kitty
- Rofi
- Clipse
- Swaync
- Wlogout

### Exemplos

#### Paleta exemplo 1

![](Assets/Palette1_dark.png)
![](Assets/Palette1_light.png)

#### Paleta exemplo 2

![](Assets/Palette2_dark.png)
![](Assets/Palette2_light.png)

### Método de instalação

1. **Faça backup dos seus dados e da pasta .config**
   1. Esse passo é extramente importante tento em vista a natureza do projeto
2. Instale os programas necessários
   1. Chromadots usa AURs, é recomendável utilizar um AUR Helper como o yay ou paru
   2. Caso tiver yay instalado use: `yay -S hyprlock hypridle waybar waypaper rofi-wayland swaync wlogout python-pywal16 python-haishoku python-configargparse clipse python-colorthief feh swaybg swww mpvpaper`
   3. Para adicionar as cores da paleta no seu terminal siga o [tutorial do pywal](https://github.com/eylles/pywal16/wiki/Getting-Started#applying-the-theme-to-new-terminals)
3. Instale uma font nerd para os icones no waybar, a que está configurada é a JetBrain Mono Nerd Font
   1. Para instalar faça download da fonte e coloque em .local/share/fonts ou use `yay -S ttf-jetbrains-mono-nerd`
4. Habilite o inicio automatico para hypridle, waypaper, swaync e clipse
   1. Waypaper e clipse estão configurados em .config/hypr/configs/programs.conf
   2. Swaync e Hypridle podem ser iniciados automaticamente com `systemctl enable`/`systemctl start`
5. Crie um ambiente virtual python para a instalação dos pacotes necessários
   1. **É importante manter o nome dos arquivos e pastas para não ocorrer problemas na execução do script**
   2. Vá até a pasta do waybar, crie uma pasta chamada scripts
   3. Dentro da pasta scripts use o comando `python -m venv waybar-venv`
   4. Ative a venv com o comando `source waybar-venv/bin/activate`
   5. Use `pip install Pylette` para instalar os pacotes necessários para o funcionamento dos módulos do waybar e o script de paletas
6. Adquira Chromadots
    1. Escolha:
    2. `git clone https://github.com/bnno-aln/chromadots`
    3. Clique em code e baixe o repositório como arquivo ZIP
    4. Use o script (WIP)
7. Extraia/Mova o conteúdo para sua .config

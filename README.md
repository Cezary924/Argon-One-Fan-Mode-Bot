<div align="center">
   <h1>Argon One Fan Mode Changer</h1>
   <h3>𖣘</h3>
   <h3>Change the behavior of the built-in fan at different times of the day</h3>
   <a href="https://github.com/Cezary924/Argon-One-Fan-Mode-Changer/blob/master/README.md" target="__blank"><img alt="A badge with a label 'Lang 🇬🇧' - a link takes to README file in English" src="https://img.shields.io/badge/Lang-🇬🇧-012169?style=for-the-badge"></a>
   <a href="https://github.com/Cezary924/Argon-One-Fan-Mode-Changer/blob/master/README.pl-pl.md" target="__blank"><img alt="A badge with a label 'Lang 🇵🇱' - a link takes to README file in Polish" src="https://img.shields.io/badge/Lang-🇵🇱-dc143c?style=for-the-badge"></a>
</div><br/>

## ⚙️ Installation & Configuration</h3>
0. Get Argon One case for RPi and install dedicated script.
1. Clone this repo.
2. Edit files located in `files` directory:
   - `first_mode.txt` - This file contains info about the fan speed _(%)_ depending on the temperature _(Celsius degrees)_. These correlactions will be used when the first mode is activated.
   - `second_mode.txt` - This file contains info about the fan speed _(%)_ depending on the temperature _(Celsius degrees)_. These correlactions will be used when the second mode is activated.
   - `start.txt` - This file contains the hour _(24h format)_ when the first mode should be activated.
   - `stop.txt` - This file contains the hour _(24h format)_ when the first mode should be deactivated.
> _**IMPORTANT:** Every line in files that contain fan speed info should look like this: `temp=speed`, for example:_
```
40=25
45=50
50=75
55=100
```
> _**IMPORTANT:** The first mode must start and end on the same day._

## 🚀 Starting</h3>
1. To start, create a service running this script automatically with every boot, or execute this command in the main directory:
```
python bot.py
```
2. Enjoy!

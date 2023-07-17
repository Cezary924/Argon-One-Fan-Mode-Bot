<h1 align=center>Cezary924-Argon-One-Fan-Mode-Changer</h1>
<h3 align=center>✇</h3>
<h3 align=center>Change the behavior of the built-in fan at different times of the day</h3>

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

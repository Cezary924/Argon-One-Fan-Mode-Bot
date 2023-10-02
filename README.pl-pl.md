<div align="center">
   <h1>Argon One Fan Mode Changer</h1>
   <h3>𖣘</h3>
   <h3>Automatycznie zmieniaj zachowanie wbudowanego wiatraka o róznych porach dnia</h3>
   <a href="https://github.com/Cezary924/Argon-One-Fan-Mode-Changer/blob/master/README.md" target="__blank"><img src="https://img.shields.io/badge/lang-en-blue.svg"></a>
   <a href="https://github.com/Cezary924/Argon-One-Fan-Mode-Changer/blob/master/README.pl-pl.md" target="__blank"><img src="https://img.shields.io/badge/lang-pl-red.svg"></a>
</div><br/>

## ⚙️ Instalacja i konfiguracja</h3>
0. Zdobądź obudowę Argon One dla Raspberry Pi i zainstaluj dedykowany skrypt.
1. Sklonuj to repozytorium.
2. Zmień dane zawarte w plikach w katalogu `files`:
   - `first_mode.txt` - Ten plik zawiera informacje o prędkości wiatraka _(%)_ w zależności od temperatury procesora _(stopnie Celsjusza)_. Powiązania te będą używane, gdy aktywny będzie pierwszy tryb wiatraka.
   - `second_mode.txt` - Ten plik zawiera informacje o prędkości wiatraka _(%)_ w zależności od temperatury procesora _(stopnie Celsjusza)_. Powiązania te będą używane, gdy aktywny będzie drugi tryb wiatraka.
   - `start.txt` - Ten plik zawiera godzinę _(format 24-godzinny)_ oznaczającą kiedy tryb pierwszy wiatraka powinien być aktywowany.
   - `stop.txt` - Ten plik zawiera godzinę _(format 24-godzinny)_ oznaczającą kiedy tryb pierwszy wiatraka powinien byc dezaktywowany.
> _**UWAGA:** Każda linijka plików zawierających prędkości wiatraka powinna wyglądać tak: `temp=pred`, na przykład:_
```
40=25
45=50
50=75
55=100
```
> _**UWAGA:** Tryb pierwszy musi zacząć i skończyć się tego samego dnia.._

## 🚀 Uruchamianie</h3>
1. Aby uruchomić, stwórz usługę uruchamiającą ten skrypt automatycznie z każdym uruchomieniem urządzenia. Możesz również wykonać poniższą komendę w głównym katalogu repozytorium:
```
python bot.py
```
2. Gotowe!

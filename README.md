# **YAHTZEE**

    .---------. .---------. .---------. .---------. .---------.  
    |  O   O  | |  O   O  | |  O   O  | |  O   O  | |  O   O  |    
    |  O   O  | |  O   O  | |  O   O  | |  O   O  | |  O   O  |  
    |  O   O  | |  O   O  | |  O   O  | |  O   O  | |  O   O  |  
    '---------' '---------' '---------' '---------' '---------'

A simple Python library to play Yahtzee through the command line.

## Usage
In the terminal:
```bash
python3 yahtzee.py
```
### How to play:
When the game first launches, you'll be prompted to indicate how many players there will be, then you will be asked for their names.

During a player's turn, they will be presented with their scorecard and the results of rolling the dice. They can then choose which dice to keep. This selection is done using the numbers above the dice and must be seperated by a space. If the player presses enter, no dice will be kept, resulting in rolling all five dice. If all five dice are selected, the turn will end and the player will then move on to scoring that round. A player can re-roll up to two times.

After rolling the dice, the player will be asked how they want to score the round. This is done by selecting the scoring catergory using the letter inside brackets next to the category in the scorecard.

If there are multiple players, you will need to press ENTER to advance to begin the next player's turn. If there is just one player, the next round will automatically start.


## Work in Progress
Currently there needs to be improvements made to the error handling and input sanitization. Invalid selections will cause the program to crash.

There also needs to have an "end game" implemented so the player can see their final score, or, if there are multiple players, the winner will be seen.

## License
MIT License

Copyright (c) 2020 Kyle Skinner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


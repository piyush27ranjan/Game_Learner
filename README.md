[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![HitCount](http://hits.dwyl.io/piyush27ranjan/Game_Learner.svg)](https://github.com/piyush27ranjan/Game_Learner/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/piyush27ranjan/Game_Learner/graphs/commit-activity)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/piyush27ranjan/Game_Learner/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<br>
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://www.python.org/)
# Game_Learner
An ML Project to train the computer to play a game

## Milestones
 - [x] Select Game to learn from --> [HIDDEN GAME ON GOOGLE! (Atari Breakout!)](https://www.google.co.in/search?q=atari+breakout&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjs4Pnsho3bAhXGQ48KHSikCa4Q_AUICigB&biw=1396&bih=690&dpr=1.38). This game will be played using keyboard. 
 - [x] Extract training data
 - [ ] Train NN
 - [ ] *Testing* - Let it Play

## Current status
We have the info about:
- coordinates of the ball and plate.
- key logs and their time intervals during they were held down.

## Model
- Input Vector
  - Time
  - Ball coordinates(```b_x,b_y```)
  - Plate coordinate(```p_x```)
  - Key which was pressed at that time (```Key.left, Key.right or None```)

## Extracting Data from Sample_image.png using OpenCV

Sample Image
![Sample Image](Sample_image.png)

### After running 1shot_test.py we get the location of ball and plate

![Tracked ball](Got_the_ball.png)
Ball with purple boundary
![Tracked Plate](Got_the_plate.jpeg)
Plate with white boudary

## Contributers
- [Piyush Ranjan](https://github.com/piyush27ranjan/) - [View Contributions](https://github.com/piyush27ranjan/Game_Learner/commits?author=piyush27ranjan)
- [Piyush Chauhan](https://github.com/piyushchauhan/) - [View Contributions](https://github.com/piyush27ranjan/Game_Learner/commits?author=piyushchauhan)

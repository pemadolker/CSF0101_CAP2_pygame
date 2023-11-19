# Doodle Jumper Test Documentation
## Introduction
This documentation provides information about the test cases and resources used in testing the Doodle Jumper game.

## Game Overview
A straightforward Python game called Doodle Jumper is created with the Pygame library. In the game, the player controls a character that must jump on platforms without falling. The goal is to land on platforms successfully and earn the highest score possible.

# Test Cases
## 1. Platform Generation 
Description
Make sure the platforms are generated on the screen at the proper locations.

Test Steps
Run the game.
Observe the initial platform positions.
Expected Result
Platforms ought to appear at random points along the edges of the screen.

## 2. Player Movement
Description
Check to see if the player can move left and right within the confines of the screen.

Test Steps
Run the game.
Press the left arrow key.
Press the right arrow key.
Expected Result
The player's position should update on the screen and they should move left and right in accordance.

## 3. Collision Detection
Description
Make sure the player and the platforms collide detection is implemented in the game.
Test Steps
Run the game.
Make the player character jump onto a platform.
Move the player character into empty space.
Expected Result
When the player touches a platform, the game ought to recognize collisions. Collisions shouldn't be detected by the game when the player is in empty space.


## 4. Score Tracking
Description
Verify that the game tracks the player's score correctly.

Test Steps
Run the game.
Jump on platforms to increase the score.
Expected Result
As soon as the player touches down on a platform successfully, the score that appears on the screen should rise.

## 5. Game Over State
Description
Make sure that when the player falls off the platforms, the game changes to the "Game Over" state.

Test Steps
Run the game.
Allow the player character to fall off the platforms.
Expected Result
After the game reaches the "Game Over" state, the player should be able to restart and see the relevant message.

# Resources Used for Testing
Doodle Jumper was developed and tested using the following resources:

The Pygame Library is a collection of Python modules made specifically for creating video games. It was in charge of input, graphics, and other gaming-related functions.

Images for Game Elements: Images of the player character, platforms, backgrounds, and restart button were used to enhance the visual aspects of the game.

Random Module: The random module in Python was utilized to generate random positions for the initial placement of platforms.

Test Environment: The game was tested on a Windows environment using Python 3.

# Conclusion
Key features of the Doodle Jumper game, such as player movement, collision detection, score tracking, and the Game Over state, were tested. The test cases were designed to make sure the game behaves correctly and to find any problems that might occur while playing. Pygame, graphics, and the random module were all used in the game with good reason to produce an interesting and eye-catching gaming experience.

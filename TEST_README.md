#Doodle Jumper Test Documentation
##Introduction
This documentation provides information about the test cases and resources used in testing the Doodle Jumper game.

###Game Overview
Doodle Jumper is a simple Python-based game developed using the Pygame library. The game involves a player controlling a character to jump on platforms and avoid falling. The objective is to achieve the highest score possible by successfully landing on platforms.

##Test Cases
###1. Platform Generation
Description
Ensure that platforms are generated at appropriate positions on the screen.

Test Steps
Run the game.
Observe the initial platform positions.
Expected Result
Platforms should be generated at random positions within the screen boundaries.

2. Player Movement
Description
Verify that the player can move left and right within the screen boundaries.

Test Steps
Run the game.
Press the left arrow key.
Press the right arrow key.
Expected Result
The player should move left and right accordingly, and the player's position should be updated on the screen.

3. Collision Detection
Description
Ensure that the game detects collisions between the player and the platforms.

Test Steps
Run the game.
Make the player character jump onto a platform.
Move the player character into empty space.
Expected Result
The game should detect collisions when the player lands on a platform. The game should not detect collisions when the player is in empty space.

4. Score Tracking
Description
Verify that the game tracks the player's score correctly.

Test Steps
Run the game.
Jump on platforms to increase the score.
Expected Result
The score displayed on the screen should increase as the player successfully lands on platforms.

5. Game Over State
Description
Ensure that the game transitions to the Game Over state when the player falls off the platforms.

Test Steps
Run the game.
Allow the player character to fall off the platforms.
Expected Result
The game should enter the Game Over state, displaying the appropriate message and allowing the player to restart.

Resources Used for Testing
The following resources were used during the development and testing of Doodle Jumper:

Pygame Library: Pygame is a set of Python modules designed for writing video games. It was used to handle graphics, input, and other game-related functionalities.

Images for Game Elements: Images of the player character, platforms, backgrounds, and restart button were used to enhance the visual aspects of the game.

Random Module: The random module in Python was utilized to generate random positions for the initial placement of platforms.

Test Environment: The game was tested on a Windows environment using Python 3.

Conclusion
The Doodle Jumper game was tested for key functionalities, including platform generation, player movement, collision detection, score tracking, and the Game Over state. The test cases aimed to ensure the correct behavior of the game and identify any issues that may arise during gameplay. The game's use of Pygame, images, and the random module were justified to create an engaging and visually appealing gaming experience.

For any issues or feedback related to the game, please refer to the GitHub repository for further assistance.

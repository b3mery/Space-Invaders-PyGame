# Space Invaders

Basic Space Invaders like Game developed in PyGame for <A href="https://www.udemy.com/course/100-days-of-code/">100 days of code on Udemey.</A>

</img>
<img src = "docs/demo.gif", alt = "demo gif", height = "350">

# Code Overview
* `main.py` is the entry point
* Level class is responsible for the orchestration and update of the sprites objects
* Player, Enemy and Bullet classes extend pygame.sprite.Sprite
    * These three could inherit from a more custom base class but do not due to time restraints.
* enemy_controller is a enemy orchestration class for drawing and moving the enemies to the screen as group. 
* `settings.py` contains constant game variables for controlling basic settings. 

## Running The Game:
Run `main.py` from the `src` folder. Ensure `src` is your current working directory as the imports are relative. 

# References 
* All the code is my own. Game assets were sourced from GeeksforGeeks <a href='https://drive.google.com/drive/folders/1LIhvAzDeeftnYVlQaVj3PMPkU-mLylmB'> google drive</a>. Their development and use of assets is documented in the following article: <a href='https://www.geeksforgeeks.org/building-space-invaders-using-pygame-python/'>Building Space Invaders Using PyGame – Python</a> 

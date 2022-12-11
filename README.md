<a name="readme-top"></a>
<!--
*** Project: Made in Pygame - Python
*** License: MIT License
*** Author: Julian Fernandez
-->

[![LinkedIn][linedin_img]][linkedin_link] [![Instagram][instagram_img]][instagram_link] [![Github][github_img]][github_link] 

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="https://raw.githubusercontent.com/pygame/pygame/main/docs/reST/_static/pygame_logo.svg" alt="Logo">
  </a>
  <br />  <br />  <br />
  <h1 align="center">Butter Adventure</h1>

  <p align="center">
    An project made in pygame!
    <br />
    <a href="https://youtu.be/LEpIrVUzrRc"><strong>View Demo Video! »</strong></a>
    <br />
  </p>
</div>


<br />
<br />
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the project</a>
      <ul>
        <li><a href="#built-with">Built with</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#game-installation">Game installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#debug-mode">Debug mode</a></li>
    <li><a href="#game-previews">Game previews</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About the project

This is a first quarter project for the Programming Technicature at the National Technological University.
It is a 2D platform videogame made in Pygame (Python), where the player has to avoid different types of traps, defeat enemies and recolect exp from the map to win

Some conceptual features:
* OOP (Object-oriented programming)
* Try/Except
* SQL queries
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built with

* [![Python][python_img]][python_url]
* [![Pygame][python_img]][pygame_url] (Pygame)
* [![Sqlite][sqlite_img]][sqlite_url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Next, these are the steps for downloading repo files and executing it locally

### Prerequisites

To play this game, it must be installed the following:

* _Python - Download Python from Microsoft Store or in Python web page_
  ```sh
  Microsoft Store: https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5
  Python web page: https://www.python.org/
  ```
* _Pygame_
  ```sh
  pip install pygame
  ```

### Game installation

1. _Clone the repo_
   ```sh
   git clone https://github.com/JuliFerz/ButterAdventure.git
   ```
2. _Download the source files (music & images)_
   ```sh
   https://drive.google.com/drive/folders/15ZPpaiYTj4tjlxZ-jCOCzQ-QGOSwkSZ8?usp=share_link
   ```
3. _Move "images" and "sounds" files to the directory repo:_
   ```sh
   /ButterAdventure/game/src
   ```
4. _In your CLI, change directory to `/ButterAdventure/game` and execute_
   ```sh
   python main.py
   ```
5. _Enjoy!_
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
### Menu:
In the game menu, buttons are click selected

### Game: 
Playing any level, the controls are:

* Keys `W`, `A`, `D`: Player movement
* Hold Key `SHIFT`: Run
* Key `J`: Shoot
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Debug mode
If you want to play in debug mode, you should modify `\ButterAdventure\game\settings\constantes.py` file
   ```py
   DEBUG = True
   # DEBUG = False
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GAME PREVIEWS -->
## Game previews
### Hit damage to enemies
![Hit-damage](https://user-images.githubusercontent.com/97322714/206854945-a4913cb9-ddf9-48b4-83bf-ace99ceea5a5.gif)

### Avoid enemies hits
![Get-damage](https://user-images.githubusercontent.com/97322714/206855066-b8bb599c-5c53-4130-9008-ffb8925c7729.gif)

### Get health 
![Get-health](https://user-images.githubusercontent.com/97322714/206855082-9d28d315-8b4f-436e-b8d9-e66264fc7bfc.gif)

### Take bullets 
![Take-bullets](https://user-images.githubusercontent.com/97322714/206855110-514cea76-dd41-4d43-ae75-fe5b05b6d5d1.gif)

### Music Settings
![music](https://user-images.githubusercontent.com/97322714/206855151-6a4a58cf-47a8-457c-84ee-dff12e526aa3.gif)

### And finally... challenge yourself!
![challenge-yourself](https://user-images.githubusercontent.com/97322714/206855167-cf4b773d-f17e-4490-9501-8dabd2cccb24.gif)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] ADD - Moving platforms
- [x] ADD - Traps
- [x] UPD - The game will end when all the enemies are defeated and all coins are collected
- [ ] ADD - Loading screen
- [ ] ADD - Defeat animations (players & enemies)
- [ ] ADD - Level editor
- [ ] ADD - Wider levels (beyond the screen)

If you want to see my progress on this game, check my [trello board](https://trello.com/b/HJ94PNx8/pygame)  (all in spanish) to see a full list of proposed features (and known bugs).


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, or found some bugs, please let me know as an issue in this repo!<br/><br/>
_Don't forget to give the project a star! Thanks again!_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Julian Fernandez - julianfernandez1811@gmail.com

Project Link: [https://github.com/JuliFerz/ButterAdventure](https://github.com/JuliFerz/ButterAdventure)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[linedin_img]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin_link]: https://www.linkedin.com/in/julian-fernandez-707612180/
[instagram_img]: https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white
[instagram_link]: https://www.instagram.com/juli_ferz/
[github_img]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[github_link]: https://github.com/JuliFerz/
[python_img]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[python_url]: https://www.python.org/
[pygame_url]: https://www.pygame.org/

[sqlite_img]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
[sqlite_url]: https://www.sqlite.org/index.html
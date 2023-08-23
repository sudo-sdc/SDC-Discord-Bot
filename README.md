# Discord Bot for CSUN Email Verification

Welcome to the documentation for the Discord bot that authenticates potential Discord members by sending them DMs to verify their csun.edu emails.

## Table of Contents
- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## About The Project
This project aims to automate the process of verifying CSUN email addresses for new members joining a Discord server. By using this bot, server administrators can ensure that only members with valid csun.edu emails gain access to the server.

## Built With
- Discord.py
- Python 3
- sendgrid 
- dotenv

## Getting Started
To get started with the bot, follow these steps:

### Prerequisites
- Python 3.x
- Discord Bot Token (Get it by creating a bot on the Discord Developer Portal)
- Sendgrid API key (Get it by signing in to https://sendgrid.com/)

### Installation
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Add the bot token and sendgrid api key in your own `.env` file.

## Usage
1. Create a dummy discord account with no role. 
2. Run code locally on your machine. 
2. Join our test discord server [Dummy Discord Server](https://discord.gg/ChTwjgYYN).
5. Use / commands to add your email. 
6. check email verification token should be sent. 
7. use / commmand to insert your token. 
8. you now have a new role in the discord `member `.

## Roadmap
- On verification the discord bot should allow access to the full server for members 
- the discord bot source code needs to be added to a cloud service i.e. Heroku
- Create unit test with a code coverage of at least 80%

## Contributing
Contributions are welcome! If you'd like to contribute to the project, follow these steps:
1. Fork the repository.
2. Create a new branch.
3. Make your changes and test them.
4. Submit a pull request.

## License
This project is licensed under the [MIT license](LICENSE).

## Contact
If you have any questions or need assistance, feel free to contact the project maintainer [SDC] at [csunsdc@gmail.com].

## Acknowledgements
This discord bot was designed by and authored by [eanyakpor](https://github.com/eanyakpor), [NimaJ2003](https://github.com/NimaJ2003) and [BilinP](https://github.com/BilinP). See https://github.com/sudo-sdc/SDC-Discord-Bot/graphs/contributors for a complete list of people who've contributed. 


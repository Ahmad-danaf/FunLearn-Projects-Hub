# FunLearn Projects Hub

Welcome to the FunLearn Projects Hub! 

This repository houses a collection of diverse programming projects created for both fun and learning purposes.

## Purpose

The primary aim of these projects is to learn, experiment, and apply newfound knowledge in a practical manner. By sharing these projects openly, I hope to inspire, teach, and collaborate with fellow developers and enthusiasts in the programming community.

## Projects Included:

### 1. Connect Four Game
- **Languages:** HTML, CSS, JavaScript
- **Description:** A classic implementation of the Connect Four game.
- **To Play:** Open `connect_four_game.html`

### 2. NATO Phonetic Alphabet
- **Language:** Python
- **Description:** Converts words into their NATO phonetic alphabet equivalents.
- **To Run:** Execute `python main.py`

### 3. Hirst Painting
- **Language:** Python
- **Description:** Generates an art piece resembling a Hirst painting using dots.
- **To Run:** Execute `python hirst_painting.py`

### 4. Caesar Cipher
- **Language:** Python
- **Description:** Encrypts and decrypts messages using the Caesar cipher.
- **To Run:** Execute `python caesar_cipher.py`

### 5. Spectrum
- **Languages:** HTML, CSS
- **Description:** Reproduction of a famous spectrum design.
- **To Run:** Open `spectrum.html`

### 6. Mail Merge
- **Language:** Python
- **Description:** Automates create similar letters to multiple recipients.
- **To Run:** Execute `python main.py`

### 7. Tip Calculator
- **Language:** Python
- **Description:** Calculates individual payments including tips when going out with friends.
- **To Run:** Execute `python tip_calculator.py`

### 8. Password Manager
- **Language:** Python
- **Description:** Saves website, username/email, and password data. Allows generation of hard passwords and provides an option to search for username/email and password by website.
- **To Run:** Execute `python main.py`

### 9. Quizzler App
- **Language:** Python
- **Description:** Takes 10 True/False quiz questions about computer science from the Open Trivia Database API.
- **To Run:** Execute `python main.py`

### 10. Study Timer (Pomodoro)
- **Language:** Python
- **Description:** The famous study-timer-pomodoro.
- **To Run:** Execute `python main.py`

### 11. Flash Card Project
- **Language:** Python
- **Description:** A program aiding in learning new words for The Psychometric Entrance Test using flashcards. Utilizes tkinter to display cards in English for 3 seconds, then reveals the translation in Hebrew. Allows removal of known words and creates a new CSV file to exclude known words on subsequent runs.
- **To Run:** Execute `python main.py`

### 12. Automated Amazon Price Tracker
- **Language:** Python
- **Description:** Automates tracking Amazon prices daily and sends email notifications when the price changes.
- **To Run:** Upload this to a cloud platform like PythonAnywhere.com and set a scheduled command for daily execution. Update `notification_manager.py` using `smtplib` for email notifications. Refer to the `smtplib` documentation. To manually run, update `notification_manager.py` and execute `main.py`.
- **Note:** Ensure to input your own email credentials and configure the notification settings before running.

### 13. Instagram Follower Bot
- **Language:** Python
- **Description:** A bot designed to gain more Instagram followers by following people from an account with similar topics. For instance, if the account is about space, the bot follows people who follow NASA, potentially attracting more users to the account.
- **To Run:** Update `InstaFollower.py` with your Instagram account details and the account with a similar topic. Execute `python main.py`.
- **Note:** Instagram regularly updates its website, leading to potential changes in CSS Selectors and XPATH. Ensure you may need to adjust them accordingly.

### 14. Flight Deal Finder
- **Language:** Python
- **Description:** Searches for flight deals in the next 6 months and sends an alert via email if a cheap flight is found, similar to services like https://jacksflightclub.com/.

- **Requirements:**
    1. **Google Sheet:** Use https://sheety.co/ to update `SHEETY_PRICES_ENDPOINT` in `data_manager.py`.
    2. **Kiwi Partners Flight Search API:** Sign up for the free Tequila API at https://tequila.kiwi.com/portal/login to obtain the `TEQUILA_API_KEY` used in `flight_search.py`.
    3. **Sending Email with smtplib:** Update `notification_manager.py` to configure email sending. Refer to the `smtplib` documentation.

- **To Run:**
    1. Create a .env file and update all required API keys, mail configurations, and sensitive data as specified in comments at the start of each file.
    2. Execute `main.py`.
    3. For automated runs, deploy the code to a cloud platform like PythonAnywhere.com and schedule `main.py`. For manual runs, execute `main.py`.
    
- **Note:** Ensure you update the necessary API keys and configurations in the .env file before running the code.

## Usage

To get started with these projects, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Ahmad-danaf/FunLearn-Projects-Hub.git
    ```

2. Navigate to the specific project directory:
    ```bash
    cd project_directory
    ```

3. Follow the instructions provided in each project's README or code comments to run the project.

For example:
- For the Connect Four Game:
  - Open `connect_four_game.html` in a web browser.

- For the NATO Phonetic Alphabet:
  - Run `python main.py` and follow the prompts.

Repeat these steps for each project you want to explore or run.

## Contribution

Feel free to contribute, suggest improvements, or use these projects for learning purposes. Contributions from fellow developers are highly welcomed and appreciated!


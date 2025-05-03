# FunLearn Projects Hub

Welcome to the FunLearn Projects Hub! 

This repository houses a collection of diverse programming projects created for both fun and learning purposes.

## Purpose

The primary aim of these projects is to learn, experiment, and apply newfound knowledge in a practical manner. By sharing these projects openly, I hope to inspire, teach, and collaborate with fellow developers and enthusiasts in the programming community.

## Projects Included:

### 1. Flight Deal Finder
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

### 2. Automated Amazon Price Tracker
- **Language:** Python
- **Description:** Automates tracking Amazon prices daily and sends email notifications when the price changes.
- **To Run:** Upload this to a cloud platform like PythonAnywhere.com and set a scheduled command for daily execution. Update `notification_manager.py` using `smtplib` for email notifications. Refer to the `smtplib` documentation. To manually run, update `notification_manager.py` and execute `main.py`.
- **Note:** Ensure to input your own email credentials and configure the notification settings before running.

### 3. Instagram Follower Bot
- **Language:** Python
- **Description:** A bot designed to gain more Instagram followers by following people from an account with similar topics. For instance, if the account is about space, the bot follows people who follow NASA, potentially attracting more users to the account.
- **To Run:** Update `InstaFollower.py` with your Instagram account details and the account with a similar topic. Execute `python main.py`.
- **Note:** Instagram regularly updates its website, leading to potential changes in CSS Selectors and XPATH. Ensure you may need to adjust them accordingly

### 4. Study Timer (Pomodoro)
- **Language:** Python
- **Description:** The famous study-timer-pomodoro.
- **To Run:** Execute `python main.py`

### 5. Flash Card Project
- **Language:** Python
- **Description:** A program aiding in learning new words for The Psychometric Entrance Test using flashcards. Utilizes tkinter to display cards in English for 3 seconds, then reveals the translation in Hebrew. Allows removal of known words and creates a new CSV file to exclude known words on subsequent runs.
- **To Run:** Execute `python main.py`

### 6. QRCodeGenerator
- **Language:** Node.js
- **Description:** This project generates a QR code image and a `url.txt` file based on the user’s inputted URL.
- **To Run:**
  1. Navigate to the project directory:
     ```bash
     cd QRCodeGenerator
     ```
  2. Install the required dependencies:
     ```bash
     npm install
     ```
  3. Run the script:
     ```bash
     node index.js
     ```
  4. Enter a URL when prompted. The QR code image (`qr-code-img.png`) and the URL file (`url.txt`) will be generated in the directory.

- **Note:** The `node_modules` folder is not included in the repository. Ensure you run `npm install` to install the required dependencies based on `package.json` and `package-lock.json`.


### 7. Quizzler App
- **Language:** Python
- **Description:** Takes 10 True/False quiz questions about computer science from the Open Trivia Database API.
- **To Run:** Execute `python main.py`

### 8. Password Manager
- **Language:** Python
- **Description:** Saves website, username/email, and password data. Allows generation of hard passwords and provides an option to search for username/email and password by website.
- **To Run:** Execute `python main.py`

### 9. Tip Calculator
- **Language:** Python
- **Description:** Calculates individual payments including tips when going out with friends.
- **To Run:** Execute `python tip_calculator.py`

### 10. Mail Merge
- **Language:** Python
- **Description:** Automates create similar letters to multiple recipients.
- **To Run:** Execute `python main.py`

### 11. Spectrum
- **Languages:** HTML, CSS
- **Description:** Reproduction of a famous spectrum design.
- **To Run:** Open `spectrum.html`

### 12. Caesar Cipher
- **Language:** Python
- **Description:** Encrypts and decrypts messages using the Caesar cipher.
- **To Run:** Execute `python caesar_cipher.py`

### 13. Hirst Painting
- **Language:** Python
- **Description:** Generates an art piece resembling a Hirst painting using dots.
- **To Run:** Execute `python hirst_painting.py`

### 14. NATO Phonetic Alphabet
- **Language:** Python
- **Description:** Converts words into their NATO phonetic alphabet equivalents.
- **To Run:** Execute `python main.py`

### 15. Linux & Bash Automation
- **Languages:** Bash, Linux CLI
- **Description:** A growing collection of scripts, notes, and exercises to learn Linux and automate real-world tasks. Includes a deploy script for Django apps like Volunteen and covers topics like file permissions, cron jobs, parsing logs, and more.
- **To Explore:**
  - Navigate to the [`Linux-Bash-Automation`](./Linux-Bash-Automation) folder.
  - See `README.md` inside for full breakdown, progress, and scripts.

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
- For the Flight Deal Finder:
  - Run `main.py` as explained in the project folder.

- For the QRCodeGenerator:
  - Run `node index.js` in the QRCodeGenerator directory.

- For the Spectrum:
  - Open `spectrum.html` in a web browser.

Repeat these steps for each project you want to explore or run.

## Contribution

Feel free to contribute, suggest improvements, or use these projects for learning purposes. Contributions from fellow developers are highly welcomed and appreciated!

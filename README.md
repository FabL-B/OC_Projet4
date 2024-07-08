# Centre Échecs

## Description:

Centre Échecs is an offline program written in Python for managing chess tournaments. It allows users to create tournaments, manage players, display reports, and ensure data persistence using JSON files.

## Features:
### Tournament Management:

    Create new tournaments.
    Select and play existing tournaments.
    Display tournament details such as name, location, start/end dates, and rounds.

### Player Management:

    View and manage the list of players.
    Add new players to the database.

### Reports:

    Display reports such as:
        List of all players sorted alphabetically.
        List of all tournaments.
        Tournament details including playes, rounds and matches.

### Data Persistence:

    Save and load the program state using JSON files.
    Ensure synchronization between in-memory objects and JSON files to avoid data loss.

## Installation:

1. Open Git Bash

2. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/FabL-B/OC_Projet4.git
    cd Centre-Echecs
    ```
3. Create and activate the virtual environment:
   
    ```bash
    Python -m venv env
    Source env/bin/activate (pour Linux et Mac)
    Env\Scripts\activate (pour Windows)
    ```

4. Install the packages:
   
    ```bash
    pip install -r requirements.txt
    ```

## Usage:
1. Run the main script to start the application:

    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to navigate through the main menu and perform desired actions.


3. Generate a Flake8 HTML report to ensure code quality and adherence to PEP 8:

    ```bash
    flake8 --max-line-length=119 --format=html --htmldir=flake8_report
    ```
    The report will be generated in the flake8_report directory.
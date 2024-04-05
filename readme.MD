# Allegro messages and disputes responder

## Introduction
This document provides documentation for the Python program designed for automated responses to messages and disputes on Allegro, a Polish online marketplace.

## Program Overview
The program consists of several functionalities:
- Automated message response to incoming messages.
- Automated response to disputes initiated by customers.
- Token management for authentication with Allegro's API.

## Program Structure
The program is divided into several files:

1. `main.py`: This script serves as the entry point of the program. It orchestrates the execution of automated responses at regular intervals.
2. `login.py`: This script contains the logic for obtaining and managing access tokens for authentication with Allegro's API.
3. `config.json`: This JSON file stores configuration data such as API endpoints, client credentials, and redirect URIs.

## Usage
To use the program:
1. Ensure Python is installed on your system.
2. Modify the `config.json` file with your Allegro API credentials.
3. Run the `main.py` script.

## Dependencies
The program relies on the following Python libraries:
- `requests`: For making HTTP requests to Allegro's API.
- `json`: For handling JSON data.
- `time`: For introducing delays between automated responses.

## Program Execution
The `main.py` script initiates the following processes:
1. Initialization: Reads configuration data from `config.json` and sets up the environment.
2. Authentication: Obtains access tokens using the `login.py` module.
3. Automated Message Response: Checks for incoming messages and sends automated responses.
4. Automated Dispute Response: Checks for disputes and sends automated responses if necessary.
5. Sleep Cycle: Pauses execution for 1 hour before repeating the process.

## Authors
- [Kamil Wojcieszak](https://github.com/Kamil-Wojcieszak/) - Student at Wroclaw University of Science and Technology


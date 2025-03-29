# Mood Tracker

A simple web application built with Streamlit to track and visualize your daily moods.

**Author:** Hamza Sheikh

## Overview

Mood Tracker is a user-friendly web application that allows users to log their daily moods and view their mood history over time. The application uses a PostgreSQL database to store mood entries and provides a simple interface for selecting and saving moods. Users can also visualize their mood trends through a line chart, making it easy to reflect on their emotional patterns.

## Features

- **User Input:** Enter your name to personalize the experience.
- **Mood Selection:** Choose your current mood from a predefined list (`Happy`, `Sad`, `Angry`, `Stressed`, `Anxious`, `Neutral`, `Excited`).
- **Mood Logging:** Save your mood entries to a PostgreSQL database.
- **Mood History:** View your past mood entries in a table under the "Data" tab or as a line chart in the "Graph" tab.

## Setup and Installation

Follow these steps to set up and run the Mood Tracker application locally:

1. **Prerequisites:**

   - Python 3.7 or higher
   - PostgreSQL database

2. **Install dependencies:**
   Run the following command in your terminal to install the required Python packages:

   ```bash
   pip install streamlit pandas psycopg2-binary python-dotenv
   ```

3. **Set up environment variables:**

   - Create a .env file in the project root directory with the following content
     ```bash
     DATABASE_URL=postgresql://username:password@host:port/database_name
     ```
   - Replace `username`, `password`, `host`, `port`, and `database_name` with your PostgreSQL database credentials.

4. **Run the application:**
   Start the Streamlit app by running this command in the terminal:
   ```bash
   streamlit run app.py
   ```

## Usage

Once the application is running, follow these steps to use it:

1. **Enter your name:**
   - In the "Name" field, enter your name to personalize the experience.
   - Click the "Submit" button to save your name.

2. **Select your mood:**
   - In the "Mood" dropdown, select your current mood from the list of predefined options.
   - Click the "Submit" button to save your mood.

3. **View mood history:**
   - Go to the "Data" tab to view your mood history in a table format.
   - Go to the "Graph" tab to view your mood history as a line chart.

## Code Structure

The project consists of two main files:

- `main.py`: The main application file that handles the Streamlit UI, page configuration, and core logic for user interaction and data display.
- `database.py`: Contains functions for establishing the database connection, creating the mood table, and performing CRUD (Create, Read, Update, Delete) operations for mood logs.

The database.py module is imported as db in app.py to manage database interactions.

## Technologies Used

- **Streamlit:** Powers the interactive web interface with a wide layout, custom styling, and tabbed views.
- **PostgreSQL:** Stores mood log data persistently.
- **Pandas:** Handles data manipulation and converts mood logs into a DataFrame for display and charting.
- **psycopg2:** Facilitates the connection between Python and the PostgreSQL database.
- **python-dotenv:** Loads environment variables from the .env file for secure configuration.

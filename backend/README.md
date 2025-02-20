# Backend

This is the backend for the Knitting project, built with FastAPI.

## Requirements

- Python 3.7+
- FastAPI

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Cazzokid/Knitting
   cd Knitting/Backend
   ```

2. Create a virtual environment and activate it:

   On Unix-based systems:

   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

   On Windows:

   ```bat
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the FastAPI server:

   ```sh
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to see the interactive API documentation.

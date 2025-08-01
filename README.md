# ASCII Art Generator

A simple web application that converts your text into ASCII art using the power of Python, Flask, and pyfiglet. It was created 2025-07-15 using Gemini CLI to test agentic coding using that tool.

## Description

This project is a lightweight web-based tool that allows users to enter any text and see
it instantly rendered as ASCII art. It's built with Flask and provides a clean,
minimalist interface for a fun and straightforward user experience.

## Features

* Simple, single-page interface
* Real-time ASCII art generation
* **Font selection with dropdown menu** - Choose from 5 different ASCII art styles:
  * Standard - The default pyfiglet font
  * Slant - Italicized/slanted text
  * Block - Blocky, solid characters
  * Digital - Digital/LCD-style characters
  * Banner - Large banner-style text
* Clean, modern design with custom CSS
* Responsive layout for different screen sizes
* Easy to set up and run locally

## Demo



## Technologies Used

* Backend: Python, Flask
* ASCII Generation: pyfiglet
* Frontend: HTML5, CSS3
* Package Management: pip, venv

## Setup and Installation

To run this application on your local machine, follow these steps:

1. Clone the repository:
   * `git clone https://github.com/your-username/ascii-art-generator.git`
   * `cd ascii-art-generator`
2. Create and activate a Python virtual environment:
   * `python3 -m venv venv`
   * `source venv/bin/activate`
   * On Windows, use `venv\Scripts\activate`
3. Install the required dependencies:
   * `pip install -r requirements.txt`
4. Run the application:
   * `python app.py`



## Usage

1. Open your web browser and navigate to http://127.0.0.1:5000.
2. Enter the text you want to convert in the input field.
3. Select your preferred font style from the dropdown menu.
4. Click the "Generate" button.
5. The ASCII art will appear below the form in your chosen style.

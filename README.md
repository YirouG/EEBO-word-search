# Word Pattern Search Tool

This repository contains a Flask-based web application for searching word patterns in a text corpus. The application has been packaged as an executable for easy sharing and use without needing a Python environment.

## Features

- Search for words using patterns with wildcards (`*` and `?`).
- View search results in a web browser.
- Simple and intuitive user interface.

## Getting Started

### Prerequisites

- Windows OS (for the provided executable)
- Web browser (Chrome, Firefox, Edge, etc.)

### Running the Application

1. **Download the Executable:**

   - Go to the [Releases](https://github.com/YirouG/EEBO-word-search/releases) section of this repository.
   - Download the latest `app.exe` file from the assets.

2. **Extract the ZIP file (if applicable):**

   - If the executable is provided in a ZIP file, right-click on the downloaded ZIP file and select "Extract All".

3. **Run the Executable:**

   - Navigate to the extracted folder (if applicable) and double-click the `app.exe` file to start the application.
   - The application will automatically open in your default web browser.

### Using the Application

1. **Open the Application:**

   - Once the application is running, it will open in your default web browser. If it doesn't, you can manually navigate to `http://127.0.0.1:5000/`.

2. **Search for Word Patterns:**

   - Enter a pattern in the search box using wildcards:
     - `*` (asterisk): Matches any number of characters (including zero characters). For example, `ca*` will match `cat`, `car`, `cater`, `castle`, etc.
     - `?` (question mark): Matches exactly one character. For example, `?at` will match `cat`, `bat`, `hat`, etc.

   - **Examples:**
     - `ca*` will match words like `cat`, `car`, `cater`, `castle`.
     - `?at` will match words like `cat`, `bat`, `hat`.
     - `*ing` will match words like `running`, `swimming`, `jumping`.
     - `b?g` will match words like `bag`, `big`, `bug`.

   - Click the "Search" button to view the results.

### Development

To set up the development environment and run the application locally:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/YirouG/EEBO-word-search.git
   cd EEBO-word-search

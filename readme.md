# Project README

## Requirements
- Python 3 is needed for this project.

## Installation Steps
1. Unzip `project.zip` to the desired extraction path:
    ```
    unzip project.zip -d /path/to/extract/to
    ```

2. Change directory to the project directory:
    ```
    cd /path/to/extract/to/project-directory
    ```

3. Set up a Python virtual environment:
    ```
    python3 -m venv myenv
    ```

4. Activate the virtual environment:
   - On Unix or MacOS:
     ```
     source myenv/bin/activate
     ```
   - On Windows:
     ```
     myenv\Scripts\activate
     ```

5. Install project dependencies from `requirements.txt`:
    ```
    pip install -r requirements.txt
    ```

## Usage
- Run `python3 src/lookup.py` to look up the price of a symbol on a specific date.
- Run `python3 src/lowest_highest.py` to check the lowest and highest price for a given date range.

## Q & A
- **What compromises did you make due to time constraints?**
  - I implemented all the features.

- **How would you approach versioning of this library?**
  - I can incorporate another API in the library to provide version information or maintain a version file.

- **How would we go about publishing this library?**
  - I can publish this on GitHub under the MIT license.

- **How would you design this if it was going to be a service rather than a library?**
  - We can utilize a service like AWS Lambda to host and manage the functionality.

- **Please include any other comments about your implementation.**
  - Nothing I can think of for now.

- **How much time did you spend on this exercise?**
  - 2 hours.

- **Please include any general feedback you have about the exercise.**
  - It was a good learning experience and enjoyable coding for me.

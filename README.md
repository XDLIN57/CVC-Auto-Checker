# Automated CVC Code Tester

This Python script uses the `pyautogui` library to automate the process of testing CVC codes in a graphical user interface. It is specifically designed for Microsoft Edge and works exclusively on screens with a resolution of 1920x1200.

## Features
- **Dynamic CVC Testing:** Automatically iterates through CVC codes ranging from `200` to `999`.
- **Fixed Coordinates:** Predefined coordinates for the input text box and confirmation button tailored to Microsoft Edge on 1920x1200 screens.
- **Keyboard and Mouse Automation:** Simulates user input by typing CVC codes and clicking buttons.
- **Error-Free Workflow:** Clears the text box after each attempt for a seamless testing process.

## How It Works
1. The script generates CVC codes as 3-digit strings.
2. It moves the mouse to the specified text box coordinates and types the CVC code.
3. The mouse then moves to the confirmation button coordinates and clicks to submit the code.
4. After a 5-second wait, the text box is cleared, and the next CVC code is entered.

## Requirements
- Python 3.x
- `pyautogui` library
- Microsoft Edge browser
- Screen resolution of 1920x1200

## Usage
1. Install the required library:
   ```bash
   pip install pyautogui
   ```
2. Ensure your screen resolution is set to 1920x1200 and you are using Microsoft Edge.
3. Run the script:
   ```bash
   python CVC_Auto_Checker.py
   ```

## Disclaimer
This script is intended for educational and testing purposes only. Ensure you have permission before using it to interact with any software or system. It is optimized for specific conditions and may not function correctly in other setups.

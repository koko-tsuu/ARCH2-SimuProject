# ARCH2-SimuProject
## Binary-16 Floating-point Converter
### Overview
- This is the repository for the Binary-16 floating point converter created for the Simulation project of CSARCH2 Group 5 Section S11. The converter is designed to take in mantissa and exponent inputs and converts it into the IEEE-754 representation format and its hexadecimal counterpart.

### Features
- Turns input into IEEE-754 Binary-16 Format
- Input: (1) binary mantissa and base-2, decimal mantissa and base-10, inclusive of special cases
- Output: (1) binary-16 format output with space between section (2) its hexadecimal equivalent (3)
with option to output in text file as download from browser
- Input mode may be toggled

## How to Run on your Machine
- Ensure that Python is installed and can be found in the PATH of your device's user and system variables.
1. Open start_server.bat
2. Open localhost:5000 in browser

If that doesn't work, please run the python script from the parent directory like this:
`py src/main.py`, and then access from your browser


### (Screenshots and video demo can be found in "testcases" folder)

## Project Experience
- This project was made using Python w/ Flask, HTML, Bootstrap 5, and JINJA

### Problems Encountered
#### On the topic of Special Cases:
- It was difficult to represent the difference between sNaN and qNan, so we decided to simply make them representable using the word itself as the input.
- Giving feedback to the user was important, so there was a lot of if statements / mapping so we would not just throw binary at the user
- This also meant that we needed to use strings as our input.
  
#### On the topic of Python speed
- Large inputs are not good for Python as calculations were very slow because we used string inputs.

#### On the topic of manipulating large ints or floats in Python
- Inputting strings and converting them to int had a length limit, so we opted code a custom to_int() function that iterates through the digits.
- This means having to manually perform multiplication, move with base 10 for easier conversion to binary, convert to 1.f format, and etc.
- This was also the primary reason why we chose to use strings to read and manipulate values.

#### On the topic of binary conversion with decimal numbers
- bin() cannot convert float or decimal, so the convertDecimalOfDecimalToBinary function was needed to manually convert decimal numbers (ex. 0.5). 


#### Prepared by:
- Alog, Lorenz Wilson
- Exconde, Isiah Reuben
- Martinez, Francis Benedict
- Tan, Colleen Julianna
- Uy, Orrin Landon

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


#### On the topic of Python speed
- Large inputs are not good for Python, calculations were very slow because we used string inputs

#### On the topic of Python str to int conversion limit
- Inputting strings and converting them to int had a length limit, so we opted code a custom to_int() function that iterates through the digits



#### Prepared by:
- Alog, Lorenz Wilson
- Exconde, Isiah Reuben
- Martinez, Francis Benedict
- Tan, Colleen Julianna
- Uy, Orrin Landon
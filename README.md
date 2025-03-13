AIME-SOLVE: Accessible Interactive Mathematical Expressions Solver for Optimized Learning and Visual Empowerment

Introduction

AIME-SOLVE is a user-friendly and fully accessible software designed to assist individuals, including those with visual impairments, in solving mathematical expressions. The application supports speech recognition for input and text-to-speech (TTS) for auditory feedback, ensuring an inclusive and interactive learning experience.

Features

Speech Recognition:

Users can input mathematical expressions and answers using voice commands.

Converts spoken input into text for seamless interaction.

Text-to-Speech Feedback:

Provides auditory feedback, instructions, and results using the TTS engine.

Mathematical Operations:

Supports addition and subtraction of symbolic mathematical expressions.

Uses SymPy to combine like terms and simplify expressions.

Step-by-Step Feedback:

Demonstrates solution steps through both text and speech output.

Displays explanations when the user's answer is incorrect.

Mobile-Friendly Design:

Optimized layout for mobile screens with accessible buttons and inputs.

Error Handling:

Detects and alerts users of invalid inputs or unsupported operations.

System Requirements

Operating System:

Windows, macOS, or Linux

Android (using Kivy-compatible APK)

Python Version:

Python 3.7 or higher

Required Dependencies:

The following libraries are required for the application:

kivy (GUI Framework)

sympy (Symbolic Mathematics)

gtts (Google Text-to-Speech)

speechrecognition (Speech Input)

os (System Operations)

Installation

Clone or Download the Repository:

git clone https://github.com/amjadsharim/AIME_SLOVE
cd AIME-SOLVE

Install Required Dependencies:

Run the following command to install all necessary libraries:

pip install -r requirements.txt

Alternatively, install dependencies manually:

pip install kivy sympy gtts SpeechRecognition

Run the Application:

python main.py

Optional (Mobile Deployment):

Convert the app into an APK using Buildozer for Android platforms.

Follow the Kivy Buildozer Guide for packaging.

Usage Instructions

Launch the application.

Speak or type the first mathematical expression in the "Expression 1" field.

Speak or type the second mathematical expression in the "Expression 2" field.

Select the operation (Addition or Subtraction) using the toggle buttons.

Speak or type your answer in the "Your Answer" field.

Press the "Solve" button to calculate the result.

View the result and step-by-step solution on the interface or hear it via TTS.

Example Inputs

Expression 1: x + 5

Expression 2: 2*x + 3

Operation: Addition

User's Answer: 3*x + 8

Expected Result: Correct!

Accessibility Features

Speech Recognition: Allows users to speak instead of typing.

Text-to-Speech (TTS): Reads out instructions, results, and feedback.

Mobile-Friendly Layout: Designed for accessibility with large, easy-to-use buttons.

Known Issues

Speech recognition may fail in noisy environments.

Limited to addition and subtraction operations for now.

Requires an internet connection for TTS and speech recognition.

Future Enhancements

Support for Multiplication and Division: Extend operations to handle more complex expressions.

Offline Mode: Integrate offline speech recognition and TTS for better accessibility.

Graphical Representation: Display graphs of equations for better visualization.

Enhanced Feedback: Provide hints for incorrect answers to guide learning.

License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the software with attribution.

Contact

For feedback, questions, or contributions:

Email: Amjad.cs@uop.edu.pk

GitHub: https://github.com/amjadsharim/AIME_SLOVE

Acknowledgments

Kivy: For the powerful and versatile GUI framework.

SymPy: For simplifying and solving mathematical expressions.

Google TTS: For providing voice feedback functionality.

SpeechRecognition: For enabling speech-based input.

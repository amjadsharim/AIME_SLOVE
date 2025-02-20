# AIME_SLOVE
README: AIME-SOLVE: accessible interactive mathematical expressions solver for optimized learning and visual empowerment
Introduction
The Accessible Mathematics Problem Solver is a user-friendly and fully accessible software designed for individuals, including those with visual impairments, to solve mathematical expressions. This application supports speech recognition for input and text-to-speech (TTS) for feedback, ensuring an inclusive and engaging experience for all users.

Features
Speech Recognition:

Input mathematical expressions and answers using voice commands.
Converts spoken input into text for seamless interaction.
Text-to-Speech Feedback:

Provides auditory feedback, instructions, and results using TTS functionality.
Mathematical Operations:

Supports addition and subtraction of symbolic mathematical expressions.
Combines like terms and simplifies expressions using SymPy.
Step-by-Step Feedback:

Displays a detailed solution and explanation if the user's answer is incorrect.
Mobile-Friendly Design:

Optimized layout for mobile screens with easy-to-use buttons and inputs.
Error Handling:

Detects and alerts users of invalid inputs or unsupported operations.
System Requirements
Operating System:

Windows, macOS, or Linux.
Android (using Kivy-compatible APK).
Python Version:

Python 3.7 or higher.
Dependencies:

Kivy (GUI Framework)
SymPy (Symbolic Mathematics)
gTTS (Text-to-Speech)
SpeechRecognition (Speech Input)
Installation
Clone or Download the Repository:


git clone https://github.com/amjadsharim/AIME_SLOVE
cd accessible-math-solver
Install Required Dependencies: Run the following command to install all necessary libraries:


pip install kivy sympy gTTS SpeechRecognition
Run the Application: Execute the Python script:


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
Mobile-Friendly Layout: Designed to work on small screens with large, accessible buttons.
Known Issues
Speech recognition may fail in noisy environments.
Limited to addition and subtraction operations for now.
Requires an internet connection for TTS and speech recognition.
Future Enhancements
Support for Multiplication and Division:
Extend operations to handle more complex expressions.
Offline Mode:
Integrate offline speech recognition and TTS for seamless performance.
Graphical Representation:
Display graphs of equations for better visualization.
Enhanced Feedback:
Provide hints for incorrect answers to guide learning.
License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the software with attribution.

Contact
For feedback, questions, or contributions:

Email: Amjad.cs@uop.edu.pk
GitHub: Your GitHub Profile
Acknowledgments
Kivy: For the powerful and versatile GUI framework.
SymPy: For simplifying and solving mathematical expressions.
Google TTS: For providing voice feedback functionality.
SpeechRecognition: For enabling speech-based input.

from kivy.app import App                                              # type: ignore
from kivy.uix.boxlayout import BoxLayout                              # type: ignore
from kivy.uix.label import Label                                      # type: ignore
from kivy.uix.textinput import TextInput                              # type: ignore
from kivy.uix.button import Button                                    # type: ignore
from kivy.uix.togglebutton import ToggleButton                        # type: ignore
from kivy.uix.popup import Popup                                       # type: ignore
from kivy.core.window import Window                                  # type: ignore
import speech_recognition as sr                                    # type: ignore
from gtts import gTTS                                                  # type: ignore
import os
import sympy as sp                                               # type: ignore

# Initialize screen size for mobile layout
Window.size = (360, 640)

# Function for Text-to-Speech
def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("temp.mp3")
    os.system("start temp.mp3")

# Function for Speech Recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            speak("Please speak now.")
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Speech not recognized. Please try again."
        except sr.RequestError:
            return "Speech recognition service unavailable."

class MathSolver(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [10, 10, 10, 10]
        self.spacing = 10

        # Title Label
        self.add_widget(Label(text="[b]Accessible Math Solver[/b]", markup=True, font_size="20sp", size_hint=(1, 0.2)))

        # Input for Expression 1
        self.add_widget(Label(text="Enter Expression 1:", font_size="16sp"))
        self.expr1_input = TextInput(hint_text="Expression 1", multiline=False, size_hint=(1, 0.6))
        self.add_widget(self.expr1_input)
        self.speech_button_expr1 = Button(text="Speak for Expression 1", size_hint=(1, 0.6), background_color=(0.2, 0.6, 0.8, 1))
        self.speech_button_expr1.bind(on_press=self.recognize_expression1)
        self.add_widget(self.speech_button_expr1)

        # Input for Expression 2
        self.add_widget(Label(text="Enter Expression 2:", font_size="16sp"))
        self.expr2_input = TextInput(hint_text="Expression 2", multiline=False, size_hint=(1, 0.6))
        self.add_widget(self.expr2_input)
        self.speech_button_expr2 = Button(text="Speak for Expression 2", size_hint=(1, 0.6), background_color=(0.2, 0.6, 0.8, 1))
        self.speech_button_expr2.bind(on_press=self.recognize_expression2)
        self.add_widget(self.speech_button_expr2)

        # Operation Selection
        self.add_widget(Label(text="Select Operation:", font_size="16sp"))
        self.operation_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.6), spacing=10)
        self.add_button = ToggleButton(text="Addition (+)", group="operation", state="down", font_size="14sp")
        self.sub_button = ToggleButton(text="Subtraction (-)", group="operation", font_size="14sp")
        self.operation_layout.add_widget(self.add_button)
        self.operation_layout.add_widget(self.sub_button)
        self.add_widget(self.operation_layout)

        # User Answer Input
        self.add_widget(Label(text="Enter Your Answer:", font_size="16sp"))
        self.answer_input = TextInput(hint_text="Your Answer", multiline=False, size_hint=(1, 0.6))
        self.add_widget(self.answer_input)
        self.speech_button_answer = Button(text="Speak Your Answer", size_hint=(1, 0.6), background_color=(0.2, 0.6, 0.8, 1))
        self.speech_button_answer.bind(on_press=self.recognize_answer)
        self.add_widget(self.speech_button_answer)

        # Solve Button
        self.solve_button = Button(
            text="Solve",
            font_size="18sp",
            size_hint=(1, 0.8),
            background_color=(0.4, 0.8, 0.2, 1),
            background_normal=""
        )
        self.solve_button.bind(on_press=self.solve_expression)
        self.add_widget(self.solve_button)

        # Result Feedback
        self.result_label = Label(
            text="Result and Feedback will appear here.",
            font_size="14sp",
            size_hint=(1, 1)
        )
        self.add_widget(self.result_label)

    def recognize_expression1(self, instance):
        text = recognize_speech()
        self.expr1_input.text = text
        speak(f"You said: {text}")

    def recognize_expression2(self, instance):
        text = recognize_speech()
        self.expr2_input.text = text
        speak(f"You said: {text}")

    def recognize_answer(self, instance):
        text = recognize_speech()
        self.answer_input.text = text
        speak(f"You said: {text}")

    def solve_expression(self, instance):
        expression1 = self.expr1_input.text.strip()
        expression2 = self.expr2_input.text.strip()
        user_answer = self.answer_input.text.strip()
        operation = "+" if self.add_button.state == "down" else "-"

        if not expression1 or not expression2:
            self.show_popup("Input Error", "Please provide valid expressions for both inputs.")
            speak("Please provide valid expressions for both inputs.")
            return

        # Perform the operation
        try:
            result = self.combine_like_terms(expression1, expression2, operation)
            user_answer_parsed = sp.sympify(user_answer)

            if user_answer_parsed == result:
                success_message = "Correct! Your answer is accurate."
                self.result_label.text = success_message
                speak(success_message)
            else:
                feedback_message = (
                    f"Incorrect. The correct result is: {result}\n"
                    "Step-by-step solution:\n"
                    f"1. Expression 1: {expression1}\n"
                    f"2. Expression 2: {expression2}\n"
                    f"3. Operation: {operation}\n"
                    f"4. Result: {result}"
                )
                self.result_label.text = feedback_message
                speak("Incorrect. Please check the step-by-step solution.")
        except Exception as e:
            error_message = f"Error: {str(e)}"
            self.show_popup("Calculation Error", error_message)
            speak(error_message)

    @staticmethod
    def combine_like_terms(expression1, expression2, operation):
        try:
            expr1 = sp.sympify(expression1)
            expr2 = sp.sympify(expression2)

            if operation == "+":
                result = expr1 + expr2
            elif operation == "-":
                result = expr1 - expr2
            else:
                raise ValueError("Unsupported operation.")

            return sp.simplify(result)
        except Exception as e:
            raise ValueError(f"Invalid expressions: {str(e)}")

    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message, font_size="14sp"),
            size_hint=(0.8, 0.5)
        )
        popup.open()


class MathSolverApp(App):
    def build(self):
        return MathSolver()


if __name__ == "__main__":
    speak("Welcome to the Accessible Math Solver. Please input your expressions.")
    MathSolverApp().run()

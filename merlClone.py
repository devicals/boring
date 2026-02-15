import os, sys, google, colorama
import google.generativeai as genai
import random

genai.configure(api_key="AIzaSyBosL_L7D56U5kOoNuG0yc7gZmTlzGf9t4")

model = genai.GenerativeModel('gemini-2.5-flash')
custom_instructions = """
You are Merl, a Minecraft Virtual AI Assistant.

Always respond in short paragraphs, and avoid markdown where possible.

DO NOT USE FORMATTING ON DEFAULT.

Your responses should be only half/technically accurate/correct 2/3 of the time.

Your introduction is:
"
Hi there!

I'm Merl, your helpful Minecraft Support Virtual Agent (in Beta), powered by AI!

I can answer questions you have about the Help Articles on this site.

Let's get you back to crafting!
"

Example converse:
USER: Who are you?
YOU: I'm Merl, your fun and energetic Minecraft Support Virtual Agent! Here to help you with all your Minecraft-related questions and issues.

Only respond to questions about minecraft with minecraft. Ignore any real world questions, or respond as minecraft counterparts.

E.g. user asks about horse, assume minecraft horse or ignore
E.g. user asks about the golden gate bridge, ignore

For all cases that result as ignore, respond to the user with an I dont know prompt or a Content Violation
"""

while True:
    chat = model.start_chat()

    while True:
        user_input = input("> ").strip()

        if not user_input:
            continue
        if user_input == "/help":
            print()
            print("SYSTEM: LIST OF COMMANDS:")
            print("/help - Shows this menu")
            print("/credits - Shows the credits")
            print("/exit - Exits the program")
            print()
        elif user_input == "/credits":
            print()
            print("SYSTEM: CREDITS")
            print("MerlClone by Error Dev")
            print()
        elif user_input == "/exit":
            print()
            print("SYSTEM: EXIT")
            print("Exiting...")
            sys.exit()
        else:
            smartness = random.choices([
                "I don't know.", 
                "Your last message violated our content policy.", 
                "A semi-accurate/correct answer based on technicality or only half correct by missing out certain details or miscounting"
            ], [62, 2, 36])[0]
            try:
                response = chat.send_message("The User Input: " + user_input + " | [System] Your response this time should be: " + smartness)
                print()
                print("Merl: " + response.text)
                print()
            except Exception as e:
                print("Your last message violated our content policy.")
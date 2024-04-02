import subprocess
import sys
try:
    import requests
except ImportError:
    print("Установка библиотеки requests")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
    print("Библиотека colorama установленна!")
try:
    import telebot
    from telebot import types, apihelper
except ImportError:
    print("Установка библиотеки telebot")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'telebot'])
    print("Библиотека colorama установленна!")
try:
    import colorama
    from colorama import init, Fore, Style, Back
except ImportError:
    print("Установка библиотеки colorama")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
    print("Библиотека colorama установленна!")

input("Библиотеки установленны! Enter для выхода.")

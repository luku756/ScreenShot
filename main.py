import pyautogui
import keyboard
import datetime
import os
import pygame

save_folder = 'screenshots'
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

pygame.mixer.init()

print("F12 누르면 전체 화면 스크린샷 저장. 종료: Ctrl+C")

try:
    while True:
        if keyboard.is_pressed('F12'):
            screenshot = pyautogui.screenshot()

            now = datetime.datetime.now()
            timestamp = now.strftime('%Y%m%d_%H%M%S_%f')[:-3]

            filename = f"fullscreen_{timestamp}.png"
            filepath = os.path.join(save_folder, filename)
            screenshot.save(filepath)

            sound_path = os.path.abspath('resources/찰칵.mp3')
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()

            print(f"스크린샷 저장됨: {filepath}")

            while keyboard.is_pressed('F12'):
                pass

except KeyboardInterrupt:
    print("\n프로그램 종료")

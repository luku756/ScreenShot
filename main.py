import pyautogui
import keyboard
import datetime
import os
import pygame
import pygetwindow as gw
import psutil
import ctypes
from ctypes import wintypes


def get_pid_from_hwnd(hwnd):
    pid = wintypes.DWORD()
    ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    return pid.value


save_folder = 'screenshots'
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

pygame.mixer.init()

print("F12 누르면 활성 윈도우 화면 스크린샷 저장. 종료: Ctrl+C")

try:
    while True:
        if keyboard.is_pressed('F12'):
            active_win = gw.getActiveWindow()
            if active_win is None:
                print("활성 윈도우를 찾을 수 없습니다. 전체 화면 캡처로 대체합니다.")
                screenshot = pyautogui.screenshot()
                proc_name = "unknown"
            else:
                hwnd = active_win._hWnd
                pid = get_pid_from_hwnd(hwnd)
                try:
                    proc = psutil.Process(pid)
                    proc_name = proc.name().replace('.exe', '').replace(' ', '_')
                except Exception:
                    proc_name = "unknown"

                left, top, width, height = active_win.left, active_win.top, active_win.width, active_win.height
                screenshot = pyautogui.screenshot(region=(left, top, width, height))

            # 프로세스 이름 폴더 생성
            proc_folder = os.path.join(save_folder, proc_name)
            if not os.path.exists(proc_folder):
                os.makedirs(proc_folder)

            now = datetime.datetime.now()
            timestamp = now.strftime('%Y%m%d_%H%M%S_%f')[:-3]

            filename = f"{proc_name}_{timestamp}.png"
            filepath = os.path.join(proc_folder, filename)
            screenshot.save(filepath)

            sound_path = os.path.abspath('resources/찰칵.mp3')
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()

            print(f"스크린샷 저장됨: {filepath}")

            while keyboard.is_pressed('F12'):
                pass

except KeyboardInterrupt:
    print("\n프로그램 종료")

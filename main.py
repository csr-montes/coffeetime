import tkinter as tk
import threading
import pyautogui
import pynput.mouse
import pynput.keyboard
import time


class Window:
    def __init__(self):
        self.create_widgets()
        self.is_running = False

    def create_widgets(self):
        self.window = tk.Tk()
        self.window.title("CoffeeTime")
        self.window.geometry("400x100")

        self.frame_button_status = tk.Frame(self.window)
        self.frame_button_status.pack(side=tk.TOP, fill=tk.X)

        self.button = tk.Button(self.frame_button_status, text="Activar / Desactivar", command=self.button_click)
        self.button.pack(side=tk.LEFT)

        self.status = tk.Label(self.frame_button_status, text="Status", anchor=tk.W)
        self.status.pack(side=tk.RIGHT)

        self.scrollbar = tk.Scrollbar(self.window)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.textarea = tk.Text(self.window, yscrollcommand=self.scrollbar.set)
        self.textarea.pack(side=tk.BOTTOM, fill=tk.BOTH)

        self.scrollbar.config(command=self.textarea.yview)

        self.window.protocol("WM_DELETE_WINDOW", self.end)

    def button_click(self):
        if not self.is_running:
            self.status["text"] = "En ejecución"
            self.is_running = True
            threading.Thread(target=self.monitor_input_activity).start()
        else:
            self.status["text"] = "Detenido"
            self.is_running = False

    def start(self):
        self.window.mainloop()

    def end(self):
        self.is_running = False
        self.window.destroy()

    def on_mouse_move(self, x, y):
        self.last_activity_time = time.time()

    def on_mouse_click(self, x, y, button, pressed):
        self.last_activity_time = time.time()

    def on_keyboard_press(self, key):
        self.last_activity_time = time.time()
        if key == self.stop_sequence[self.current_sequence]:
            self.current_sequence += 1
            if self.current_sequence == len(self.stop_sequence):
                self.is_running = False
        else:
            self.current_sequence = 0

    def monitor_input_activity(self):
        self.last_activity_time = time.time()
        self.stop_sequence = (pynput.keyboard.Key.ctrl_l, pynput.keyboard.Key.alt_l, pynput.keyboard.Key.delete)
        self.current_sequence = 0

        mouse_listener = pynput.mouse.Listener(on_move=self.on_mouse_move, on_click=self.on_mouse_click)
        keyboard_listener = pynput.keyboard.Listener(on_press=self.on_keyboard_press)

        mouse_listener.start()
        keyboard_listener.start()

        while self.is_running:
            if time.time() - self.last_activity_time > 60:
                message = time.strftime("%Y-%m-%d %H:%M:%S") + " - Inactividad registrada\n"
                self.textarea.insert(tk.END, message)
                self.textarea.see(tk.END)

                for i in range(100, 110):
                    pyautogui.moveTo(0, i * 5)
                for i in range(0, 2):
                    pyautogui.press('numlock')

            time.sleep(1)

        mouse_listener.stop()
        keyboard_listener.stop()
        pynput.keyboard.Controller().press(pynput.keyboard.Key.esc)


v = Window()
v.start()

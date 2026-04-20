import sys
has_win32gui = False
try:
    import win32gui
    import win32con
    has_win32gui = True
except:
    pass

def run():
    if not has_win32gui:
        print("no win32gui")
        return
    all_windows = []
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title and title.strip():
                windows.append(title)
        return True

    win32gui.EnumWindows(callback, all_windows)
    print(all_windows)
run()

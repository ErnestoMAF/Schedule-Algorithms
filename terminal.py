import time

class Drawer:

    def draw_process(self, process, character='#'):
        print()
        for i in range(1, process.execution_time + 1): 
            print_characters = int((i / process.execution_time) * 50)
            print(f"{process.process_name:<25} [{character * print_characters:<50}] {i}/{process.execution_time}s", end='\r')
            time.sleep(0.3) 
    
    def draw_schedule(self, processes):
        for process in processes:
            self.draw_process(process)


class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def show(self):
        print(self.title)
        print("=" * len(self.title))
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")
        print()
        

class MainMenu(Menu):
    def __init__(self):
        super().__init__("Main Menu",
                          [ "Upload processes file",
                            "Upload process",
                            "Show process",
                            "Schedule Algorithm"
                            ])

class ScheduleMenu(Menu):
    def __init__(self):
        super().__init__("Schedule Menu",
                          [ "FCFS",
                            "SFJ",
                            "Priority",
                            "Round Robin",
                            "Exit"
                            ])
from terminal import *
from file import OpenFile, FileProcesses
from process import *
from schedule import * 
import os

if __name__ == "__main__":

    file_path = 'process.txt'
    processes = ProcessArray()

    while True:
        main_menu = MainMenu().show()
        option = input("Select an option: ")
        os.system('clear')

        if option == "1":
            os.system('clear')
            #Open file and obtain an array with processes data
            try:
                with OpenFile(file_path) as file:
                    file_processes = FileProcesses(file)
                    processes_in_file = file_processes.get_process()
                #Get and ProcessArray struct with Process
                processes._generate_processes(processes_in_file)
                print("Process upload successfully!")
                input("Press Enter to continue...")
                os.system('clear')
            except Exception as e:
                print(f"Error: {e}")
                
        elif option == "2":            
            process_position = False
            while process_position != '1' and process_position != '2':
                os.system('clear')
                print("New Process")
                process_name = input("Name: ")
                process_execution_time = input("Execution time: ")
                process_priority = input("Priority: ")
                process_position= input("\nProcess position: \n1.At the beggining \n2.At the end \nPosition:")
                try:
                    process = Process(process_name,process_execution_time,process_priority)
                    if (process_position == '1' or process_position == '2') and process:
                     processes.processes.insert(0,process) if process_position == '1' else processes.processes.append(process)
                    else:
                        print("Invalid value for process position.")
                except:
                    print("Invalid value for process.")
                input("Press Enter to continue...")
                os.system('clear')

        elif option == "3":
            os.system('clear')
            print(f"{processes}\n") if processes else print("No processes in system.\n")
            input("Press Enter to continue...")
            os.system('clear')
        
        elif option == "4":
            if processes:
                scheduler = Scheduler()
                drawer = Drawer()

                while True:
                    os.system('clear')
                    main_menu = ScheduleMenu().show()
                    option_schedule = input("Select an option: ")
                    os.system('clear')

                    if option_schedule == "1":
                        scheduler.set_strategy(FCFS())
                    elif option_schedule == "2":
                        scheduler.set_strategy(SFC())                    
                    elif option_schedule == "3":
                        scheduler.set_strategy(Priority())
                    elif option_schedule == "4":
                        scheduler.set_strategy(RoundRobin(3))
                    elif option_schedule == "5":
                        break
                    else:
                        print("Invalid Option.\n")
                        input("Press Enter to continue...")
                        os.system('clear')
                    
                    
                    scheduled_processes = scheduler.schedule_processes(processes.processes)
                    drawer.draw_schedule(scheduled_processes)
                    input("\nPress Enter to continue...")
                    os.system('clear')
            else:
                print("No processes in system.\n")
                input("Press Enter to continue...")
                os.system('clear')
        else:
            print("Invalid Option.\n")
            input("Press Enter to continue...")
            os.system('clear')
            
 
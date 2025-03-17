class Process:
    def __init__(self, process_name, execution_time, priority=0):
        try:
            self.execution_time = int(execution_time)
            self.priority = int(priority)
            self.process_name = str(process_name)

        except (ValueError, TypeError) as e:
            print(f"Error with process arguments: {e}")

    def __repr__(self):
        return f"Process(name={self.process_name}, time={self.execution_time}, priority={self.priority})"
    

class ProcessArray:
    def __init__(self):
        self.processes = []

    def _generate_processes(self, processes_in_file):
        processes = []
        for process in processes_in_file:
            process_name = process[0]
            execution_time = process[1] 
            priority = process[2]
            processes.append(Process(process_name, execution_time, priority))
        self.processes = processes
        return processes

    def __repr__(self):
        return "\n".join([f"Index: {i+1}, {str(p)}" for i, p in enumerate(self.processes)])
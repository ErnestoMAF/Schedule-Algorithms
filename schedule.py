from abc import ABC, abstractmethod
import copy

class SchedulerStrategy(ABC):
    @abstractmethod
    def schedule(self, processes):
        pass

class FCFS(SchedulerStrategy):
    def schedule(self, processes):
        return processes

class SJF(SchedulerStrategy):
    def schedule(self, processes):
        # Ordenar por tiempo de ejecución (el más corto primero)
        return sorted(processes, key=lambda p: p.execution_time)

class Priority(SchedulerStrategy):
    def schedule(self, processes):
        # Ordenar por priodidad
        return sorted(processes, key=lambda p: p.priority,reverse=True)

class RoundRobin(SchedulerStrategy):

    def __init__(self, quantum):
        self.quantum = quantum

    def schedule(self, processes):
        from process import Process
        scheduled_processes = []  
        temp_processes = copy.deepcopy(processes)

        while temp_processes:
            current_process = temp_processes.pop(0)

            if current_process.execution_time > self.quantum:
                scheduled_processes.append(Process(current_process.process_name, self.quantum,))
                current_process.execution_time -= self.quantum
                temp_processes.append(current_process)
            else:
                scheduled_processes.append(Process(current_process.process_name, current_process.execution_time))
        return scheduled_processes
            
class Scheduler:
    def set_strategy(self, strategy):
        self.strategy = strategy

    def schedule_processes(self, processes):
        return self.strategy.schedule(processes)

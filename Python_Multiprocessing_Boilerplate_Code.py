import multiprocessing as mp
import time

# Example functions for computation
def task_one(x1):
    pass

def task_two(x2):
    pass

def task_three(x3):
    pass

if __name__ == "__main__":
    x1=  # argument can be int, float, bool, string 
    x2=  # argument can be int, float, bool, string 
    x3=  # argument can be int, float, bool, string 

    # Parallel execution
    print("Running in parallel...")
    par_start_time = time.time()

    # Create individual processes for each task
    process1 = mp.Process(target=task_one, args=(x1,))
    process2 = mp.Process(target=task_two, args=(x2,))
    process3 = mp.Process(target=task_three, args=(x3,))

    # Pass the name of the process function to target
  
    # args take tuple so if your process function take one parameter then
    # you must add comma (n,) so the python can know it is a tuple and not 
    # int, float, bool, string

    # Start the processes
    process1.start()  # Start Process 1
    process2.start()  # Start Process 2
    process3.start()  # Start Process 3

    # Wait for all processes to finish
    process1.join()   # Wait till Process 1 finish then go to next instruction
    process2.join()   # Wait till Process 2 finish then go to next instruction
    process3.join()   # Wait till Process 3 finish then go to next instruction

    par_end_time = time.time()

    # Calculate the total time
    parallel_time = par_end_time - par_start_time
    print(f"Parallel execution time: {parallel_time:.2f} seconds\n")

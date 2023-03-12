def measure_performance(time, psutil, func, *args, **kwargs):
    # Get start time and memory usage
    start_time = time.time()
    start_mem = psutil.Process().memory_info().rss

    # Run the function with the provided arguments and keyword arguments
    func_result = func(*args, **kwargs)

    # Get end time and memory usage
    end_time = time.time()
    end_mem = psutil.Process().memory_info().rss

    # Print results
    print("Function took {} seconds to run.".format(end_time - start_time))
    print("Function used {:.2f} MB of memory.".format((end_mem - start_mem) / (1024 * 1024)))
    print("Total memory available: {:.2f} GB".format(psutil.virtual_memory().total / (1024 * 1024 * 1024)))
    print("CPU usage: {:.2f}%".format(psutil.cpu_percent()))
    
    return func_result
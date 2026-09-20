import sys, gc

_inputs = []

def get_input(prompt):
    try:
        val = input(prompt).strip()
    except:
        val = "q"
    _inputs.append(val)
    if len(_inputs) > 30:
        _inputs.pop(0)
    return val

def handle_crash(exception, extra_state=""):
    try:
        f = open("crashlog.txt", "w")
        try:
            f.write("=== CRASH LOG ===\n")
            
            # 1. Traceback & Error Details
            try:
                # MicroPython native traceback printer
                sys.print_exception(exception, f)
            except:
                f.write("Error: " + type(exception).__name__ + ": " + str(exception) + "\n")
            
            # 2. System & Memory Information
            try:
                f.write("Platform: " + str(sys.platform) + "\n")
                f.write("Version: " + str(sys.version) + "\n")
                f.write("Mem Free: " + str(gc.mem_free()) + " B\n")
                f.write("Mem Alloc: " + str(gc.mem_alloc()) + " B\n")
            except:
                pass

            # 3. Active Modules
            try:
                f.write("Modules: " + ", ".join(list(sys.modules.keys())) + "\n")
            except:
                pass

            # 4. Button / Input History
            f.write("Inputs: " + " -> ".join(_inputs) + "\n")
            
            # 5. Extra State Details
            if extra_state:
                f.write("State: " + str(extra_state) + "\n")
                
            f.write("=================\n")
        finally:
            f.close()
    except:
        pass


def file_read(file_p):
    """Read file and handles all types of file errors."""
    try:
        with open(file_p,"r") as f:
            data = f.read().strip()
        if not data:
            raise ValueError("file is empty.")
        return data
    except FileNotFoundError:
        print("check the file or file_path.")
        return None 
    except UnicodeDecodeError:
        print(" Enter a valid string file. encoding issue.")
        return None
    except (IOError, OSError) as e:
        print(f"file cannot be read: {e}")
        return None
    except ValueError as e:
        print(e)
        return None    

def taking_input():
    """Take input from the user and retrun it if the input is valid."""
    format = input("If you want to enter a file (press f) or a text (press t) :").strip().lower()

    if format == "t":
        data = input("enter your text :").strip()
        if not data:
            print("print data is empty")
            return None

    elif format == "f":
        file_p =input("Enter the path of your file.").strip()
        data = file_read(file_p)

    else:
        print("only press f or t.")
        return None
        
    if data is not None and  len(data) <= 8:
        print("Data is too small to summarize.")
        return None
    return data
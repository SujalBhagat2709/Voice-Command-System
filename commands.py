from listen import listen_command

def execute_command(command):
    
    if "hello" in command:
        return "Hello! How can I help you?"
    
    elif "time" in command:
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")
    
    elif "exit" in command:
        return "Exiting system"
    
    return "Unknown command"


if __name__ == "__main__":
    
    command = listen_command()
    
    print("You said:", command)
    
    print("Response:", execute_command(command))
def display_shutting_down():
    """Displays the message for shutting down."""
    print("Shutting down...")

def display_abort_shutdown():
    """Displays the message for aborting the shutdown."""
    print("Abort shut down.")

def display_error_message():
    """Displays the message for invalid input."""
    print("Sorry, invalid input.")

def shutdown():
    """
    Prompts the user for confirmation to shut down and calls
    relevant functions based on the input.
    """
    user_input = input("Are you sure you want to shut down? (Yes/No): ")
    
    user_input = user_input.lower()

    if user_input == "yes":
        display_shutting_down()
    elif user_input == "no":
        display_abort_shutdown()
    else:
        display_error_message()

if __name__ == "__main__":
    shutdown()

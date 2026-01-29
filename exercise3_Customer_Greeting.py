def format_greeting(name,title="Customer"):
    #remove extra spaces
    cleaned_name = name.strip()

    #handle empty input (default)
    if cleaned_name == "":
        return "Hello, Valued Customer!"
    
    #capitalize first letter of each word
    cleaned_name = cleaned_name.title()

    first_name = cleaned_name.split()[0]
    return f"Hello, {title} {first_name}!"


#Main program
full_name = input("What is your full name? ")
greeting = format_greeting(full_name)
print(greeting)
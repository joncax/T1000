# T1000 - Centered Interface (requires 'pip install rich')

from rich.console import Console
from rich.panel import Panel
from rich.text import Text # <-- NEW IMPORT

# Initialize the console object for colored output
console = Console()

# --- ARITHMETIC FUNCTIONS (Unchanged) ---
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "[bold red]ERROR: Division by zero is not permitted.[/bold red]"
    return x / y

# --- INTERFACE ---

def t1000_interface_rich():
  
     # 1. Create a blank Text object
    menu_text = Text(justify="center") 
    
    # 2. Append each line with its specific color
    # The "\n" is included at the end of each appended string.
    
    menu_text.append("Select Operation (Input Expected):\n", style="bold cyan")
    menu_text.append("1. Add (+)\n", style="green")
    menu_text.append("2. Subtract (-)\n", style="yellow")
    menu_text.append("3. Multiply (*)\n", style="blue")
    menu_text.append("4. Divide (/)\n", style="red")
    menu_text.append("5. Terminate (exit)\n\n\n", style="magenta") 
    # Added extra newlines for consistent panel width

    # Use a Panel for the initial display
    console.print(
        Panel(
            menu_text, # <-- Using the new Text object
            title="[bold red]T-1000 CALCULATOR INTERFACE[/bold red]",
            subtitle="Processing Unit Online",
            border_style="cyan",
            expand=False
        )
    )
    
    running = True
    while running:
        choice = console.input("[bold cyan]T-1000 Command[/bold cyan] (1/2/3/4/5): ")

        if choice == '5':
            console.print("\n[bold red]T-1000: Mission complete. Terminating process...[/bold red]")
            running = False
            continue

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(console.input("Enter [yellow]first number[/yellow]: "))
                num2 = float(console.input("Enter [yellow]second number[/yellow]: "))
            except ValueError:
                console.print("[bold red]ERROR:[/bold red] Invalid input. Please enter a valid number.\n")
                continue
            
            result = None
            op_symbol = ""
            
            # --- Perform Calculation ---
            if choice == '1':
                op_symbol = "+"
                result = add(num1, num2)
            # ... (rest of the calculation logic is unchanged)
            elif choice == '2':
                op_symbol = "-"
                result = subtract(num1, num2)
            elif choice == '3':
                op_symbol = "*"
                result = multiply(num1, num2)
            elif choice == '4':
                op_symbol = "/"
                result = divide(num1, num2)

            console.print(f"\n[bold green]Calculation:[/bold green] {num1} {op_symbol} {num2}")
            console.print(f"[bold white on blue]Result:[/bold white on blue] [bold yellow]{result}[/bold yellow]\n")

        else:
            console.print("[bold red]WARNING:[/bold red] Invalid input. Please enter a choice between 1 and 5.\n")

# Run the main function
if __name__ == "__main__":
    t1000_interface_rich()

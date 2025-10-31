# T1000 - Live Display Calculator (Final Working Version)

from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text
from rich.live import Live 

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
        return Text("ERROR: Division by zero is not permitted.", style="bold white on red")
    return x / y

# --- INTERFACE COMPONENTS (Unchanged) ---
def get_menu_panel():
    """Generates the main menu panel (static)."""
    menu_text = Text(justify="center") 
    menu_text.append("Select Operation (Input Expected):\n", style="bold cyan")
    menu_text.append("1. Add (+)\n", style="green")
    menu_text.append("2. Subtract (-)\n", style="yellow")
    menu_text.append("3. Multiply (*)\n", style="blue")
    menu_text.append("4. Divide (/)\n", style="red")
    menu_text.append("5. Terminate (exit)\n\n\n", style="magenta") 

    return Panel(
        menu_text,
        title="[bold red]T-1000 CALCULATOR INTERFACE[/bold red]",
        subtitle="Processing Unit Online",
        border_style="cyan",
        expand=False
    )

def get_display_panel(status):
    """Generates the live result display panel."""
    display_content = status if isinstance(status, (Text, Panel)) else f"[bold yellow]{status}[/bold yellow]"
    
    return Panel(
        display_content,
        title="[bold white]LIVE DISPLAY[/bold white]",
        border_style="yellow",
        expand=True
    )

def generate_screen(status):
    """Combines the display and menu into one screen layout."""
    display = get_display_panel(status)
    menu = get_menu_panel()
    
    # Use Group to stack renderables vertically (the fix for the previous error)
    return Group(display, menu)


# --- MAIN INTERFACE FUNCTION (Inputs Moved) ---

def t1000_interface_live():
    
    current_status = "T-1000 Unit Operational. Ready for calculation."
    
    # 1. Start the Live display in the background
    with Live(generate_screen(current_status), screen=True, refresh_per_second=4) as live:
        
        running = True
        while running:
            
            # 2. CAPTURE USER CHOICE OUTSIDE THE LIVE RENDERING LOOP
            # We use console.input, which renders the prompt on top of the Live output.
            choice = console.input("[bold cyan]\n[T-1000 Command][/bold cyan] (1/2/3/4/5): ")

            if choice == '5':
                current_status = "[bold white on red]T-1000: Mission complete. Terminating process...[/bold white on red]"
                live.update(generate_screen(current_status))
                running = False
                continue

            if choice in ('1', '2', '3', '4'):
                try:
                    # 3. CAPTURE NUMBERS OUTSIDE THE LIVE RENDERING LOOP
                    # We use console.input again for the numbers.
                    num1 = float(console.input("Enter [yellow]first number[/yellow]: "))
                    num2 = float(console.input("Enter [yellow]second number[/yellow]: "))
                except ValueError:
                    current_status = "[bold red]ERROR:[/bold red] Invalid input. Please enter a valid number."
                    live.update(generate_screen(current_status))
                    continue
                
                result = None
                op_symbol = ""
                
                # --- Perform Calculation (Unchanged) ---
                if choice == '1':
                    op_symbol = "+"
                    result = add(num1, num2)
                elif choice == '2':
                    op_symbol = "-"
                    result = subtract(num1, num2)
                elif choice == '3':
                    op_symbol = "*"
                    result = multiply(num1, num2)
                elif choice == '4':
                    op_symbol = "/"
                    result = divide(num1, num2)

                # --- Update Status ---
                if isinstance(result, Text):
                    current_status = result 
                else:
                    current_status = f"{num1} {op_symbol} {num2} = [bold white]{result}[/bold white]"
                
                # 4. Manually trigger a display refresh with the new status
                live.update(generate_screen(current_status))

            else:
                current_status = "[bold red]WARNING:[/bold red] Invalid input. Please enter a choice between 1 and 5."
                live.update(generate_screen(current_status))
                
# Run the main function
if __name__ == "__main__":
    t1000_interface_live()

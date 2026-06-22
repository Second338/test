import tkinter as tk
from tkinter import ttk
import uuid


class GreetingWindow:
    """Displays a greeting window with poetry"""
    
    def __init__(self, parent_app):
        self.parent_app = parent_app
        
        # Create the greeting window
        self.root = tk.Tk()
        self.root.title("Greeting")
        self.root.geometry("600x400")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Setup UI
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the greeting window UI"""
        # Main frame with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Title label
        title_label = ttk.Label(
            main_frame,
            text="Welcome",
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 15))
        
        # Text widget for poetry (read-only)
        self.text_display = tk.Text(main_frame, height=12, width=70, wrap=tk.WORD)
        self.text_display.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 15))
        
        # Insert the Poe excerpt
        poe_text = """But the Raven still beguiling all my fancy into smiling,
Straight I wheeled a cushioned seat in front of bird, and bust and door;
    Then, upon the velvet sinking, I betook myself to linking
    Fancy unto fancy, thinking what this ominous bird of yore—
What this grim, ungainly, ghastly, gaunt, and ominous bird of yore
            Meant in croaking "Nevermore.\""""
        
        self.text_display.insert(1.0, poe_text)
        self.text_display.config(state="disabled")
        
        # Scrollbar for text display
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.text_display.yview)
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        self.text_display.config(yscrollcommand=scrollbar.set)
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        
        # Close button
        close_button = ttk.Button(button_frame, text="Close", command=self.on_close)
        close_button.grid(row=0, column=0, padx=5, sticky=(tk.W, tk.E))
        
        # Start App button
        start_button = ttk.Button(button_frame, text="Start Application", command=self.start_app)
        start_button.grid(row=0, column=1, padx=5, sticky=(tk.W, tk.E))
    
    def start_app(self):
        """Start the main application"""
        self.parent_app.create_window()
        self.on_close()
    
    def on_close(self):
        """Handle window close event"""
        self.root.destroy()
    
    def run(self):
        """Start the greeting window's event loop"""
        self.root.mainloop()


class TextWindow:
    """Represents a single window with a text field"""
    
    def __init__(self, parent_app, window_number):
        self.parent_app = parent_app
        self.window_number = window_number
        self.window_id = str(uuid.uuid4())[:8]
        
        # Create the main window
        self.root = tk.Tk()
        self.root.title(f"Text Window {window_number}")
        self.root.geometry("400x300")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Create the UI
        self.setup_ui()
        
        # Track this window
        self.parent_app.windows.append(self)
    
    def setup_ui(self):
        """Set up the user interface for this window"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Label
        title_label = ttk.Label(
            main_frame,
            text=f"Window {self.window_number} (ID: {self.window_id})",
            font=("Arial", 12, "bold")
        )
        title_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        # Text entry label
        entry_label = ttk.Label(main_frame, text="Enter text:")
        entry_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        
        # Text entry field
        self.text_entry = ttk.Entry(main_frame, width=40)
        self.text_entry.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        self.text_entry.focus()
        
        # Text display area (read-only)
        display_label = ttk.Label(main_frame, text="Displayed text:")
        display_label.grid(row=3, column=0, sticky=tk.W, pady=(10, 5))
        
        # Text widget to display entered text
        self.text_display = tk.Text(main_frame, height=8, width=40, state="disabled")
        self.text_display.grid(row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Scrollbar for text display
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.text_display.yview)
        scrollbar.grid(row=4, column=1, sticky=(tk.N, tk.S))
        self.text_display.config(yscrollcommand=scrollbar.set)
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        
        # Display button
        display_button = ttk.Button(button_frame, text="Display Text", command=self.display_text)
        display_button.grid(row=0, column=0, padx=5, sticky=(tk.W, tk.E))
        
        # Clear button
        clear_button = ttk.Button(button_frame, text="Clear", command=self.clear_text)
        clear_button.grid(row=0, column=1, padx=5, sticky=(tk.W, tk.E))
        
        # New Window button
        new_window_button = ttk.Button(button_frame, text="New Window", command=self.open_new_window)
        new_window_button.grid(row=0, column=2, padx=5, sticky=(tk.W, tk.E))
    
    def display_text(self):
        """Display the text from the entry field"""
        text = self.text_entry.get()
        if text:
            self.text_display.config(state="normal")
            self.text_display.insert(tk.END, text + "\n")
            self.text_display.config(state="disabled")
            self.text_display.see(tk.END)
            self.text_entry.delete(0, tk.END)
    
    def clear_text(self):
        """Clear all displayed text"""
        self.text_entry.delete(0, tk.END)
        self.text_display.config(state="normal")
        self.text_display.delete(1.0, tk.END)
        self.text_display.config(state="disabled")
    
    def open_new_window(self):
        """Open a new text window"""
        self.parent_app.create_window()
    
    def on_close(self):
        """Handle window close event"""
        if self in self.parent_app.windows:
            self.parent_app.windows.remove(self)
        self.root.destroy()
    
    def run(self):
        """Start the window's event loop"""
        self.root.mainloop()


class TextFieldApp:
    """Main application class"""
    
    def __init__(self):
        self.windows = []
        self.window_counter = 0
    
    def create_window(self):
        """Create a new text window"""
        self.window_counter += 1
        window = TextWindow(self, self.window_counter)
        # Don't call mainloop here; windows run independently
        return window
    
    def run(self):
        """Start the application with the first window"""
        self.create_window()


if __name__ == "__main__":
    app = TextFieldApp()
    
    # Show greeting window first
    greeting = GreetingWindow(app)
    greeting.run()

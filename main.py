import tkinter as tk
from tkinter import ttk
import uuid


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
        entry_label = ttk.Label(main_frame, text="Enter text please:")
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
    app.run()
    tk.mainloop()

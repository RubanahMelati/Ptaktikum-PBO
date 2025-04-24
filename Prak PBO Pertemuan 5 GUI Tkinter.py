import tkinter as tk
from tkinter import messagebox
import datetime

class DailyNotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Catatan Harian")
        self.notes = {}  # Dictionary to store notes: {title: {content, timestamp}}
        
        # Setup Menu
        self.menubar = tk.Menu(self.root)
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="Keluar", command=self.exit_app)
        self.menubar.add_cascade(label="File", menu=file_menu)
        
        help_menu = tk.Menu(self.menubar, tearoff=0)
        help_menu.add_command(label="Tentang", command=self.show_about)
        self.menubar.add_cascade(label="Bantuan", menu=help_menu)
        self.root.config(menu=self.menubar)
        
        # Main Frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(padx=10, pady=10, sticky="nsew")
        
        # Title Entry
        tk.Label(self.main_frame, text="Judul:").grid(row=0, column=0, sticky="w")
        self.title_entry = tk.Entry(self.main_frame, width=50)
        self.title_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="ew")
        
        # Buttons
        tk.Button(self.main_frame, text="Tambah Catatan", command=self.add_note).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self.main_frame, text="Hapus Catatan", command=self.delete_note).grid(row=1, column=2, padx=5, pady=5)
        
        # Listbox and Scrollbar
        self.listbox_frame = tk.Frame(self.main_frame)
        self.listbox_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
        
        self.scrollbar = tk.Scrollbar(self.listbox_frame, orient="vertical")
        self.listbox = tk.Listbox(self.listbox_frame, width=40, height=15, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.listbox.bind("<<ListboxSelect>>", self.show_note)
        
        # Text Area - Mulai dengan state="normal" agar bisa diedit
        self.text_area = tk.Text(self.main_frame, width=40, height=15, state="normal")
        self.text_area.grid(row=2, column=2, padx=5, sticky="nsew")
        
        # Configure grid weights
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)
        self.main_frame.rowconfigure(2, weight=1)
        self.listbox_frame.columnconfigure(0, weight=1)
        self.listbox_frame.rowconfigure(0, weight=1)
    
    def add_note(self):
        title = self.title_entry.get().strip()
        content = self.text_area.get("1.0", tk.END).strip()
        
        if not title and not content:
            messagebox.showerror("Error", "Judul dan isi catatan tidak boleh kosong!")
        elif not title:
            messagebox.showerror("Error", "Judul tidak boleh kosong!")
        elif not content:
            messagebox.showerror("Error", "Isi catatan tidak boleh kosong!")
        else:
            if title in self.notes:
                messagebox.showerror("Error", "Judul catatan sudah ada, gunakan judul lain!")
                return
            
            # Store note with timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-d %H:%M:%S")
            self.notes[title] = {"content": content, "timestamp": timestamp}
            
            # Add to listbox
            self.listbox.insert(tk.END, f"{title} ({timestamp})")
            self.title_entry.delete(0, tk.END)
            
            # Clear text area and keep it enabled for new input
            self.text_area.delete("1.0", tk.END)
            messagebox.showinfo("Sukses", "Catatan berhasil ditambahkan!")
    
    def show_note(self, event):
        try:
            index = self.listbox.curselection()[0]
            title_with_time = self.listbox.get(index)
            title = title_with_time.split(" (")[0]
            
            # Display content in text area (read-only)
            self.text_area.config(state="normal")
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", self.notes[title]["content"])
            self.text_area.config(state="disabled")
        except IndexError:
            pass
    
    def delete_note(self):
        try:
            index = self.listbox.curselection()[0]
            title_with_time = self.listbox.get(index)
            title = title_with_time.split(" (")[0]
            
            # Confirm deletion
            if messagebox.askyesno("Konfirmasi", f"Hapus catatan '{title}'?"):
                del self.notes[title]
                self.listbox.delete(index)
                
                # Clear text area and enable it for new input
                self.text_area.config(state="normal")
                self.text_area.delete("1.0", tk.END)
                # Remove the line that disables the text area
                messagebox.showinfo("Sukses", "Catatan berhasil dihapus!")
        except IndexError:
            messagebox.showerror("Error", "Pilih catatan yang akan dihapus!")
    
    def exit_app(self):
        if messagebox.askyesno("Keluar", "Apakah Anda yakin ingin keluar?"):
            self.root.quit()
    
    def show_about(self):
        messagebox.showinfo("Tentang", "Aplikasi Catatan Harian\nVersi 1.0\nDibuat dengan Tkinter")

if __name__ == "__main__":
    root = tk.Tk()
    app = DailyNotesApp(root)
    root.mainloop()
import tkinter as tk
from getLoc import table_data

def on_search():
    search_text = search_var.get().lower()
    search_results.delete(0, tk.END)
    for item in cities:
        if search_text in item.lower():
            search_results.insert(tk.END, item)

def on_search_entry_changed(event):
    on_search()

def on_select(event):
    widget = event.widget
    selected_index = widget.curselection()[0]
    selected_item = widget.get(selected_index)
    search_var.set(selected_item)

# Sample data
cities = [row[0] for row in table_data]
Loc = [[row[1], row[2]] for row in table_data]

# GUI setup
root = tk.Tk()
root.title("Search Bar with Dropdown")

search_var = tk.StringVar()
search_var.trace("w", lambda name, index, mode: on_search())

search_entry = tk.Entry(root, textvariable=search_var)
search_entry.pack(padx=10, pady=10, fill=tk.X)

search_results = tk.Listbox(root, selectmode=tk.SINGLE)
search_results.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(search_results)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
search_results.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=search_results.yview)

for item in cities:
    search_results.insert(tk.END, item)

search_results.bind('<<ListboxSelect>>', on_select)
search_entry.bind('<KeyRelease>', on_search_entry_changed)

root.mainloop()

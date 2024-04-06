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
    #testing collected info
    search_value = "Yorkton, SK, Canada"
    corresponding_data = data_dict.get(search_value)
    # Add label in the center of additional_info_frame
    additional_label = tk.Label(additional_info_frame, text=corresponding_data, bg="white")
    additional_label.pack(expand=True, fill="both", pady=10)  # Pack the label with expansion
    search_var.set(selected_item)

# Sample data
cities = [row[0] for row in table_data]
Loc = [[row[1], row[2]] for row in table_data]
data_dict = {cities[i]: Loc[i] for i in range(len(cities))}


# GUI setup
root = tk.Tk()
root.title("Search Bar with Dropdown")

search_var = tk.StringVar()
search_var.trace("w", lambda name, index, mode: on_search())

search_entry = tk.Entry(root, textvariable=search_var)
search_entry.pack(padx=10, pady=10, fill=tk.X)

search_results_frame = tk.Frame(root)
search_results_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

search_results = tk.Listbox(search_results_frame, selectmode=tk.SINGLE)
search_results.grid(row=0, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(search_results_frame, orient=tk.VERTICAL, command=search_results.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
search_results.config(yscrollcommand=scrollbar.set)

# Additional widget on the right of scrollbar
additional_info_frame = tk.Frame(search_results_frame)
additional_info_frame.grid(row=0, column=2, sticky="nsew")

# Configure weights to make the widgets expand properly
search_results_frame.grid_rowconfigure(0, weight=1)
search_results_frame.grid_columnconfigure(0, weight=1)
search_results_frame.grid_columnconfigure(2, weight=1)
# Create a blank widget taking up 50% width and 100% height on the right
additional_info_frame = tk.Frame(search_results_frame, bg="white")
additional_info_frame.grid(row=0, column=2, sticky="nsew")
for item in cities:
    search_results.insert(tk.END, item)

search_results.bind('<<ListboxSelect>>', on_select)
search_entry.bind('<KeyRelease>', on_search_entry_changed)

root.mainloop()

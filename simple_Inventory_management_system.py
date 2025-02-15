import tkinter as tk
from tkinter import messagebox

class InventoryManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.inventory = {}
        
        # Labels
        tk.Label(root, text="Product Name:").grid(row=0, column=0)
        tk.Label(root, text="Quantity:").grid(row=1, column=0)
        tk.Label(root, text="Price:").grid(row=2, column=0)
        
        # Entry Fields
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=1, column=1)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=2, column=1)
        
        # Buttons
        tk.Button(root, text="Add Product", command=self.add_product).grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="View Inventory", command=self.view_inventory).grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="Remove Product", command=self.remove_product).grid(row=5, column=0, columnspan=2)
        
        # Inventory Display
        self.inventory_listbox = tk.Listbox(root, width=50)
        self.inventory_listbox.grid(row=6, column=0, columnspan=2)
    
    def add_product(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        
        if name and quantity.isdigit() and price.replace('.', '', 1).isdigit():
            self.inventory[name] = {'Quantity': int(quantity), 'Price': float(price)}
            messagebox.showinfo("Success", f"{name} added to inventory.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Invalid input. Please enter correct details.")
    
    def view_inventory(self):
        self.inventory_listbox.delete(0, tk.END)
        for product, details in self.inventory.items():
            self.inventory_listbox.insert(tk.END, f"{product} - Quantity: {details['Quantity']}, Price: ${details['Price']:.2f}")
    
    def remove_product(self):
        selected = self.inventory_listbox.get(tk.ACTIVE)
        if selected:
            product_name = selected.split(' - ')[0]
            if product_name in self.inventory:
                del self.inventory[product_name]
                messagebox.showinfo("Success", f"{product_name} removed from inventory.")
                self.view_inventory()
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManager(root)
    root.mainloop()

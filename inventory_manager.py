# 1. Defining the List (Our current stock)
# Notice the square brackets [] and commas ,
gpu_inventory = ["A100", "H100", "B100"]

print("--- Initial Inventory ---")
print(gpu_inventory)

# 2. Adding a new product (The .append method)
# This adds an item to the very END of the list
gpu_inventory.append("RTX 4090")

print("\n--- After Product Launch ---")
print(f"Updated Stock: {gpu_inventory}")

# 3. Counting items (The len function)
total_chips = len(gpu_inventory)
print(f"We are now managing {total_chips} different product lines.")
# Discontinuing an old model
discontinued = "A100"
if discontinued in gpu_inventory:
    gpu_inventory.remove(discontinued)
    print(f"\nProduct Lifecycle Update: {discontinued} has been discontinued.")
print(f"Current Active Inventory: {gpu_inventory}")
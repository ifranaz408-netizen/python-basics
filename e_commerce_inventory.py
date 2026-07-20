class Product:
    """Generic base class representing a general product in the inventory."""

    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def display_details(self):
        """Displays common product information."""
        print(f"[{self.product_id}] {self.name}")
        print(f"  Price: ${self.price:.2f}")
        print(f"  Stock: {self.stock} units")

    def restock(self, quantity: int):
        """Adds stock to the item."""
        self.stock += quantity
        print(
            f"--> Restocked {quantity} units of {self.name}. New total: {self.stock}"
        )


class Electronics(Product):
    """Child class representing electronic devices."""

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        brand: str,
        warranty_months: int,
    ):
        # Call base class constructor
        super().__init__(product_id, name, price, stock)
        self.brand = brand
        self.warranty_months = warranty_months

    def display_details(self):
        """Overrides parent display_details to include electronics-specific details."""
        super().display_details()
        print(f"  Brand: {self.brand}")
        print(f"  Warranty: {self.warranty_months} Months")


class Clothing(Product):
    """Child class representing apparel/clothing items."""

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        size: str,
        material: str,
    ):
        # Call base class constructor
        super().__init__(product_id, name, price, stock)
        self.size = size
        self.material = material

    def display_details(self):
        """Overrides parent display_details to include clothing-specific details."""
        super().display_details()
        print(f"  Size: {self.size}")
        print(f"  Material: {self.material}")


# ==========================================
# EXECUTION & DEMONSTRATION
# ==========================================
if __name__ == "__main__":
    # Instantiating specific products
    laptop = Electronics(
        product_id="E101",
        name="Pro Laptop 15",
        price=1299.99,
        stock=12,
        brand="TechCorp",
        warranty_months=24,
    )

    tshirt = Clothing(
        product_id="C202",
        name="Classic Crewneck T-Shirt",
        price=24.50,
        stock=50,
        size="L",
        material="100% Organic Cotton",
    )

    inventory = [laptop, tshirt]

    print("=" * 45)
    print("      E-COMMERCE INVENTORY MANAGEMENT      ")
    print("=" * 45)

    # Utilizing Polymorphism to display product details
    for item in inventory:
        item.display_details()
        print("-" * 45)

    # Restocking an item (Inherited base behavior)
    laptop.restock(5)

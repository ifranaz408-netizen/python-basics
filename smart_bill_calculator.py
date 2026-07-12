def calculate_bill(*args, **kwargs):
  subtotal = 0
  for price in args:
    subtotal = subtotal + price
  
  tax_rate =kwargs.get('tax', 0.1)
  discount = kwargs.get('discount', 0)
  service =kwargs.get('service', 0)
  if discount > 0:
    amount_after_discount = subtotal - (subtotal * discount)
    
  else :
   amount_after_discount = subtotal
    
  tax_amount = amount_after_discount *tax_rate
  total =amount_after_discount + tax_amount + service
  return {
    "Subtotal": f"Rs {round(subtotal, 2)}",
    "Discount": f"Rs {round(discount, 2)}",
    "Tax": f"Rs {round(tax_amount, 2)}",
    "Service": f"Rs {round(service, 2)}",
    "Final Total": f"Rs {round(total, 2)}",
  }

#car price
car_price = input("Enter car price: ")
car_price = int(car_price)
#extra cost
tax = car_price * 0.2
license = car_price * 0.1
dealer_preps = 20
delivery = 300
#total price
total_price = car_price + tax + license + dealer_preps + delivery
print("\nTotal price for this car is: ", total_price)
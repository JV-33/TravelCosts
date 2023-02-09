def calculate_fuel_cost(distance, price_per_km, fuel_price_per_liter, fuel_consumption):
    fuel_cost = (fuel_consumption / 100) * fuel_price_per_liter * distance
    total_cost = fuel_cost + (distance * price_per_km)
    return total_cost

distance = float(input("Ievadi attālumu (km): "))
price_per_km = float(input("Ievadi cenu par km (eiro): "))
fuel_consumption = float(input("Ievadi degvielas patēriņu (litri uz 100 km): "))

diesel_price = 1.80
petrol_price = 1.75

diesel_cost = calculate_fuel_cost(distance, price_per_km, diesel_price, fuel_consumption)
petrol_cost = calculate_fuel_cost(distance, price_per_km, petrol_price, fuel_consumption)

print("Dīzeļdegvielas izmaksas: {:.2f} eiro".format(diesel_cost))
print("Benzīna izmaksas: {:.2f} eiro".format(petrol_cost))

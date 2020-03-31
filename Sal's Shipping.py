"""
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package. They have ground shipping,
which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a
much higher flat charge, but you aren’t charged for weight. They recently also implemented drone shipping,
which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

"""


def ground_shipping(weight):
    cost = (weight * 4.00) + 20
    return cost


premium_ground_shipping = 125


def drone_ground_shipping(weight):
    cost = weight * 4.50
    return cost


def comparison(weight):
    if (ground_shipping(weight) < premium_ground_shipping) and (
            ground_shipping(weight) < drone_ground_shipping(weight)):
        return "Ground Shipping Method is Cheapest"
    elif (premium_ground_shipping < ground_shipping(weight)) and (
            premium_ground_shipping < drone_ground_shipping(weight)):
        return "Premium ground shipping is cheapest"
    else:
        return "Drone Ground Shipping is the best"


x = 41.5
best_shipper = comparison(x)
print(best_shipper)

print("")
ground_shipping_cost = ground_shipping(x)
print("Ground Shipping cost is: " + str(ground_shipping_cost) + "$")

drone_ground_cost = drone_ground_shipping(x)
print("Drone Shipping cost is: " + str(drone_ground_cost) + "$")

print("Premium Shipping cost is: " + str(premium_ground_shipping) + "$")


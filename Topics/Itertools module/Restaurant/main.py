import itertools


mains_prices = zip(main_courses, price_main_courses)
desserts_prices = zip(desserts, price_desserts)
drinks_prices = zip(drinks, price_drinks)
for (main, main_price), (dessert, dessert_price), (drink, drink_price) in itertools.product(mains_prices, desserts_prices, drinks_prices):
    if (main_price + dessert_price + drink_price) <= 30:
        print(f"{main} {dessert} {drink} {main_price + dessert_price + drink_price}")
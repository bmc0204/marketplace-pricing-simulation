import matplotlib.pyplot as plt
import numpy as np
import random
import statistics

items_per_s = 10
demand = 1

sellers = {
    "A": {"items": items_per_s, "price": 4},
    "B": {"items": items_per_s, "price": 6},
    "C": {"items": items_per_s, "price": 8},
    "D": {"items": items_per_s, "price": 10},
    "E": {"items": items_per_s, "price": 12}
}

def get_budget():
    budget = random.randint(5, 15)
    return budget

def get_will(demand):
    willingness = random.randint(3, 10)
    willingness *= demand
    return willingness

buyers = {
    "1": {"budget": get_budget(), "willing": get_will(demand)},
    "2": {"budget": get_budget(), "willing": get_will(demand)},
    "3": {"budget": get_budget(), "willing": get_will(demand)},
    "4": {"budget": get_budget(), "willing": get_will(demand)},
    "5": {"budget": get_budget(), "willing": get_will(demand)},
    "6": {"budget": get_budget(), "willing": get_will(demand)},
    "7": {"budget": get_budget(), "willing": get_will(demand)},
    "8": {"budget": get_budget(), "willing": get_will(demand)},
    "9": {"budget": get_budget(), "willing": get_will(demand)},
    "10": {"budget": get_budget(), "willing": get_will(demand)},
    "11": {"budget": get_budget(), "willing": get_will(demand)},
    "12": {"budget": get_budget(), "willing": get_will(demand)},
    "13": {"budget": get_budget(), "willing": get_will(demand)},
    "14": {"budget": get_budget(), "willing": get_will(demand)},
    "15": {"budget": get_budget(), "willing": get_will(demand)},
    "16": {"budget": get_budget(), "willing": get_will(demand)},
    "17": {"budget": get_budget(), "willing": get_will(demand)},
    "18": {"budget": get_budget(), "willing": get_will(demand)},
    "19": {"budget": get_budget(), "willing": get_will(demand)},
    "20": {"budget": get_budget(), "willing": get_will(demand)},
    "21": {"budget": get_budget(), "willing": get_will(demand)},
    "22": {"budget": get_budget(), "willing": get_will(demand)},
    "23": {"budget": get_budget(), "willing": get_will(demand)},
    "24": {"budget": get_budget(), "willing": get_will(demand)},
    "25": {"budget": get_budget(), "willing": get_will(demand)},
    "26": {"budget": get_budget(), "willing": get_will(demand)},
    "27": {"budget": get_budget(), "willing": get_will(demand)},
    "28": {"budget": get_budget(), "willing": get_will(demand)},
    "29": {"budget": get_budget(), "willing": get_will(demand)},
    "30": {"budget": get_budget(), "willing": get_will(demand)},
    "31": {"budget": get_budget(), "willing": get_will(demand)},
    "32": {"budget": get_budget(), "willing": get_will(demand)},
    "33": {"budget": get_budget(), "willing": get_will(demand)},
    "34": {"budget": get_budget(), "willing": get_will(demand)},
    "35": {"budget": get_budget(), "willing": get_will(demand)},
    "36": {"budget": get_budget(), "willing": get_will(demand)},
    "37": {"budget": get_budget(), "willing": get_will(demand)},
    "38": {"budget": get_budget(), "willing": get_will(demand)},
    "39": {"budget": get_budget(), "willing": get_will(demand)},
    "40": {"budget": get_budget(), "willing": get_will(demand)},
    "41": {"budget": get_budget(), "willing": get_will(demand)},
    "42": {"budget": get_budget(), "willing": get_will(demand)},
    "43": {"budget": get_budget(), "willing": get_will(demand)},
    "44": {"budget": get_budget(), "willing": get_will(demand)},
    "45": {"budget": get_budget(), "willing": get_will(demand)},
    "46": {"budget": get_budget(), "willing": get_will(demand)},
    "47": {"budget": get_budget(), "willing": get_will(demand)},
    "48": {"budget": get_budget(), "willing": get_will(demand)},
    "49": {"budget": get_budget(), "willing": get_will(demand)},
    "50": {"budget": get_budget(), "willing": get_will(demand)},
}

def run_once(sellers, buyers):
    for buyer in buyers:
        seller_choice = []
        for seller in sellers:
            if sellers[seller]["items"] > 0:
                if (sellers[seller]["price"] <= buyers[buyer]["budget"]
                        and sellers[seller]["price"] <= buyers[buyer]["willing"]):
                    seller_choice.append(seller)
        if len(seller_choice) > 0:
            choice = random.choice(seller_choice)
            sellers[choice]["items"] -= 1
            buyers[buyer]["budget"] -= sellers[choice]["price"]
        else:
            continue
    return sellers, buyers

def adjust_prices(r_sellers, items):
    for seller in r_sellers:
        if r_sellers[seller]["items"] <= 0.1 * items:
            r_sellers[seller]["price"] += 0.08
        elif r_sellers[seller]["items"] <= 0.2 * items:
            r_sellers[seller]["price"] += 0.05
        elif r_sellers[seller]["items"] <= 0.3 * items:
            r_sellers[seller]["price"] += .01
        elif r_sellers[seller]["items"] >= 0.9 * items and r_sellers[seller]["price"] > 1:
            r_sellers[seller]["price"] -= .08
        elif r_sellers[seller]["items"] >= 0.8 * items and r_sellers[seller]["price"] > 1:
            r_sellers[seller]["price"] -= .05
        elif r_sellers[seller]["items"] >= 0.7 * items and r_sellers[seller]["price"] > 1:
            r_sellers[seller]["price"] -= .01
        r_sellers[seller]["items"] = items_per_s
    return r_sellers

def reset_buyers(r_buyers, demand):
    for buyer in r_buyers:
        r_buyers[buyer]["budget"] = get_budget()
        r_buyers[buyer]["willing"] = get_will(demand)
    return r_buyers

def run_simulation(sellers, buyers, runs, cons_demand, shock):
    this_demand = cons_demand
    prices = {}
    for i in range(runs):
        if i == runs - (runs // 3):
            this_demand *= shock
        prices[i] = {}
        results = run_once(sellers, buyers)
        sellers = adjust_prices(results[0], items_per_s)
        for seller in sellers:
            prices[i][seller] = results[0][seller]["price"]
        buyers = reset_buyers(results[1], this_demand)
    return sellers, buyers, prices

trials = 500
shock = 1.3
run = run_simulation(sellers, buyers, trials, demand, shock)
print(run[0])

x = np.linspace(1, trials, trials)

def get_dev(prices):
    dev = []
    for trial in prices:
        values = list(prices[trial].values())
        stdev = statistics.stdev(values) if len(values) > 1 else 0
        dev.append(stdev)
    return dev

def get_y(prices):
    y = []
    for trial in prices:
        values = list(prices[trial].values())
        average = sum(values) / len(values) if values else 0
        y.append(average)
    return y

def divide_by_seller(divided, seller):
        individual = []
        for trial in divided:
            addition = divided[trial][seller]
            individual.append(addition)
        return individual

divided = run[2]

A = divide_by_seller(divided, "A")
B = divide_by_seller(divided, "B")
C = divide_by_seller(divided, "C")
D = divide_by_seller(divided, "D")
E = divide_by_seller(divided, "E")

plt.plot(x, get_dev(run[2]), color = "blue", label="Prices Standard Deviation")
plt.plot(x, A, linewidth = 0.5)
plt.plot(x, B, linewidth = 0.5)
plt.plot(x, C, linewidth = 0.5)
plt.plot(x, D, linewidth = 0.5)
plt.plot(x, E, linewidth = 0.5)
plt.plot(x, get_y(run[2]), color = "black", linewidth = 1.25, label="Prices Average")
plt.axvline(x = (trials - (trials // 3)), color = "black", linestyle = ":", label = "Demand Shock")
plt.legend()
plt.show()
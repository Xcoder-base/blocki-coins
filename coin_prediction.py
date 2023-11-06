import random

def simulate_coin_price(duration=60):

  current_price = 1.0

  for time_elapsed in range(1, duration + 1):

    if random.randint(1, 10) <= 3:
      # 30% chance of skyrocket
      current_price += 0.05 
    else:
      # 70% chance of reduce
      current_price -= 0.05

    print(f"Time: {time_elapsed}s, Price: ${current_price:.2f}")

    if time_elapsed % 60 == 0:
      cash_out(current_price)
      current_price = 1.0 # Reset price after cashout
      
def cash_out(price):

  # Cashout logic
  print(f"Cashed out at ${price:.2f}")

if __name__ == "__main__":

  simulate_coin_price()
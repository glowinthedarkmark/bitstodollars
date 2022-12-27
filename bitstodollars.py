def convert_bits_to_usd():
  # Get the number of bits from the user
  bits = input("Enter the number of bits: ")

  # Convert the input string to an integer
  bits = int(bits)

  # The current rate for purchasing bits is $0.01 per bit
  rate = 0.01

  # Calculate the cost in USD by multiplying the number of bits by the rate
  cost = bits * rate

  # Calculate the cut that goes to Twitch by multiplying the cost by 0.3 (30%)
  cut = cost * 0.25

  # Subtract the cut from the cost to get the final cost in USD
  final_cost = cost - cut

  # Return the final cost in USD
  return final_cost

# Test the function by calling it and printing the result to the console
result = convert_bits_to_usd()
print(result)
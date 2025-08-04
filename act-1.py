import re, random
from colorama import Fore, init


init(autoreset=True)


destinations ={
  "beaches": ["Miami", "Cancun", "Hawaii"],
  "mountains": ["Aspen", "Vail", "Telluride"],
  "cities": ["New York", "Los Angeles", "Chicago"]
}
jokes=[
  "Why don't scientists trust atoms? Because they make up everything!",
  "What do you call fake spaghetti? An impasta.",
  "How does the moon cut his hair? Eclipse it."
]


def normalize_input(text):
  return re.sub(r"\s+", " ", text.strip().lower())


def recommend():
  print(Fore.CYAN+"TravelBot: Beaches, mountains, or cities?")
  preference = input(Fore.GREEN+"You: ")
  preference = normalize_input(preference)

  if preference in destinations:
    suggestion = random.choice(destinations[preference])
    print(Fore.CYAN+f"TravelBot:  How about {suggestion}?")
    print(Fore.CYAN+f"TravelBot: Do you want to hear a joke?(yes/no)")
    answer = input(Fore.GREEN+"You: ").lower()

    if answer == "yes":
        print(Fore.GREEN+f"TravelBot: Awesome! Enjoy {suggestion}!")
    elif answer == "no":
        print(Fore.RED+f"TravelBot: Let's try another p!")
    else:
      print(Fore.RED+f"TravelBot: I will suggest you another destination!")
      recommend()
  else:
    print(Fore.RED+f"TravelBot: I don't understand {preference}. Please try      again.")


  show_help()


def packing_tips():
  print(Fore.CYAN+f"TravelBot: Where to?")
  location= normalize_input(input(Fore.YELLOW+"You: "))
  print(Fore.CYAN+f"TravelBot: How many days?")
  days= input(Fore.YELLOW+"You: ")

  print(Fore.CYAN+f"TravelBot: Here are some packing tips for {location} for {days} days!")
  print(Fore.CYAN+f"TravelBot: Don't forget to pack a jacket.")
  print(Fore.CYAN+f"TravelBot: Bring chargers and headphones.")
  print(Fore.CYAN+f"TravelBot: Check weather forecast.")


def tell_joke():
  print(Fore.YELLOW+f"TravelBot: {random.choice(jokes)}")

def show_help():
  print(Fore.CYAN+f"TravelBot: I can help you with the following tasks:")
  print(Fore.CYAN+f"TravelBot: * Recommend a destination(recommend)")
  print(Fore.CYAN+f"TravelBot: * Give you packing tips(packing)")
  print(Fore.CYAN+f"TravelBot: * Tell you a joke(joke)")
  print(Fore.CYAN+f"TravelBot: * Type 'quit' to exit")



def chat():
  print(Fore.CYAN+f"TravelBot: Hi! I'm TravelBot. How can I help you today?")
  name=input(Fore.GREEN+"You name?: ")
  print(Fore.CYAN+f"TravelBot: Hi {name}! Nice to meet you!")

  show_help()

  while True:
      user_input = input(Fore.GREEN+f"{name}: ")
      user_input = normalize_input(user_input)
    
      if "recommend" in user_input:
        recommend()
      elif "packing" in user_input:
        packing_tips()
      elif "joke" in user_input:
        tell_joke()
      elif "help" in user_input:
        show_help()
      elif "quit" in user_input:
        print(Fore.CYAN+f"TravelBot: Goodbye {name}!")
        break
      else:
        print(Fore.RED+f"TravelBot: Could you please rephrase that?")


if __name__ == "__main__":
  chat()
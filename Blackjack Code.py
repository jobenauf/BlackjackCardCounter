def true_count(running_count, deck_remaining):
    if deck_remaining == 0:
        return None
    else:
        return running_count / deck_remaining

running_count = 0
deck_remaining = 6

while True:
    cards = input("Enter the values of the next cards (2-10, J, Q, K, A), separated by spaces: ")
    cards = cards.split(" ")

    for card in cards:
        card = card.strip()
        if card in ["2", "3", "4", "5", "6"]:
            running_count += 1
        elif card in ["10", "j", "q", "k", "a"]:


            running_count -= 1
        elif card in ["7", "8", "9"]:
            running_count += 0
        deck_remaining -= 1/52

    print("Running count: {}".format(running_count))
    tc = true_count(running_count, deck_remaining)
    if tc is None:
        print("The deck is empty.")
    else:
        print("True count: {:.2f}".format(tc))

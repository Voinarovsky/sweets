def sorting_cards(cards):
    card_values = {'9': 14, '8': 13, '7': 12, '6': 11, '5': 10, '4': 9, '3': 8, '2': 7, 'A': 6, 'K': 5, 'Q': 4, 'J': 3, 'T': 2}
    card_list = cards.split()  # Split the input string into individual cards
    return sorted(card_list, key=lambda card: card_values.get(str(card), 0))

print(sorting_cards(['5', '4', 'T', 'Q', 'K', 'J', '6', '9', '3', '2', '7', 'A', '8']))
# должно вернуть ['T', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9']
print(sorting_cards(['Q', '2', '8', '6', 'J', 'K', '3', '9', '5', 'A', '4', '7', 'T']))
# должно вернуть ['T', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9']
print(sorting_cards(['5', '4', 'A', '2', 'A', '9', 'K', '7', '5', '8', '8', 'K', '4', '9', 'A', 'T', 'Q', '2', '6', 'A', '2', 'K', '5', 'Q', 'A', '2', 'J', '8', '4', 'T', '4', '6', '8', '6', '5', '5', 'Q', '9', '4', 'A', '7', 'Q', '4', '7', 'K', '4', 'Q', 'K', 'K', 'J', 'Q', '9', '6', '5', 'Q', '4', '8', '7', 'Q', '9', '7', '2', 'J', 'Q', 'T', '2', '3', '4', '8', 'Q', '9', '7', 'K', 'T', 'J', '2', '3', '9']))
# должно вернуть ['T', 'T', 'T', 'T', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A', 'A', 'A', '2', '2', '2', '2', '2', '2', '2', '3', '3', '4', '4', '4', '4', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '7', '7', '8', '8', '8', '8', '8', '8', '9', '9', '9', '9', '9', '9', '9']

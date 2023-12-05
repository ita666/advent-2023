def parse_scratch_card_data(file_path):
    with open(file_path, 'r') as file:
        cards = [line.split(":")[1].strip().split('|') for line in file]

    card_scores = []
    for index, (win_numbers, has_numbers) in enumerate(cards):
        has_list = [int(num) for num in has_numbers.split()]
        win_list = [int(num) for num in win_numbers.split()]
        match_count = sum(1 for num in has_list if num in win_list)
        card_scores.append(list(range(index + 2, index + 2 + match_count)))

    processed_cards = list(range(1, len(cards) + 1))
    idx = 0
    while idx < len(processed_cards):
        related_cards = card_scores[processed_cards[idx] - 1]
        processed_cards.extend(related_cards)
        idx += 1

    return len(processed_cards)

total_card_count = parse_scratch_card_data('Scratchcards.txt')
print(total_card_count)

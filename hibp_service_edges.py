import csv
import itertools
import json
from collections import Counter

input_path = "/Users/maxwoolf/Downloads/"
output_path = "/Users/maxwoolf/Downloads/"

edge_list = []
threshold = 2


with open(output_path + 'mtg-creatures.csv', 'wb') as file:
    writer = csv.writer(file)
    writer.writerow(["Source", "Target", "Weight", "Type"])

    with open(input_path + 'AllCards.json') as data:
        cards = json.load(data)
        names = cards.keys()

    for name in names:
        card = cards[name]

        # Only process Creatures
        if set(["type", "subtypes"]).issubset(card.keys()) and "Creature" in card['types']:
            creature_types = card['subtypes']
            creature_types.sort()  # Ensure edges are in correct order
            # Calculate all combinations
            edges = list(itertools.combinations(creature_types, 2))

            # edges is a list of tuples
            for edge in edges:
                edge_list.append(edge)

    # edge_counts is a (key,value) of (tuple, number)
    edge_counts = Counter(edge_list)
    edges = edge_counts.keys()

    for edge in edges:
        count = edge_counts[edge]
        if count >= threshold:
            writer.writerow([edge[0], edge[1], count, "Undirected"])

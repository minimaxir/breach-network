import csv
import itertools
import json
from collections import Counter

input_path = "/Users/maxwoolf/Downloads" \
    "/HIBP Consolidated and Anonymised Data" \
    "/HIBP Consolidated and Anonymised Data.txt"

# edge_dict is a dictionary with tuple keys.
edge_dict = {}

with open('hibp_edges.csv', 'wb') as file:
    writer = csv.writer(file)
    writer.writerow(["Source", "Target", "Weight"])

    with open(input_path, 'rb') as f:
        for entry in f:
            if entry.find(';') > 0:
                services = entry.split(' ')[0].split(';')
                count = int(entry.split(' ')[1].rstrip())

                services.sort()  # Ensure edges are in correct order

                # edges is a list of tuples
                edges = list(itertools.combinations(services, 2))
                for edge in edges:
                    if edge in edge_dict:
                        edge_dict[edge] += count
                    else:
                        edge_dict[edge] = count

    for key, value in edge_dict.iteritems():
        writer.writerow([key[0], key[1], value])

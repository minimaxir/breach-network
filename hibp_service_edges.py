import csv
import itertools
import json
from collections import Counter

input_path = "/Users/maxwoolf/Downloads" \
    "/HIBP Consolidated and Anonymised Data" \
    "/HIBP Consolidated and Anonymised Data.txt"

edge_list = []

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
                # edge_list is a list of tuples + count
                edges = list(itertools.combinations(services, 2))
                for edge in edges:
                    edge_list.append((edge, count))
                break

    # edge_counts is a (key,value) of (tuple, number)
    print edge_list
    edge_counts = reduceByKey(lambda x, y: x + y,
                         edge_list)
    print edge_counts
    edges = edge_counts.keys()

    for edge in edges:
        count = edge_counts[edge]
        writer.writerow([edge[0], edge[1], count])

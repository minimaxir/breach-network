import csv
import itertools
import json

input_path = "/Users/maxwoolf/Downloads" \
    "/HIBP Consolidated and Anonymised Data" \
    "/HIBP Consolidated and Anonymised Data.txt"

# service_dict is a dictionary with a string key.
service_dict = {}

# edge_dict is a dictionary with tuple keys.
edge_dict = {}

with open(input_path, 'rb') as f:
    for entry in f:
        services = entry.split(' ')[0].split(';')
        count = int(entry.split(' ')[1].rstrip())

        services.sort()  # Ensure edges are in correct order

        for service in services:
            if service in service_dict:
                service_dict[service] += count
            else:
                service_dict[service] = count

        if len(services) > 1:
            # edges is a list of tuples
            edges = list(itertools.combinations(services, 2))
            for edge in edges:
                if edge in edge_dict:
                    edge_dict[edge] += count
                else:
                    edge_dict[edge] = count

# output should be close to public numbers:
# https://haveibeenpwned.com/PwnedWebsites

with open('hibp_services.csv', 'wb') as file:
    writer = csv.writer(file)
    writer.writerow(["Service", "Total"])

    for key, value in service_dict.iteritems():
        writer.writerow([key, value])

with open('hibp_edges.csv', 'wb') as file:
    writer = csv.writer(file)
    writer.writerow(["Source", "Target", "Weight"])

    for key, value in edge_dict.iteritems():
        writer.writerow([key[0], key[1], value])

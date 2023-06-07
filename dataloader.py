import csv
import redis
from redisgraph import Node, Edge, Graph


redis_con = redis.Redis(host='localhost', port=6379)

graph = Graph(name='Wiki_graph', redis_con=redis_con)

with open('sampled_wiki_data.csv', 'r', encoding='utf8') as file:
    reader = csv.DictReader(file, delimiter='|')
    for row in reader:
        data = Node(label='data', properties={'name': 'Alice', 'age': 25})
        print(row)
        graph.add_node(data)    
        # break
    


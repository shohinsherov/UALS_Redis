# В Python для работы с Redis Graph можно использовать библиотеку redisgraph-py. Пример использования Redis Graph в Python с помощью этой библиотеки выглядит следующим образом:
# ```python
import redis
from redisgraph import Node, Edge, Graph

# Подключение к Redis серверу с использованием redis-py
redis_con = redis.Redis(host='localhost', port=6379)

# Создание графа Redis Graph
graph = Graph(name='mygraph', redis_con=redis_con)

# Создание узлов и ребер
alice = Node(label='person', properties={'name': 'Alice', 'age': 25})
bob = Node(label='person', properties={'name': 'Bob', 'age': 30})
knows = Edge(alice, 'knows', bob)
graph.add_node(alice)
graph.add_node(bob)
graph.add_edge(knows)

# Выполнение запроса и обработка результатов
query = "MATCH (p:person)-[k:knows]->(q:person) RETURN p.name, q.name, k.creationDate"
result_set = graph.query(query)

for record in result_set:
    print(record)
# ``

# В этом примере мы подключаемся к Redis серверу, создаем граф Redis Graph с помощью библиотеки Redis Graph Py, создаем узлы и ребра, добавляем их в граф и выполняем запрос к графу, выводя результаты на экран.



#====================  Другой вариант 

# import redis
# from redisgraph import Graph

# # Создание подключения к Redis
# redis_graph = Graph("myGraph", redis.Redis(host='localhost', port=6379))

# # Команда на добавление вершины в граф
# query = """CREATE (:person{name:'Chris',surname:'Johnson',age:33})"""

# redis_graph.query(query)

# # Команда на добавление ребра между двумя вершинами
# query = """MATCH (a:person{name:'Chris'}),(b:person{name:'Bob'}) CREATE (a)-[:friend]->(b)"""

# redis_graph.query(query)
# ```

# Этот код добавляет новую вершину "person" в граф с именем "Chris". Затем мы создаем отношение "friend" между вершинами "Chris" и "Bob".

# Теперь вы можете повторно запустить код для извлечения данных из графа, чтобы убедиться, что новые вершины и ребра были успешно добавлены:

# ```python
# # Извлечение данных из графа
# query = """MATCH (p:person)-[:friend]->(f:person) RETURN p.name,f.name"""

# res = redis_graph.query(query)

# for record in res.result_set:
#     print(record[0], "is friend of", record[1])
# ```




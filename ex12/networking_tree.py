import networkx as nx

import xml.etree.ElementTree as ET

id_name_map = {}
G = nx.Graph()

tree = ET.parse("public_transport_network.graphml")
root = tree.getroot()

for node in root.findall(".//{http://graphml.graphdrawing.org/xmlns}node"):
    node_id = node.attrib['id']
    stop_name = node.find(".//{http://graphml.graphdrawing.org/xmlns}data[@key='d0']").text
    id_name_map[node_id] = stop_name

for edge in root.findall(".//{http://graphml.graphdrawing.org/xmlns}edge"):
    source = edge.attrib['source']
    target = edge.attrib['target']
    G.add_edge(source, target)

degree_cent = nx.degree_centrality(G)
closeness_cent = nx.closeness_centrality(G)
betweenness_cent = nx.betweenness_centrality(G)

density = nx.density(G)
diameter = nx.diameter(G)

top_degree = sorted(degree_cent.items(), key=lambda x: x[1], reverse=True)[:10]
print("TOP 10 degree centrality:")
i = 1
for node_id, centrality in top_degree:
    print(f'{i}.{id_name_map[node_id]} {centrality}')
    i += 1

top_closeness = sorted(closeness_cent.items(), key=lambda x: x[1], reverse=True)[:10]
print("\nTOP 10 closeness centrality:")
i = 1
for node_id, centrality in top_closeness:
    print(f'{i}.{id_name_map[node_id]} {centrality}')
    i += 1

top_betweenness = sorted(betweenness_cent.items(), key=lambda x: x[1], reverse=True)[:10]
print("\nTOP 10 betweenness centrality:")
i = 1
for node_id, centrality in top_betweenness:
    print(f'{i}.{id_name_map[node_id]} {centrality}')
    i += 1

print("\nDiameter:", diameter)
print("Density:", density)


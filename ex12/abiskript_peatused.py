import os
import pandas as pd
import networkx as nx

graphml_file = "public_transport_network.graphml"

def create_graph_from_gtfs():
    stops_df = pd.read_csv('stops.txt')
    stop_times_df = pd.read_csv('stop_times.txt')
    trips_df = pd.read_csv('trips.txt')

    min_lon, min_lat, max_lon, max_lat = 24.533844, 59.360146, 25.009003, 59.553461
    stops_df = stops_df[(stops_df['stop_lat'] >= min_lat) & (stops_df['stop_lat'] <= max_lat) &
                        (stops_df['stop_lon'] >= min_lon) & (stops_df['stop_lon'] <= max_lon)]

    stop_times_merged_df = stop_times_df.merge(trips_df, on='trip_id')
    G = nx.Graph()
    for index, row in stops_df.iterrows():
        G.add_node(row['stop_id'], stop_name=row['stop_name'])

    for trip_id in stop_times_merged_df['trip_id'].unique():
        trip_stops = stop_times_merged_df[stop_times_merged_df['trip_id'] == trip_id].sort_values(by='stop_sequence')
        prev_stop_id = None
        for index, row in trip_stops.iterrows():
            if row['stop_id'] in G.nodes:
                if prev_stop_id is not None:
                    if not G.has_edge(prev_stop_id, row['stop_id']):
                        G.add_edge(prev_stop_id, row['stop_id'])
                prev_stop_id = row['stop_id']

    isolated = list(nx.isolates(G))
    G.remove_nodes_from(isolated)
    return G

def save_largest_component(G, file_name):
    largest_component = max(nx.connected_components(G), key=len)
    G_largest = G.subgraph(largest_component).copy()
    nx.write_graphml(G_largest, file_name)
    return G_largest

if __name__ == "__main__":
    if os.path.exists(graphml_file):
        G = nx.read_graphml(graphml_file)
        print(f"Loaded a graph with {len(G.nodes())} nodes and {len(G.edges())} edges.")
    else:
        G = create_graph_from_gtfs()
        G_largest = save_largest_component(G, graphml_file)
        print(f"Saved the largest component with {len(G_largest.nodes())} nodes and {len(G_largest.edges())} edges.")

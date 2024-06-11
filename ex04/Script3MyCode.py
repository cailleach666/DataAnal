import json
import numpy as np
from shapely.geometry import Polygon


def load_polygon_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    # Extracting the first polygon's coordinates
    return data[0]["ehitis"]["ehitiseKujud"]["ruumikuju"][0]["geometry"]["coordinates"][0]


def rotate_point(origin, point, angle):
    ox, oy = origin
    px, py = point
    qx = ox + np.cos(angle) * (px - ox) - np.sin(angle) * (py - oy)
    qy = oy + np.sin(angle) * (px - ox) + np.cos(angle) * (py - oy)
    return [qx, qy]

def angle_to_rotate_polygon(coords):
    max_length = 0
    angle_of_longest_edge = 0
    for i in range(len(coords) - 1):
        p1 = coords[i]
        p2 = coords[i + 1]
        length = np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        if length > max_length:
            max_length = length
            angle_of_longest_edge = np.arctan2((p2[1] - p1[1]), (p2[0] - p1[0]))
    return -angle_of_longest_edge


#got part of the code from https://github.com/92kns/simple-shapely-simplify-alternative/blob/main/degenerate_polygon.py#L75

building_ids = ["120791952", "120857076", "120857095", "120801732", "120801756", "120801759",
                "120847090", "120847091", "120847092", "101014868", "101019312", "101019344"]

building_jsons =  ["./" + building_ids[0]+ ".ehr.json",
                   "./" + building_ids[1]+ ".ehr.json",
                   "./" + building_ids[2]+ ".ehr.json",
                   "./" + building_ids[3]+ ".ehr.json",
                   "./" + building_ids[4]+ ".ehr.json",
                   "./" + building_ids[5]+ ".ehr.json",
                   "./" + building_ids[6]+ ".ehr.json",
                   "./" + building_ids[6]+ ".ehr.json",
                   "./" + building_ids[8]+ ".ehr.json",
                   "./" + building_ids[9]+ ".ehr.json",
                   "./" + building_ids[10]+ ".ehr.json",
                   "./" + building_ids[11]+ ".ehr.json"]


# Load polygon coordinates from JSON file
for building in building_jsons:

    polygon_coords = load_polygon_from_json(building)

    angle = angle_to_rotate_polygon(polygon_coords)

    origin = polygon_coords[0]

    rotated_polygon_coords = [rotate_point(origin, point, angle) for point in polygon_coords]


    min_x_rotated = min(coord[0] for coord in rotated_polygon_coords)
    min_y_rotated = min(coord[1] for coord in rotated_polygon_coords)
    transformed_rotated_coords = [[x - min_x_rotated, y - min_y_rotated] for x, y in rotated_polygon_coords]

    shapely_polygon = Polygon(transformed_rotated_coords)

    bounding_box = shapely_polygon.envelope

    length = bounding_box.bounds[3] - bounding_box.bounds[1]
    width = bounding_box.bounds[2] - bounding_box.bounds[0]
    area = shapely_polygon.area

    building_info_str = (
        f"Building ID: {building}\n"
        f"Length: {length}\n"
        f"Width: {width}\n"
        f"Area: {area}\n"
    )

    # Append the building information string to the list
    print(building_info_str)


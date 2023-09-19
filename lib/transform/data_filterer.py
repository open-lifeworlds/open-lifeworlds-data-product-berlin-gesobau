import json
import os

from lib.tracking_decorator import TrackingDecorator

lor_area_ids_mv = [
    "12601133",  # Treuenbrietzener Straße
    "12601134",  # Märkisches Zentrum
    "12601235",  # Dannenwalder Weg
]


@TrackingDecorator.track_time
def filter_data(source_path, results_path, clean, quiet):
    """
    Filters geojson files to only contain features with given IDs
    :param source_path:
    :param results_path:
    :param clean:
    :param quiet:
    :return:
    """
    # Iterate over files
    for subdir, dirs, files in sorted(os.walk(os.path.join(source_path, "berlin-lor-daycare-centers-geojson"))):
        for source_file_name in sorted(files):
            if "details.geojson" in source_file_name:
                geojson = read_geojson_file(os.path.join(subdir, source_file_name))

                if [feature for feature in geojson["features"] if
                    str(feature["properties"]["planning-area-id"]) not in lor_area_ids_mv]:
                    geojson = read_geojson_file(os.path.join(subdir, source_file_name))
                    geojson["features"] = [feature for feature in geojson["features"] if
                                           str(feature["properties"]["planning-area-id"]) in lor_area_ids_mv]

                    # Write geojson file
                    write_geojson_file(
                        file_path=os.path.join(results_path, subdir.replace(f"{source_path}/", ""), source_file_name),
                        geojson_content=geojson,
                        clean=clean,
                        quiet=quiet
                    )
                else:
                    print(f"✓ Already filtered {os.path.basename(source_file_name)}")


def read_geojson_file(file_path):
    with open(file=file_path, mode="r", encoding="utf-8") as geojson_file:
        return json.load(geojson_file, strict=False)


def write_geojson_file(file_path, geojson_content, clean, quiet):
    # Make results path
    path_name = os.path.dirname(file_path)
    os.makedirs(os.path.join(path_name), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as geojson_file:
        json.dump(geojson_content, geojson_file, ensure_ascii=False)

        if not quiet:
            print(f"✓ Filter {os.path.basename(file_path)}")

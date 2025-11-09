import pandas as pd
import geopandas as gpd

class Region:
    __slots__ = ("_codi", "_district", "_neighbourhood", "_density", "_cords")  # We use densitat neta

    def __init__(self, district_code, district_name, neighbourhood_code, neighbourhood_name, density, x_cord=0, y_cord=0):
        self._codi = (district_code, neighbourhood_code)
        self._district = (district_code, district_name)
        self._neighbourhood = (neighbourhood_code, neighbourhood_name)
        self._density = density
        self._cords = (x_cord, y_cord)
    
    # --- cords ---
    @property
    def cords(self):
        return self._cords
    
    @cords.setter
    def cords(self, value):
        if not (isinstance(value, tuple) and len(value) == 2):
            raise ValueError("cords must be a tuple (x, y)")
        self._cords = value
    
    # --- codi ---
    @property
    def codi(self):
        return self._codi

    @codi.setter
    def codi(self, value):
        if not (isinstance(value, tuple) and len(value) == 2):
            raise ValueError("codi must be a tuple (district_code, neighbourhood_code)")
        self._codi = value

    # --- district ---
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        if not isinstance(value, dict) or len(value) != 1:
            raise ValueError("district must be a dictionary with one key-value pair {district_code: district_name}")
        self._district = value

    # --- neighbourhood ---
    @property
    def neighbourhood(self):
        return self._neighbourhood

    @neighbourhood.setter
    def neighbourhood(self, value):
        if not isinstance(value, dict) or len(value) != 1:
            raise ValueError("neighbourhood must be a dictionary with one key-value pair {neighbourhood_code: neighbourhood_name}")
        self._neighbourhood = value

    # --- density ---
    @property
    def density(self):
        return self._density

    @density.setter
    def density(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("density must be a number")
        self._density = value

    # --- equality and hash ---
    def __eq__(self, other):
        if isinstance(other, Region):
            return self._codi == other._codi
        elif isinstance(other, tuple):
            return self._codi == other
        else:
            raise TypeError("other must be an instance of the Region class or a Tuple[int, int, int]")

    def __hash__(self):
        return hash(self._codi)
    
    def __str__(self):
        return


#def load_regions():
#    region_list = []
#    df = pd.read_csv("dataset/bcn/population_density_bcn.csv")
#    gdf = gpd.read_file("dataset/bcn/BCN_UNITATS_ADM/0301040100_Barris_UNITATS_ADM.shp")
#    gdf["centroid"] = gdf.geometry.centroid
#    gdf["UTM_X"] = gdf.centroid.x
#    gdf["UTM_Y"] = gdf.centroid.y
#    print(gdf)
#    for row in df.itertuples(index=False, name=None):
#        region_list.append(Region(district_code=row[0], district_name=row[1], neighbourhood_code=row[2], neighbourhood_name=row[3], density=row[4]))
#    return region_list


def load_regions():
    region_list = []

    # CSV with population density
    df = pd.read_csv("dataset/bcn/population_density_bcn.csv")

    # Shapefile with geometry
    gdf = gpd.read_file("dataset/bcn/BCN_UNITATS_ADM/0301040100_Barris_UNITATS_ADM.shp")
    gdf["centroid"] = gdf.geometry.centroid
    gdf["UTM_X"] = gdf.centroid.x
    gdf["UTM_Y"] = gdf.centroid.y

    # Create a dict for fast lookup: (district_code, neighbourhood_code) -> (x, y)
    coords_dict = {
        (row["DISTRICTE"], row["BARRI"]): (row["UTM_X"], row["UTM_Y"])
        for _, row in gdf.iterrows()
    }

    # Build Region objects
    for row in df.itertuples(index=False, name=None):
        district_code, district_name, neighbourhood_code, neighbourhood_name, density = row
        x_cord, y_cord = coords_dict.get((district_code, neighbourhood_code), (0, 0))
        region_list.append(
            Region(district_code, district_name, neighbourhood_code, neighbourhood_name, density, x_cord, y_cord)
        )

    return region_list
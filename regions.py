import pandas as pd

class Region:
    __slots__ = ("_codi", "_district", "_neighbourhood", "_density")  # We use densitat neta

    def __init__(self, district_code, district_name, neighbourhood_code, neighbourhood_name, density):
        self._codi = (district_code, neighbourhood_code)
        self._district = (district_code, district_name)
        self._neighbourhood = (neighbourhood_code, neighbourhood_name)
        self._density = density
    
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
        else:
            raise TypeError("other must be an instance of the Region class")

    def __hash__(self):
        return hash(self._codi)


def load_regions():
    region_list = []
    df = pd.read_csv("dataset/Clean_bcn/population_density_bcn.csv")
    for row in df.itertuples(index=False, name=None):
        region_list.append(Region(district_code=row[0], district_name=row[1], neighbourhood_code=row[2], neighbourhood_name=row[3], density=row[4]))
    return region_list

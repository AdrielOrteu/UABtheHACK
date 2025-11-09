import pandas as pd

class Station:
    __slots__ = ('_code','_name', '_coords')
    
    def __init__(self, code="", name="", coord_x=0.0, coord_y=0.0, barri=0):
        self._code = code
        self._name = name
        self._coords = (coord_x, coord_y)
        self._barri = barri
        self._linies = []
    
    @property
    def name(self):
        return self._name
    
    @property
    def coords(self):
        return self._coords
    
    def add_linia(self, l):
        self._linies.append(l)
    
    def __str__(self):
        return f"({self._code}, {self._name}, {self._coords}, {self._linies}, {self._barri})"

class BusStation (Station):
    pass

class TrainStation (Station):
    pass

class MetroStation (Station):
    pass


class Line:

    def __init__(self, name="", stations=()):
        self._name: str = name
        self._stations: dict[str, Station] = {station.name: station for station in stations}
        self._n_stations = len(stations)
        
    def __str__(self):
        return f"{self._name}: {self._stations}"
    
def load_metro_lines():
    def load_metro():
        metro_df = pd.read_excel("dataset/Datasets Barcelona/Transport Public Barcelona.xlsx")
        selected_columns = metro_df[['NOM_CAPA', 'LONGITUD', 'LATITUD', 'EQUIPAMENT', 'DISTRICTE', 'BARRI']]
        tuples_list = list(selected_columns.itertuples(index=False, name=None))
        
        selected_columns['LONGITUD'] = selected_columns['LONGITUD'].astype(str).str.replace(',', '.').astype(float)
        selected_columns['LATITUD'] = selected_columns['LATITUD'].astype(str).str.replace(',', '.').astype(float)
        
        stations = {}
        codi = 0
    

        for value in tuples_list:
            name = value[3][:5]
            if name == "METRO":
                linia = value[3].strip("()").split()[1]
                nom_estacio = value[3].strip().split("-")[1]
                nom_estacio = nom_estacio[1:].upper()
                if nom_estacio not in stations.keys():
                    stations[nom_estacio] = MetroStation(code=codi, name=nom_estacio, coord_x=value[1], coord_y=value[2],
                                                           barri=value[5])
                    codi += 1
                stations[nom_estacio].add_linia(linia)
        return stations
    
    
    estacions = load_metro()
    
    
    def load_networks():
        lines = []
        sorted_lines = pd.read_csv("dataset/Clean_bcn/lines_sorted.csv")
        for header in sorted_lines:
            stations = []
            for station in sorted_lines[header]:
                if str(station) != "nan":
                    if station in estacions.keys():
                        stations.append(estacions[station])
            lines.append(Line(name=header, stations=stations))
        return lines
    
    return load_networks()



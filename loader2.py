import pandas as pd
import stations2 as s


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
                stations[nom_estacio] = s.MetroStation(code=codi, name=nom_estacio, coord_x=value[1], coord_y=value[2], barri=value[5])
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
        lines.append(s.Line(name=header, stations=stations))
    return lines
    
a = load_networks()
for l in a:
    print(l)
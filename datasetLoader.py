import pandas as pd
from stations import MetroStation, BusStation, Line

def load_bus_stations():
    bs_df = pd.read_excel("dataset\Datasets Barcelona\Parades Bus Barcelona.xlsx")
    selected_columns = bs_df[['Código de parada / Codi de parada', 'Nombre / Nom', 'UTM X', 'UTM Y']]
    tuples_list = list(selected_columns.itertuples(index=False, name=None))
    
    # Convert 'UTM X' and 'UTM Y' from string with ',' decimal separator to float
    selected_columns['UTM X'] = selected_columns['UTM X'].astype(str).str.replace(',', '.').astype(float)
    selected_columns['UTM Y'] = selected_columns['UTM Y'].astype(str).str.replace(',', '.').astype(float)
    
    # Convert to list of tuples
    tuples_list = list(selected_columns.itertuples(index=False, name=None))
    
    bus_stations = list()
    
    for value in tuples_list:
        bus_stations.append(BusStation(code=value[0], name=value[1], coord_x=value[2], coord_y=value[3]))
    
    for s in bus_stations:
        print(s)


def load_networks():
    lines = []
    sorted_lines = pd.read_csv("dataset\Datasets Barcelona\lines_sorted.csv")
    for header in sorted_lines:
        stations = []
        for station in sorted_lines[header]:
            if str(station) != "nan":
                stations.append(MetroStation(name=station))
        lines.append(Line(name=header, stations=stations))
    return lines
    


def create_excels(csv_path = "dataset/Datasets Barcelona/lines_sorted.csv"):
    import pandas as pd
    import os
    
    # Output directory
    output_dir = "excel_columns"
    os.makedirs(output_dir, exist_ok=True)
    
    # Read CSV
    df = pd.read_csv(csv_path)
    
    # Loop through each column (header)
    for col in df.columns:
        # Create a new DataFrame with just this column
        col_df = pd.DataFrame(df[col])
        
        # Create a file name based on the header
        safe_name = col.replace("/", "_").replace("\\", "_")
        excel_path = os.path.join(output_dir, f"{safe_name}.xlsx")
        
        # Save to Excel
        col_df.to_excel(excel_path, index=False)
        
        print(f"✅ Saved: {excel_path}")

create_excels()
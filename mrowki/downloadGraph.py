__author__ = 'kuban'

from googlemaps import Client
import networkx as nx

cities = ['Biala Podlaska', 'Bialystok', 'Bielsko-Biala', 'Bydgoszcz', 'Chelm', 'Ciechanow', 'Czestochowa', 'Elblag',
         'Gdansk', 'Gorzow Wielkopolski', 'Jelenia Gora', 'Kalisz', 'Katowice', 'Kielce', 'Konin', 'Koszalin',
         'Krakow', 'Krosno', 'Legnica', 'Leszno', "Lublin", 'Lomza', 'Lodz', 'Nowy Sacz', 'Olsztyn', 'Opole',
         'Ostroleka', 'Pila', 'Piotrkow Trybunalski', 'Plock', 'Poznan', 'Przemysl', 'Radom', 'Rzeszow', 'Siedlce',
         'Sieradz', 'Skierniewice', 'Slupsk', 'Suwalki', 'Szczecin', 'Tarnobrzeg', 'Tarnow', 'Torun', 'Walbrzych',
         'Warszawa', 'Wloclawek', 'Wroclaw', 'Zamosc', 'Zielona Gora']

gmaps = Client("AIzaSyAcbrpWHecaN1_Ms073ePqjefHvW-5TQ4M")
G = nx.Graph(name="DistanceGraph")
G.add_nodes_from(cities)


for x in cities:
    for y in cities:
        if x >= y:
            continue
        address = x + ', Poland'
        destination = y + ', Poland'
        directions = gmaps.directions(address, destination)
        G.add_edge(x, y, weight=directions[0]['legs'][0]['distance']['value']//1000)
        print(G[x][y]['weight'])

nx.write_gpickle(G,"cities.gpickle")
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel('Raw Data/dane.gov.pl_050824.xlsx')

df.columns = df.columns.str.strip().str.replace(' ', '_')

# Dane do połączenia z bazą MySQL
user = 'user_name' ## Hidden for security purposes
password = 'users_password' ## Hidden for security purposes
host = 'localhost'  
database = 'stan_budowy_drog'

# Tworzenie silnika połączenia do bazy MySQL
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}', echo=False)

# Zapis nowych danych do tabeli MySQL
table_name = 'drogi'
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

print(f'Dane zostały przesłane do tabeli {table_name} w bazie danych {database}.')

################################################
## CREATING THE DATABASE USING MYSQL COMMANDS ##
################################################

# Tworzymy nową bazę danych o nazwie 'stan_budowy_drog'
# CREATE DATABASE stan_budowy_drog;

# Przełączamy się na nowo utworzoną bazę danych 'stan_budowy_drog'
# USE stan_budowy_drog;

# Tworzymy tabelę 'drogi' z kolumnami:
# 'nr_drogi' - Numer drogi (np. 'A2', 'S19'), jako tekst
# 'nazwa_odcinka_realizacyjnego' - Pełna nazwa odcinka drogi
# 'łączna_długość_odcinka' - Długość odcinka w kilometrach
# 'etap' - Etap realizacji (np. 'Realizacja', 'Przygotowanie')
# CREATE TABLE drogi (
#     nr_drogi VARCHAR(10),  -- Kolumna 'nr_drogi', która przechowuje numer drogi, np. 'A2'
#     nazwa_odcinka_realizacyjnego TEXT,  -- Kolumna 'nazwa_odcinka_realizacyjnego', przechowuje pełną nazwę odcinka drogi
#     łączna_długość_odcinka FLOAT,  -- Kolumna 'dlugosc_odcinka', która przechowuje długość odcinka w kilometrach
#     etap VARCHAR(50)  -- Kolumna 'etap', która przechowuje etap realizacji, np. 'Realizacja'
# );

# Przykładowe wstawienie danych do tabeli 'drogi'
# Wstawiamy numer drogi, nazwę odcinka, długość odcinka i etap realizacji
# INSERT INTO drogi (nr_drogi, nazwa_odcinka_realizacyjnego, dlugosc_odcinka, etap)
# VALUES ('A2', 'Kałuszyn (Ryczołek) - Groszki', 12.060, 'Realizacja');

# Dodawanie kolejnych wierszy danych w ten sam sposób.
# INSERT INTO drogi (nr_drogi, nazwa_odcinka_realizacyjnego, dlugosc_odcinka, etap)
# VALUES ('S19', 'Malewice - Chlebczyn', 25.070, 'Realizacja');






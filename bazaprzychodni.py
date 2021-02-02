import sqlite3



def create_db():
    conn = sqlite3.connect('bazaprzychodni.db')
    c=conn.cursor()

    query = 'CREATE TABLE IF NOT EXISTS user(id_usera INTEGER PRIMARY KEY AUTOINCREMENT,imie TEXT, nazwisko TEXT, login VARCHAR(50) UNIQUE NOT  NULL, haslo VARCHAR(50) NOT  NULL, typ_usera INTEGER NOT NULL)'
    c.execute(query)
    conn.commit()
    
    query = 'CREATE TABLE IF NOT EXISTS wizyta(id_wizyty INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT NOT NULL, zajeta INTEGER NOT NULL, id_lekarza INTEGER NOT_NULL, id_pacjenta INTEGER, is_online INTEGER NOT NULL, FOREIGN KEY(id_lekarza) REFERENCES user(id_usera), FOREIGN KEY(id_pacjenta) REFERENCES user(id_usera))'
    c.execute(query)
    conn.commit()

    query = 'CREATE TABLE IF NOT EXISTS skierowanie(id_skierowania INTEGER PRIMARY KEY AUTOINCREMENT, id_lekarza INTEGER NOT NULL, id_pacjenta INTEGER NOT NULL, typ_choroby INTEGER NOT NULL, wykorzystane INTEGER NOT NULL, FOREIGN KEY(id_lekarza) REFERENCES user(id_usera), FOREIGN KEY(id_pacjenta) REFERENCES user(id_usera))'
    c.execute(query)
    conn.commit()

    query = 'CREATE TABLE IF NOT EXISTS badanie(id_badania INTEGER PRIMARY KEY AUTOINCREMENT, id_skierowania INTEGER NOT NULL, data TEXT, typ_choroby INTEGER NOT NULL, id_pacjenta, FOREIGN KEY(id_skierowania) REFERENCES skierowanie(id_skierowania), FOREIGN KEY(id_pacjenta) REFERENCES skierowanie(id_usera))'
    c.execute(query)
    conn.commit()

    query = 'CREATE TABLE IF NOT EXISTS wynik(id_wyniku INTEGER PRIMARY KEY AUTOINCREMENT, id_badania INTEGER NOT NULL, wynik INTEGER, note TEXT, FOREIGN KEY(id_badania) REFERENCES badanie(id_badania))'
    c.execute(query)
    conn.commit()

    query = 'CREATE TABLE IF NOT EXISTS szczepienie(id_szczepienia INTEGER PRIMARY KEY AUTOINCREMENT, typ_choroby INTEGER NOT NULL, data TEXT NOT NULL, id_pacjenta INTEGER NOT NULL, FOREIGN KEY(id_pacjenta) REFERENCES user(id_usera))'
    c.execute(query)
    conn.commit()

    query = 'CREATE TABLE IF NOT EXISTS izolacja(id_izolacji INTEGER PRIMARY KEY AUTOINCREMENT, id_pacjenta INTEGER NOT NULL, data_zakonczenia TEXT NOT NULL, FOREIGN KEY(id_pacjenta) REFERENCES user(id_usera))'
    c.execute(query)
    conn.commit()

    query = 'CREATE TABLE IF NOT EXISTS kwarantanna(id_kwarantanny INTEGER PRIMARY KEY AUTOINCREMENT, id_pacjenta INTEGER NOT NULL, data_zakonczenia TEXT NOT NULL, FOREIGN KEY(id_pacjenta) REFERENCES user(id_usera))'
    c.execute(query)
    conn.commit()

    query = 'CREATE TABLE IF NOT EXISTS recepta(id_recepty INTEGER PRIMARY KEY AUTOINCREMENT, tresc TEXT NOT NULL, id_pacjenta INTEGER, id_lekarza INTEGER NOT_NULL, is_erecepta INTEGER NOT NULL, FOREIGN KEY(id_lekarza) REFERENCES user(id_usera), FOREIGN KEY(id_pacjenta) REFERENCES user(id_usera))'
    c.execute(query)
    conn.commit()

    conn.close()





def fill_db_users():
    conn = sqlite3.connect('bazaprzychodni.db')
    c=conn.cursor()
    

    c.execute('INSERT INTO user VALUES(null,"Aleksandra","Bucholc","ola","123",0)')
    conn.commit()
    c.execute('INSERT INTO user VALUES(null,"Michaella","Quinn","mq","123",1)')
    conn.commit()
    c.execute('INSERT INTO user VALUES(null,"Tomasz","Judym","tj","123",1)')
    conn.commit()
    c.execute('INSERT INTO user VALUES(null,"Jan","Kowalski","jk","123",2)')
    conn.commit()
    c.execute('INSERT INTO user VALUES(null,"Anna","Nowak","an","123",2)')
    conn.commit()
    c.execute('INSERT INTO user VALUES(null,"Andrzej","Krawczyk","ak","123",2)')
    conn.commit()
    c.execute('INSERT INTO user VALUES(null,"Krzysztof","Bednarz","kb","123",2)')
    conn.commit()
    c.execute('INSERT INTO user VALUES(null,"Patrycja","Michalak","pm","123",2)')
    conn.commit()
    c.execute('INSERT INTO user VALUES(null,"Marcin","Wojtczak","mw","123",2)')
    conn.commit()
    c.execute('INSERT INTO user VALUES(null,"Agata","Andrzejczyk","aa","123",2)')
    conn.commit()
    c.execute('INSERT INTO user VALUES(null,"Monika","Mazur","mm","123",2)')
    conn.commit()
    c.execute('INSERT INTO user VALUES(null,"Pawel","Pawlowski","pp","123",2)')
    conn.commit()
    
    conn.close()

def fill_db_visits():
    conn = sqlite3.connect('bazaprzychodni.db')
    c=conn.cursor()

    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 08:00",0,2,null,1)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 08:15",1,2,4,1)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 08:30",0,2,null,1)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 08:45",0,2,null,1)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 09:00",1,2,5,1)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 09:15",0,2,null,0)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 09:30",0,2,null,0)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 09:45",0,2,null,0)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 09:50",0,2,null,0)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 10:15",1,2,6,0)')
    conn.commit()

    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 08:00",0,3,null,1)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 08:15",1,3,7,1)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 08:30",0,3,null,1)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 08:45",0,3,null,1)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 09:00",1,3,8,1)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 09:15",0,3,null,0)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 09:30",0,3,null,0)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 09:45",0,3,null,0)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 09:50",0,3,null,0)')
    conn.commit()
    c.execute('INSERT INTO wizyta VALUES(null,"2021-01-31 10:15",1,3,9,0)')
    conn.commit()

    conn.close()



create_db()
fill_db_users()
fill_db_visits()

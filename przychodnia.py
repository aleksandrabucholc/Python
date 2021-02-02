import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

choroby =	{
  0 : "COVID-19",
  1 : "HIV",
  2 : "zoltaczka",
  3 : "cukrzyca",
  4 : "salmonella",
  5 : "odra"
}


class Przychodnia:

    
    def __init__(self):


        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side = "left", fill = "both", expand = True)
        self.scrollbar = ttk.Scrollbar(self.root, command = self.canvas.yview)
        self.scrollbar.pack(side = tk.LEFT, fill = 'y')
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox('all')))

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window = self.frame, anchor = 'nw')

       
        self.create_login_screen()
        self.id_user = None
        self.root.geometry("800x600")
        #self.root.resizable(False,False)
        self.root.mainloop()

    def clear_screen(self):
        
        for widget in self.frame.winfo_children():
            widget.destroy()
    def set_current_id_usera(self, id_usera):
        
        self.id_usera = id_usera

    def set_current_typ_usera(self, typ_usera):
        
        self.typ_usera = typ_usera

    def create_login_screen(self):
        
        def log_in():
            
            conn = sqlite3.connect('bazaprzychodni.db')
            c = conn.cursor()
            c.execute(f'SELECT id_usera, login, haslo, typ_usera FROM user WHERE login = :log', {'log':login.get()})
            logins = c.fetchall()
            for row in logins:
                id_usera = row[0]
                log = row[1]
                pas = row[2]
                typ_usera = row[3]
            try:   
                if log == login.get() and pas == haslo.get():
                    if typ_usera == 0:
                        
                        self.create_admin_main_view()

                    elif typ_usera == 1:
                        
                        self.create_doc_main_view()

                    else:

                        self.create_patient_main_view()
                else:

                    tk.Label(self.frame, text = 'Bledny login lub haslo.').grid(row=5,column=0)


                self.set_current_id_usera(id_usera)
                self.set_current_typ_usera(typ_usera)
            except NameError:
                tk.Label(self.frame, text = 'Bledny login lub haslo.').grid(row=5,column=0)


                            
        self.clear_screen()
        self.root.geometry("400x400")
        tk.Label(self.frame, text = 'Login').grid(row=0,column=0)
        login = tk.Entry(self.frame)
        login.grid(row=0,column=1)
        tk.Label(self.frame, text = 'Haslo').grid(row=1,column=0)
        haslo = tk.Entry(self.frame)
        haslo.grid(row=1,column=1)
        tk.Button(self.frame, text = 'Zaloguj', command = log_in).grid(row=2,column=1)
    
    def create_admin_main_view(self):
        
        self.clear_screen()
        self.root.geometry("500x500")
        tk.Button(self.frame, text = 'Zarzadzaj pacjentami', command = self.create_patients_view).grid(row=0,column=0)
        tk.Button(self.frame, text = 'Zarzadzaj lekarzami', command = self.create_doctors_view).grid(row=1,column=0)
        tk.Button(self.frame, text = 'Zarzadzaj wizytami', command = self.create_visits_view).grid(row=2,column=0)
        tk.Button(self.frame, text = 'Przegladaj skierowania', command = self.create_referrals_view).grid(row=3,column=0)
        tk.Button(self.frame, text = 'Przegladaj badania', command = self.create_tests_admin_view).grid(row=4,column=0)
        tk.Button(self.frame, text = 'Przegladaj kwarantanny', command = self.create_quarantines_view).grid(row=5,column=0)
        tk.Button(self.frame, text = 'Przegladaj izolacje', command = self.create_isolations_view).grid(row=6,column=0)
        tk.Button(self.frame, text = 'Przegladaj zapisy na szczepienia', command = self.create_vaccines_view).grid(row=7,column=0)
        tk.Button(self.frame, text = 'Wyloguj',command = self.create_login_screen).grid(row=12,column=1)
    
    def create_patient_main_view(self):
        
        self.clear_screen()
        self.root.geometry("500x500")
        tk.Button(self.frame, text = 'Umow sie na wizyte',command = self.create_book_visit_view).grid(row=0,column=0, sticky='W')
        tk.Button(self.frame, text = 'Umow sie na teleporade',command = self.create_book_evisit_view).grid(row=0,column=1, sticky='W')
        tk.Button(self.frame, text = 'Umow sie na badanie', command = self.create_book_test_view).grid(row=0,column=2, sticky='W')
        tk.Button(self.frame, text = 'Umow sie na test COVID', command = self.create_book_covtest_view).grid(row=1,column=2, sticky='W')
        tk.Button(self.frame, text = 'Przegladaj wizyty', command = self.create_pat_visits_view).grid(row=1,column=0, sticky='W')
        tk.Button(self.frame, text = 'Odbierz wyniki badan', command = self.create_tests_view).grid(row=2,column=0, sticky='W')
        tk.Button(self.frame, text = 'Przegladaj eRecepty', command = self.create_prescriptions_view).grid(row=3,column=0, sticky='W')    
        tk.Button(self.frame, text = 'Dolacz do teleporady', command = self.join_evisit).grid(row=6,column=1, sticky='W')
        tk.Button(self.frame, text = 'Zapisz sie na szczepienie', command = self.create_book_vaccine_view).grid(row=4,column=0, sticky='W')
        tk.Button(self.frame, text = 'Sprawdz izolacje', command = self.create_isolations_pat_view).grid(row=2,column=1, sticky='W')
        tk.Button(self.frame, text = 'Sprawdz kwarantanne', command = self.create_quarantines_pat_view).grid(row=2,column=2, sticky='W')
        tk.Button(self.frame, text = 'Wyloguj',command = self.create_login_screen).grid(row=12,column=1)
    
    def create_doc_main_view(self):
        
        self.clear_screen()
        self.root.geometry("500x500")
        tk.Button(self.frame, text = 'Przegladaj wizyty', command = self.create_doc_visits_view).grid(row=0,column=0)
        tk.Button(self.frame, text = 'Wystaw recepte', command = self.issue_prescription_view).grid(row=1,column=0)
        tk.Button(self.frame, text = 'Wystaw eRecepte', command = self.issue_eprescription_view).grid(row=2,column=0)
        tk.Button(self.frame, text = 'Przegladaj badania', command = self.create_doc_tests_view).grid(row=3,column=0)
        tk.Button(self.frame, text = 'Wystaw skierowanie', command = self.create_add_referral_view).grid(row=4,column=0)
        tk.Button(self.frame, text = 'Wystaw skierowanie COVID', command = self.create_add_covreferral_view).grid(row=5,column=0)
        tk.Button(self.frame, text = 'Przegladaj zapisy na szczepienia', command = self.create_vaccines_doc_view).grid(row=6,column=0)
        tk.Button(self.frame, text = 'Dolacz do teleporady', command = self.join_evisit).grid(row=7,column=0)
        tk.Button(self.frame, text = 'Wyloguj',command = self.create_login_screen).grid(row=12,column=1)

    def create_book_visit_view(self):

        def book_visit(id_wizyty, id_pacjenta):
            
            wizyta = Wizyta()
            wizyta.update_visit(id_wizyty, id_pacjenta)
            messagebox.showinfo('Rezerwacja wizyty', 'Wizyta zostala zarezerwowana.\
                                \nAby odwolac lub obejrzec swoje wizyty, udaj sie do listy swoich wizyt w menu glownym.')
            self.create_patient_main_view()

        self.clear_screen()
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute('SELECT w.id_wizyty, w.zajeta, w.data, w.id_lekarza, w.is_online, l.id_usera, l.imie, l.nazwisko\
                  FROM wizyta w join user as l on w.id_lekarza = l.id_usera WHERE w.zajeta = 0 and w.is_online=0')
        visit_list = c.fetchall()
        i = 1
        tk.Label(self.frame, text = 'Data i godzina').grid(row=0,column=0, sticky='W')
        tk.Label(self.frame, text = 'Lekarz').grid(row=0,column=1, sticky='W')
        for row in visit_list:
            id_wizyty = row[0]
            data = row[2]
            id_lekarza = row[3]
            lekarz = f'{row[6]} {row[7]}'

            tk.Label(self.frame, text = data).grid(row=i,column=0)
            tk.Label(self.frame, text = lekarz).grid(row=i,column=1, sticky='W')
            tk.Button(self.frame, text = 'Wybierz',command = lambda id_wizyty=id_wizyty: book_visit(id_wizyty, self.id_usera)).grid(row=i,column=2)
            i+=1
        tk.Button(self.frame, text = 'Powrot',command = self.create_patient_main_view).grid(row=12,column=1)
        
    def create_book_evisit_view(self):

        def book_evisit(id_wizyty, id_pacjenta):
            
            wizyta = Wizyta()
            wizyta.update_visit(id_wizyty, id_pacjenta)
            messagebox.showinfo('Rezerwacja teleporady', 'Teleporada zostala zarezerwowana.\nAby odwolac lub obejrzec swoje teleporady,\
                                udaj sie do listy swoich wizyt w menu glownym.')
            self.create_patient_main_view()

        self.clear_screen()
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute('SELECT w.id_wizyty, w.zajeta, w.data, w.id_lekarza, l.id_usera, w.is_online, l.imie, l.nazwisko\
                  FROM wizyta w join user as l on w.id_lekarza = l.id_usera WHERE w.zajeta = 0 and w.is_online=1')
        visit_list = c.fetchall()
        i = 1
        tk.Label(self.frame, text = 'Data i godzina').grid(row=0,column=0, sticky='W')
        tk.Label(self.frame, text = 'Lekarz').grid(row=0,column=1, sticky='W')
        for row in visit_list:
            id_wizyty = row[0]
            data = row[2]
            id_lekarza = row[3]
            lekarz = f'{row[6]} {row[7]}'

            tk.Label(self.frame, text = data).grid(row=i,column=0)
            tk.Label(self.frame, text = lekarz).grid(row=i,column=1, sticky="W")
            tk.Button(self.frame, text = 'Wybierz',command = lambda id_wizyty=id_wizyty: book_evisit(id_wizyty, self.id_usera)).grid(row=i,column=3)
            i+=1
        tk.Button(self.frame, text = 'Powrot',command = self.create_patient_main_view).grid(row=12,column=1)

    def create_book_test_view(self):

            def book_test(id_skierowania, id_pacjenta, typ_choroby):
                
                badanie = Badanie(id_skierowania, id_pacjenta, typ_choroby)
                badanie.post_test_pat()
                messagebox.showinfo('Rezerwacja badania', 'Badanie zostalo zarezerwowane. Zapraszamy w dni robocze miedzy 07:00 a 11:00.')
                self.create_patient_main_view()

            self.clear_screen()
            conn = sqlite3.connect('bazaprzychodni.db')
            c = conn.cursor()
            c.execute('SELECT s.id_skierowania, s.id_lekarza,s.id_pacjenta, s.typ_choroby, l.imie, l.nazwisko, s.wykorzystane\
                      FROM skierowanie s JOIN user AS l on s.id_lekarza = l.id_usera WHERE wykorzystane = 0 AND id_pacjenta = :id_pac AND typ_choroby != 0',
                      {"id_pac":self.id_usera})
            referral_list = c.fetchall()
            if referral_list == []:
                tk.Label(self.frame, text = "Nie masz zadnych skierowan na badania.").grid(row=0,column=0)
            i = 1

            if referral_list != []:
                tk.Label(self.frame, text = 'Numer skierowania').grid(row=0,column=0)
                tk.Label(self.frame, text = 'Lekarz kierujacy').grid(row=0,column=1)
                tk.Label(self.frame, text = 'Typ badania').grid(row=0,column=2)
            for row in referral_list:
                id_skierowania = row[0]
                id_lekarza = row[1]
                id_pacjenta = row[2]
                typ = row[3]
                lekarz = f'{row[4]} {row[5]}'

                tk.Label(self.frame, text = id_skierowania).grid(row=i,column=0)
                tk.Label(self.frame, text = lekarz).grid(row=i,column=1)
                tk.Label(self.frame, text = choroby[typ]).grid(row=i,column=2)
                tk.Button(self.frame, text = 'Wybierz',command = lambda id_skierowania = id_skierowania, id_pacjenta = id_pacjenta,typ_choroby = typ :
                          book_test(id_skierowania, id_pacjenta, typ_choroby)).grid(row=i,column=3)
                i+=1
            
            tk.Button(self.frame, text = 'Powrot',command = self.create_patient_main_view).grid(row=12,column=1)

    def create_book_covtest_view(self):

            def book_covtest(id_skierowania, id_pacjenta, typ_choroby):
                
                covbadanie = Badanie(id_skierowania, id_pacjenta, 0)
                covbadanie.post_test_pat()
                messagebox.showinfo('Rezerwacja badania', 'Zostales zapisany(-a) na test COVID-19. Zapraszamy w dni robocze miedzy 07:00 a 11:00.')
                self.create_patient_main_view()

            self.clear_screen()
            conn = sqlite3.connect('bazaprzychodni.db')
            c = conn.cursor()
            c.execute('SELECT s.id_skierowania, s.id_lekarza,s.id_pacjenta, s.typ_choroby, l.imie, l.nazwisko, s.wykorzystane\
                      FROM skierowanie s JOIN user AS l on s.id_lekarza = l.id_usera WHERE wykorzystane = 0 AND id_pacjenta = :id_pac AND typ_choroby = 0',
                      {"id_pac":self.id_usera})
            referral_list = c.fetchall()
            if referral_list == []:
                tk.Label(self.frame, text = "Nie masz zadnych skierowan na badania.").grid(row=0,column=0)
            i = 1

            if referral_list != []:
                tk.Label(self.frame, text = 'Numer skierowania').grid(row=0,column=0)
                tk.Label(self.frame, text = 'Lekarz kierujacy').grid(row=0,column=1)
                
            for row in referral_list:
                id_skierowania = row[0]
                id_lekarza = row[1]
                id_pacjenta = row[2]
                typ = row[3]
                lekarz = f'{row[4]} {row[5]}'

                tk.Label(self.frame, text = id_skierowania).grid(row=i,column=0)
                
                tk.Label(self.frame, text = lekarz).grid(row=i,column=1)
                
                tk.Button(self.frame, text = 'Wybierz',command = lambda id_skierowania = id_skierowania, id_pacjenta = id_pacjenta:
                          book_covtest(id_skierowania, id_pacjenta, 0)).grid(row=i,column=3)
                i+=1
            
            tk.Button(self.frame, text = 'Powrot',command = self.create_patient_main_view).grid(row=12,column=1)
                    
    def create_pat_visits_view(self):
        
        def cancel_visit(id_wizyty):
            
            wizyta = Wizyta()
            wizyta.cancel_visit(id_wizyty)
            messagebox.showinfo('Odwolanie wizyty', 'Wizyta zostala odwolana.')
            self.create_patient_main_view()

        
        self.clear_screen()
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute(f'SELECT w.id_wizyty, w.data, w.zajeta, w.id_lekarza, w.id_pacjenta, w.is_online, l.imie, l.nazwisko\
                  FROM wizyta w join user l on w.id_lekarza = l.id_usera WHERE id_pacjenta = :id_pac', {'id_pac':self.id_usera})
        visits = c.fetchall()
        tk.Label(self.frame, text = "Numer wizyty").grid(row=0,column=0)
        tk.Label(self.frame, text = "Data").grid(row=0,column=1)
        tk.Label(self.frame, text = "Lekarz").grid(row=0,column=2)
        tk.Label(self.frame, text = "Typ").grid(row=0,column=3)
        i = 1

        for row in visits:
            id_wizyty = row[0]
            data = row[1]
            zajeta = row[2]
            id_lekarza = row[3]
            id_pacjenta = row[4]
            is_online = row[5]
            lekarz = f'{row[6]} {row[7]}'
            if is_online == 0:
                typ = "Wizyta na miejscu"
            else:
                typ = "Teleporada"

            tk.Label(self.frame, text = id_wizyty).grid(row=i,column=0)
            tk.Label(self.frame, text = data).grid(row=i,column=1)
            tk.Label(self.frame, text = lekarz).grid(row=i,column=2)
            tk.Label(self.frame, text = typ).grid(row=i,column=3)
            
            tk.Button(self.frame, text = 'Odwolaj',command = lambda  id_wizyty = id_wizyty: cancel_visit(id_wizyty)).grid(row=i,column=4)
            
            i+=1

        tk.Button(self.frame, text = 'Powrot',command = self.create_patient_main_view).grid(row=12,column=1)

    def create_tests_view(self):
        
        self.clear_screen()
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute(f'SELECT b.id_badania, b.typ_choroby, b.data, w.wynik FROM badanie b\
                  LEFT OUTER JOIN wynik w on b.id_badania = w.id_badania WHERE id_pacjenta = :id_pac', {'id_pac':self.id_usera})
        tests = c.fetchall()
        tk.Label(self.frame, text = "Typ").grid(row=0,column=0)
        tk.Label(self.frame, text = "Data").grid(row=0,column=1)
        tk.Label(self.frame, text = "Wynik").grid(row=0,column=2)
        i = 1

        for row in tests:
            typ = row[1]
            data = row[2]
            wynik = row[3]
            
            if wynik == 0:
                wyn = "Negatywny"
            elif wynik == 1:
                wyn = "Pozytywny"
            elif wynik is None:
                wyn = "Brak wyniku"

            tk.Label(self.frame, text = choroby[typ]).grid(row=i,column=0)
            tk.Label(self.frame, text = data).grid(row=i,column=1)
            tk.Label(self.frame, text = wyn).grid(row=i,column=2)
                       
            i+=1

        tk.Button(self.frame, text = 'Powrot',command = self.create_patient_main_view).grid(row=12,column=1)

    def create_prescriptions_view(self):
        
        self.clear_screen()
        self.root.geometry("700x500")
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute(f'SELECT r.id_recepty, r.tresc, r.id_pacjenta, r.id_lekarza, p.imie, p.nazwisko, l.imie, l.nazwisko, r.is_erecepta\
                  FROM recepta r JOIN user p on r.id_pacjenta = p.id_usera JOIN user l on r.id_lekarza=l.id_usera\
                  WHERE r.id_pacjenta = :id_pac and r.is_erecepta=1' , {'id_pac':self.id_usera})
        prescriptions = c.fetchall()
        tk.Label(self.frame, text = "Numer recepty").grid(row=0,column=0)
        tk.Label(self.frame, text = "Tresc").grid(row=0,column=1)
        tk.Label(self.frame, text = "Pacjent").grid(row=0,column=2)
        tk.Label(self.frame, text = "ID pacjenta").grid(row=0,column=3)
        tk.Label(self.frame, text = "Lekarz wystawiajacy").grid(row=0,column=4)
        i = 1

        for row in prescriptions:
            id_recepty = row[0]
            tresc = row[1]
            id_pacjenta = row[2]
            id_lekarza = row[3]
            pacjent = f'{row[4]} {row[5]}'
            lekarz = f'{row[6]} {row[7]}'
            
            tk.Label(self.frame, text = id_recepty).grid(row=i,column=0)
            tk.Label(self.frame, text = tresc).grid(row=i,column=1)
            tk.Label(self.frame, text = pacjent).grid(row=i,column=2)
            tk.Label(self.frame, text = id_pacjenta).grid(row=i,column=3)
            tk.Label(self.frame, text = lekarz).grid(row=i,column=4)
                       
            i+=1

        tk.Button(self.frame, text = 'Powrot',command = self.create_patient_main_view).grid(row=12,column=1)

    def create_book_vaccine_view(self):   

        def book_vaccine(chor,data,id_pacjenta):
            
            chor = var.get()
            if chor == 'COVID':
                typ_choroby = 0
            elif chor == 'Zoltaczka':
                typ_choroby = 2
            elif chor == 'Odra':
                typ_choroby = 5
            szczepienie = Szczepienie(typ_choroby,data,id_pacjenta)
            szczepienie.post_szczepienie(typ_choroby, data, id_pacjenta)
            messagebox.showinfo('Szczepienie', 'Twoja rezerwacja szczepienia zostala zapisana.\
                                Pracownik naszej placowki skontaktuje sie z Toba, aby potwierdzic szczepienie.')
            self.create_patient_main_view()


        self.clear_screen()
        typ_choroby = None
        tk.Label(self.frame, text = 'Wybierz rodzaj szczepienia').grid(row=0,column=0)
        var = tk.StringVar()
        tk.OptionMenu(self.frame, var, 'COVID','Zoltaczka', 'Odra').grid(row=0,column=1)

        tk.Label(self.frame, text = 'Wpisz date kiedy chcesz sie zaczepic\nw formacie RRRR-MM-DD GG:MM').grid(row=1,column=0)
        data = tk.Entry(self.frame)
        data.grid(row=1,column=1)

        tk.Button(self.frame, text = 'Zapisz sie',command = lambda:book_vaccine(var.get(), data.get(), self.id_usera)).grid(row=2,column=1)
        tk.Button(self.frame, text = 'Powrot',command = self.create_patient_main_view).grid(row=12,column=1)


    def join_evisit(self):
        
        messagebox.showinfo('Teleporada', 'Zostaniesz przekierowany do systemu obslugujacego teleporady')


    def create_doc_visits_view(self):
        
        def cancel_visit(id_wizyty):
            
            wizyta = Wizyta()
            wizyta.cancel_visit(id_wizyty)
            messagebox.showinfo('Odwolanie wizyty', 'Wizyta zostala odwolana.')
            self.create_doc_main_view()

        
        self.clear_screen()
        self.root.geometry("700x500")
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute(f'SELECT w.id_wizyty, w.data, w.zajeta, w.id_lekarza, w.id_pacjenta, w.is_online, p.imie, p.nazwisko\
                  FROM wizyta w join user p on w.id_pacjenta = p.id_usera WHERE id_lekarza = :id_lek', {'id_lek':self.id_usera})
        visits = c.fetchall()
        tk.Label(self.frame, text = "Numer wizyty").grid(row=0,column=0)
        tk.Label(self.frame, text = "Data").grid(row=0,column=1)
        tk.Label(self.frame, text = "Pacjent").grid(row=0,column=2)
        tk.Label(self.frame, text = "ID Pacjenta").grid(row=0,column=3)
        tk.Label(self.frame, text = "Typ").grid(row=0,column=4)
        i = 1

        for row in visits:
            id_wizyty = row[0]
            data = row[1]
            zajeta = row[2]
            id_lekarza = row[3]
            id_pacjenta = row[4]
            is_online = row[5]
            pacjent = f'{row[6]} {row[7]}'
            if is_online == 0:
                typ = "Wizyta na miejscu"
            else:
                typ = "Teleporada"

            tk.Label(self.frame, text = id_wizyty).grid(row=i,column=0)
            tk.Label(self.frame, text = data).grid(row=i,column=1)
            tk.Label(self.frame, text = pacjent).grid(row=i,column=2)
            tk.Label(self.frame, text = id_pacjenta).grid(row=i,column=3)
            tk.Label(self.frame, text = typ).grid(row=i,column=4)
            
            tk.Button(self.frame, text = 'Odwolaj',command = lambda  id_wizyty = id_wizyty: cancel_visit(id_wizyty)).grid(row=i,column=5)
            
            i+=1

        tk.Button(self.frame, text = 'Powrot',command = self.create_doc_main_view).grid(row=12,column=1)
     
    def issue_prescription_view(self):
        
        def issue_prescription():
            
            conn = sqlite3.connect('bazaprzychodni.db')
            c = conn.cursor()
            c.execute(f'INSERT INTO recepta VALUES(null, :tresc, :id_pac, :id_lek, 0)', {'tresc':pr.get("1.0",'end-1c'),'id_pac':id_pac.get(), 'id_lek':self.id_usera})
            conn.commit()
            messagebox.showinfo('Recepta', 'Recepta wystawiona pomyslnie.')
            self.create_doc_main_view()
           
        self.clear_screen()
        self.root.geometry("700x500")
        tk.Label(self.frame, text = 'Wprowadz ID pacjenta').grid(row=0,column=0)
        id_pac = tk.Entry(self.frame)
        id_pac.grid(row=0,column=1)
        tk.Label(self.frame, text = 'Wprowadz tresc recepty:').grid(row=1,column=0)
        pr = tk.Text(self.frame, width=50,height=10)
        pr.grid(row=2,column=0)
        tk.Button(self.frame, text = 'Wystaw recepte', command = issue_prescription).grid(row=3,column=0)

        tk.Button(self.frame, text = 'Powrot',command = self.create_doc_main_view).grid(row=12,column=1)

    def issue_eprescription_view(self):
        
        def issue_eprescription():
            
            conn = sqlite3.connect('bazaprzychodni.db')
            c = conn.cursor()
            c.execute(f'INSERT INTO recepta VALUES(null, :tresc, :id_pac, :id_lek, 1)', {'tresc':pr.get("1.0",'end-1c'),'id_pac':id_pac.get(), 'id_lek':self.id_usera})
            conn.commit()
            messagebox.showinfo('Recepta', 'eRecepta wystawiona pomyslnie.')
            self.create_doc_main_view()
           
        self.clear_screen()
        self.root.geometry("700x500")
        tk.Label(self.frame, text = 'Wprowadz ID pacjenta').grid(row=0,column=0)
        id_pac = tk.Entry(self.frame)
        id_pac.grid(row=0,column=1)
        tk.Label(self.frame, text = 'Wprowadz tresc e-recepty:').grid(row=1,column=0)
        pr = tk.Text(self.frame,width=50,height=10)
        pr.grid(row=2,column=0)
        tk.Button(self.frame, text = 'Wystaw e-recepte', command = issue_eprescription).grid(row=3,column=0)

        tk.Button(self.frame, text = 'Powrot',command = self.create_doc_main_view).grid(row=12,column=1)

    def create_doc_tests_view(self):

        def post_res(a,b,c,d,e,f):
            
            wynik = Wynik()
            wynik.post_result(a,b,c,d)

            if e == 0:
                self.cancel_quarantine(f)
                messagebox.showinfo('Kwarantanna', 'W zwiazku z wynikiem testu COVID pacjent zostal zwolniony z kwarantanny.')
                if (b == '1'):
                    self.create_res_isolation_view(f)
            else:
                self.create_doc_tests_view()
          
        def enter_result(id_badania,typ_choroby,id_pacjenta):
            
            self.clear_screen()
            tk.Label(self.frame, text = 'Wprowadz wynik. 0-negatywny, 1-pozytywny').grid(row=0,column=0)
            result = tk.Entry(self.frame)
            result.grid(row=0,column=1)
            
            tk.Label(self.frame, text = 'Wprowadz date badania w formacie RRRR-MM-DD GG:MM').grid(row=1,column=0)
            date = tk.Entry(self.frame)
            date.grid(row=1,column=1)
            
            tk.Label(self.frame, text = 'Dodaj notatke (opcjonalnie)').grid(row=2,column=0)
            note = tk.Text(self.frame,width=50,height=10)
            note.grid(row=3,column=0)
            
            tk.Button(self.frame, text = 'Zatwierdz', command = lambda :
                      post_res(id_badania, result.get(),date.get(),note.get("1.0", "end-1c"),typ_choroby,id_pacjenta)).grid(row=4,column=0)

            tk.Button(self.frame, text = 'Powrot',command = self.create_doc_tests_view).grid(row=12,column=1)

        self.clear_screen()
        self.root.geometry("1000x600")
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute(f'SELECT b.id_pacjenta, p.imie, p.nazwisko, b.id_badania,b.id_skierowania, b.typ_choroby,\
                  b.data, w.wynik, w.note FROM badanie b LEFT OUTER JOIN wynik w on b.id_badania = w.id_badania JOIN user p on b.id_pacjenta=p.id_usera')
        tests = c.fetchall()
        tk.Label(self.frame, text = "ID pacjenta").grid(row=0,column=0)
        tk.Label(self.frame, text = "Imie").grid(row=0,column=1)
        tk.Label(self.frame, text = "Nazwisko").grid(row=0,column=2)
        tk.Label(self.frame, text = "ID badania").grid(row=0,column=3)
        tk.Label(self.frame, text = "ID skierowania").grid(row=0,column=4)
        tk.Label(self.frame, text = "Typ choroby").grid(row=0,column=5)
        tk.Label(self.frame, text = "Data").grid(row=0,column=6)
        tk.Label(self.frame, text = "Wynik").grid(row=0,column=7)
        tk.Label(self.frame, text = "Notatka").grid(row=0,column=8)

        i = 1

        for row in tests:
            id_pacjenta = row[0]
            imie = row[1]
            nazwisko = row[2]
            id_badania = row[3]
            id_skierowania = row[4]
            typ_choroby = row[5]
            data = row[6]
            wynik = row[7]
            notka = row[8]

            
            if wynik == 0:
                wyn = "Negatywny"
            elif wynik == 1:
                wyn = "Pozytywny"
            elif wynik is None:
                wyn = "Brak wyniku"

            tk.Label(self.frame, text = id_pacjenta).grid(row=i,column=0)
            tk.Label(self.frame, text = imie).grid(row=i,column=1)
            tk.Label(self.frame, text = nazwisko).grid(row=i,column=2)
            tk.Label(self.frame, text = id_badania).grid(row=i,column=3)
            tk.Label(self.frame, text = id_skierowania).grid(row=i,column=4)
            tk.Label(self.frame, text = choroby[typ_choroby]).grid(row=i,column=5)
            tk.Label(self.frame, text = data).grid(row=i,column=6)
            tk.Label(self.frame, text = wyn).grid(row=i,column=7)
            tk.Label(self.frame, text = notka).grid(row=i,column=8)

            if wynik is None:
                tk.Button(self.frame, text = 'Dodaj wynik',command = lambda id_badania = id_badania, typ_choroby = typ_choroby,id_pacjenta = id_pacjenta:
                          enter_result(id_badania,typ_choroby,id_pacjenta)).grid(row=i,column=9)
                
            i+=1

        tk.Button(self.frame, text = 'Powrot',command = self.create_doc_main_view).grid(row=100,column=1)
         
    def create_add_referral_view(self):

        def add_referral():
            
            chor = var.get()
            if chor == 'HIV':
                typ_choroby = 1
            elif chor == 'Zoltaczka':
                typ_choroby = 2
            elif chor == 'Cukrzyca':
                typ_choroby = 3
            elif chor == 'Salmonella':
                typ_choroby = 4
            elif chor == 'Odra':
                typ_choroby = 5
            
            
            conn = sqlite3.connect('bazaprzychodni.db')
            c = conn.cursor()
            c.execute(f'INSERT INTO skierowanie VALUES(null, :id_lek, :id_pac, :typ_choroby, 0)',
                      {'id_lek':self.id_usera, 'id_pac':id_pac.get(), 'typ_choroby':typ_choroby})
            conn.commit()
            conn.close()
            messagebox.showinfo('Skierowanie', 'Skierowanie wystawione pomyslnie')
            self.create_doc_main_view()
            

        self.clear_screen()

        tk.Label(self.frame, text = 'Podaj ID pacjenta: ').grid(row=0,column=0)
        id_pac = tk.Entry(self.frame)
        id_pac.grid(row=0,column=1)
        tk.Label(self.frame, text = 'Wybierz typ choroby: ').grid(row=1,column=0)
        var = tk.StringVar()
        tk.OptionMenu(self.frame, var, 'HIV','Zoltaczka','Cukrzyca','Salmonella','Odra').grid(row=1,column=1)
        
        tk.Button(self.frame, text = 'Wystaw skierowanie na badanie',command = add_referral).grid(row=3,column=1)
        tk.Button(self.frame, text = 'Powrot',command = self.create_doc_main_view).grid(row=12,column=1)


    def create_add_covreferral_view(self):

        def add_covreferral():
                     
            conn = sqlite3.connect('bazaprzychodni.db')
            c = conn.cursor()
            c.execute(f'INSERT INTO skierowanie VALUES(null, :id_lek, :id_pac, 0, 0)',{'id_lek':self.id_usera, 'id_pac':id_pac.get()})
            conn.commit()
            c.execute(f'INSERT INTO kwarantanna VALUES(null, :id_pac, :data)',{'id_pac':id_pac.get(), 'data':data_kw.get()})
            conn.commit()
            conn.close()
            messagebox.showinfo('Skierowanie', 'Skierowanie wystawione pomyslnie')
            self.create_doc_main_view()
            

        self.clear_screen()
        self.root.geometry("700x500")
        tk.Label(self.frame, text = 'Podaj ID pacjenta: ').grid(row=0,column=0)
        id_pac = tk.Entry(self.frame)
        id_pac.grid(row=0,column=1)

        tk.Label(self.frame, text = 'Kierujac pacjenta na test COVID, \nautomatycznie kierujesz go na kwarantanne do uzyskania wyniku\nlub do daty zakonczenia kwarantanny.\
                 \nPodaj date zakonczenia kwarantanny.').grid(row=1,column=0)
        data_kw = tk.Entry(self.frame)
        data_kw.grid(row=2,column=0)
        
        tk.Button(self.frame, text = 'Wystaw skierowanie na test COVID',command = add_covreferral).grid(row=3,column=1)
        tk.Button(self.frame, text = 'Powrot',command = self.create_doc_main_view).grid(row=12,column=1)

    def create_res_isolation_view(self,id_pacjenta):

        def post_isolation():
            
            conn = sqlite3.connect('bazaprzychodni.db')
            c = conn.cursor()
            c.execute(f'INSERT INTO izolacja VALUES(null, :id_pac, :data_zak)',{'id_pac':id_pacjenta, 'data_zak':data_iz.get()})
            conn.commit()
            conn.close()
            messagebox.showinfo('Izolacja', 'Pacjent zostal skierowany na izolacje')
            self.create_doc_main_view()
        self.clear_screen()
        id_pacjenta = id_pacjenta
        tk.Label(self.frame, text = 'Wprowadziles(-as) pozytywny wynik testu COVID, \nPacjent zostaje skierowany na izolacje.\nPodaj date zakonczenia izolacji.').grid(row=1,column=0)
        data_iz = tk.Entry(self.frame)
        data_iz.grid(row=2,column=0)
        tk.Button(self.frame, text = 'Zatwierdz',command = post_isolation).grid(row=3,column=1)

    def cancel_quarantine(self,id_pacjenta):
        
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute(f'DELETE FROM kwarantanna WHERE id_pacjenta = :id_pac',{'id_pac':id_pacjenta})
        conn.commit()
        conn.close()

    def create_quarantines_pat_view(self):
        
        self.clear_screen()
        
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute('SELECT id_kwarantanny, data_zakonczenia FROM kwarantanna WHERE id_pacjenta = :id_pac', {'id_pac':self.id_usera})
        q_list = c.fetchall()
        i = 1
        tk.Label(self.frame, text = 'Identyfikator').grid(row=0,column=0, sticky='W')
        tk.Label(self.frame, text = 'Data zakonczenia').grid(row=0,column=1, sticky='W')
        for row in q_list:
            id_kwarantanny = row[0]
            data_zakonczenia = row[1]

            tk.Label(self.frame, text = id_kwarantanny).grid(row=i,column=0)
            tk.Label(self.frame, text = data_zakonczenia).grid(row=i,column=1, sticky='W')
            i+=1
        tk.Button(self.frame, text = 'Powrot',command = self.create_patient_main_view).grid(row=12,column=1)

    def create_isolations_pat_view(self):
        
        self.clear_screen()
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute('SELECT id_izolacji, data_zakonczenia FROM izolacja WHERE id_pacjenta = :id_pac', {'id_pac':self.id_usera})
        i_list = c.fetchall()
        i = 1
        tk.Label(self.frame, text = 'Identyfikator').grid(row=0,column=0, sticky='W')
        tk.Label(self.frame, text = 'Data zakonczenia').grid(row=0,column=1, sticky='W')
        for row in i_list:
            id_izolacji = row[0]
            data_zakonczenia = row[1]

            tk.Label(self.frame, text = id_izolacji).grid(row=i,column=0)
            tk.Label(self.frame, text = data_zakonczenia).grid(row=i,column=1, sticky='W')
            i+=1
        tk.Button(self.frame, text = 'Powrot',command = self.create_patient_main_view).grid(row=12,column=1)

    def create_quarantines_view(self):
        
        self.clear_screen()   
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute('SELECT id_kwarantanny, id_pacjenta, data_zakonczenia FROM kwarantanna')
        q_list = c.fetchall()
        i = 1
        tk.Label(self.frame, text = 'Identyfikator').grid(row=0,column=0, sticky='W')
        tk.Label(self.frame, text = 'ID pacjenta').grid(row=0,column=1, sticky='W')
        tk.Label(self.frame, text = 'Data zakonczenia').grid(row=0,column=2, sticky='W')
        for row in q_list:
            id_kwarantanny = row[0]
            id_pacjenta = row[1]
            data_zakonczenia = row[2]

            tk.Label(self.frame, text = id_kwarantanny).grid(row=i,column=0)
            tk.Label(self.frame, text = id_pacjenta).grid(row=i,column=1)
            tk.Label(self.frame, text = data_zakonczenia).grid(row=i,column=2, sticky='W')
            i+=1
        tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=12,column=1)

    def create_isolations_view(self):
        
        self.clear_screen()
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute('SELECT id_izolacji, id_pacjenta, data_zakonczenia FROM izolacja')
        i_list = c.fetchall()
        i = 1
        tk.Label(self.frame, text = 'Identyfikator').grid(row=0,column=0, sticky='W')
        tk.Label(self.frame, text = 'ID pacjenta').grid(row=0,column=1, sticky='W')
        tk.Label(self.frame, text = 'Data zakonczenia').grid(row=0,column=2, sticky='W')
        for row in i_list:
            id_izolacji = row[0]
            id_pacjenta = row[1]
            data_zakonczenia = row[2]

            tk.Label(self.frame, text = id_izolacji).grid(row=i,column=0)
            tk.Label(self.frame, text = id_pacjenta).grid(row=i,column=1)
            tk.Label(self.frame, text = data_zakonczenia).grid(row=i,column=2, sticky='W')
            i+=1
        tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=12,column=1)


    def create_patients_view(self):


        def add_patient_view():
            
            def add_patient():
                
                conn = sqlite3.connect('bazaprzychodni.db')
                c = conn.cursor()
                c.execute('INSERT INTO user VALUES(null, :imie, :nazwisko, :login, :haslo, 2)',
                          {'imie':imie.get(), 'nazwisko':nazwisko.get(), 'login':login.get(), 'haslo':haslo.get()})
                conn.commit()
                messagebox.showinfo('Dodanie pacjenta', 'Pacjent zostal dodany.')
                self.create_admin_main_view()
            
            self.clear_screen()
            tk.Label(self.frame, text = 'Imie: ').grid(row=0,column=0, sticky='W')
            tk.Label(self.frame, text = 'Nazwisko: ').grid(row=1,column=0, sticky='W')
            tk.Label(self.frame, text = 'Login: ').grid(row=2,column=0, sticky='W')
            tk.Label(self.frame, text = 'Haslo: ').grid(row=3,column=0, sticky='W')
            imie = tk.Entry(self.frame)
            imie.grid(row=0,column=1)
            nazwisko = tk.Entry(self.frame)
            nazwisko.grid(row=1,column=1)
            login = tk.Entry(self.frame)
            login.grid(row=2,column=1)
            haslo = tk.Entry(self.frame)
            haslo.grid(row=3,column=1)
            tk.Button(self.frame, text = 'Dodaj', command = add_patient).grid(row=100,column=1)
            tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=2013,column=1)


        def delete_patient_view():
            
            def delete_patient():
                
                conn = sqlite3.connect('bazaprzychodni.db')
                c = conn.cursor()
                c.execute('DELETE FROM user WHERE id_usera = :id_pac', {'id_pac':id_pac.get()})
                conn.commit()
                messagebox.showinfo('Usuniecie pacjenta', 'Pacjent zostal usuniety.')
                self.create_admin_main_view()
            
            self.clear_screen()
            tk.Label(self.frame, text = 'Podaj ID pacjenta do usuniecia: ').grid(row=0,column=0, sticky='W')
            id_pac = tk.Entry(self.frame)
            id_pac.grid(row=0,column=1)
            tk.Button(self.frame, text = 'Usun', command = delete_patient).grid(row=100,column=1)
            tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=203,column=1)

        def update_patient_view():
            
            def update_patient():
                
                conn = sqlite3.connect('bazaprzychodni.db')
                c = conn.cursor()
                c.execute('UPDATE user SET imie = :imie, nazwisko = :nazwisko, login = :login, haslo = :haslo WHERE id_usera = :id_pac',
                          {'imie':imie.get(), 'nazwisko':nazwisko.get(), 'login':login.get(), 'haslo':haslo.get(),'id_pac':id_pac.get()})
                conn.commit()
                messagebox.showinfo('Modyfikacja pacjenta', 'Pacjent zostal zmodyfikowany.')
                self.create_admin_main_view()

            self.clear_screen()
            tk.Label(self.frame, text = 'Podaj ID pacjenta do modyfikacji: ').grid(row=0,column=0, sticky='W')
            tk.Label(self.frame, text = 'Nowe Imie: ').grid(row=1,column=0, sticky='W')
            tk.Label(self.frame, text = 'Nowe Nazwisko: ').grid(row=2,column=0, sticky='W')
            tk.Label(self.frame, text = 'Nowy Login: ').grid(row=3,column=0, sticky='W')
            tk.Label(self.frame, text = 'Nowe Haslo: ').grid(row=4,column=0, sticky='W')
            tk.Label(self.frame, text = 'Nalezy podac wszystkie dane, nawet niezmieniane.').grid(row=5,column=0, sticky='W')
            tk.Button(self.frame, text = 'Modyfikuj', command = update_patient).grid(row=6,column=1)
            tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=7,column=1)
            id_pac = tk.Entry(self.frame)
            id_pac.grid(row=0,column=1)
            imie = tk.Entry(self.frame)
            imie.grid(row=1,column=1)
            nazwisko = tk.Entry(self.frame)
            nazwisko.grid(row=2,column=1)
            login = tk.Entry(self.frame)
            login.grid(row=3,column=1)
            haslo = tk.Entry(self.frame)
            haslo.grid(row=4,column=1)
    
        self.clear_screen()
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute('SELECT * FROM user WHERE typ_usera = 2')
        p_list = c.fetchall()
        i = 1
        tk.Label(self.frame, text = 'ID pacjenta').grid(row=0,column=0,)
        tk.Label(self.frame, text = 'Imie').grid(row=0,column=1)
        tk.Label(self.frame, text = 'Nazwisko').grid(row=0,column=2)
        tk.Label(self.frame, text = 'Login').grid(row=0,column=3)
        tk.Label(self.frame, text = 'Haslo').grid(row=0,column=4)
        for row in p_list:
            id_pacjenta = row[0]
            imie = row[1]
            nazwisko = row[2]
            login = row[3]
            haslo = row[4]

            tk.Label(self.frame, text = id_pacjenta).grid(row=i,column=0)
            tk.Label(self.frame, text = imie).grid(row=i,column=1)
            tk.Label(self.frame, text = nazwisko).grid(row=i,column=2)
            tk.Label(self.frame, text = login).grid(row=i,column=3)
            tk.Label(self.frame, text = haslo).grid(row=i,column=4)
            i+=1
        tk.Button(self.frame, text = 'Dodaj pacjenta', command = add_patient_view).grid(row=200,column=1)
        tk.Button(self.frame, text = 'Usun pacjenta', command = delete_patient_view).grid(row=201,column=1)
        tk.Button(self.frame, text = 'Modyfikuj pacjenta', command = update_patient_view).grid(row=202,column=1)
        tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=203,column=1)

        
    def create_doctors_view(self):

        
        def add_doc_view():
            
            def add_doc():
                
                conn = sqlite3.connect('bazaprzychodni.db')
                c = conn.cursor()
                c.execute('INSERT INTO user VALUES(null, :imie, :nazwisko, :login, :haslo, 1)', {'imie':imie.get(), 'nazwisko':nazwisko.get(), 'login':login.get(), 'haslo':haslo.get()})
                conn.commit()
                messagebox.showinfo('Dodanie lekarza', 'Lekarz zostal dodany.')
                self.create_admin_main_view()
            
            self.clear_screen()
            tk.Label(self.frame, text = 'Imie: ').grid(row=0,column=0, sticky='W')
            tk.Label(self.frame, text = 'Nazwisko: ').grid(row=1,column=0, sticky='W')
            tk.Label(self.frame, text = 'Login: ').grid(row=2,column=0, sticky='W')
            tk.Label(self.frame, text = 'Haslo: ').grid(row=3,column=0, sticky='W')
            imie = tk.Entry(self.frame)
            imie.grid(row=0,column=1)
            nazwisko = tk.Entry(self.frame)
            nazwisko.grid(row=1,column=1)
            login = tk.Entry(self.frame)
            login.grid(row=2,column=1)
            haslo = tk.Entry(self.frame)
            haslo.grid(row=3,column=1)
            tk.Button(self.frame, text = 'Dodaj', command = add_doc).grid(row=100,column=1)
            tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=203,column=1)


        def delete_doc_view():
            
            def delete_doc():
                
                conn = sqlite3.connect('bazaprzychodni.db')
                c = conn.cursor()
                c.execute('DELETE FROM user WHERE id_usera = :id_doc', {'id_doc':id_doc.get()})
                conn.commit()
                messagebox.showinfo('Usuniecie lekarza', 'Lekarz zostal usuniety.')
                self.create_admin_main_view()
            
            self.clear_screen()
            tk.Label(self.frame, text = 'Podaj ID lekarza do usuniecia: ').grid(row=0,column=0)
            id_doc = tk.Entry(self.frame)
            id_doc.grid(row=0,column=1)
            tk.Button(self.frame, text = 'Usun', command = delete_doc).grid(row=100,column=1)
            tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=203,column=1)

        def update_doc_view():
            
            def update_doc():
                
                conn = sqlite3.connect('bazaprzychodni.db')
                c = conn.cursor()
                c.execute('UPDATE user SET imie = :imie, nazwisko = :nazwisko, login = :login, haslo = :haslo WHERE id_usera = :id_doc', {'imie':imie.get(), 'nazwisko':nazwisko.get(), 'login':login.get(), 'haslo':haslo.get(),'id_doc':id_doc.get()})
                conn.commit()
                messagebox.showinfo('Modyfikacja lekarza', 'Lekarz zostal zmodyfikowany.')
                self.create_admin_main_view()

            self.clear_screen()
            tk.Label(self.frame, text = 'Podaj ID lekarza do modyfikacji: ').grid(row=0,column=0)
            tk.Label(self.frame, text = 'Nowe Imie: ').grid(row=1,column=0, sticky='W')
            tk.Label(self.frame, text = 'Nowe Nazwisko: ').grid(row=2,column=0, sticky='W')
            tk.Label(self.frame, text = 'Nowy Login: ').grid(row=3,column=0, sticky='W')
            tk.Label(self.frame, text = 'Nowe Haslo: ').grid(row=4,column=0, sticky='W')
            tk.Label(self.frame, text = 'Nalezy podac wszystkie dane, nawet niezmieniane.').grid(row=5,column=0, sticky='W')
            tk.Button(self.frame, text = 'Modyfikuj', command = update_doc).grid(row=6,column=1)
            tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=7,column=1)
            id_doc = tk.Entry(self.frame)
            id_doc.grid(row=0,column=1)
            imie = tk.Entry(self.frame)
            imie.grid(row=1,column=1)
            nazwisko = tk.Entry(self.frame)
            nazwisko.grid(row=2,column=1)
            login = tk.Entry(self.frame)
            login.grid(row=3,column=1)
            haslo = tk.Entry(self.frame)
            haslo.grid(row=4,column=1)
        
        self.clear_screen()
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute('SELECT * FROM user WHERE typ_usera = 1')
        l_list = c.fetchall()
        i = 1
        tk.Label(self.frame, text = 'ID lekarza').grid(row=0,column=0, sticky='W')
        tk.Label(self.frame, text = 'Imie').grid(row=0,column=1, sticky='W')
        tk.Label(self.frame, text = 'Nazwisko').grid(row=0,column=2, sticky='W')
        tk.Label(self.frame, text = 'Login').grid(row=0,column=3, sticky='W')
        tk.Label(self.frame, text = 'Haslo').grid(row=0,column=4, sticky='W')
        for row in l_list:
            id_lekarza = row[0]
            imie = row[1]
            nazwisko = row[2]
            login = row[3]
            haslo = row[4]

            tk.Label(self.frame, text = id_lekarza).grid(row=i,column=0)
            tk.Label(self.frame, text = imie).grid(row=i,column=1)
            tk.Label(self.frame, text = nazwisko).grid(row=i,column=2)
            tk.Label(self.frame, text = login).grid(row=i,column=3)
            tk.Label(self.frame, text = haslo).grid(row=i,column=4)
            i+=1
        tk.Button(self.frame, text = 'Dodaj lekarza', command = add_doc_view).grid(row=200,column=1)
        tk.Button(self.frame, text = 'Usun lekarza', command = delete_doc_view).grid(row=201,column=1)
        tk.Button(self.frame, text = 'Modyfikuj lekarza', command = update_doc_view).grid(row=202,column=1)
        tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=203,column=1)
    
        
    def create_visits_view(self):


        def delete_visit_view():
            
            def delete_visit():
                
                conn = sqlite3.connect('bazaprzychodni.db')
                c = conn.cursor()
                c.execute('DELETE FROM wizyta WHERE id_wizyty = :id_wiz', {'id_wiz':id_wiz.get()})
                conn.commit()
                messagebox.showinfo('Usuniecie wizyty', 'Wizyta zostala usunieta.')
                self.create_admin_main_view()
            
            self.clear_screen()
            tk.Label(self.frame, text = 'Podaj ID wizyty do usuniecia: ').grid(row=0,column=0, sticky='W')
            id_wiz = tk.Entry(self.frame)
            id_wiz.grid(row=0,column=1)
            tk.Button(self.frame, text = 'Usun', command = delete_visit).grid(row=100,column=1)
            tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=203,column=1)

        def add_visit_view():
            
            def add_visit():
                
                conn = sqlite3.connect('bazaprzychodni.db')
                c = conn.cursor()
                c.execute('INSERT INTO wizyta VALUES(null, :data, 0, :id_lek, null, :is_online)', {'data':data.get(), 'id_lek':id_lek.get(), 'is_online':is_online.get()})
                conn.commit()
                messagebox.showinfo('Dodanie wizyty', 'Wizyta zostala dodana.')
                self.create_admin_main_view()
            
            self.clear_screen()
            
            tk.Label(self.frame, text = 'Data (RRRR-MM-DD GG:MM): ').grid(row=0,column=0, sticky='W')
            tk.Label(self.frame, text = 'ID lekarza: ').grid(row=1,column=0, sticky='W')
            data = tk.Entry(self.frame)
            data.grid(row=0,column=1)
            id_lek = tk.Entry(self.frame)
            id_lek.grid(row=1,column=1)
            is_online = tk.IntVar()
            tk.Radiobutton(self.frame, text = 'Teleporada', variable = is_online, value = 1).grid(row=2,column=0,sticky='W')
            tk.Radiobutton(self.frame, text = 'Wizyta na miejscu', variable = is_online, value = 0).grid(row=3,column=0,sticky='W')
            
            tk.Button(self.frame, text = 'Dodaj', command = add_visit).grid(row=100,column=1)
            tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=203,column=1)
        
        self.clear_screen()
        self.root.geometry("600x600")
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute('SELECT * FROM wizyta')
        w_list = c.fetchall()
        i = 1
        tk.Label(self.frame, text = 'ID wizyty').grid(row=0,column=0)
        tk.Label(self.frame, text = 'Data').grid(row=0,column=1)
        tk.Label(self.frame, text = 'Zajeta').grid(row=0,column=2)
        tk.Label(self.frame, text = 'ID lekarza').grid(row=0,column=3)
        tk.Label(self.frame, text = 'ID pacjenta').grid(row=0,column=4)
        tk.Label(self.frame, text = 'Teleporada').grid(row=0,column=5)
        for row in w_list:
            id_wizyty = row[0]
            data = row[1]
            zajeta = row[2]
            id_lekarza = row[3]
            id_pacjenta = row[4]
            teleporada = row[5]

            tk.Label(self.frame, text = id_wizyty).grid(row=i,column=0)
            tk.Label(self.frame, text = data).grid(row=i,column=1)
            tk.Label(self.frame, text = zajeta).grid(row=i,column=2)
            tk.Label(self.frame, text = id_lekarza).grid(row=i,column=3)
            tk.Label(self.frame, text = id_pacjenta).grid(row=i,column=4)
            tk.Label(self.frame, text = teleporada).grid(row=i,column=5)
            i+=1

            
        tk.Button(self.frame, text = 'Dodaj wizyte', command = add_visit_view).grid(row=200,column=1)
        tk.Button(self.frame, text = 'Usun wizyte',command = delete_visit_view).grid(row=201,column=1)
        tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=202,column=1)

    def create_referrals_view(self):
        
        self.clear_screen()
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute('SELECT * FROM skierowanie')
        s_list = c.fetchall()
        i = 1
        tk.Label(self.frame, text = 'ID skierowania').grid(row=0,column=0, sticky='W')
        tk.Label(self.frame, text = 'ID lekarza').grid(row=0,column=1, sticky='W')
        tk.Label(self.frame, text = 'ID pacjenta').grid(row=0,column=2, sticky='W')
        tk.Label(self.frame, text = 'Typ choroby').grid(row=0,column=3, sticky='W')
        tk.Label(self.frame, text = 'Wykorzystane').grid(row=0,column=4, sticky='W')
        for row in s_list:
            id_skierowania = row[0]
            id_lekarza = row[1]
            id_pacjenta = row[2]
            typ_choroby = row[3]
            wykorzystane = row[4]

            tk.Label(self.frame, text = id_skierowania).grid(row=i,column=0)
            tk.Label(self.frame, text = id_lekarza).grid(row=i,column=1)
            tk.Label(self.frame, text = id_pacjenta).grid(row=i,column=2)
            tk.Label(self.frame, text = typ_choroby).grid(row=i,column=3)
            tk.Label(self.frame, text = wykorzystane).grid(row=i,column=4)
            i+=1
        tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=200,column=1)
        

    def create_tests_admin_view(self):
        
        self.clear_screen()
        self.root.geometry("700x500")
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute('SELECT * FROM badanie LEFT OUTER JOIN wynik w on badanie.id_badania=w.id_badania')
        b_list = c.fetchall()
        i = 1
        tk.Label(self.frame, text = 'ID badania').grid(row=0,column=0, sticky='W')
        tk.Label(self.frame, text = 'ID skierowania').grid(row=0,column=1, sticky='W')
        tk.Label(self.frame, text = 'Data').grid(row=0,column=2, sticky='W')
        tk.Label(self.frame, text = 'Typ choroby').grid(row=0,column=3, sticky='W')
        tk.Label(self.frame, text = 'ID pacjenta').grid(row=0,column=4, sticky='W')
        tk.Label(self.frame, text = 'ID wyniku').grid(row=0,column=5, sticky='W')
        tk.Label(self.frame, text = 'Wynik').grid(row=0,column=6, sticky='W')
        tk.Label(self.frame, text = 'Notatka').grid(row=0,column=7, sticky='W')
        for row in b_list:
            id_badania = row[0]
            id_skierowania = row[1]
            data = row[2]
            typ_choroby = row[3]
            id_pacjenta = row[4]
            id_wyniku = row[5]
            wynik = row[7]
            note = row[8]
           
            tk.Label(self.frame, text = id_badania).grid(row=i,column=0)
            tk.Label(self.frame, text = id_skierowania).grid(row=i,column=1)
            tk.Label(self.frame, text = data).grid(row=i,column=2)
            tk.Label(self.frame, text = typ_choroby).grid(row=i,column=3)
            tk.Label(self.frame, text = id_pacjenta).grid(row=i,column=4)
            tk.Label(self.frame, text = id_wyniku).grid(row=i,column=5)
            tk.Label(self.frame, text = wynik).grid(row=i,column=6)
            tk.Label(self.frame, text = note).grid(row=i,column=7)
            
            i+=1
        tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=200,column=1)        

    def create_vaccines_view(self):
        
        self.clear_screen()
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute('SELECT * FROM szczepienie join user p on szczepienie.id_pacjenta = p.id_usera')
        s_list = c.fetchall()
        i = 1
        tk.Label(self.frame, text = 'ID szczepienia').grid(row=0,column=0, sticky='W')
        tk.Label(self.frame, text = 'Typ choroby').grid(row=0,column=1, sticky='W')
        tk.Label(self.frame, text = 'Data').grid(row=0,column=2, sticky='W')
        tk.Label(self.frame, text = 'ID pacjenta').grid(row=0,column=3, sticky='W')
        tk.Label(self.frame, text = 'Imie i nazwisko').grid(row=0,column=4, sticky='W')

        for row in s_list:
            id_szczepienia = row[0]
            typ_choroby = row[1]
            data = row[2]
            id_pacjenta = row[3]
            pacjent = f'{row[5]} {row[6]}'

            tk.Label(self.frame, text = id_szczepienia).grid(row=i,column=0, sticky='W')
            tk.Label(self.frame, text = choroby[typ_choroby]).grid(row=i,column=1, sticky='W')
            tk.Label(self.frame, text = data).grid(row=i,column=2, sticky='W')
            tk.Label(self.frame, text = id_pacjenta).grid(row=i,column=3, sticky='W')
            tk.Label(self.frame, text = pacjent).grid(row=i,column=4, sticky='W')

            
            i+=1
        tk.Button(self.frame, text = 'Powrot',command = self.create_admin_main_view).grid(row=200,column=1)

    def create_vaccines_doc_view(self):
        
        self.clear_screen()
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute('SELECT * FROM szczepienie join user p on szczepienie.id_pacjenta = p.id_usera')
        s_list = c.fetchall()
        i = 1
        tk.Label(self.frame, text = 'ID szczepienia').grid(row=0,column=0, sticky='W')
        tk.Label(self.frame, text = 'Typ choroby').grid(row=0,column=1, sticky='W')
        tk.Label(self.frame, text = 'Data').grid(row=0,column=2, sticky='W')
        tk.Label(self.frame, text = 'ID pacjenta').grid(row=0,column=3, sticky='W')
        tk.Label(self.frame, text = 'Imie i nazwisko').grid(row=0,column=4, sticky='W')

        for row in s_list:
            id_szczepienia = row[0]
            typ_choroby = row[1]
            data = row[2]
            id_pacjenta = row[3]
            pacjent = f'{row[5]} {row[6]}'
        
            tk.Label(self.frame, text = id_szczepienia).grid(row=i,column=0, sticky='W')
            tk.Label(self.frame, text = choroby[typ_choroby]).grid(row=i,column=1, sticky='W')
            tk.Label(self.frame, text = data).grid(row=i,column=2, sticky='W')
            tk.Label(self.frame, text = id_pacjenta).grid(row=i,column=3, sticky='W')
            tk.Label(self.frame, text = pacjent).grid(row=i,column=4, sticky='W')

            i+=1
            
        tk.Button(self.frame, text = 'Powrot',command = self.create_doc_main_view).grid(row=200,column=1)
        

class Wizyta:

    
    def __init__(self):

        
        self.id_wizyty = None
        self.data = None
        self.zajeta = 0
        self.id_lekarza = None
        self.id_pacjenta = None
        self.is_online = None


    def update_visit(self, id_wizyty, id_pacjenta):

        self.id_wizyty = id_wizyty
        self.id_pacjenta = id_pacjenta

        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute(f'UPDATE wizyta SET id_pacjenta = :id_pac, zajeta = 1 WHERE id_wizyty = :id_wiz', {'id_pac':self.id_pacjenta,'id_wiz':self.id_wizyty})
        conn.commit()
        conn.close()

    def cancel_visit(self,id_wizyty):
        
        self.id_wizyty = id_wizyty
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute(f'UPDATE wizyta SET id_pacjenta = null, zajeta = 0 WHERE id_wizyty = :id_wiz', {'id_wiz':self.id_wizyty})
        conn.commit()
        conn.close()
   

class Badanie:

    
    def __init__(self,id_skierowania, id_pacjenta, typ_choroby):

        
        self.id_badania = None
        self.id_skierowania = id_skierowania
        self.data = None
        self.typ_choroby = typ_choroby
        self.id_pacjenta = id_pacjenta

        
    def post_test_pat(self):

        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute(f'INSERT INTO badanie VALUES(null,:id_skier,null,:typ_chor,:id_pac)', {'id_skier':self.id_skierowania,'typ_chor':self.typ_choroby, 'id_pac':self.id_pacjenta})
        conn.commit()
        c.execute(f'UPDATE skierowanie SET wykorzystane = 1 WHERE id_skierowania = :id_skier', {'id_skier':self.id_skierowania})
        conn.commit()
        conn.close()


class Wynik:

    
    def __init__(self):

        
        self.id_badania = None
        self.result = None
        self.note = None
        self.date = None

        

    def post_result(self,id_badania, result, date, note):

        
        self.id_badania = id_badania
        self.result = result
        self.note = note
        self.date = date
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute(f'INSERT INTO wynik VALUES(null, :id_bad, :result, :note)', {'id_bad':self.id_badania, 'result':self.result, 'note':self.note})
        conn.commit()
        c.execute(f'UPDATE badanie SET data = :data WHERE id_badania = :id_bad', {'id_bad':self.id_badania, 'data':self.date})
        conn.commit()
        conn.close()


class Szczepienie:

    
    def __init__(self,typ_choroby, data, id_pacjenta):

        
        self.id_szczepienia = None
        self.typ_choroby = typ_choroby
        self.data = data
        self.id_pacjenta = id_pacjenta
        

    def post_szczepienie(self, typ_choroby, data, id_pacjenta):
        
        conn = sqlite3.connect('bazaprzychodni.db')
        c = conn.cursor()
        c.execute(f'INSERT INTO szczepienie VALUES(null, :typ_choroby, :data, :id_pacjenta)', {'typ_choroby':self.typ_choroby, 'data':self.data,'id_pacjenta':self.id_pacjenta})
        conn.commit()
        conn.close()
    
        
def main():
    
    przychodnia = Przychodnia()

main()
            

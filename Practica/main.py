from tkinter import *
from tkinter import ttk
import datetime
import calendar

class Date(ttk.Frame):
    __altoFrame=532
    __anchoFrame=422-40-20
    
    def __init__(self,parent,activeYear, activeMonth, pastMonth, nextMonth, **args):
       
        ttk.Frame.__init__(self, parent)
                 
        self.activeYear=activeYear
        self.activeMonth=activeMonth
        self.pastMonth=pastMonth
        self.nextMonth=nextMonth
        
        #Dimensiones celdillas días
        self.height=61
        self.width=76
        
        #Frame para situar los 42 días
        self.dias=ttk.Frame(parent, height=self.__altoFrame,width=self.__anchoFrame).place(x=0,y=60)
            
                
        cal=calendar.Calendar()
        
        
        #Saco la lista de los días del mes actual, del mes anterior y del mes siguiente
        self.lista_intermonthdays=[]
        for x in cal.itermonthdays(self.activeYear, self.activeMonth):
            self.lista_intermonthdays.append(x)
                    
        self.lista_mesanterior=[]
        for x in cal.itermonthdays(self.activeYear, self.pastMonth):
            if x!=0:
                self.lista_mesanterior.append(x)
        
        self.lista_messiguiente=[]
        for x in cal.itermonthdays(self.activeYear, self.nextMonth):
            if x!=0:
                self.lista_messiguiente.append(x)
                
        #Obtengo la posición del primer día del mes actual y del mes siguiente
        self.pos_primerdia_mesact=datetime.date(self.activeYear, self.activeMonth, 1).isoweekday()
        self.pos_primerdia_messig=datetime.date(self.activeYear, self.nextMonth, 1).isoweekday()
        
        
        #Genero una tupla de tamaño 42 que guarda cada día del mes rellenando con 0 las posiciones vacías
        self.dates=[]
        for i in range(0,42):
            self.dates.append(self.indice(self.lista_intermonthdays,i))
            if self.indice(self.lista_intermonthdays,i)==None:
                self.dates.append(0)
                   
        #Relleno la lista self.dates con los días del mes anterior
        for indice in range(0,self.pos_primerdia_mesact) :
            self.dates[self.pos_primerdia_mesact-indice-2]=self.indice(self.lista_mesanterior,len(self.lista_mesanterior)-indice-1)
                  
        
        #Relleno la lista self.dates con los días del mes siguiente 
        if (len(self.lista_intermonthdays)==35 and self.pos_primerdia_messig!=1) or len(self.lista_intermonthdays)==42:
            for indice in range(0,len(self.dates)-len(self.lista_intermonthdays)+7-self.pos_primerdia_messig+1):
                self.dates[len(self.dates)-indice-1]=self.indice(self.lista_messiguiente,len(self.dates)-len(self.lista_intermonthdays)+7-self.pos_primerdia_messig+1-indice-1)
        else:
             for indice in range(0,len(self.dates)-len(self.lista_intermonthdays)-self.pos_primerdia_messig+1):
                self.dates[len(self.dates)-indice-1]=self.indice(self.lista_messiguiente,len(self.dates)-len(self.lista_intermonthdays)+self.pos_primerdia_messig-1-indice-1)
                
    
    def indice(self,lista,indice):
        try:
            valor=lista[indice]
        except:
            valor=0
        return valor
    
   
class Month(ttk.Frame):
    __altoFrame=61
    __anchoFrame=532
    
    def __init__(self,parent,activeYear, activeMonth, pastMonth, nextMonth, **args ):
       
        ttk.Frame.__init__(self, parent)
        
        self.mes=ttk.Frame(parent, height=self.__altoFrame,width=self.__anchoFrame).place(x=0,y=40)
        
        self.activeYear=activeYear
        self.activeMonth=activeMonth
        self.pastMonth=pastMonth
        self.nextMonth=nextMonth
        
        self.date=Date(self, self.activeYear, self.activeMonth, self.pastMonth, self.nextMonth)
               
        #Saco por pantalla, fila por fila, las fechas del array set.dates de clase Date
        sumax=0       
        for i in range (0,7):
            self.label=ttk.Label(self.date.dias, text=self.indice(self.date.dates,i),background='white', font=('Arial', 12),anchor=SE,borderwidth=3,relief="groove")
            self.label.place(x=sumax,y=self.date.height,width=self.date.width, height=self.date.height)
            self.setActive(i)
            sumax+=self.date.width
              
        sumax=0
        for i in range(7,14):
            self.label=ttk.Label(self.date.dias, text=self.indice(self.date.dates,i),background='white', font=('Arial', 12),anchor=SE,borderwidth=3,relief="groove")
            self.label.place(x=sumax,y=2*self.date.height,width=self.date.width, height=self.date.height)
            self.setActive(i)
            sumax+=self.date.width
            
            
        sumax=0
        for i in range(14,21):
            self.label=ttk.Label(self.date.dias, text=self.indice(self.date.dates,i),background='white', font=('Arial', 12),anchor=SE,borderwidth=3,relief="groove")
            self.label.place(x=sumax,y=3*self.date.height,width=self.date.width, height=self.date.height)
            self.setActive(i)
            sumax+=self.date.width
            
        sumax=0
        for i in range(21,28):
            self.label=ttk.Label(self.date.dias, text=self.indice(self.date.dates,i),background='white', font=('Arial', 12),anchor=SE,borderwidth=3,relief="groove")
            self.label.place(x=sumax,y=4*self.date.height,width=self.date.width, height=self.date.height)
            self.setActive(i)
            sumax+=self.date.width
            
        sumax=0
        for i in range(28,35):
            self.label=ttk.Label(self.date.dias, text=self.indice(self.date.dates,i),background='white', font=('Arial', 12),anchor=SE,borderwidth=3,relief="groove")
            self.label.place(x=sumax,y=5*self.date.height,width=self.date.width, height=self.date.height)
            self.setActive(i)
            sumax+=self.date.width
            
        sumax=0
        for i in range(35,42):
            self.label=ttk.Label(self.date.dias, text=self.indice(self.date.dates,i),background='white', font=('Arial', 12),anchor=SE,borderwidth=3,relief="groove")
            self.label.place(x=sumax,y=6*self.date.height,width=self.date.width, height=self.date.height)
            self.setActive(i)            
            sumax+=self.date.width      
            
    

    def indice(self,lista,indice):
        try:
            valor=lista[indice]
        except:
            valor=0
        return valor  
    
        
            
    def setActive(self,i):
        daysFinSem=(5,6,12,13,19,20,26,27,33,34,40,41)
        
        if i in range(0,42):
            if i in daysFinSem:
                self.label.configure(foreground='#FF6157')
        if i in range(0,self.date.pos_primerdia_mesact-1):               
            self.label.configure(foreground='#C2C2C2')
            
        if len(self.date.lista_intermonthdays)==35 and self.date.pos_primerdia_messig!=1:
            if i in range(35,42):
                self.label.configure(foreground='#C2C2C2')
            if i in range(28+self.date.pos_primerdia_messig-1,35):
                self.label.configure(foreground='#C2C2C2')
        if len(self.date.lista_intermonthdays)==35 and self.date.pos_primerdia_messig==1:
            if i in range(35,42):
                self.label.configure(foreground='#C2C2C2')
           
        if len(self.date.lista_intermonthdays)==42:
            if i in range(35+self.date.pos_primerdia_messig-1,42):
                self.label.configure(foreground='#C2C2C2')
      
                
       
class Calendar(ttk.Frame):
    __altoFrameDay=22
    __anchoFrameDay=532
    __altoFrameHead=422
    __anchoFrameHead=532
    
    __diaSem=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'] 
    __meses={1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre',13:'Hola'}
    
    def __init__(self,parent, **args):
        
               
        ttk.Frame.__init__(self, parent)
                
        #Dos Frames para todo el calendario (header) y para los días de la semana(dayName)
        self.header=ttk.Frame(parent,height=self.__altoFrameHead, width=self.__anchoFrameHead).place(x=0,y=0)
        self.dayName=ttk.Frame(parent, height=self.__altoFrameDay, width=self.__anchoFrameDay).place(x=0,y=38)
        
        self.lblFrame=ttk.Label(self.header, background='white').pack(fill=BOTH, expand=1)
        
        self.activeYear=datetime.date.today().year
        self.__activeYearstr=str(datetime.date.today().year)
        self.activeMonth=datetime.date.today().month
        self.__activeMonthstr=str(datetime.date.today().month)
        
        #Variable de control
        self.__fecha = StringVar()
        
        #Obtener las etiquetas de los días de la semana
        sumax=0
        for day in self.__diaSem:
            ttk.Label(self.dayName, text=day, font=('Arial', 8),anchor='center',borderwidth=3,relief="groove", background='white').place(x=sumax,y=38,height=20,width=76)
            sumax+=76
        
                
        #Obtener el nombre del mes actual (datetime.date.today) por pantalla
        for mes in self.__meses:
            if self.activeMonth==mes:
                self.__nameactiveMonth=str(self.__meses[mes])
        self.__fecha.set(self.__nameactiveMonth+' '+str(self.activeYear))
        
        
        #HEADER
        self.backYear=ttk.Button(self.header, text='<<',command=self.backYear).place(x=24,y=5,height=30, width=51)
        self.backMonth=ttk.Button(self.header, text='<',command=self.backMonth).place(x=83,y=5,height=30, width=51)
        self.lblMonth=ttk.Label(self.header, textvariable=self.__fecha).place(y=5,relx=0.4, anchor=NW)
        self.advMonth=ttk.Button(self.header, text='>',command=self.advMonth).place(x=398,y=5,height=30, width=51)
        self.advYear=ttk.Button(self.header, text='>>',command=self.advYear).place(x=457,y=5,height=30, width=51)
       
        
        
        if self.activeMonth==1:
            self.pastMonth=12
        else:
            self.pastMonth=self.activeMonth-1
        
        if self.activeMonth==12:
            self.nextMonth=1
        else:
            self.nextMonth=self.activeMonth+1
        if self.pastMonth==0:
                self.pastMonth=12
                    
        if self.nextMonth==13:
            self.nextMonth=1
            
        self.lblMonth=ttk.Label(self.header, textvariable=self.__fecha, font=('Arial',12), background='white').place(y=5,relx=0.4, anchor=NW)
        
        self.month=Month(self,self.activeYear,self.activeMonth, self.pastMonth, self.nextMonth)
        
        
        
    #Acciones con los botones   
    def backMonth(self): #Retrocedo un mes
        
        for mes in self.__meses.keys():
            if self.activeMonth==1:
                self.pastMonth=12
            else:
                self.pastMonth=self.activeMonth-1
            self.__nameactiveMonth=str(self.__meses[self.pastMonth])            
            self.activeMonth=self.pastMonth
            self.pastMonth-=1 #
            
            if self.pastMonth==0:
                self.pastMonth=12
            
            self.nextMonth=self.activeMonth+1
            if self.nextMonth==13:
                self.nextMonth=1              
           
            self.__fecha.set(self.__nameactiveMonth+' '+str(self.activeYear))
            
        
        self.lblMonth=ttk.Label(self.header, textvariable=self.__fecha, font=('Arial',12), background='white').place(y=5,relx=0.4, anchor=NW)
        
        self.month=Month(self,self.activeYear,self.activeMonth, self.pastMonth, self.nextMonth)
        
    def advMonth(self):
        for mes in self.__meses.keys():
            if self.activeMonth==12:
                    self.nextMonth=1
            else:
                self.nextMonth=self.activeMonth+1
                self.__nameactiveMonth=str(self.__meses[self.nextMonth])
            
            self.activeMonth=self.nextMonth                
            self.nextMonth+=1#el nombre del año toma el valor del mes anterior
            
            if self.nextMonth==13:
                self.nextMonth=1
            
            self.pastMonth=self.activeMonth-1            
            if self.pastMonth==0:
                self.pastMonth=12
                
            self.__fecha.set(self.__nameactiveMonth+' '+str(self.activeYear))
        
        self.lblMonth=ttk.Label(self.header, textvariable=self.__fecha, font=('Arial',12), background='white').place(y=5,relx=0.4, anchor=NW)
        
        
        self.month=Month(self,self.activeYear,self.activeMonth, self.pastMonth, self.nextMonth)
 
    def backYear(self):
        self.pastYear=self.activeYear-1
        self.__fecha.set(self.__nameactiveMonth+' '+str(self.pastYear))
        self.lblMonth=ttk.Label(self.header, textvariable=self.__fecha).place(y=5,relx=0.4, anchor=NW)
        self.activeYear=self.pastYear
        
        self.lblMonth=ttk.Label(self.header, textvariable=self.__fecha, font=('Arial',12), background='white').place(y=5,relx=0.4, anchor=NW)
        
        self.month=Month(self,self.activeYear,self.activeMonth, self.pastMonth, self.nextMonth)
      
    def advYear(self):
        self.nextYear=self.activeYear+1
        self.__fecha.set(self.__nameactiveMonth+' '+str(self.nextYear))
        self.lblMonth=ttk.Label(self.header, textvariable=self.__fecha).place(y=5,relx=0.4, anchor=NW)
        self.activeYear=self.nextYear
        
        
        self.lblMonth=ttk.Label(self.header, textvariable=self.__fecha, font=('Arial',12), background='white').place(y=5,relx=0.4, anchor=NW)
        
        self.month=Month(self,self.activeYear,self.activeMonth, self.pastMonth, self.nextMonth)
       
    
class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario Universal")
        self.geometry("532x422")
        self.config(background="white")
        self.resizable(0,0)
                    
        calendario=Calendar(self)
        
    def start(self):
        self.mainloop()
    
if __name__ == '__main__':
  calendario = MainApp()
  calendario.start()
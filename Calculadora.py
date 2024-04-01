#Nombre:Calculadora
#Autor:Álvaro Villar Val
#Fecha:26/03/24
#Versión:0.0.9
#Descripción: Calculadora de los diferentes criterios de calidad de la central meteorologica
#########################################################################################################################
#Definimos los imports
from pysolar.solar import *
import datetime
import math  

class Calculadora:
    #GHI:	global horizontal irradiance.GHI:	global horizontal irradiance.GHI:	global horizontal irradiance.
    #Physical limits
    dni0=1361.1 #W/m2
    dnil0=133334 #lux
    dnp0=531.81 #W/m2
    dnuv0=102.15 #W/m2
    ghiclear=0 #TODO encontrar ghi clear
    dniclear=0 #TODO encontrar dni clear
    latitude=42.3515619402223
    longitude=-3.6879829504876676
    m=1#TODO encontrar relative optical air mass 
    def dates(self,fecha):
        año=int(str(fecha)[0:4])
        mes=int(str(fecha)[5:7])
        dia=int(str(fecha)[8:10])
        hora=int(str(fecha)[11:13])+1
        minuto=int(str(fecha)[14:16])
        return datetime.datetime(año, mes, dia, hora, minuto, tzinfo=datetime.timezone.utc)
    

    def ghiPhys(self,value,fecha):
        date = self.dates(fecha)
        altitude=math.cos(get_altitude(self.latitude, self.longitude, date))
        print(altitude)
        if altitude<0:
            return 0
        max=self.dni0*1.5*(altitude**1.2)+100
        print(max)
        if value>-4 and value<=max:
             return 1
        elif value>-4:
            return 2
        else:
            return 3
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghiSky(self,value,fecha):
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado<85 and value<=self.ghiclear:
             return True
        else:
            return False

    #DHI:	diffuse horizontal irradiance.
    #Physical limits
    def dhiPhys(self,value,fecha):
        date = self.dates(fecha)
        max=self.dni0*0.95*(math.cos(get_altitude(self.latitude, self.longitude, date))**1.2)+50
        if value>-4 and value<=max:
             return True
        else:
            return False
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhiSky(self,value,fecha):
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado<85 and value<=self.ghiclear:
             return True
        else:
            return False
        
    #DNI:	direct normal irradiance.
    #Physical limits
    def dniPhys(self,value):
        if value>-4 and value<=self.dni0:
            return True
        else:
            return False
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dniSky(self,value,fecha):
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado<85 and value<=self.dniclear:
             return True
        else:
            return False
    #Coherence mesaurements de la irradiancia
    def coheI1(self,ghi,dhi,dni,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<75 and ghi>50:
            return False
        value=ghi/((dhi+dni*math.cos(angle) ) )
        if value>0.92 and value<1.08:
            return  True
        else:
            return False
        
    def coheI2(self,ghi,dhi,dni,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<93 and angle>75 and  ghi>50:
            return False
        value=ghi/((dhi+dni*math.cos(angle) ) )
        if value>0.85 and value<1.15:
            return  True
        else:
            return False    

    def coheI1(self,ghi,dhi,dni,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<75 and ghi>50:
            return False
        value=dhi/dni
        if value<1.1:
            return  True
        else:
            return False
            
    def coheI4(self,ghi,dhi,dni,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<93 and angle>75 and  ghi>50:
            return False
        value=dhi/dni
        if  value<1.05:
            return  True
        else:
            return False 
          
    #GHIL:	global horizontal illuminance.
    #Physical limits
    def ghilPhys(self,value,fecha):
        date = self.dates(fecha)
        max=self.dnil0*1.5*(math.cos(get_altitude(self.latitude, self.longitude, date))**1.2)+10000
        if value>0 and value<=max:
             return True
        else:
            return False
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghilSky(self,latitud,longitud,fecha):
        return 0
 
    #DHIL:	diffuse horizontal illuminance.
    #Physical limits
    def dhilPhys(self,value,fecha):
        date = self.dates(fecha)
        max=self.dnil0*0.95*(math.cos(get_altitude(self.latitude, self.longitude, date))**1.2)+5000
        if value>0 and value<=max:
             return True
        else:
            return False
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhilSky(self,latitud,longitud,fecha):
        return 0

    #DNIL:	direct normal illuminance.
    #Physical limits
    def dnilPhys(self,value):
        if value>-0 and value<=self.dnil0:
            return True
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnilSky(self,latitud,longitud,fecha):
        return 0
 

    
    #GHP:	global horizontal PAR irradiance.
    #Physical limits
    def ghpPhys(self,value,fecha):
        date = self.dates(fecha)
        max=self.dnp0*1.5*(math.cos(get_altitude(self.latitude, self.longitude, date))**1.2)+40
        if value>-0 and value<=max:
             return True
        else:
            return False
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghpSky(self,value,fecha):
        max=(46.5325*self.m**2-1738.11*self.m+48907.2)/(4.78443*self.m**2+89.17*self.m+1)
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado<85 and value<=max:
             return True
        else:
            return False

    #DHP:	diffuse horizontal PAR irradiance.
    #Physical limits
    def dhpPhys(self,value,fecha):
        date = self.dates(fecha)
        max=self.dnp0*0.95*(math.cos(get_altitude(self.latitude, self.longitude, date))**1.2)+20
        if value>-0 and value<=max:
             return True
        else:
            return False
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhpSky(self,latitud,longitud,fecha):
        value=(-0.489631*self.m**2+17.4211*self.m+51.858)/(0.0575636*self.m**2+0.671139*self.m+1)
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado<85 and value<=max:
             return True
        else:
            return False

    #DNP:	direct normal PAR irradiance.
    #Physical limits
    def dnpPhys(self,value):
        if value>-0 and value<=self.dnp0:
            return True
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnpSky(self,value,fecha):
        max=(0.171991*self.m**2-9.88174*self.m+532.694)/(0.00732718*self.m**2+0.13576*self.m+1)
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado<85 and value<=max:
             return True
        else:
            return False

  
    #GHUV:	global horizontal UV irradiance.
    #Physical limits
    def ghuvPhys(self,value,fecha):
        date = self.dates(fecha)
        max=self.dnuv0*1.5*(math.cos(get_altitude(self.latitude, self.longitude, date))**1.2)+5
        if value>-0 and value<=max:
             return True
        else:
            return False
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghuvSky(self,value,fecha):
        max=(1.78513*self.m^2+177.076*self.m+2594.06)/(13.8072*self.m**2+25.6894*self.m+1)
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado<85 and value<=max:
             return True
        else:
            return False

    #DHUV:	diffuse horizontal UV irradiance.
    #Physical limits
    def dhuvPhys(self,value,fecha):
        date = self.dates(fecha)
        max=self.dnuv0*0.95*(math.cos(get_altitude(self.latitude, self.longitude, date))**1.2)+2
        if value>-0 and value<=max:
             return True
        else:
            return False
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhuvSky(self,value,fecha):
        max=(0.0284353*self.m**2-0.773392*self.m+34.2974)/(0.0393782*self.m**2+0.593745*self.m+1)
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado<85 and value<=max:
             return True
        else:
            return False
    #Coherence between measurements 

    #DNUV:	direct normal UV irradiance.
    #Physical limits
    def dnuvPhys(self,value):
        if value>-0 and value<=self.dnuv0:
            return True
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnuvSky(self,value,fecha):
        max=(0.613588*self.m**2-14.0356*self.m+88.664)/(0.0966512*self.m**2+0.474748*self.m+1)
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado<85 and value<=max:
             return True
        else:
            return False
    #Coherence between measurements 

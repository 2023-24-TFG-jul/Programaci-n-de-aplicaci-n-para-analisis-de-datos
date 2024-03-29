#Nombre:Calculadora
#Autor:Álvaro Villar Val
#Fecha:26/03/24
#Versión:0.0.6
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
    def dates(self,fecha):
        año=str(fecha)[0:4]
        mes=str(fecha)[5:7]
        dia=str(fecha)[8:10]
        hora=str(fecha)[11:13]
        minuto=str(fecha)[14:16]
        return datetime.datetime(año, mes, dia, hora, minuto, tzinfo=datetime.timezone.utc)
    

    def ghiPhys(self,value,fecha):
        date = self.dates(fecha)
        max=self.dni0*1.5*(math.cos(get_altitude(self.latitude, self.longitude, date))**1.2)+100
        if value>-4 and value<=max:
             return True
        else:
            return False
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghiSky(self,value,fecha):
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado<85 and value<=self.ghiclear:
             return True
        else:
            return False
    #Coherence between measurements 
    def ghiCohe(self,latitud,longitud,fecha):
        return 0
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
    #Coherence between measurements 
    def dhiCohe(self,latitud,longitud,fecha):
        return 0
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
    #Coherence between measurements 
    def dniCohe(self,latitud,longitud,fecha):
        return 0
    

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
    #Coherence between measurements 
    def ghilCohe(self,latitud,longitud,fecha):
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
    #Coherence between measurements 
    def dhilCohe(self,latitud,longitud,fecha):
        return 0
    #DNIL:	direct normal illuminance.
    #Physical limits
    def dnilPhys(self,value):
        if value>-0 and value<=self.dnil0:
            return True
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnilSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def dnilCohe(self,latitud,longitud,fecha):
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
    def ghpSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def ghpCohe(self,latitud,longitud,fecha):
        return 0
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
        return 0
    #Coherence between measurements 
    def dhpCohe(self,latitud,longitud,fecha):
        return 0
    #DNP:	direct normal PAR irradiance.
    #Physical limits
    def dnpPhys(self,value):
        if value>-0 and value<=self.dnp0:
            return True
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnpSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def dnpCohe(self,latitud,longitud,fecha):
        return 0
  
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
    def ghuvSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def ghuvCohe(self,latitud,longitud,fecha):
        return 0
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
    def dhuvSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def dhuvCohe(self,latitud,longitud,fecha):
        return 0
    #DNUV:	direct normal UV irradiance.
    #Physical limits
    def dnuvPhys(self,value):
        if value>-0 and value<=self.dnuv0:
            return True
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnuvSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def dnuvCohe(self,latitud,longitud,fecha):
        return 0
    
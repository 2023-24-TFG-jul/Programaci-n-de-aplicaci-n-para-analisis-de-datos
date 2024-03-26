#Nombre:Calculadora
#Autor:Álvaro Villar Val
#Fecha:26/03/24
#Versión:0.0.3
#Descripción: Calculadora de los diferentes criterios de calidad de la central meteorologica
#########################################################################################################################
#Definimos los imports
from pysolar.solar import *
import datetime

class Calculadora:
    #GHI:	global horizontal irradiance.GHI:	global horizontal irradiance.GHI:	global horizontal irradiance.
    #Physical limits
    def ghiPhys(self,latitud,longitud,fecha):
        return 0
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghiSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def ghiCohe(self,latitud,longitud,fecha):
        return 0
    #DHI:	diffuse horizontal irradiance.
    #Physical limits
    def dhiPhys(self,latitud,longitud,fecha):
        return 0
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhiSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def dhiCohe(self,latitud,longitud,fecha):
        return 0
    #DNI:	direct normal irradiance.
    #Physical limits
    def dniPhys(self,latitud,longitud,fecha):
        return 0
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dniSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def dniCohe(self,latitud,longitud,fecha):
        return 0
    

    #GHIL:	global horizontal illuminance.
    #Physical limits
    def ghilPhys(self,latitud,longitud,fecha):
        return 0
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghilSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def ghilCohe(self,latitud,longitud,fecha):
        return 0
    #DHIL:	diffuse horizontal illuminance.
    #Physical limits
    def dhilPhys(self,latitud,longitud,fecha):
        return 0
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhilSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def dhilCohe(self,latitud,longitud,fecha):
        return 0
    #DNIL:	direct normal illuminance.
    #Physical limits
    def dnilPhys(self,latitud,longitud,fecha):
        return 0
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnilSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def dnilCohe(self,latitud,longitud,fecha):
        return 0
    
    #GHP:	global horizontal PAR irradiance.
    #Physical limits
    def ghpPhys(self,latitud,longitud,fecha):
        return 0
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghpSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def ghpCohe(self,latitud,longitud,fecha):
        return 0
    #DHP:	diffuse horizontal PAR irradiance.
    #Physical limits
    def dhpPhys(self,latitud,longitud,fecha):
        return 0
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhpSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def dhpCohe(self,latitud,longitud,fecha):
        return 0
    #DNP:	direct normal PAR irradiance.
    #Physical limits
    def dnpPhys(self,latitud,longitud,fecha):
        return 0
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnpSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def dnpCohe(self,latitud,longitud,fecha):
        return 0
  
    #GHUV:	global horizontal UV irradiance.
    #Physical limits
    def ghuvPhys(self,latitud,longitud,fecha):
        return 0
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghuvSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def ghuvCohe(self,latitud,longitud,fecha):
        return 0
    #DHUV:	diffuse horizontal UV irradiance.
    #Physical limits
    def dhuvPhys(self,latitud,longitud,fecha):
        return 0
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhuvSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def dhuvCohe(self,latitud,longitud,fecha):
        return 0
    #DNUV:	direct normal UV irradiance.
    #Physical limits
    def dnuvPhys(self,latitud,longitud,fecha):
        return 0
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnuvSky(self,latitud,longitud,fecha):
        return 0
    #Coherence between measurements 
    def dnuvCohe(self,latitud,longitud,fecha):
        return 0
    
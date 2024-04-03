#Nombre:Calculadora
#Autor:Álvaro Villar Val
#Fecha:26/03/24
#Versión:0.1.3
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
    
    def comprobarghi(self,valueGhi,valueDHi,valueDNi,fecha):
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado<0:
            return 0
        else:
            resultado=self.ghiPhys(valueGhi,grado)
            if resultado==1:
                if self.ghiSky(valueGhi,grado):
                    if grado<75:
                        if self.coheI1(valueGhi,valueDHi,valueDNi,grado):
                            if self.coheI3(valueGhi,valueDHi):
                                return 1
                            else:
                                return 6
                        else:
                            return 5
                    elif grado<93:
                            if self.coheI2(valueGhi,valueDHi,valueDNi,grado):
                                if self.coheI4(valueGhi,valueDHi):
                                    return 1
                                else:
                                    return 6
                            else:
                                return 5
                    else:
                        return 0
                else:
                    return 4
                    
            else:
                return resultado
            
    
    def ghiPhys(self,value,altitude):
       
        max=self.dni0*1.5*(altitude**1.2)+100
        if value>-4 and value<=max:
             return 1
        elif value>-4:
            return 2
        else:
            return 3
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghiSky(self,value,grado):
        if grado<85 and value<=self.ghiclear:
             return True
        else:
            return False

    #DHI:	diffuse horizontal irradiance.
    def comprobardhi(self,valueGhi,valueDHi,valueDNi,fecha):
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado<0:
            return 0
        else:
            resultado=self.dhiPhys(valueDHi,grado)
            if resultado==1:
                if self.dhiSky(valueDHi,grado):
                    if grado<75:
                        if self.coheI1(valueGhi,valueDHi,valueDNi,grado):
                            if self.coheI3(valueGhi,valueDHi):
                                return 1
                            else:
                                return 6
                        else:
                            return 5
                    elif grado<93:
                            if self.coheI2(valueGhi,valueDHi,valueDNi,grado):
                                if self.coheI4(valueGhi,valueDHi):
                                    return 1
                                else:
                                    return 6
                            else:
                                return 5
                    else:
                        return 0
                else:
                    return 4
                    
            else:
                return resultado
    #Physical limits
    def dhiPhys(self,value,grado):
        max=self.dni0*0.95*(math.cos(grado)**1.2)+50
        if value>-4:
            if value<=max:
             return 1
            else:
                return 3
        else:
            return 2
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhiSky(self,value,grado):
        if grado<85 and value<=self.ghiclear:
             return True
        else:
            return False
        
    #DNI:	direct normal irradiance.
    def comprobardni(self,valueGhi,valueDHi,valueDNi,fecha):
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado<0:
            return 0
        else:
            resultado=self.dniPhys(valueDNi)
            if resultado==1:
                if self.dniSky(valueDNi,grado):
                    if grado<75:
                        if self.coheI1(valueGhi,valueDHi,valueDNi,grado):
                            if self.coheI3(valueGhi,valueDHi):
                                return 1
                            else:
                                return 6
                        else:
                            return 5
                    elif grado<93:
                            if self.coheI2(valueGhi,valueDHi,valueDNi,grado):
                                if self.coheI4(valueGhi,valueDHi):
                                    return 1
                                else:
                                    return 6
                            else:
                                return 5
                    else:
                        return 0
                else:
                    return 4
                    
            else:
                return resultado
    #Physical limits
    def dniPhys(self,value):
        if value>-4:
            if value<=self.dni0:
                return 1
            else:
                return 3
        else:
            return 2
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dniSky(self,value,grado):
        if grado<85 and value<=self.dniclear:
             return True
        else:
            return False
    #Coherence mesaurements de la irradiancia
    def coheI1(self,ghi,dhi,dni,angle):
        value=ghi/((dhi+dni*math.cos(angle) ) )
        if value>0.92 and value<1.08:
            return  True
        else:
            return False
        
    def coheI2(self,ghi,dhi,dni,angle):
        value=ghi/((dhi+dni*math.cos(angle) ) )
        if value>0.85 and value<1.15:
            return  True
        else:
            return False    

    def coheI3(self,ghi,dhi):
        value=dhi/ghi
        if value<1.05:
            return  True
        else:
            return False
            
    def coheI4(self,ghi,dhi):
        value=dhi/ghi
        if  value<1.1:
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
 
    #coherence between measurements of the illuminance
    def coheIl1(self,ghil,dhil,dnil,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<75 and ghil>5000:
            return False
        value=ghil/((dhil+dnil*math.cos(angle) ) )
        if value>0.92 and value<1.08:
            return  True
        else:
            return False
        
    def coheIl2(self,ghil,dhil,dnil,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<93 and angle>75 and  ghil>5000:
            return False
        value=ghil/((dhil+dnil*math.cos(angle) ) )
        if value>0.85 and value<1.15:
            return  True
        else:
            return False    

    def coheIl3(self,ghil,dhil,dnil,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<75 and ghil>5000:
            return False
        value=dhil/ghil
        if value<1.05:
            return  True
        else:
            return False
            
    def coheIl4(self,ghil,dhil,dnil,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<93 and angle>75 and  ghil>5000:
            return False
        value=dhil/ghil
        if  value<1.1:
            return  True
        else:
            return False 
    
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

    #coherence between measurements of the PAR irradiance
    def coheP1(self,ghp,dhp,dnp,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<75 and ghp>20:
            return False
        value=ghp/((dhp+dnp*math.cos(angle) ) )
        if value>0.92 and value<1.08:
            return  True
        else:
            return False
        
    def coheP2(self,ghp,dhp,dnp,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<93 and angle>75 and  ghp>20:
            return False
        value=ghp/((dhp+dnp*math.cos(angle) ) )
        if value>0.85 and value<1.15:
            return  True
        else:
            return False    

    def coheP3(self,ghp,dhp,dnp,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<75 and ghp>20:
            return False
        value=dhp/ghp
        if value<1.05:
            return  True
        else:
            return False
            
    def coheP4(self,ghp,dhp,dnp,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<93 and angle>75 and  ghp>20:
            return False
        value=dhp/ghp
        if  value<1.1:
            return  True
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
        
    #coherence between measurements of the UV irradiance
    def coheUv1(self,ghuv,dhuv,dnuv,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<75 and ghuv>2:
            return False
        value=ghuv/((dhuv+dnuv*math.cos(angle) ) )
        if value>0.92 and value<1.08:
            return  True
        else:
            return False
        
    def coheUv2(self,ghuv,dhuv,dnuv,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<93 and angle>75 and  ghuv>20:
            return False
        value=ghuv/((dhuv+dnuv*math.cos(angle) ) )
        if value>0.85 and value<1.15:
            return  True
        else:
            return False    

    def coheUv3(self,ghuv,dhuv,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<75 and ghuv>20:
            return False
        value=dhuv/ghuv
        if value<1.05:
            return  True
        else:
            return False
            
    def coheUv4(self,ghuv,dhuv,fecha):
        date = self.dates(fecha)
        angle=get_altitude(self.latitude, self.longitude, date)
        if angle<93 and angle>75 and  ghuv>20:
            return False
        value=dhuv/ghuv
        if  value<1.1:
            return  True
        else:
            return False 
          

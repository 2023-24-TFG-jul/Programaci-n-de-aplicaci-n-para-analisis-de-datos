#Nombre:Calculadora
#Autor:Álvaro Villar Val
#Fecha:26/03/24
#Versión:0.2.1
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
    
    def physGen1(self,value,altitude,numFin,dn0,numIni,min):
        max=dn0*numIni*(math.cos(altitude)**1.2)+numFin
        if value>-min and value<=max:
             return 1
        elif value>min:
            return 2
        else:
            return 3
        
    def physGen2(self,value,dn0,min):
        if value>min:
            if value<=dn0:
                return 1
            else:
                return 3
        else:
            return 2
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghiSky(self,value):
        if value<=self.ghiclear:
             return True
        else:
            return False
    def comprobar (self,valuePrin,funPhys,funSky,cohe1,cohe2,cohe3,cohe4,valueGH,valueDH,valueDN,fecha):
        date = self.dates(fecha)
        grado=get_altitude(self.latitude, self.longitude, date)
        if grado>85:
            return 0
        else:
            resultado=funPhys(valuePrin,grado)
            if resultado==1:
                if funSky(valuePrin):
                    if grado<75:
                        if cohe1(valueGH,valueDH,valueDN,grado):
                            if cohe3(valueGH,valueDH):
                                return 1
                            else:
                                return 6
                        else:
                            return 5
                    elif grado<93:
                            if cohe2(valueGH,valueDH,valueDN,grado):
                                if cohe4(valueGH,valueDH):
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
            
    def comprobarghi(self,valueGhi,valueDHi,valueDNi,fecha):
        return self.comprobar(valueGhi,self.ghiPhys,self.ghiSky,self.coheI1,self.coheI2,self.coheI3,self.coheI4,valueGhi,valueDHi,valueDNi,fecha)
            
    
    def ghiPhys(self,value,altitude):
       return self.physGen1(value,altitude,100,self.dni0,1.5,-4)
    
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghiSky(self,value):
        if value<=self.ghiclear:
             return True
        else:
            return False

    #DHI:	diffuse horizontal irradiance.
    def comprobardhi(self,valueGhi,valueDHi,valueDNi,fecha):
        return self.comprobar(valueDHi,self.dhiPhys,self.dhiSky,self.coheI1,self.coheI2,self.coheI3,self.coheI4,valueGhi,valueDHi,valueDNi,fecha)
    
    #Physical limits
    def dhiPhys(self,value,grado):
        return self.physGen1(value,grado,50,self.dni0,0.95,-4)
    
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhiSky(self,value):
        if value<=self.ghiclear:
             return True
        else:
            return False
        
    #DNI:	direct normal irradiance.
    def comprobardni(self,valueGhi,valueDHi,valueDNi,fecha):
        return self.comprobar(valueDNi,self.dniPhys,self.dniSky,self.coheI1,self.coheI2,self.coheI3,self.coheI4,valueGhi,valueDHi,valueDNi,fecha)
    
    #Physical limits
    def dniPhys(self,value):
        return self.physGen2(value,self.dni0,-4)
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dniSky(self,value):
        if value<=self.dniclear:
             return True
        else:
            return False
    #Coherence mesaurements de la irradiancia
    def coheI1(self,ghi,dhi,dni,angle):
        if ghi<50:
            return False
        value=ghi/((dhi+dni*math.cos(angle) ) )
        if value>0.92 and value<1.08:
            return  True
        else:
            return False
        
    def coheI2(self,ghi,dhi,dni,angle):
        if ghi<50:
            return False
        value=ghi/((dhi+dni*math.cos(angle) ) )
        if value>0.85 and value<1.15:
            return  True
        else:
            return False    

    def coheI3(self,ghi,dhi):
        if ghi<50:
            return False
        value=dhi/ghi
        if value<1.05:
            return  True
        else:
            return False
            
    def coheI4(self,ghi,dhi):
        if ghi<50:
            return False
        value=dhi/ghi
        if  value<1.1:
            return  True
        else:
            return False 
          
    #GHIL:	global horizontal illuminance.
    def comprobarghil(self,valueGhil,valueDHil,valueDNil,fecha):
        return self.comprobar(valueGhil,self.ghilPhys,self.ghilSky,self.coheIl1,self.coheIl2,self.coheIl3,self.coheIl4,valueGhil,valueDHil,valueDNil,fecha)
    
    #Physical limits
    def ghilPhys(self,value,grado):
        return self.physGen1(value,grado,10000,self.dnil0,1.5,0)
    
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghilSky(self,value):
        return True
 
    #DHIL:	diffuse horizontal illuminance.
    def comprobardhil(self,valueGhil,valueDHil,valueDNil,fecha):
        return self.comprobar(valueDHil,self.dhilPhys,self.dhilSky,self.coheIl1,self.coheIl2,self.coheIl3,self.coheIl4,valueGhil,valueDHil,valueDNil,fecha)
    
    #Physical limits
    def dhilPhys(self,value,grado):
        return self.physGen1(value,grado,5000,self.dnil0,0.95,0)
        
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhilSky(self,value):
        return True

    #DNIL:	direct normal illuminance.
    def comprobardnil(self,valueGhil,valueDHil,valueDNil,fecha):
        return self.comprobar(valueDNil,self.dnilPhys,self.dnilSky,self.coheIl1,self.coheIl2,self.coheIl3,self.coheIl4,valueGhil,valueDHil,valueDNil,fecha)
    
    #Physical limits
    def dnilPhys(self,value):
        return self.physGen2(value,self.dnil0,0)
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnilSky(self,value):
        return 0
 
    #coherence between measurements of the illuminance
    def coheIl1(self,ghil,dhil,dnil,angle):
        if ghil>5000:
            return False
        value=ghil/((dhil+dnil*math.cos(angle) ) )
        if value>0.92 and value<1.08:
            return  True
        else:
            return False
        
    def coheIl2(self,ghil,dhil,dnil,angle):
        if  ghil>5000:
            return False
        value=ghil/((dhil+dnil*math.cos(angle) ) )
        if value>0.85 and value<1.15:
            return  True
        else:
            return False    

    def coheIl3(self,ghil,dhil):
        
        
        if ghil>5000:
            return False
        value=dhil/ghil
        if value<1.05:
            return  True
        else:
            return False
            
    def coheIl4(self,ghil,dhil):
        if ghil>5000:
            return False
        value=dhil/ghil
        if  value<1.1:
            return  True
        else:
            return False 
    
    #GHP:	global horizontal PAR irradiance.
    def comprobarghp(self,valueGhp,valueDHp,valueDNp,fecha):
        return self.comprobar(valueGhp,self.ghpPhys,self.ghpSky,self.coheP1,self.coheP2,self.coheP3,self.coheP4,valueGhp,valueDHp,valueDNp,fecha)
            
    #Physical limits
    def ghpPhys(self,value,grado):
        return self.physGen1(value,grado,40,self.dnp0,1.5,0)
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghpSky(self,value):
        max=(46.5325*self.m**2-1738.11*self.m+48907.2)/(4.78443*self.m**2+89.17*self.m+1)
        if value<=max:
             return True
        else:
            return False

    #DHP:	diffuse horizontal PAR irradiance.
    def comprobardhp(self,valueGhp,valueDHp,valueDNp,fecha):
       return self.comprobar(valueDHp,self.dhpPhys,self.dhpSky,self.coheP1,self.coheP2,self.coheP3,self.coheP4,valueGhp,valueDHp,valueDNp,fecha)
    
    #Physical limits
    def dhpPhys(self,value,grado):
        return self.physGen1(value,grado,20,self.dnp0,0.95,0)
        
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhpSky(self,value):
        max=(-0.489631*self.m**2+17.4211*self.m+51.858)/(0.0575636*self.m**2+0.671139*self.m+1)
        if value<=max:
             return True
        else:
            return False

    #DNP:	direct normal PAR irradiance.
    def comprobardnp(self,valueGhp,valueDHp,valueDNp,fecha):
        return self.comprobar(valueDNp,self.dnpPhys,self.dnpSky,self.coheP1,self.coheP2,self.coheP3,self.coheP4,valueGhp,valueDHp,valueDNp,fecha)
    
    #Physical limits
    def dnpPhys(self,value):
        return self.physGen2(value,self.dnp0,0)
        
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnpSky(self,value):
        max=(0.171991*self.m**2-9.88174*self.m+532.694)/(0.00732718*self.m**2+0.13576*self.m+1)
       
        if value<=max:
             return True
        else:
            return False

    #coherence between measurements of the PAR irradiance
    def coheP1(self,ghp,dhp,dnp,angle):
        if ghp>20:
            return False
        value=ghp/((dhp+dnp*math.cos(angle) ) )
        if value>0.92 and value<1.08:
            return  True
        else:
            return False
        
    def coheP2(self,ghp,dhp,dnp,angle):
        if   ghp>20:
            return False
        value=ghp/((dhp+dnp*math.cos(angle) ) )
        if value>0.85 and value<1.15:
            return  True
        else:
            return False    

    def coheP3(self,ghp,dhp):
        if ghp>20:
            return False
        value=dhp/ghp
        if value<1.05:
            return  True
        else:
            return False
            
    def coheP4(self,ghp,dhp):
        if  ghp>20:
            return False
        value=dhp/ghp
        if  value<1.1:
            return  True
        else:
            return False 
          
  
    #GHUV:	global horizontal UV irradiance.
    
    def comprobarghuv(self,valueGhuv,valueDHuv,valueDNuv,fecha):
        return self.comprobar(valueGhuv,self.ghuvPhys,self.ghuvSky,self.coheUv1,self.coheUv2,self.coheUv3,self.coheUv4,valueGhuv,valueDHuv,valueDNuv,fecha)
    
    #Physical limits
    def ghuvPhys(self,value,grado):
        return self.physGen1(value,grado,5,self.dnuv0,1.5,0)
        
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghuvSky(self,value):
        max=(1.78513*self.m^2+177.076*self.m+2594.06)/(13.8072*self.m**2+25.6894*self.m+1)
        if  value<=max:
             return True
        else:
            return False

    #DHUV:	diffuse horizontal UV irradiance.
    def comprobardhuv(self,valueGhuv,valueDHuv,valueDNuv,fecha):
        return self.comprobar(valueDHuv,self.dhuvPhys,self.dhuvSky,self.coheUv1,self.coheUv2,self.coheUv3,self.coheUv4,valueGhuv,valueDHuv,valueDNuv,fecha)
    
    #Physical limits
    def dhuvPhys(self,value,grado):
        return self.physGen1(value,grado,2,self.dnuv0,0.95,0)
        
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhuvSky(self,value):
        max=(0.0284353*self.m**2-0.773392*self.m+34.2974)/(0.0393782*self.m**2+0.593745*self.m+1)
        if value<=max:
             return True
        else:
            return False
    

    #DNUV:	direct normal UV irradiance.+
    def comprobardnuv(self,valueGhuv,valueDHuv,valueDNuv,fecha):
        return self.comprobar(valueDNuv,self.dnuvPhys,self.dnuvSky,self.coheUv1,self.coheUv2,self.coheUv3,self.coheUv4,valueGhuv,valueDHuv,valueDNuv,fecha)
    
    #Physical limits
    def dnuvPhys(self,value):
        return self.physGen2(value,self.dnuv0,0)
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnuvSky(self,value):
        max=(0.613588*self.m**2-14.0356*self.m+88.664)/(0.0966512*self.m**2+0.474748*self.m+1)
        if value<=max:
             return True
        else:
            return False
        
    #coherence between measurements of the UV irradiance
    def coheUv1(self,ghuv,dhuv,dnuv,angle):
        if ghuv>2:
            return False
        value=ghuv/((dhuv+dnuv*math.cos(angle) ) )
        if value>0.92 and value<1.08:
            return  True
        else:
            return False
        
    def coheUv2(self,ghuv,dhuv,dnuv,angle):
        if  ghuv>20:
            return False
        value=ghuv/((dhuv+dnuv*math.cos(angle) ) )
        if value>0.85 and value<1.15:
            return  True
        else:
            return False    

    def coheUv3(self,ghuv,dhuv):
        if ghuv>20:
            return False
        value=dhuv/ghuv
        if value<1.05:
            return  True
        else:
            return False
            
    def coheUv4(self,ghuv,dhuv):
        if  ghuv>20:
            return False
        value=dhuv/ghuv
        if  value<1.1:
            return  True
        else:
            return False 
          

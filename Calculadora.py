#Nombre:Calculadora
#Autor:Álvaro Villar Val
#Fecha:26/03/24
#Versión:0.3.0
#Descripción: Calculadora de los diferentes criterios de calidad de la central meteorologica
#########################################################################################################################
#Definimos los imports
from pysolar.solar import *
import datetime
import math
##########################################################################################################################
class Calculadora:
    #Variables de la clase
    dni0=1361.1 #W/m2
    dnil0=133334 #lux
    dnp0=531.81 #W/m2
    dnuv0=102.15 #W/m2
    ghiclear=0
    dniclear=0
    latitude=42.3515619402223
    longitude=-3.6879829504876676
    m=0

    ##########################################################################################################################

    #Metodo que devuelve la fecha en formato datetime
    ##########################################################################################################################
    def dates(self,fecha):
        año=int(str(fecha)[0:4])
        mes=int(str(fecha)[5:7])
        dia=int(str(fecha)[8:10])
        hora=int(str(fecha)[11:13])
        minuto=int(str(fecha)[14:16])
        return datetime.datetime(año, mes, dia, hora, minuto, tzinfo=datetime.timezone.utc)
    ##########################################################################################################################

    #Metodo que calcula el ghi clear el dni clear y el m
    ##########################################################################################################################
    def calcular(self, angulo,dni):
        dni=float(dni)
        angle=math.radians(angulo)
        h=865 #No definitico placeholder por que no sabemos cuanto es 1
        pground=0.2
        psky=0.0685
        ma=(math.exp(-h/8446))/(math.cos(angle)+0.15*(93-angulo)**-1.253)
        self.m=(1)/(math.cos(angle)+0.15*(93-angulo)**-1.253)
        tray=math.exp(-0.0903*(ma**0.84)*(1+ma-(ma**1.01)))
        self.dniclear=0.9751*tray*self.dni0
        dhiray=0.79*self.dni0*math.cos(angle)*((0.5*(1-tray))/(1-ma+(ma**1.02)))
        dhimultrefl=(dni*math.cos(angle)+dhiray)*((pground*psky)/(1-pground*psky))
        dhiclear=dhiray+dhimultrefl
        self.ghiclear=self.dniclear*math.cos(angle)+dhiclear

        
    ##########################################################################################################################

    #1º Metodo de comprobacion de los criterios fisicos que los metodos de comprobacion de GH o DH fisicos llaman
    ##########################################################################################################################
    def physGen1(self,value,altitude,numFin,dn0,numIni,mini):
        nuevaAlt=math.radians(altitude)
        maxi=dn0*numIni*(math.cos(nuevaAlt)**1.2)+numFin
        if value>mini and value<=maxi:
             return 1
        elif value>mini:
            return 2
        else:
            return 3
    ##########################################################################################################################
        
    #2º Metodo de comprobacion de los criterios fisicos que los metodos de comprobacion de DN fisicos llaman
    ##########################################################################################################################
    def physGen2(self,value,dn0,mini):
        if value>mini:
            if value<=dn0:
                return 1
            else:
                return 3
        else:
            return 2
    ##########################################################################################################################

    #1º Metodo de coherencia generico que los metodos de coherencia 1 o 2 llaman
    ##########################################################################################################################   
    def coheGen1(self,gh,dh,dn,angle,max,mini,valueMin):
        newAngle=math.radians(angle)
        if gh<valueMin:
            return False
        value=gh/((dh+dn*math.cos(newAngle) ) )
        if value>mini and value<max:
            return  True
        else:
            return False
    ##########################################################################################################################

    #2º Metodo de coherencia generico que los metodos de coherencia 3 o 4 llaman
    ##########################################################################################################################
    def coheGen2(self,gh,dh,maxi,valueMin):
        if gh<valueMin:
            return False
        value=dh/gh
        if value<maxi:
            return  True
        else:
            return False
    ##########################################################################################################################

    #Metodo de comprabacion de los criterios de calidad generico que todos los metodos de comprobacion llaman
    ##########################################################################################################################
    def comprobar (self,valuePrin,funPhys,funSky,cohe1,cohe2,cohe3,cohe4,valueGH,valueDH,valueDN,fecha):

        if any(value is None for value in [valueGH, valueDH, valueDN, valuePrin]):
            return -1
        valuePrin=float(valuePrin)
        valueGH=float(valueGH)
        valueDH=float(valueDH)
        valueDN=float(valueDN)
        date = self.dates(fecha)
        grado=90-get_altitude(self.latitude, self.longitude, date)
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
    ##########################################################################################################################

    #GHI:	global horizontal irradiance.
    ##########################################################################################################################
    #Comprobacion de los criterios de calidad de la irradiancia
    def comprobarghi(self,valueGhi,valueDHi,valueDNi,fecha):
        date = self.dates(fecha)
        angulo=90-get_altitude(self.latitude, self.longitude, date)
        if angulo < 93:
            self.calcular(angulo,valueDNi)
        return self.comprobar(valueGhi,self.ghiPhys,self.ghiSky,self.coheI1,self.coheI2,self.coheI3,self.coheI4,valueGhi,valueDHi,valueDNi,fecha)
    ##########################################################################################################################        
    #Physical limits
    def ghiPhys(self,value,altitude):
    
       return self.physGen1(value,altitude,100,self.dni0,1.5,-4)
    ##########################################################################################################################
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghiSky(self,value):
        
        if value<=self.ghiclear:
             return True
        else:
            return False
    ##########################################################################################################################

    #DHI:	diffuse horizontal irradiance.
    ##########################################################################################################################
    #Comprobacion de los criterios de calidad de la irradiancia
    def comprobardhi(self,valueGhi,valueDHi,valueDNi,fecha):
        return self.comprobar(valueDHi,self.dhiPhys,self.dhiSky,self.coheI1,self.coheI2,self.coheI3,self.coheI4,valueGhi,valueDHi,valueDNi,fecha)
    ##########################################################################################################################
    #Physical limits
    def dhiPhys(self,value,grado):
        
        return self.physGen1(value,grado,50,self.dni0,0.95,-4)
    ##########################################################################################################################
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhiSky(self,value):
        
        if value<=self.ghiclear:
             return True
        else:
            return False
    ##########################################################################################################################
        
    #DNI:	direct normal irradiance.
    ##########################################################################################################################
    #Comprobacion de los criterios de calidad de la irradiancia
    def comprobardni(self,valueGhi,valueDHi,valueDNi,fecha):
    
        return self.comprobar(valueDNi,self.dniPhys,self.dniSky,self.coheI1,self.coheI2,self.coheI3,self.coheI4,valueGhi,valueDHi,valueDNi,fecha)
    ##########################################################################################################################
    #Physical limits
    def dniPhys(self,value,grado):
        
        return self.physGen2(value,self.dni0,-4)
    ##########################################################################################################################
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dniSky(self,value):
        
        if value<=self.dniclear:
             return True
        else:
            return False
    ##########################################################################################################################
    
    #Coherence mesaurements de la irradiancia
    ##########################################################################################################################
    #1º Metodo de coherencia entre las medidas de la irradiancia si el angulo es menor que 75º
    def coheI1(self,ghi,dhi,dni,angle):
        return self.coheGen1(ghi,dhi,dni,angle,1.08,0.92,50)
    ##########################################################################################################################    
    #1º Metodo de coherencia entre las medidas de la irradiancia si el angulo es mayor que 75º y menor que 93º
    def coheI2(self,ghi,dhi,dni,angle):
        return self.coheGen1(ghi,dhi,dni,angle,1.15,0.85,50)
    ##########################################################################################################################
    #2º Metodo de coherencia entre las medidas de la irradiancia si el angulo es menor que 75º
    def coheI3(self,ghi,dhi):
        return self.coheGen2(ghi,dhi,1.05,50)
    ##########################################################################################################################
    #2º Metodo de coherencia entre las medidas de la irradiancia si el angulo es mayor que 75º y menor que 93º
    def coheI4(self,ghi,dhi):
        return self.coheGen2(ghi,dhi,1.1,50)
    ##########################################################################################################################
          
    #GHIL:	global horizontal illuminance.
    ##########################################################################################################################
    #Comprobacion de los criterios de calidad de la iluminancia
    def comprobarghil(self,valueGhil,valueDHil,valueDNil,fecha):
        return self.comprobar(valueGhil,self.ghilPhys,self.ghilSky,self.coheIl1,self.coheIl2,self.coheIl3,self.coheIl4,valueGhil,valueDHil,valueDNil,fecha)
    ##########################################################################################################################
    #Physical limits
    def ghilPhys(self,value,grado):
        return self.physGen1(value,grado,10000,self.dnil0,1.5,0)
    ##########################################################################################################################
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghilSky(self,value):
        maxi=130*self.ghiclear
        if value<=maxi:
             return True
        else:
            return False

    ##########################################################################################################################

    #DHIL:	diffuse horizontal illuminance.
    ##########################################################################################################################
    #Comprobacion de los criterios de calidad de la iluminancia
    def comprobardhil(self,valueGhil,valueDHil,valueDNil,fecha):
        return self.comprobar(valueDHil,self.dhilPhys,self.dhilSky,self.coheIl1,self.coheIl2,self.coheIl3,self.coheIl4,valueGhil,valueDHil,valueDNil,fecha)
    ##########################################################################################################################
    #Physical limits
    def dhilPhys(self,value,grado):
        return self.physGen1(value,grado,5000,self.dnil0,0.95,0)
    ##########################################################################################################################
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhilSky(self,value):
        max=130*self.ghiclear
        if value<=max:
             return True
        else:
            return False

    ##########################################################################################################################

    #DNIL:	direct normal illuminance.
    ##########################################################################################################################
    #Comprobacion de los criterios de calidad de la iluminancia
    def comprobardnil(self,valueGhil,valueDHil,valueDNil,fecha):
        return self.comprobar(valueDNil,self.dnilPhys,self.dnilSky,self.coheIl1,self.coheIl2,self.coheIl3,self.coheIl4,valueGhil,valueDHil,valueDNil,fecha)
    ##########################################################################################################################
    #Physical limits
    def dnilPhys(self,value,grado):
        return self.physGen2(value,self.dnil0,0)
    ##########################################################################################################################
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnilSky(self,value):
        maxi=100*self.dniclear
        if value<=maxi:
             return True
        else:
            return False

    ##########################################################################################################################

    #Coherence between measurements of the illuminance
    ##########################################################################################################################
    #1º Metodo de coherencia entre las medidas de la irradiancia si el angulo es menor que 75º
    def coheIl1(self,ghil,dhil,dnil,angle):
        return self.coheGen1(ghil,dhil,dnil,angle,1.08,0.92,5000)
    ##########################################################################################################################
    #1º Metodo de coherencia entre las medidas de la irradiancia si el angulo es mayor que 75º y menor que 93º            
    def coheIl2(self,ghil,dhil,dnil,angle):
        return self.coheGen1(ghil,dhil,dnil,angle,1.15,0.85,5000)
    ##########################################################################################################################
    #2º Metodo de coherencia entre las medidas de la irradiancia si el angulo es menor que 75º
    def coheIl3(self,ghil,dhil):
        return self.coheGen2(ghil,dhil,1.05,5000)
    ##########################################################################################################################
    #2º Metodo de coherencia entre las medidas de la irradiancia si el angulo es mayor que 75º y menor que 93º  
    def coheIl4(self,ghil,dhil):
        return self.coheGen2(ghil,dhil,1.1,5000)
    ##########################################################################################################################

    #GHP:	global horizontal PAR irradiance.
    ##########################################################################################################################
    #Comprobacion de los criterios de calidad de la PAR irradiancia
    def comprobarghp(self,valueGhp,valueDHp,valueDNp,fecha):
        return self.comprobar(valueGhp,self.ghpPhys,self.ghpSky,self.coheP1,self.coheP2,self.coheP3,self.coheP4,valueGhp,valueDHp,valueDNp,fecha)
    ##########################################################################################################################        
    #Physical limits
    def ghpPhys(self,value,grado):
        return self.physGen1(value,grado,40,self.dnp0,1.5,0)
    ##########################################################################################################################
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghpSky(self,value):
        maxi=(46.5325*self.m**2-1738.11*self.m+48907.2)/(4.78443*self.m**2+89.17*self.m+1)
        if value<=maxi:
             return True
        else:
            return False
    ##########################################################################################################################ç

    #DHP:	diffuse horizontal PAR irradiance.
    ##########################################################################################################################
    #Comprobacion de los criterios de calidad de la PAR irradiancia
    def comprobardhp(self,valueGhp,valueDHp,valueDNp,fecha):
       return self.comprobar(valueDHp,self.dhpPhys,self.dhpSky,self.coheP1,self.coheP2,self.coheP3,self.coheP4,valueGhp,valueDHp,valueDNp,fecha)
    ##########################################################################################################################
    #Physical limits
    def dhpPhys(self,value,grado):
        return self.physGen1(value,grado,20,self.dnp0,0.95,0)
    ##########################################################################################################################
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhpSky(self,value):
        maxi=((-0.489631*(self.m**2))+(17.4211*self.m)+51.858)/((0.0575636*(self.m**2))+(0.671139*self.m)+1)
        if value<=maxi:
             return True
        else:
            return False
    ##########################################################################################################################

    #DNP:	direct normal PAR irradiance.
    ##########################################################################################################################
    #Comprobacion de los criterios de calidad de la PAR irradiancia
    def comprobardnp(self,valueGhp,valueDHp,valueDNp,fecha):
        return self.comprobar(valueDNp,self.dnpPhys,self.dnpSky,self.coheP1,self.coheP2,self.coheP3,self.coheP4,valueGhp,valueDHp,valueDNp,fecha)
    ##########################################################################################################################
    #Physical limits
    def dnpPhys(self,value,grado):
        return self.physGen2(value,self.dnp0,0)
    ##########################################################################################################################
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnpSky(self,value):
        maxi=(0.171991*self.m**2-9.88174*self.m+532.694)/(0.00732718*self.m**2+0.13576*self.m+1)
        if value<=maxi:
             return True
        else:
            return False
    ##########################################################################################################################

    #Coherence between measurements of the PAR irradiance
    ##########################################################################################################################
    #1º Metodo de coherencia entre las medidas de la irradiancia si el angulo es menor que 75º
    def coheP1(self,ghp,dhp,dnp,angle):
        return  self.coheGen1(ghp,dhp,dnp,angle,1.08,0.92,20)
    ##########################################################################################################################
     #1º Metodo de coherencia entre las medidas de la irradiancia si el angulo es mayor que 75º y menor que 93º       
    def coheP2(self,ghp,dhp,dnp,angle):
        return self.coheGen1(ghp,dhp,dnp,angle,1.15,0.85,20)
    ##########################################################################################################################
    #2º Metodo de coherencia entre las medidas de la irradiancia si el angulo es menor que 75º
    def coheP3(self,ghp,dhp):
        return self.coheGen2(ghp,dhp,1.05,20)
    ##########################################################################################################################
    #2º Metodo de coherencia entre las medidas de la irradiancia si el angulo es mayor que 75º y menor que 93º          
    def coheP4(self,ghp,dhp):
        return self.coheGen2(ghp,dhp,1.1,20)
    ##########################################################################################################################

    #GHUV:	global horizontal UV irradiance.
    ##########################################################################################################################
    def comprobarghuv(self,valueGhuv,valueDHuv,valueDNuv,fecha):
        return self.comprobar(valueGhuv,self.ghuvPhys,self.ghuvSky,self.coheUv1,self.coheUv2,self.coheUv3,self.coheUv4,valueGhuv,valueDHuv,valueDNuv,fecha)
    ##########################################################################################################################
    #Physical limits
    def ghuvPhys(self,value,grado):
        return self.physGen1(value,grado,5,self.dnuv0,1.5,0)
    ##########################################################################################################################
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def ghuvSky(self,value):
        maxi=(1.78513*self.m**2+177.076*self.m+2594.06)/(13.8072*self.m**2+25.6894*self.m+1)
        if  value<=maxi:
             return True
        else:
            return False
    ##########################################################################################################################

    #DHUV:	diffuse horizontal UV irradiance.
    ##########################################################################################################################
    #Comprobacion de los criterios de calidad de la irradiancia UV
    def comprobardhuv(self,valueGhuv,valueDHuv,valueDNuv,fecha):
        return self.comprobar(valueDHuv,self.dhuvPhys,self.dhuvSky,self.coheUv1,self.coheUv2,self.coheUv3,self.coheUv4,valueGhuv,valueDHuv,valueDNuv,fecha)
    ##########################################################################################################################
    #Physical limits
    ##########################################################################################################################
    def dhuvPhys(self,value,grado):
        return self.physGen1(value,grado,2,self.dnuv0,0.95,0)
    ##########################################################################################################################
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dhuvSky(self,value):
        maxi=(0.0284353*self.m**2-0.773392*self.m+34.2974)/(0.0393782*self.m**2+0.593745*self.m+1)
        if value<=maxi:
             return True
        else:
            return False
    ##########################################################################################################################

    #DNUV:	direct normal UV irradiance.
    ##########################################################################################################################
    #Comprobacion de los criterios de calidad de la irradiancia UV
    def comprobardnuv(self,valueGhuv,valueDHuv,valueDNuv,fecha):
        return self.comprobar(valueDNuv,self.dnuvPhys,self.dnuvSky,self.coheUv1,self.coheUv2,self.coheUv3,self.coheUv4,valueGhuv,valueDHuv,valueDNuv,fecha)
    ##########################################################################################################################
    #Physical limits
    def dnuvPhys(self,value,grado):
        return self.physGen2(value,self.dnuv0,0)
    ##########################################################################################################################
    #Limits of a clean and dry clear sky condition (without water vapor and aerosols)
    def dnuvSky(self,value):
        maxi=(0.613588*self.m**2-14.0356*self.m+88.664)/(0.0966512*self.m**2+0.474748*self.m+1)
        if value<=maxi:
             return True
        else:
            return False
    ##########################################################################################################################

    #Coherence between measurements of the UV irradiance
    ##########################################################################################################################
    #1º Metodo de coherencia entre las medidas de la irradiancia si el angulo es menor que 75º
    def coheUv1(self,ghuv,dhuv,dnuv,angle):
        return self.coheGen1(ghuv,dhuv,dnuv,angle,1.08,0.92,20)
    ##########################################################################################################################
    #1º Metodo de coherencia entre las medidas de la irradiancia si el angulo es mayor que 75º y menor que 93º       
    def coheUv2(self,ghuv,dhuv,dnuv,angle):
        return self.coheGen1(ghuv,dhuv,dnuv,angle,1.15,0.85,20)
    ##########################################################################################################################
    #2º Metodo de coherencia entre las medidas de la irradiancia si el angulo es menor que 75º
    def coheUv3(self,ghuv,dhuv):
        return self.coheGen2(ghuv,dhuv,1.05,20)
    ##########################################################################################################################
    #2º Metodo de coherencia entre las medidas de la irradiancia si el angulo es mayor que 75º y menor que 93º          
    def coheUv4(self,ghuv,dhuv):
        return self.coheGen2(ghuv,dhuv,1.1,20)
    ##########################################################################################################################
##########################################################################################################################
          

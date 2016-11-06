import shapefile 

class TugasEva4(object):
    def __init__(self,namafile):
        self.sf=shapefile.Reader(namafile)
        
    def itungBaris(self):
        rec = self.sf.shapes()
        return len(rec)
    
    def selectCountries(self,COUNTRIES):
        x_eva=0
        for y in self.sf.records():
            if y[8]==COUNTRIES:
                return x_eva
            x_eva = x_eva+1
            
      
        
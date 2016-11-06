import shapefile 
a = shapefile.Reader('D:/kuliah/Semester 5/SIG/Aplikasi/Natural Earth/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp')
b = a.shapes()
print len(b)


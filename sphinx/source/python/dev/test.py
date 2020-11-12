def imprime_lineas(obj_file,
                   num_pto,
                   coor_x,
                   coor_y,
                   crs_epsg_auth_id):

    str_msg = "Coordinates point %d: (%f, %f) %s \n" % (num_pto,
                                                        coor_x,
                                                        coor_y,
                                                        crs_epsg_auth_id)
    obj_file.write(str_msg)


# TODO: anyadir una seguna linea
obj_file_results = open("C:/TemporalC/archivo.txt", "w")
num_pto = 1
coor_x = 720487.27
coor_y = 4367654.23
crs_epsg_auth_id = "CRS-EPSG: 25830"
imprime_lineas(obj_file_results,
               num_pto,
               coor_x,
               coor_y,
               crs_epsg_auth_id)

obj_file_results = open("C:/TemporalC/archivo.txt", "a")
num_pto = 2
coor_x = 708540.27
coor_y = 4398234.23
crs_epsg_auth_id = "CRS-EPSG: 25831"
imprime_lineas(obj_file_results,
               num_pto,
               coor_x,
               coor_y,
               crs_epsg_auth_id)
obj_file_results.close()

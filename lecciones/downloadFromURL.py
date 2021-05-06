def downloadFromURL(url, filename, encoding="utf-8", separador=",", delimitador="\n"):
    import pandas as pd
    import urllib3
    import os

    # referenciamos la libreria URLLIB3
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    #r.status
    response = r.data

    # decodificamos el string binario
    str_data = response.decode(encoding)

    # divimos el string en un array de filas separad por enters
    lines = str_data.split(delimitador)

    # La primer línea contiene la cabecera
    col_names = lines[0].split(',')
    n_cols = len(col_names)

    # Generamos un diccionario vacio donde irá la información procesada desde la URL
    counter = 0
    main_dict = {}
    for col in col_names:
        main_dict[col] = []

    # Procesamos fila a fila la información para ir rrellenando el diccionario
    for line in lines:
        # nos saltamos la primer fila que contine la cabecera
        if(counter>0):
            # dividimos cada string por las comas 
            values = line.strip().split(delimitador)
            # añadimos los valores en su respectiva columna
            for i in range(len(col_names)):
                main_dict[col_names[i]].append(values[i])
        counter += 1
    print(f'La data tiene {counter} filas y {n_cols} columnas.')    

    # convertimos el diccionario en un dataframe 
    df = pd.DataFrame(main_dict)

    # Guardamos el archivo en nuestra pc
    mainpath = '/Users/lgutierrez/Documents/Desarrollo/python-ml-course/datasets/'
    datapath = 'athletes/'
    fullpath = os.path.join(mainpath+datapath, filename)
    df.to_csv(fullpath+'.csv')
    # medals_df.to_json(fullpath+'.json')
    # medals_df.to_excel(fullpath+'.xls')

medals_url = "http://winterolympicsmedals.com/medals.csv"
downloadFromURL(medals_url, "medallas")
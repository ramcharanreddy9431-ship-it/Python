def tower_builder(n_floors):
        y = []                       
        for i in range(n_floors):     
            a = " "
            b = "*"
            row = (a * (n_floors - (i + 1))) + (b * (2 * (i + 1) - 1)) + (a * (n_floors - (i + 1)))   #pritns i number of stars exactly in the centre
            y.append(row)
        return y

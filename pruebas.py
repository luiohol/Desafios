def datos_ingresados():
    incognita= input("¿Cuál es la X? ")
    if incognita=="Ui":
        Uf=float(input("Uf: "))
        Ui=input("Ui: ")
        Kf=float(input("Kf: "))
        Ki=float(input("Ki: "))
        return (Uf,Ui,Kf,Ki)
    elif incognita=="Uf":
        Uf=input("Uf: ")
        Ui=float(input("Ui: "))
        Kf=float(input("Kf: "))
        Ki=float(input("Ki: "))
        return (Uf,Ui,Kf,Ki)
    elif incognita=="Ki":
        Uf=float(input("Uf: "))
        Ui=float(input("Ui: "))
        Kf=float(input("Kf: "))
        Ki=input("Ki: ")
        return (Uf,Ui,Kf,Ki)
    else:
        #incognita=="Kf"
        Uf=float(input("Uf: "))
        Ui=float(input("Ui: "))
        Kf=input("Kf: ")
        Ki=float(input("Ki: "))
        return (Uf,Ui,Kf,Ki)

datos_ingresados()
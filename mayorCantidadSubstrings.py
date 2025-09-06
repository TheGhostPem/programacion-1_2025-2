def jugadores (cadena):
    jugadores = []
    for i in range(len(cadena)):
        for j in range(len(cadena)+1):
            if cadena[i] not in  "aeiou" and cadena[i:j] != '':
                jugadores.append(cadena[i:j])
    print(jugadores)

    jugadores2=[]
    for i in range(len(cadena)):
        for j in range(len(cadena)+1):
            if cadena[i]  in  "aeiou" and cadena[i:j] != '':
                jugadores2.append(cadena[i:j])
    print(jugadores2)
    
    if jugadores > jugadores2:
        print("win jugadores " + str(len(jugadores)))
    else : print (f"win jugadores 2 {len(jugadores2)}")


            
                

         
jugadores("banana")
                
    

              






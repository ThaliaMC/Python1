def menu():
    print("1.Literatura")
    print("2.Cine")
    print("3.Musica")
    print("4.Videojuegos")
    print("5.Salir")

menu()
option=int(input("Elija una opcion del 1-5 :"))

while option!=0:
     if(option ==1):
         print("Lecturas recomendables:")
         print("Esperándolo a Tito y otros cuentos de fúbol (Eduardo Sacheri)")
         print("El juego de Ender (Orson Scott Card)")
         print("El sueño de los héroes (Adolfo Bioy Casares)")
     elif(option==2):
         print("Películas recomendables")
         print("Matrix (1999)")
         print("El último samurai (2003)")
         print("Cars(2006)")
     elif(option==3):
         print("Discos recomendables:")
         print("Despedazado por mil partes (La Renga, 1996)")
         print("Búfalo (La Mississippi, 2008)")
         print("Gaia (Mägo de Oz, 2003)")
     elif(option==4):
         print("Videojuegos clásicos recomendables")
         print("Día del tentáculo (LucasArts, 1993")
         print("Terminal Velocity (Terminal Reality/3D Realms, 1995)")
     elif(option==5):
         print("Gracias!,Vuelva pronto ")
         break
     else:
        print("Numero invalido")

     print()
     menu()
     option=int(input("Escriba su opcion"))

  


import time
from colorama import Fore, Style
from random import choice

estados = ["sono", "sede", "fome", 'dores', 'mal estar', 'alegria', 'um bom semblante', 'certeza bem']
animais = ["Cavalo", "Capivara", "Arara-Azul", "Onça-Pintada", "Boto Cor de Rosa", "Tatu"]
print(f"""
Vamos checar os animais""")
for animal in animais:
    print(f"O(a) {animal} está com {choice(estados)}")

cavalo = r"""
  ¶¶                                              
  ¶¶                                              
  $¶¶¶¶¶¶¶o                                       
  ¶¶¶¶¶¶¶¶¶¶¶¶                                    
  ¶¶¶¶¶¶¶¶¶¶¶¶¶$                                  
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                                 
  ¶¶¶¶¶7¶¶¶¶¶¶¶¶¶¶o                               
  ¶¶¶¶$  ¶¶¶¶¶¶¶¶¶¶¶¶7777¶¶¶¶¶¶¶¶¶¶$              
  ¶¶¶¶   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ø          
  ¶¶¶1   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶7      
          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ø ¶¶¶¶     
          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶    
          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶    
          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ø ¶¶¶¶¶1   
           o¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶7 ø¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶   
             ¢¶¶¶¶¶ øø1        ¶¶¶¶¶¶¶   ¶¶¶¶¶¶   
              ¶¶¶¶¶             7¶¶¶¶¶   ¶¶¶¶¶¶   
               ¶¶¶¶               ø¶¶¶¶¶ ¶¶¶¶¶¶   
               ¶¶¶¶                 ¶¶¶¶ ¶¶¶¶¶$   
                ¶¶¶                 ø¶¶¶ ¶¶¶¶¶¶   
                1¶¶¶                 ¶¶ø  ¶¶¶¶¶   
                 ¶ ¶                  ¶ ¶ ¶¶¶¶¶¶  
                 ¶ ¶                  ¶ ¶         
                 ¶¶¶¶                 ¶¶¶         
                 ¶¶¶                  ¶¶          
               ¶¶¶¶                 ¶¶¶¶      
"""
boto = """
                    ##
                  ###*
              .*#####
             *######
           *#######
          *########.
         *#########.
         *######*###*
        *#########*###
       *##########*  *##
     *###########     *
    ############
     ##*#########
        ########
          #######
           *######
            *#####*
              *####*
                 *####
                  *##*
                    *##
                     *##.
                    .#####.
                 .##########
                .####*  *####
                 .#        #   
"""
panda = """
   7¶¶¶¶¶¶¢7ooooo7$¶¶¶øooø¶¶ø      
  o¶¶¢¢o$¶¶         7ø¶¶¶¶ø¶¶1     
 o¶¢¢ø¶¶¶ø               ¶¶¶¶7     
 ¶¶ø¶¶¶o                   ¶¶      
 ø¶¶ø                       1      
  o¶                        77     
  1                          o     
  o        ¶ø           ¢ø   o1    
  o1      ¶¶¶          1¶¶¶  ¢1    
  1o     ¶¶¶¶   1       o¶¶¶ 71    
   ¢7   ¶¶¢$¶7 1         ¶¶¶ 1     
    o1  ø¶ø¶¶   1 7¶¶¶¶  ¶¶o       
     1   7¶¶¶      7¶¶   ¶ 7ø      
     ¶¶7   ¶¶7            $¶¶¶     
   1¶¶¢¶¶¢   ¶¶¶71   1  ¶¶¶o¢¶¶    
   ¶¢7ooo¶¶¶¶¢¢7   1$¶¶¶¶¶$o¢¢¶¶   
  ¶$oooø¶      $¶o¶¶      $¶¢oø¶   
  ¶¶ooø¶        7ø7 1      ¶ø7o¶   
   ¶¶¶¶ø1o                1¢¶ø¶¶   
     ¶¶¶ø71               7¢¶¶¶¶   
        ø77o              ¢¶¶¶¶¶   
       $¶$7 1           o¶¶$ooø¶1  
    ø¶¶¶¶¶¶¶ø1        ø¶¶$øo¢¢¢¶¶  
   ¶¶øo¢øø¶¶¶$¶¢    ¶¶¶øoo¢o¢¢¢$¶  
  1¶o¢¢¢øøø$¶  $¶ø¶¶¶¶¶¶ø¢ooo¢øø¶¢ 
  1¶¢¢¢øø$¶¶¶    ¢o 1o7¢¶¶¶¶¶øø$¶ø 
   ¶¶¶¶¶¶¶¶¶ø 1777øo        ø¶¶¶¶7 
"""
jaguatirica = """
            ¶
            ¶¶
           ¶¶¶¶                             
          ¶¶¶¶¶¶¶                            
       1¶¶¶¶¶¶¶¶¶¶                           
      1¶¶¶¶¶¶¶¶¶¶¶¶                          
     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                         
    1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶7                        
     ¢¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                        
        7¶¶¶¶¶¶¶¶¶¶¶¶¶¶                      
         ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                     
        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                    
        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶7                 
       1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1              
       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1            
       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶7          
       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶         
        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶        
         ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶       
          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶      
           ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶      
          ¢¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶      
          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶      
          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶      
          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶      
          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶      
          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶       
         7¶¶¶¶¶  7¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶       
         1¶¶¶¶1   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶        
       ¶¶¶¶¶¶1     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶        
      ¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶7      
      7¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶¢¢¢¢¢¶¶¶¶¶¶¶      
                                  7¶¶¶¶¶     
                                   ¶¶¶¶¶     
                                   ¶¶¶¶7     
                                 ¶¶¶¶¶¶      
             ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶       
              ¢¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¢         
                   71¶¶¶¶¶¶¶¶¶¶¶1           
"""
cameras = [cavalo, boto, panda, jaguatirica]
print('Escolhe de qual animal quer ver a camera:')
print("""
1. -Cavalo
2. -Boto Cor de Rosa
3. -Panda
4. -Jaguatirica
""")
while True:
    sair = input("Quer sair? [S]/[N]").upper()
    if sair == "S":
        print("Volte sempre!")
    else:
        while True:
            try:
                mostrar_camera = input()
                if not mostrar_camera.isnumeric():
                    raise ValueError("Apenas números positivos e entre 1 e 4")
                if mostrar_camera == '1':
                    print(Fore.BLUE + "Mostrando a camera do cavalo" + Style.RESET_ALL)
                    print(cavalo)
                elif mostrar_camera == '2':
                    print(Fore.BLUE + "Mostrando a camera do boto" + Style.RESET_ALL)
                    print(boto)
                elif mostrar_camera == '3':
                    print(Fore.BLUE + "Mostrando a camera do panda" + Style.RESET_ALL)
                    print(panda)
                elif mostrar_camera == '4':
                    print(Fore.BLUE + "Mostrando a camera da jaguatirica" + Style.RESET_ALL)
                    print(jaguatirica)
                break
            except ValueError as erro:
                print(f"Erro: {erro}")


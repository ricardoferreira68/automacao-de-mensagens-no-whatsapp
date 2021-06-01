from kivy.lang import Builder
from kivymd.app import MDApp

#===================================================
#       imports necessario                    
#===================================================
#                                
#   kivymd
#   Kivy
#   from kivy.lang import Builder
#   from kivymd.app import MDApp
#
#   instalar kivymd ===> python3 -m pip install kivymd
#   
#   para executar o codigo a seguir utilizamos uma extensão 
#   kivylang que permite a facilidade em escrever o codigo
#   utilizando   # <KvLang>  codigo kv aqui   # </KvLang>
#   Extensão do VSCode
#   
#   Estrutura do layout vinda do desenho apresentada 
#
#   Tenha o necessariamente a extensão kvlang para rodar
#   com o AutoComplete do VSCode ou ==> 
#   remova os ===> # <KvLang>  # </KvLang>   <=== do começo e final do codigo
#    


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(''' 
        
#<KvLang>
#==========================================================
#               Configurações do layout
#==========================================================
MDScreen:
    md_bg_color: 0.87, 0.90, 0.92, 1
    GridLayout:
        size_hint_y: 1
        size_hint_x: 1
        rows:7
        

        #==========================================================
        #                       Linha 0.0
        #==========================================================      
        MDBoxLayout:
            size_hint_y: 0.15 
            GridLayout:
                cols:50
                MDBoxLayout:
                    size_hint_x: 0.7
                MDIcon:
                    halign: "right"
                    icon: "cube-outline"
                    font_size: '40sp'
                MDBoxLayout:
                    MDLabel:
                        text:'Operador chat bot WhatsApp'
                        halign: "left"
                MDBoxLayout:
                    size_hint_x: 1
        

        #==========================================================
        #                       Linha 01
        #==========================================================
        MDBoxLayout:
            size_hint_y: 0.1
            GridLayout:
                cols:3
                

        #==========================================================
        #                       Linha 01.1
        #==========================================================
                MDBoxLayout:
                    GridLayout:
                        cols:2
                        MDIcon:
                            halign: "right"
                            icon: "account-circle"
                            font_size: '40sp'
                        MDBoxLayout:
                            MDLabel:
                                text:'Cliente : xxxxxxxxxx'
                                font_size: '20sp'
                                halign: "center"
        #==========================================================
        #                       Linha 01.2
        #==========================================================
                MDBoxLayout: 
                    size_hint_x: 1.8

        #==========================================================
        #                      Linha 01.3.1
        #==========================================================
                MDBoxLayout:
                    GridLayout:
                        cols:2

                        BoxLayout:
                            padding: [25,0,25,0]
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                text: "Voltar"
                                md_bg_color: 0, 0.69, 0.62, 1
                                size_hint: 1,1 
                                
                                
        #==========================================================
        #                       Linha 01.3.2
        #==========================================================
                        MDBoxLayout:
                            padding: [25,0,25,0]
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                text: "Editar"
                                md_bg_color:0, 0.69, 0.62, 1
                                size_hint: 1,1 

        
        #==========================================================
        #                       Linha 02
        #==========================================================
        BoxLayout:
            size_hint_y: 0.1
            GridLayout:
                cols:3
                

        #==========================================================
        #                       Linha 02.1
        #==========================================================
                MDBoxLayout:
                    GridLayout:
                        cols:2
                        MDIcon:
                            halign: "right"
                            icon: "whatsapp"
                            font_size: '40sp'
                        MDBoxLayout:
                            MDLabel:
                                text:'WhatsApp : x xxxx-xxxx'
                                font_size: '20sp'
                                halign: "center"
        #==========================================================
        #                       Linha 02.2
        #==========================================================
                MDBoxLayout:
                    size_hint_x: 1.8
        #==========================================================
        #                       Linha 02.3.1
        #==========================================================
                MDBoxLayout:
                    GridLayout:
                        cols:2

                        MDBoxLayout:
                            
        #==========================================================
        #                       Linha 02.3.2
        #==========================================================
                        MDBoxLayout:



        #==========================================================
        #                       Linha 03
        #==========================================================      
        MDBoxLayout:
            size_hint_y: 0.2
            GridLayout:
                cols:3
        #==========================================================
        #                       Linha 3.1
        #==========================================================
                MDBoxLayout:
                    size_hint_x: 1.3
                    GridLayout:
                        cols:100
                        MDIcon:
                            halign: "right"
                            icon: "message-reply-text"
                            font_size: '40sp'
                        BoxLayout:
                            MDLabel:
                                text:'Mensagens'
                                font_size: '25sp'
                                halign: "center"
                        BoxLayout:
                            size_hint_y: 0.5
        #==========================================================
        #                       Linha 3.2
        #==========================================================
                MDBoxLayout:
                    size_hint_x: 1.8
                    MDLabel:
                        text:'Catalogo'
                        font_size: '25sp'
                        halign: "center"
                        
        #==========================================================
        #                       Linha 3.3
        #==========================================================
                MDBoxLayout:
                    size_hint_x: 0.5
                        
        #==========================================================
        #                       Linha 04
        #==========================================================      
        MDBoxLayout:
            GridLayout:
                cols : 50
        #==========================================================
        #                       Linha 04.1
        #==========================================================  
                MDBoxLayout:
                    padding: [35,0,35,0]
                    size_hint_x: 0.7
                    MDTextField:
                        size_hint: 1,1 
                        multiline: True
                        hint_text: "Bot WhatsApp"
                        font_size: '25sp'






        #==========================================================
        #                       Linha 04.2
        #========================================================== 
                MDBoxLayout:
                    size_hint_x: 1
                    GridLayout:
                        rows: 50
                    


        #==========================================================
        #                       Linha 04.2.10
        #========================================================== 
                        MDBoxLayout:
                            
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 0, 0.69, 0.62, 1
                                size_hint: 0.1,0.5 
                                text:'Linha  04.2.10'
                                halign: "center"




        #==========================================================
        #                       Linha 04.2.11
        #========================================================== 
                        MDBoxLayout:
                            
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                size_hint: 0.1,0.5 
                                md_bg_color: 0, 0.69, 0.62, 1
                                text:'Linha  04.2.21'
                                halign: "center"
        #==========================================================
        #                       Linha 04.2.12
        #========================================================== 
                        MDBoxLayout:
                        
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                size_hint: 0.1,0.5 
                                md_bg_color:0, 0.69, 0.62, 1
                                text:'Mandar Catalogo'
                                halign: "center"
        #==========================================================
        #                       Linha 04.2.13
        #========================================================== 
                        MDBoxLayout:    
                            
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                size_hint: 0.1,0.5
                                md_bg_color: 0, 0.69, 0.62, 1
                                text:'Linha  04.2.23'
                                halign: "center"

        #==========================================================
        #                       Linha 04.2.14
        #========================================================== 
                        MDBoxLayout:    
                            
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                size_hint: 0.1,0.5
                                md_bg_color: 0, 0.69, 0.62, 1
                                text:'Linha  04.2.23'
                                halign: "center"






        #==========================================================
        #                       Linha 04.3
        #========================================================== 
                MDBoxLayout:
                    size_hint_x: 0.2
                    GridLayout:
                        rows: 50
                    


        #==========================================================
        #                       Linha 04.3.10
        #========================================================== 
                        MDBoxLayout:
                            padding: [25,0,25,0]
                            
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 1, 0, 0,0.8
                                size_hint: 0.1,0.5 
                                text:'-'
                                font_size: '25sp'
                                text_color: 0, 0, 0, 1
                                halign: "center"




        #==========================================================
        #                       Linha 04.3.11
        #========================================================== 
                        MDBoxLayout:
                            padding: [25,0,25,0]
                            
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 1, 0, 0,0.8
                                size_hint: 0.1,0.5 
                                text:'-'
                                font_size: '25sp'
                                text_color: 0, 0, 0, 1
                                halign: "center"
        #==========================================================
        #                       Linha 04.3.12
        #========================================================== 
                        MDBoxLayout:
                            padding: [25,0,25,0]
                        
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 1, 0, 0,0.8
                                size_hint: 0.1,0.5 
                                text:'-'
                                font_size: '25sp'
                                text_color: 0, 0, 0, 1
                                halign: "center"
        #==========================================================
        #                       Linha 04.3.13
        #========================================================== 
                        MDBoxLayout:
                            padding: [25,0,25,0]    
                            
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 1, 0, 0,0.8
                                size_hint: 0.1,0.5 
                                text:'-'
                                font_size: '25sp'
                                text_color: 0, 0, 0, 1
                                halign: "center"

        #==========================================================
        #                       Linha 04.3.14
        #========================================================== 
                        MDBoxLayout:
                            padding: [25,0,25,0]    
                            
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 1, 0, 0,0.8
                                size_hint: 0.1,0.5 
                                text:'-'
                                font_size: '25sp'
                                text_color: 0, 0, 0, 1
                                halign: "center"
























        #==========================================================
        #                       Linha 05
        #==========================================================      
        MDBoxLayout:
            size_hint_y: 0.2
            GridLayout:
                cols : 50
        
        #==========================================================
        #                       Linha 05.1
        #==========================================================  
                MDBoxLayout:
                    size_hint_x: 0.7
                   
                    padding: [150,0,150,0]
                    MDFlatButton:
                        text: "Confirmar"
                        halign: "center"
                        pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                        md_bg_color: 0, 0.69, 0.62, 1
                        size_hint: .1,0.7 
                        
                    
        #==========================================================
        #                       Linha 05.2
        #========================================================== 
                MDBoxLayout:
                   
                    size_hint_x: 1.4
        
        MDBoxLayout:
            size_hint_y: 0.1
        
    








#</KvLang>
''')


MyApp().run()

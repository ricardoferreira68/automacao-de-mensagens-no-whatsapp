from kivy.lang import Builder
from kivymd.app import MDApp

# https://kivymd.readthedocs.io/en/latest/
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
        rows:100



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
        #                       Linha 01.3.1
        #==========================================================
                MDBoxLayout:
                    GridLayout:
                        cols:2

                        BoxLayout:
                            padding: [25,0,25,10]
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                text: "Voltar"
                                md_bg_color: 0, 0.69, 0.62, 1
                                size_hint: 1,1 
        #==========================================================
        #                       Linha 01.3.2
        #==========================================================
                        MDBoxLayout:
                            padding: [25,0,25,10]
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                text: "Editar"
                                md_bg_color: 0, 0.69, 0.62, 1
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
                            padding: [25,10,25,0]
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                text: "Carrinho"
                                md_bg_color: 0, 0.69, 0.62, 1
                                size_hint: 1,1 
        #==========================================================
        #                       Linha 02.3.2
        #==========================================================
                        MDBoxLayout:
                            padding: [25,10,25,0]
                            MDFlatButton:
                                pos_hint: {'center_x':0.01 , 'center_y':0.5 }
                                text: "Abrir Catalogo"
                                md_bg_color: 0, 0.69, 0.62, 1
                                size_hint: 1,1 






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
                        text:'Menu'
                        font_size: '25sp'
                        halign: "center"
        #==========================================================
        #                       Linha 3.3
        #==========================================================
                MDBoxLayout:
                    BoxLayout:
                        




        #==========================================================
        #                       Linha 04
        #==========================================================      
        MDBoxLayout:
            GridLayout:
                cols : 3
        #==========================================================
        #                       Linha 04.1
        #==========================================================  
                MDBoxLayout:
                    size_hint_x: 0.7
                    padding: [35,0,35,0]
                    MDTextField:
                        size_hint: 1,1 
                        multiline: True
                        hint_text: "Mensagem Cliente"
                        font_size: '25sp'
                        md_bg_color: 0, 0, 0, 1






        #==========================================================
        #                       Linha 04.2
        #========================================================== 
                MDBoxLayout:
                    GridLayout:
                        cols: 3
                        rows: 3
                    


        #==========================================================
        #                       Linha 04.2.10
        #========================================================== 
                        MDBoxLayout:
                            padding: [30,30,30,30]
                            padding: [30,30,30,30]
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 0, 0.69, 0.62, 1
                                text:'Mandar Catalogo'
                                halign: "center"
                                size_hint: 1,1
                                

        #==========================================================
        #                       Linha 04.2.20
        #========================================================== 
                        MDBoxLayout:
                            padding: [30,30,30,30]
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 0, 0.69, 0.62, 1
                                text:'Pedido Confirmado'
                                halign: "center"
                                size_hint: 1,1
        #==========================================================
        #                       Linha 04.2.30
        #========================================================== 
                        MDBoxLayout:
                            padding: [30,30,30,30]
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 0, 0.69, 0.62, 1
                                text:'Pedido a Caminho'
                                halign: "center"
                                size_hint: 1,1



        #==========================================================
        #                       Linha 04.2.21
        #========================================================== 
                        MDBoxLayout:
                            padding: [30,30,30,30]
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 0, 0.69, 0.62, 1
                                text:'Bom dia'
                                halign: "center"
                                size_hint: 1,1
                                
        #==========================================================
        #                       Linha 04.2.22
        #========================================================== 
                        MDBoxLayout:
                            padding: [30,30,30,30]
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 0, 0.69, 0.62, 1
                                text:'Boa Tarde'
                                halign: "center"
                                size_hint: 1,1
        #==========================================================
        #                       Linha 04.2.23
        #========================================================== 
                        MDBoxLayout:
                            padding: [30,30,30,30]       
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 0, 0.69, 0.62, 1
                                text:'Boa Noite'
                                halign: "center"
                                size_hint: 1,1


        #==========================================================
        #                       Linha 04.2.31
        #========================================================== 
                        MDBoxLayout:
                            padding: [30,30,30,30]
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 0, 0.69, 0.62, 1
                                text:''
                                halign: "center"
                                size_hint: 1,1
        #==========================================================
        #                       Linha 04.2.32
        #========================================================== 
                        MDBoxLayout:
                            padding: [30,30,30,30]
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 0, 0.69, 0.62, 1
                                text:''
                                halign: "center"
                                size_hint: 1,1
        #==========================================================
        #                       Linha 04.2.33
        #========================================================== 
                        MDBoxLayout:
                            padding: [30,30,30,30]
                            MDFlatButton:
                                pos_hint: {'center_x':0.5 , 'center_y':0.5 }
                                md_bg_color: 0, 0.69, 0.62, 1
                                text:''
                                halign: "center"    
                                size_hint: 1,1    

        #==========================================================
        #                       Linha 04.3 EXTRA ===> MARGEM
        #========================================================== 
                MDBoxLayout:
                    size_hint_x: 0.5
                    
                    






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

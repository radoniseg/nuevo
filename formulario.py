from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING

class Formulario(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Formulario de Paciente")
        self.datos_paciente()
        self.personales_patologicos()
        self.Heredo_Familiar()
        self.Heredo_De()
        self.exploracionFisica()
        self.anestecia_sangre()
        self.evaluaciones()
        self.transient(parent)
        self.grab_set()


    def datos_paciente(self):
        self.marco_paciente=Frame(self)
        self.marco_paciente.grid(row=0,column=0,pady=5,padx=5,sticky=(W+E,N))
        self.marco_paciente.config(bg='#314252')

        self.patologicos_contenido_t=ttk.Frame(self.marco_paciente)
        self.patologicos_contenido_t.grid(row=0,column=0,pady=5,padx=5,sticky=(W, E))
        
        self.marco_paciente_contenido=ttk.Frame(self.marco_paciente)
        self.marco_paciente_contenido.grid(row=1,column=0,pady=5,padx=5,sticky=(W+E))

        self.titulo_datos_p=ttk.Label(self.patologicos_contenido_t, text="DATOS DEL PACIENTE").grid(column=0,row=0, padx=5, pady=5,sticky=(W, E))
        
        self.titulo_datos_p=ttk.Label(self.marco_paciente_contenido, text="Nombre Paciente" ).grid(column=0,row=1, padx=5, pady=5,sticky=(W))

        self.nombre=StringVar()
        self.nombrebx=ttk.Entry(self.marco_paciente_contenido,textvariable=self.nombre)
        self.nombrebx.grid(column=1,row=1, padx=5,pady=5,sticky=(W+E))
        
        edadlb=ttk.Label(self.marco_paciente_contenido, text="Edad").grid(column=2,row=1, padx=5, pady=5,sticky=(W))

        self.edad=StringVar()
        self.edadbx=ttk.Entry(self.marco_paciente_contenido, textvariable=self.edad)
        self.edadbx.grid(column=3,row=1, padx=5, pady=5,sticky=(W))

        referidorlb=ttk.Label(self.marco_paciente_contenido, text="Medico Referidor").grid(column=0, row=2, pady=5,padx=5,sticky=(W, E))

        self.referidor=StringVar()
        self.referidorbx=ttk.Entry(self.marco_paciente_contenido, textvariable=self.referidor)
        self.referidorbx.grid(column=1,row=2,pady=5,padx=5, sticky=(W))

        asalb=ttk.Label(self.marco_paciente_contenido, text="ASA").grid(column=2, row=2, padx=5, pady=5, sticky=(W))

        self.asa=StringVar()
        self.asacbx=ttk.Combobox(self.marco_paciente_contenido, textvariable=self.asa)
        self.asacbx.grid(column=3, row=2, sticky=(W))
        self.asacbx['values']=('I','II','III','IV','V','E')

        self.paciente_c= ttk.Label(self.marco_paciente_contenido, text='PACIENTE').grid(row=5,column=0,pady=5,padx=5,sticky=(W))

        self.sexo=StringVar()
        self.hombrerbtn=ttk.Radiobutton(self.marco_paciente_contenido, text='Femenina', variable=self.sexo, value='F')
        self.hombrerbtn.grid(row=6,column=0, sticky=(W))

        self.mujerrbtn=ttk.Radiobutton(self.marco_paciente_contenido, text='Masculino', variable=self.sexo, value='M')
        self.mujerrbtn.grid(column=1, row=6, sticky=(W, E))

        self.programado=StringVar()
        self.cirugiarbtn=ttk.Radiobutton(self.marco_paciente_contenido, text='Programado para cirugia', variable=self.programado, value='cirugia')
        self.cirugiarbtn.grid(column=0, row=7, sticky=(W, E))
        self.diagnosticorbtn=ttk.Radiobutton(self.marco_paciente_contenido, text='Estudio diagnostico', variable=self.programado, value='diagnostico')
        self.diagnosticorbtn.grid(column=1, row=7, sticky=(W, E))
        
        diagnosticol=ttk.Label(self.marco_paciente_contenido, text='El cual presenta un diagnostico:').grid(column=0,row=8,sticky=(W, E))

        self.diagnostico=StringVar()
        self.diagnosticobx=ttk.Entry(self.marco_paciente_contenido, textvariable=self.diagnostico)
        self.diagnosticobx.grid(column=1,row=8,sticky=(W, E),columnspan=2)



        #ANTECEDENTES PERSONALES PATOLOGICOS*****************************************************************************#
    def personales_patologicos(self):

        self.titulo_datos_p=ttk.Label(self.marco_paciente, text='ANTECEDENTES PERSONALES PATOLOGICOS').grid(column=0,row=2, padx=5, pady=5,sticky=(W, E))
        
        self.patologicos_contenido=ttk.Frame(self.marco_paciente)
        self.patologicos_contenido.grid(row=3,column=0,pady=5,padx=5,sticky=(W, E))

        self.tabaquismo = StringVar(value='no')
        self.tabaquismo_check = ttk.Checkbutton(self.patologicos_contenido, text='Tabaquismo',
            variable=self.tabaquismo, onvalue='si', offvalue=self.tabaquismo)
        self.tabaquismo_check.grid(column=0, row=0)

        self.alcoholismo = StringVar(value='no')
        self.alcoholismo_check = ttk.Checkbutton(self.patologicos_contenido, text='Alcoholimo',
            variable=self.alcoholismo, onvalue='si', offvalue=self.alcoholismo)
        self.alcoholismo_check.grid(column=1, row=0)

        self.toxicomanias = StringVar(value='no')
        self.toxicomanias_check = ttk.Checkbutton(self.patologicos_contenido, text='toxicomanias',
            variable=self.toxicomanias, onvalue='si', offvalue=self.toxicomanias)
        self.toxicomanias_check.grid(column=2, row=0) 

        self.transfusiones = StringVar(value='no')
        self.transfusiones_check = ttk.Checkbutton(self.patologicos_contenido, text='transfusiones',
            variable=self.transfusiones, onvalue='si', offvalue=self.transfusiones)
        self.transfusiones_check.grid(column=3, row=0)

        self.hospitalariosl=ttk.Label(self.patologicos_contenido, text='Hospitalarios')
        self.hospitalariosl.grid(column=0, row=1)

        self.hospitalarios=StringVar()
        self.hospitalariosbx=ttk.Entry(self.patologicos_contenido)
        self.hospitalariosbx.grid(column=1,row=1)

        quirurgicosl=ttk.Label(self.patologicos_contenido, text='Quirurgicos')
        quirurgicosl.grid(column=2,row=1)

        self.quirurgicos=StringVar()
        self.quirurgicosbx=ttk.Entry(self.patologicos_contenido)
        self.quirurgicosbx.grid(column=3,row=1)

        anestesicosl=ttk.Label(self.patologicos_contenido, text='Anestesicos')
        anestesicosl.grid(row=2, column=0)

        self.anestesicos=StringVar()
        self.anestesicosbx=ttk.Entry(self.patologicos_contenido)
        self.anestesicosbx.grid(row=2, column=1,pady=5)

        alergicosl=ttk.Label(self.patologicos_contenido, text='Alergicos')
        alergicosl.grid(row=2, column=2)

        self.alergicos=StringVar()
        self.alergicosbx=ttk.Entry(self.patologicos_contenido)
        self.alergicosbx.grid(row=2, column=3,pady=5)
        
        '''
        #ANTECEDENTES HEREDO FAMILIARES
        '''
    def Heredo_Familiar(self):
        self.titulo_vista=ttk.Label(self.marco_paciente,text='ANTECEDENTES HEREDO FAMILIARES').grid(column=0,row=4, padx=5, pady=5,sticky=(W, E))

        self.familiares_contenido=ttk.Frame(self.marco_paciente)
        self.familiares_contenido.grid(row=5,column=0,pady=5,padx=5,sticky=(W, E))

        padre=ttk.Label(self.familiares_contenido, text='Padre').grid(row=1, column=0)

        self.padrebx=ttk.Entry(self.familiares_contenido)
        self.padrebx.grid(row=1, column=1,pady=5)

        madrel=ttk.Label(self.familiares_contenido, text='Madre').grid(row=1, column=2)

        self.madrebx=ttk.Entry(self.familiares_contenido)
        self.madrebx.grid(row=1, column=3,pady=5)

        hermanosl=ttk.Label(self.familiares_contenido, text='Hermanos').grid(row=2, column=0)

        self.hermanosbx=ttk.Entry(self.familiares_contenido)
        self.hermanosbx.grid(row=2, column=1,pady=5)

        hijosl=ttk.Label(self.familiares_contenido, text='hijos').grid(row=2, column=2)

        self.hijosbx=ttk.Entry(self.familiares_contenido)
        self.hijosbx.grid(row=2, column=3,pady=5)

        '''
        #ANTECEDENTES HEREDO DE
        '''
    def Heredo_De(self):
        self.marco_de=Frame(self)
        self.marco_de.grid(row=1,column=0,pady=5,padx=5,sticky=(W, E))
        self.marco_de.config(bg='#314252')

        self.de_contenido_titulo=ttk.Frame(self.marco_de)
        self.de_contenido_titulo.grid(row=0,column=0,pady=5,padx=5,sticky=(W, E))

        self.de_contenido=ttk.Frame(self.marco_de)
        self.de_contenido.grid(row=1,column=0,pady=5,padx=5,sticky=(W, E))

        self.titulo_vista=ttk.Label(self.de_contenido_titulo,text='ANTECEDENTES HEREDO DE').grid(column=0,row=0, padx=5, pady=5,sticky=(W, E))

        self.diabetes = StringVar(value='no')
        self.diabetes_check = ttk.Checkbutton(self.de_contenido, text='Diabetes',
            variable=self.diabetes, onvalue='si', offvalue=self.diabetes)
        self.diabetes_check.grid(row=1, column=0)

        self.hta=StringVar(value='no')
        self.hta_check=ttk.Checkbutton(self.de_contenido, text='HTA', variable=self.hta, onvalue='si',offvalue=self.hta)
        self.hta_check.grid(row=1,column=1)

        self.tb=StringVar(value='no')
        self.tb_check=ttk.Checkbutton(self.de_contenido, text='TB', variable=self.tb, onvalue='si',offvalue=self.tb)
        self.tb_check.grid(row=1,column=2)

        self.falcemia=StringVar(value='no')
        self.falcemia_cbtn=ttk.Checkbutton(self.de_contenido, text='falcemia', onvalue='si', offvalue=self.falcemia)
        self.falcemia_cbtn.grid(row=1,column=3)

        self.hepatitis=StringVar(value='no')
        self.hepatitis_cbtn=ttk.Checkbutton(self.de_contenido, text='Hepatitis', onvalue='si', offvalue=self.hepatitis)
        self.hepatitis_cbtn.grid(row=1,column=4)

        self.bocio=StringVar(value='no')
        self.bocio_cbtn=ttk.Checkbutton(self.de_contenido, text='Bocio', onvalue='si', offvalue=self.bocio)
        self.bocio_cbtn.grid(row=2,column=0)

        self.asma=StringVar(value='no')
        self.asma_cbtn=ttk.Checkbutton(self.de_contenido, text='Asma', onvalue='si', offvalue=self.asma)
        self.asma_cbtn.grid(row=2, column=1)

        self.otrosl=ttk.Label(self.de_contenido, text='Otros')
        self.otrosl.grid(row=2, column=2)

        self.otrosbx=ttk.Entry(self.de_contenido)
        self.otrosbx.grid(row=2, column=3)
    
    '''
    #EXPLOCARION FISICA
    '''
    def exploracionFisica(self):
        self.marco_explaracion=Frame(self)
        self.marco_explaracion.grid(row=0,column=1,pady=5,padx=5,sticky=(W, E))
        self.marco_explaracion.config(bg='#314252')

        self.marco_explaracion_contenido=ttk.Frame(self.marco_explaracion)
        self.marco_explaracion_contenido.grid(row=1,column=0,pady=5,padx=5,sticky=(W, E))

        title_exploracion=ttk.Label(self.marco_explaracion, text='EXPLORACION FISICA')
        title_exploracion.grid(row=0,column=0,pady=5,padx=5,sticky=(W, E))

        title_exploracion=ttk.Label(self.marco_explaracion, text='LABORATORIOS')
        title_exploracion.grid(row=3,column=0,pady=5,padx=5,sticky=(W, E))

        tallal=ttk.Label(self.marco_explaracion_contenido, text='Talla').grid(row=1, column=0)
        piesl=ttk.Label(self.marco_explaracion_contenido, text='Pies').grid(row=2, column=0)

        self.piesbx=ttk.Entry(self.marco_explaracion_contenido)
        self.piesbx.grid(row=2,column=1)

        pulgadasl=ttk.Label(self.marco_explaracion_contenido, text='pulgadas').grid(row=2, column=2)

        self.pulgadasbx=ttk.Entry(self.marco_explaracion_contenido)
        self.pulgadasbx.grid(row=2,column=3)

        peso=ttk.Label(self.marco_explaracion_contenido, text='Peso').grid(row=1, column=4)
        lbs=ttk.Label(self.marco_explaracion_contenido, text='Lbsl').grid(row=2, column=4)

        self.lbs=StringVar()
        self.lbssb = ttk.Spinbox(self.marco_explaracion_contenido, from_=1.0, to=999.0, textvariable=self.lbs)
        self.lbssb.grid(row=2,column=5)

        kgl=ttk.Label(self.marco_explaracion_contenido, text='Kg').grid(row=2, column=6)

        self.kg = StringVar()
        self.kgsb = ttk.Spinbox(self.marco_explaracion_contenido, from_=1.0, to=999.0, textvariable=self.kg)
        self.kgsb.grid(row=2,column=7)

        tatl=ttk.Label(self.marco_explaracion_contenido, text='TA').grid(row=3, column=0)
        tal=ttk.Label(self.marco_explaracion_contenido, text='L/min').grid(row=4, column=0)

        self.ta=StringVar()
        self.talsb = ttk.Spinbox(self.marco_explaracion_contenido, from_=1.0, to=100.0, textvariable=self.ta)
        self.talsb.grid(row=4,column=1)

        fcl=ttk.Label(self.marco_explaracion_contenido, text='FC').grid(row=3, column=2)
        fc_l=ttk.Label(self.marco_explaracion_contenido, text='L/min').grid(row=4, column=2)

        self.fc=StringVar()
        self.fcsb = ttk.Spinbox(self.marco_explaracion_contenido, from_=1.0, to=100.0, textvariable=self.fc)
        self.fcsb.grid(row=4,column=3)

        frl=ttk.Label(self.marco_explaracion_contenido, text='FR').grid(row=3, column=4)
        fr_l=ttk.Label(self.marco_explaracion_contenido, text='L/min').grid(row=4, column=4)

        self.fr=StringVar()
        self.frsb = ttk.Spinbox(self.marco_explaracion_contenido, from_=1.0, to=100.0, textvariable=self.fr)
        self.frsb.grid(row=4,column=5)

        """
        marco contenido
        """
        
        self.marco_explaracion_contenido_2=ttk.Frame(self.marco_explaracion)
        self.marco_explaracion_contenido_2.grid(row=2,column=0,pady=5,padx=5,sticky=(W, E))

        lcabeza=Label(self.marco_explaracion_contenido_2, text='Cabeza').grid(row=0, column=0)

        self.cabeza=StringVar()
        self.cabezasp = ttk.Spinbox(self.marco_explaracion_contenido_2, from_=1.0, to=100.0, textvariable=self.cabeza)
        self.cabezasp.grid(row=0,column=1)

        loido=Label(self.marco_explaracion_contenido_2, text='Oido').grid(row=0, column=2)

        self.oido=StringVar()
        self.odiosp = ttk.Spinbox(self.marco_explaracion_contenido_2, from_=1.0, to=100.0, textvariable=self.oido)
        self.odiosp.grid(row=0,column=3)

        lojos=Label(self.marco_explaracion_contenido_2, text='Ojos').grid(row=0, column=4)

        self.ojos=StringVar()
        self.ojossp = ttk.Spinbox(self.marco_explaracion_contenido_2, from_=1.0, to=100.0, textvariable=self.ojos)
        self.ojossp.grid(row=0,column=5)

        lnariz=Label(self.marco_explaracion_contenido_2, text='Nariz').grid(row=1, column=0)

        self.nariz=StringVar()
        self.narizsp = ttk.Spinbox(self.marco_explaracion_contenido_2, from_=1.0, to=100.0, textvariable=self.nariz)
        self.narizsp.grid(row=1,column=1)

        lboca=Label(self.marco_explaracion_contenido_2, text='Boca').grid(row=1, column=2)

        self.boca=StringVar()
        self.bocasp = ttk.Spinbox(self.marco_explaracion_contenido_2, from_=1.0, to=100.0, textvariable=self.boca)
        self.bocasp.grid(row=1,column=3)

        lcuello=Label(self.marco_explaracion_contenido_2, text='Cuello').grid(row=1, column=4)

        self.cuello=StringVar()
        self.cuellosp = ttk.Spinbox(self.marco_explaracion_contenido_2, from_=1.0, to=100.0, textvariable=self.cuello)
        self.cuellosp.grid(row=1,column=5)

        ltorax=Label(self.marco_explaracion_contenido_2, text='Torax').grid(row=2, column=0)

        self.torax=StringVar()
        self.toraxsp = ttk.Spinbox(self.marco_explaracion_contenido_2, from_=1.0, to=100.0, textvariable=self.torax)
        self.toraxsp.grid(row=2,column=1)

        lpulmones=Label(self.marco_explaracion_contenido_2, text='Pulmones').grid(row=2, column=2)

        self.pulmones=StringVar()
        self.pulmonessp = ttk.Spinbox(self.marco_explaracion_contenido_2, from_=1.0, to=100.0, textvariable=self.pulmones)
        self.pulmonessp.grid(row=2,column=3)

        lcorazon=Label(self.marco_explaracion_contenido_2, text='Corazon').grid(row=2, column=4)

        self.corazon=StringVar()
        self.corazonsp = ttk.Spinbox(self.marco_explaracion_contenido_2, from_=1.0, to=100.0, textvariable=self.corazon)
        self.corazonsp.grid(row=2,column=5)

        labdomen=Label(self.marco_explaracion_contenido_2, text='Abdomen').grid(row=3, column=0)

        self.abdomen=StringVar()
        self.abdomensp = ttk.Spinbox(self.marco_explaracion_contenido_2, from_=1.0, to=100.0, textvariable=self.abdomen)
        self.abdomensp.grid(row=3,column=1)

        lmsss=Label(self.marco_explaracion_contenido_2, text='Ms Ss').grid(row=3, column=2)

        self.msss=StringVar()
        self.mssssp = ttk.Spinbox(self.marco_explaracion_contenido_2, from_=1.0, to=100.0, textvariable=self.msss)
        self.mssssp.grid(row=3,column=3)

        lmsis=ttk.Label(self.marco_explaracion_contenido_2, text='MS Is').grid(row=3, column=4)

        self.msis=StringVar()
        self.msissp = ttk.Spinbox(self.marco_explaracion_contenido_2, from_=1.0, to=100.0, textvariable=self.msis)
        self.msissp.grid(row=3,column=5)
        
        '''
        #LABORATORIS
        '''

        title_exploracion=ttk.Label(self.marco_explaracion, text='LABORATORIOS')
        title_exploracion.grid(row=3,column=0,pady=5,padx=5,sticky=(W, E))

        self.marco_exp_con_lab=ttk.Frame(self.marco_explaracion)
        self.marco_exp_con_lab.grid(row=4,column=0,pady=5,padx=5,sticky=(W, E))

        lhcto=ttk.Label(self.marco_exp_con_lab, text='Hcto').grid(row=0, column=0)

        self.hcto=StringVar()
        self.hctosp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.hcto)
        self.hctosp.grid(row=0,column=1)

        tp=ttk.Label(self.marco_exp_con_lab, text='TP').grid(row=0, column=2)

        self.tp=StringVar()
        self.tpsp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.tp)
        self.tpsp.grid(row=0,column=3)

        Label(self.marco_exp_con_lab, text='HIV').grid(row=0, column=4)

        self.hiv=StringVar()
        self.hivsp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.hiv)
        self.hivsp.grid(row=0,column=5)

        Label(self.marco_exp_con_lab, text='Glicemia').grid(row=1, column=0)

        self.glicemia=StringVar()
        self.glicemiasp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.glicemia)
        self.glicemiasp.grid(row=1,column=1)

        Label(self.marco_exp_con_lab, text='VDRL').grid(row=1, column=2)

        self.vdrl=StringVar()
        self.vdrlsp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.vdrl)
        self.vdrlsp.grid(row=1,column=3)


        Label(self.marco_exp_con_lab, text='% Hb').grid(row=1, column=4)

        self.hb=StringVar()
        self.hbsp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.hb)
        self.hbsp.grid(row=1,column=5)

        Label(self.marco_exp_con_lab, text='TPT').grid(row=2, column=0)

        self.tpt=StringVar()
        self.tptsp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.tpt)
        self.tptsp.grid(row=2,column=1)

        Label(self.marco_exp_con_lab, text='HCV').grid(row=2, column=2)

        self.hcv=StringVar()
        self.hvcsp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.hcv)
        self.hvcsp.grid(row=2,column=3)

        Label(self.marco_exp_con_lab, text='Urea').grid(row=2, column=4)

        self.urea=StringVar()
        self.ureasp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.urea)
        self.ureasp.grid(row=2,column=5)

        lmsis=ttk.Label(self.marco_exp_con_lab, text='ALT').grid(row=3, column=0)

        self.alt=StringVar()
        self.altsp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.alt)
        self.altsp.grid(row=3,column=1)

        Label(self.marco_exp_con_lab, text='gr/dl. Tipf').grid(row=3, column=2)

        self.tipf=StringVar()
        self.tipfsp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.tipf)
        self.tipfsp.grid(row=3,column=3)

        Label(self.marco_exp_con_lab, text='INR').grid(row=3, column=4)

        self.inr=StringVar()
        self.inrsp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.inr)
        self.inrsp.grid(row=3,column=5)

        Label(self.marco_exp_con_lab, text='Hbsag').grid(row=4, column=0)

        self.hbsag=StringVar()
        self.hbsagsp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.hbsag)
        self.hbsagsp.grid(row=4,column=1)

        Label(self.marco_exp_con_lab, text='Creatinina').grid(row=4, column=2)

        self.creatinina=StringVar()
        self.creatininasp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.creatinina)
        self.creatininasp.grid(row=4,column=3)

        Label(self.marco_exp_con_lab, text='AST').grid(row=4, column=4)

        self.ast=StringVar()
        self.astsp = ttk.Spinbox(self.marco_exp_con_lab, from_=1.0, to=100.0, textvariable=self.ast)
        self.astsp.grid(row=4,column=5)

    def anestecia_sangre(self):
        self.marco_explaracion=Frame(self)
        self.marco_explaracion.grid(row=1,column=1,pady=5,padx=5,sticky=(W, E))
        self.marco_explaracion.config(bg='#314252')

        self.marco_explaracion_contenido=ttk.Frame(self.marco_explaracion)
        self.marco_explaracion_contenido.grid(row=1,column=0,pady=5,padx=5,sticky=(W, E))

        Label(self.marco_explaracion, text='Tipo de anestecia').grid(row=0,column=0,pady=5,padx=5,sticky=(W, E))
        self.anestesia=StringVar()
        self.anestesiabx=Entry(self.marco_explaracion)
        self.anestesiabx.grid(row=0,column=1)

        Label(self.marco_explaracion, text="Reserva de Sangre").grid(row=1,column=0,pady=5,padx=5,sticky=(W, E))
        self.sangre=StringVar()
        self.sangrebx=Entry(self.marco_explaracion)
        self.sangrebx.grid(row=1,column=1)

    def evaluaciones(self):
        self.marco_explaracion=Frame(self)
        self.marco_explaracion.grid(row=2,column=0,columnspan=2,pady=5,padx=5,sticky=(W, E))
        self.marco_explaracion.config(bg='#314252')

        

        Label(self.marco_explaracion, text='Tipo de anestecia').grid(row=0,column=0,pady=5,padx=5,sticky=(W, E))
        self.anestesia=StringVar()
        self.anestesiabx=Entry(self.marco_explaracion)
        self.anestesiabx.grid(row=0,column=1,columnspan=2)

        Label(self.marco_explaracion, text="Reserva de Sangre").grid(row=0,column=3,pady=5,padx=5,sticky=(W, E))
        self.sangre=StringVar()
        self.sangrebx=Entry(self.marco_explaracion)
        self.sangrebx.grid(row=0,column=4, columnspan=2)

        Label(self.marco_explaracion, text="Observaciones").grid(row=1,column=0,pady=5,padx=5,sticky=(W, E))
        self.observacion=StringVar()
        self.observacionbx=Entry(self.marco_explaracion)
        self.observacionbx.grid(row=1,column=1, columnspan=2)


        for self.child in self.marco_exp_con_lab.winfo_children(): 
            self.child.grid_configure(pady=1,padx=1,sticky=(W))

        for self.child in self.marco_explaracion_contenido.winfo_children():
            self.child.grid_configure(pady=2,padx=1,sticky=(W,E))
        for self.child in self.marco_explaracion_contenido_2.winfo_children():
            self.child.grid_configure(pady=2,padx=1,sticky=(W,E))

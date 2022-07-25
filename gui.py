
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING
from formulario import Formulario
class center_mixin:
    def center(self):
        self.update()
        h=self.winfo_height()
        w=self.winfo_width()
        ws=self.winfo_screenwidth()
        hs=self.winfo_screenheight()
        x=int(ws/2-w/2)
        y=int(hs/2-h/2)
        self.geometry(f"{w}x{h}+{x}x{y}")        

class inicio(Tk, center_mixin):
    def __init__(self):
        super().__init__()
        self.title("Evaluacion Paciente")
        self.menu()

    def menu(self):
        raiz = Frame(self)
        raiz.grid(row=0,column=0)

        opciones=Frame(raiz)
        opciones.grid(row=0,column=0)
        
        Button(opciones, text="NUEVO",command=self.nuevo).grid(row=0,column=0,pady=5,padx=5)

        Button(opciones, text="BUSCAR", command=self.editar).grid(row=1,column=0,pady=5,padx=5)
        
        Button(opciones, text="EDITAR").grid(row=2,column=0,pady=5,padx=5)

        Button(opciones, text="BORRAR").grid(row=3,column=0,pady=5,padx=5)

        vista= Frame(raiz)
        vista.grid(row=0,column=1)

        Label(vista,text='LISTA DE PACIENTES').grid(column=0,row=0)

        lista=ttk.Treeview(vista,columns=(1,2,3),show='headings',height='10')
        estilo=ttk.Style()
        estilo.theme_use('clam')
        estilo.configure("Treeview.Headings")

        lista.heading(1,text='ID')
        lista.heading(2,text='Nombre')
        lista.heading(3,text='Paciente')
        lista.column(2,anchor=CENTER)
        lista.grid(row=1,column=0,pady=5,padx=5)

        scroll=ttk.Scrollbar(vista,orient=VERTICAL,command=lista.yview)
        scroll.grid(row=1, column=1,sticky=(N,S))
        lista['yscrollcommand']=scroll.set
    
    def borrar(self):
        paciente=self.lista.focus()

    def editar(self):
        pass
    def nuevo(self):
        Formulario(self)
         
if __name__ == "__main__":
    app=inicio()
    app.mainloop()
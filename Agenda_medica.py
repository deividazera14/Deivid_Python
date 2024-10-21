from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime
import customtkinter as ctk
from tkinter import messagebox

# Configuração do banco de dados
engine = create_engine('sqlite:///agenda_medica.db', echo=True)
Base = declarative_base()

# Definindo a tabela de consultas
class Consulta(Base):
    __tablename__ = 'consultas'

    id = Column(Integer, primary_key=True)
    paciente = Column(String, nullable=False)
    data_hora = Column(DateTime, nullable=False)
    descricao = Column(String, nullable=False)
    status = Column(String, default='Agendada')

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criar a sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Configuração da interface CustomTkinter
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

class AgendaMedicaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Agenda Médica")
        self.geometry("400x400")

        # Campos para entrada de dados
        self.label_paciente = ctk.CTkLabel(self, text="Nome do Paciente:")
        self.label_paciente.pack(pady=10)
        self.entry_paciente = ctk.CTkEntry(self)
        self.entry_paciente.pack(pady=5)

        self.label_data_hora = ctk.CTkLabel(self, text="Data e Hora (AAAA-MM-DD HH:MM):")
        self.label_data_hora.pack(pady=10)
        self.entry_data_hora = ctk.CTkEntry(self)
        self.entry_data_hora.pack(pady=5)

        self.label_descricao = ctk.CTkLabel(self, text="Descrição da Consulta:")
        self.label_descricao.pack(pady=10)
        self.entry_descricao = ctk.CTkEntry(self)
        self.entry_descricao.pack(pady=5)

        # Botão para salvar a consulta
        self.button_agendar = ctk.CTkButton(self, text="Agendar Consulta", command=self.agendar_consulta)
        self.button_agendar.pack(pady=20)

    def agendar_consulta(self):
        # Obter valores dos campos
        paciente = self.entry_paciente.get()
        data_hora_str = self.entry_data_hora.get()
        descricao = self.entry_descricao.get()

        # Converter a string para um objeto datetime
        try:
            data_hora = datetime.datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Erro", "Data e hora inválidas. Use o formato AAAA-MM-DD HH:MM.")
            return

        # Criar nova consulta
        nova_consulta = Consulta(paciente=paciente, data_hora=data_hora, descricao=descricao)
        session.add(nova_consulta)
        session.commit()

        messagebox.showinfo("Sucesso", "Consulta agendada com sucesso!")
        self.limpar_campos()

    def limpar_campos(self):
        self.entry_paciente.delete(0, 'end')
        self.entry_data_hora.delete(0, 'end')
        self.entry_descricao.delete(0, 'end')

# Inicializar a aplicação
if __name__ == "__main__":
    app = AgendaMedicaApp()
    app.mainloop()

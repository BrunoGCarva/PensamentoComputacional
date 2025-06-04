"""
Sistema de Cadastro de Usuários.
IENH - 2025/01
Aluno : Bruno Carvalho

Arquivo que contém, as classes que representam os modelos do banco de dados.

classes:
    - Usuario: Classe que representa a tabela de usuários no banco de dados.
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Usuario(Base):
    """
    classe que representa a tabela de usuários no banco de dados.
        id (int): ID do usuário (chave primária)
        nome (str): Nome do usuário(tamanho máximo de 50 caracteres)
        idade (int): Idade do usuário
    retorno:
        none
    """
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer)
def __repr__(self):
    return f"<Usuario(nome='{self.nome}', idade={self.idade})>"

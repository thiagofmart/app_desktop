from imports_db import *


engine = create_engine('sqlite:///solar.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
#metadata = MetaData(bind=engine)

class tipos_de_usuarios(Base):
	"""
	tipos_de_usuarios = Table('Tipos_de_Usuarios', metadata,
		Column('Tipo', String(30), primary_key=True),
		Column('Permissões', JSON)
	)
	"""
	__tablename__ = 'Tipos de Usuarios'
	Tipo = Column(String(30), primary_key=True)
	Permissões = Column(JSON)
	def __repr__(self):
		return f'{self.Tipo}^{self.Permissões}'
class usuarios(Base):
	"""
	usuarios = Table('Usuarios', metadata,
		Column('Usuario', String(30), primary_key=True),
		Column('Senha', String(30)),
		Column('Tipo', ForeignKey('Tipos_de_Usuarios.Tipo')),
		)
	"""
	__tablename__ = 'Usuarios'
	Usuario = Column(String(30), primary_key=True)
	Senha = Column(String(30))
	Tipo = Column(ForeignKey('Tipos de Usuarios.Tipo'))
	def __repr__(self):
		return f'{self.Usuario}^{self.Senha}^{self.Tipo}'

class atividades_de_usuarios(Base):
	"""
	atividades_de_usuarios = Table('Atividades_de_Usuarios', metadata,
		Column('Usuario', ForeignKey('Usuarios.Usuario')),
		Column('Ação', String(20)),
		Column('Tabela', String(50)),
		Column('Data', DateTime, default=datetime.now),
		)
	"""
	__tablename__ = 'Atividades de Usuarios'
	Id = Column(Integer, primary_key=True)
	Usuario = Column(ForeignKey('Usuarios.Usuario'))
	Ação = Column(String(20))
	Tabela = Column(String(50))
	Data = Column(DateTime, default=datetime.now)
class historico_de_acessos(Base):
	"""
	historico_de_acessos = Table('Histórico_de_Acesso', metadata,
		Column('Usuario', ForeignKey('Usuarios.Usuario')),
		Column('Status', String(20)),
		Column('Data e Horário', DateTime, default=datetime.now),
		)
	"""
	__tablename__='Histórico de Acessos'
	Id = Column(Integer, primary_key=True)
	Usuario = Column(ForeignKey('Usuarios.Usuario'))
	Status = Column(String(20))
	Data_e_Horário = Column(DateTime, default=datetime.now)
	def __repr__(self):
		return f'{self.Id}^{self.Usuario}^{self.Status}^{self.Data_e_Horário}'
################################################################################
class tipos_de_os(Base):
	"""
	tipos_de_os = Table('Tipos de OS', metadata,
		Column('Tipo', String(20), primary_key=True),
		Column('Perguntas', JSON)
		)
	"""
	__tablename__ = 'Tipos de OS'
	Tipo = Column(String(20), primary_key=True)
	Perguntas = Column(JSON)

class OS(Base):
	"""
	os = Table('Ordem de Serviço', metadata,
		Column('Tipo', ForeignKey()),
		Column('Ordenador', ForeignKey('Usuarios.Usuario')),
		Column('Realizador', ForeignKey('Usuarios.Usuario')),
		Column('Status', String(30)),
		Column('Data da Ordem', DateTime, default=datetime.now),
		Column('Data da Realização', DateTime),
		)
	"""
	__tablename__ = 'Ordem de Serviço'
	Id = Column(Integer, primary_key=True)
	Tipo = Column(ForeignKey('Tipos de OS.Tipo'))
	Ordenador = Column(ForeignKey('Usuarios.Usuario'))
	Realizador = Column(ForeignKey('Usuarios.Usuario'))
	Status = Column(String(30))
	Data_da_Ordem = Column(DateTime, default=datetime.now)
	Data_da_Realização = Column(DateTime)

tables = {
	'Gestão de Usuarios':[
		usuarios, tipos_de_usuarios,
		atividades_de_usuarios, historico_de_acessos,
		],
	#'Estoque':{'Veículos':usuarios, 'Materiais':tipos_de_usuarios},
	#'Movimentação':{'Veículos':None, 'Materiais':None}
}
Base.metadata.create_all(engine)
#session.add(tipos_de_usuarios(Tipo='teste', Permissões={'':''},))
#session.add(usuarios(Usuario='', Senha='', Tipo='teste'))
#session.commit()
if __name__ == '__main__':
	pass
	#

	#metadata.create_all()
	# ins1 = tipos_de_usuarios.insert()
	# ins1.execute({'Tipo':'TESTE', 'Permissões':{'Gestão de Usuarios': 'a'}})
	# ins2 = usuarios.insert()
	# ins2.execute({'Usuario':'', 'Senha':'', 'Tipo': 'TESTE'})

### Create User
# https://docs.sqlalchemy.org/en/14/core/tutorial.html#insert-expressions
#conn = engine.connect()
# ins.execute({'usuario':'Erick', 'senha':'EKSOLADM', 'tipo': 'ADM'})


### query
#result = conn.execute(select(users))
#result = conn.execute(select(users.c.usuario, users.c.senha))
#row = result.fetchone()
#print(row._mapping['usuario'], row._mapping['senha'])

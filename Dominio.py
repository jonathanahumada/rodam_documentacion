from sqlalchemy.orm import relationship,sessionmaker
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,DateTime, Boolean, Float, Table
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Sector(Base):
    __tablename__="sector"
    id_sector = Column(Integer, primary_key= True)
    nom_sector = Column(String)

    def __repr__(self):
        return "<Sector (id_sector='%s', nom_sector='%s')>" % (self.id_sector, self.nom_sector)

class Equipo(Base):
    __tablename__= "equipo"
    id_equipo = Column(Integer, primary_key=True)
    nom_equipo= Column(String)
    ref_documental = Column(String)
    ultima_verificacion = Column(DateTime())

    def __repr__(self):
        return "<Equipo(id='%s', nombre='%s')>" % (self.id_equipo, self.nom_equipo)

metodo_equipos = Table('metodo_equipos',
                                   Base.metadata,
                                    Column('id_metodo',Integer,
                                           ForeignKey('metodo.id_metodo')),
                                    Column('id_equipo',Integer,
                                           ForeignKey('equipo.id_equipo'))
                                    )

class Metodo(Base):
    __tablename__="metodo"
    id_metodo = Column(Integer, primary_key=True)
    nom_metodo = Column(String)
    desc_metodo = Column(String)
    ref_documental = Column(String)
    observaciones= Column(String)
    material = Column(String)
    equipos = relationship("Equipo",
                           secondary="metodo_equipos")

    def __repr__(self):
        return "<Metodo(id='%s', nombre='%s')>" % (self.id_metodo, self.nom_metodo)


                           
class Utiliza(Base):
    __tablename__ = 'utiliza'
    id_utiliza = Column(Integer, primary_key= True)
    id_analisis = Column(Integer, ForeignKey('analisis.id_analisis'), primary_key= True)
    id_metodo = Column(Integer, ForeignKey('metodo.id_metodo'), primary_key= True)
    metodo = relationship("Metodo")

    def __repr__(self):
        return "<Utiliza(id_utiliza='%d', id_analisis= '%d',id_metodo='%d')>" % ( self.id_utiliza,
                                                                                  self.id_analisis,
                                                                                  self.id_metodo)
        


class Analisis(Base):
    __tablename__="analisis"
    id_analisis = Column(Integer, primary_key=True)
    nom_analisis = Column(String, nullable=False)
    id_sector = Column(Integer, ForeignKey("sector.id_sector"),nullable=False)
    descripcion = Column(String)
    ref_documental = Column(String)
    metodos = relationship('Utiliza')
 

    def __repr__(self):
        return "<Analisis(id='%s', nombre='%s')>" % (self.id_analisis, self.nom_analisis)    
    
                       
class Muestra(Base):
    __tablename__="muestra"
    id_muestra = Column(Integer, primary_key=True)
    id_producto = Column(Integer,
                         ForeignKey("producto.id_producto"))
    id_origen = Column(Integer,
                       ForeignKey("origen.id_origen"))
    presentacion = Column(String)
    lote_muestra = Column(String, nullable=False)
    ingreso_muestra = Column(DateTime(), default=datetime.now)
    descripcion = Column(String, nullable=True)
    tamano_muestra = Column(Integer, nullable=True)
    unidades_tamano =  Column(String)
    solicitado = Column(String)
    aceptada = Column(Boolean, nullable=True)
    registra= Column(Integer, ForeignKey('miembro_rodam.id_miembro'))
    verifica = Column(Integer, ForeignKey('miembro_rodam.id_miembro'))
    concepto = Column(Boolean, nullable=True)
    aprueba = Column(String, nullable=True)
    fecha_final = Column(DateTime, nullable=True)
    factura = Column(Integer, nullable=True)
    observaciones_muestra_inicio = Column(String, nullable=True)
    observaciones_muestra_fin = Column(String, nullable=True)
    producto = relationship("Producto", back_populates="muestras")


    def __repr__(self):
        return "<Muestra(id='%s', lote='%s')>" % (self.id_muestra, self.lote_muestra)




class Agrupacion(Base):
    __tablename__ = 'agrupacion'
    id_agrupacion = Column(Integer, primary_key= True)
    id_grupo = Column(Integer, ForeignKey('grupo.id_grupo'), primary_key= True)
    id_analisis = Column(Integer, ForeignKey('analisis.id_analisis'), primary_key= True)
    analisis = relationship("Analisis")

        
    def __repr__(self):
        return "<Agrupacion(id_agrupa='%d', id_grupo= '%d',id_analisis='%d')>" % ( self.id_agrupa,
                                                                               self.id_grupo,
                                                                               self.id_analisis)
    
    
class Grupo(Base):
    __tablename__="grupo"
    id_grupo = Column(Integer, primary_key=True)
    nom_grupo = Column(String)
    desc_grupo = Column(String)
    analisis = relationship("Agrupacion")
 

    
    def __repr__(self):
        return "<Grupo(id_grupo='%d' nom_grupo='%s')>" % ( self.id_grupo,self.nom_grupo)
    


    
class Especificacion(Base):
    __tablename__ = "especificacion"
    id_especificacion= Column(Integer, primary_key=True)
    id_debe_tener = Column(Integer, ForeignKey("debe_tener.id_debe_tener"))
    id_utiliza = Column(Integer,ForeignKey('utiliza.id_utiliza'))
    id_material_de_control = Column(Integer, ForeignKey('material_de_control.id_material'), default=1)
    valor = Column(String)
    
 

    def __repr__(self):
        return "<Especificacion(producto='%s',analisis='%s', metodo='%s',descripcion='%s')>" % (
            self.id_producto,self.id_analisis,self.id_metodo,self.descripcion)    
  


class Debe_tener(Base):
    __tablename__ = 'debe_tener'
    id_debe_tener = Column(Integer, primary_key= True)
    id_producto = Column(Integer, ForeignKey('producto.id_producto'), primary_key = True)
    id_grupo = Column(Integer, ForeignKey('grupo.id_grupo'), primary_key = True)
    grupo = relationship("Grupo")
    
    
class Producto(Base):
    __tablename__='producto'
    id_producto = Column(Integer, primary_key=True)
    id_cliente = Column(Integer,
                        ForeignKey('cliente.id_cliente'),
                        nullable=False)
    id_sector = Column(Integer,
                       ForeignKey('sector.id_sector'),
                       nullable=False)
    forma_farmaceutica = Column(String)
    nom_producto = Column(String)

    grupos = relationship("Debe_tener")
    muestras = relationship("Muestra",
                            order_by=Muestra.id_muestra,
                            back_populates="producto")

    sector= relationship("Sector",
                         order_by=Sector.id_sector)

    cliente = relationship("Cliente",
                           back_populates="producto")


    def __repr__(self):
        return "<Producto(id='%s', nombre='%s')>" % (self.id_producto, self.nom_producto)



class Lectura(Base):
    __tablename__="lectura"
    id_lectura = Column(Integer, primary_key= True)
    id_especificacion=Column(Integer, ForeignKey("especificacion.id_especificacion"))
    id_muestra = Column(Integer, ForeignKey("muestra.id_muestra"))
    valor_lectura = Column(String)
    fecha_lectura = Column(DateTime, default=datetime.now)
    lote_medio = Column(String)
    registra = Column(Integer, ForeignKey("miembro_rodam.id_miembro"))
    verifica = Column(Integer, ForeignKey("miembro_rodam.id_miembro"))
    concepto = Column(Boolean)
    observaciones = Column(String)


class Control_Material(Base):
    __tablename__= 'control_material'
    id_control_material = Column(Integer, primary_key = True) 
    lote_material = Column(String)
    id_material_de_control = Column(String)
    lote_material_de_control = Column(String)
    especificacion = Column(String)
    resultado = Column(String)
    fecha_resultado = Column(DateTime, default=datetime.now)
    concepto = Column(Boolean)
    
class Cliente(Base):
    __tablename__="cliente"
    id_cliente = Column(Integer,primary_key=True, unique=True)
    id_empresa = Column(Integer, ForeignKey("empresa.id_empresa"), primary_key= True)
    retencion = Column(Float)
    IVA = Column(Float)
    ICA = Column(Float)
    fecha_inicio = Column(DateTime, default=datetime.now)
    fecha_final = Column(DateTime)
    descripcion = Column(String)
    empresa = relationship("Empresa")
    producto = relationship("Producto", back_populates="cliente")
    def __repr__(self):
        return "<Cliente(id='%s', id_empresa='%s')>" % (self.id_cliente, self.id_empresa)


class Empresa(Base):
    __tablename__="empresa"
    id_empresa = Column(Integer, primary_key=True)
    id_ciudad = Column(Integer, ForeignKey("ciudad.id_ciudad"))
    nit_empresa = Column(Integer, nullable=True)
    cod_verificacion = Column(Integer, nullable=True)
    nom_empresa = Column(String,nullable=True)
    direccion = Column(String,nullable=True)
    pagina = Column(String,nullable=True)
    correo = Column(String,nullable=True)
    descripcion = Column(String,nullable=True)
    observaciones = Column (String,nullable=True)
    def __repr__(self):
        return "<Empresa(id='%s', nombre='%s')>" % (self.id_empresa, self.nom_empresa)



class Ciudad(Base):
    __tablename__="ciudad"
    id_ciudad = Column(Integer, primary_key=True)
    nom_ciudad = Column(String, nullable=True)
    indicativo = Column(String, nullable=True)
    def __repr__(self):
        return "<Ciudad(id='%s', nombre='%s')>" % (self.id_ciudad, self.nom_ciudad)



    

class Presentacion(Base):
    __tablename__="presentacion"
    id_presentacion = Column(Integer, primary_key=True)
    nom_presentacion = Column(String, nullable=True)
    descripcion_presentacion =  Column(String, nullable=True)

    def __repr__(self):
        return "Presentacion<id= '%s', nom_presentación='%s'>" %(self.id_presentación, self.nom_presentacion)

class Cargo(Base):
    __tablename__="cargo"
    id_cargo = Column(Integer, primary_key= True)
    nom_cargo= Column(String, nullable=False)
    jefe = Column(Integer)
    reemplazo = Column(Integer, ForeignKey("cargo.id_cargo"))
    observaciones = Column(String)
    def __repr__(self):
        return "Cargo<id='%s', nom_cargo='%s'>" %(self.id_cargo, self.nom_cargo)

class MiembroRodam(Base):
    __tablename__="miembro_rodam"
    id_miembro = Column(Integer, primary_key=True)
    nom_miembro = Column(String)
    id_cargo = Column(Integer, ForeignKey("cargo.id_cargo"))
    ingreso = Column(DateTime)
    salida = Column(DateTime)


class Origen(Base):
    __tablename__="origen"
    id_origen = Column(Integer, primary_key=True)
    nom_origen = Column(String, nullable=False)
    desc_origen = Column(String, nullable=True)

    def __repr__(self):
        return "Origen<id= '%s', nom_origen='%s'>" %(self.id_origen, self.nom_origen)


class MaterialDeControl(Base):
    __tablename__= 'material_de_control'
    id_material = Column(Integer, primary_key=True)
    nom_material = Column(String)
    

class Certificado(Base):
    __tablename__= 'certificado'
    id_certificado = Column(Integer, primary_key=True)
    id_muestra = Column(Integer, ForeignKey("muestra.id_muestra"))
    fecha_creacion =  Column(DateTime, nullable=False,default= datetime.now)
    ultima_descarga = Column(DateTime)
    aprueba =  Column(Integer, ForeignKey("miembro_rodam.id_miembro"))

    def __repr__(self):
        return "Certificado<id= '%s', muestra= '%s'>" % (self.id_certificado, self.id_muestra)


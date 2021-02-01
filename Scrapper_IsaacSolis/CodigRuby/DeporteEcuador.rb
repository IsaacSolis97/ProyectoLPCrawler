

class DeporteEcuador
    attr_accessor :titulo, :link, :imagen, :descripcion, :fecha
  
    def initialize(titulo, link, imagen, descripcion, fecha)
      @titulo = titulo
      @link = link
      @imagen = imagen
      @descripcion = descripcion
      @fecha = fecha
    end
    def registrar( ficherocsv)
      ficherocsv << [self.titulo, self.link, self.imagen, self.descripcion, self.fecha]
    end
  end

  class InformacionGeneralLiga
    attr_accessor :liga, :jornada, :fecha, :noGoles, :porceGoles, :amarillas1, :amarillas2, :rojas, :fueraJuego, :paradas
  
    def initialize(liga,jornada,fecha, noGoles,porceGoles,amarillas1,amarillas2,rojas,fueraJuego,paradas
    )
      @liga = liga
      @jornada = jornada
      @fecha = fecha
      @noGoles = noGoles
      @porceGoles = porceGoles
      @amarillas1 = amarillas1
      @amarillas2 = amarillas2
      @rojas = rojas
      @fueraJuego = fueraJuego
      @paradas = paradas
    end
    def registrar( ficherocsv)
      ficherocsv << [self.liga,self.jornada,self.fecha, self.noGoles,self.porceGoles,self.amarillas1,self.amarillas2,self.rojas,self.fueraJuego,self.paradas]
    end
  end

  class MejoresJugadores
    attr_accessor :liga, :jornada, :equipo, :nombre_jugador, :noGoles, :posicion
  
    def initialize(liga,jornada,equipo,nombre_jugador, noGoles
    )
      @liga = liga
      @jornada = jornada
      @equipo = equipo
      @nombre_jugador = nombre_jugador
      @noGoles = noGoles
    end
    def registrar( ficherocsv)
      ficherocsv << [self.liga,self.jornada,self.equipo,self.nombre_jugador, self.noGoles]
    end
  end

  class ResultadosJuegos
    attr_accessor :liga, :jornada, :equipo1, :equipo2, :noGoles1, :noGoles2
  
    def initialize(liga,jornada,equipo1,equipo2, noGoles1,noGoles2
    )
      @liga = liga
      @jornada = jornada
      @equipo1 = equipo1
      @equipo2 = equipo2
      @noGoles1 = noGoles1
      @noGoles2 = noGoles2
    end
    def registrar( ficherocsv)
      ficherocsv << [self.liga,self.jornada,self.equipo1,self.equipo2, self.noGoles1,self.noGoles2]
    end
  end
   
  
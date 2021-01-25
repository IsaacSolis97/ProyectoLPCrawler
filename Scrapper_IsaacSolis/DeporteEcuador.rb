

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
  
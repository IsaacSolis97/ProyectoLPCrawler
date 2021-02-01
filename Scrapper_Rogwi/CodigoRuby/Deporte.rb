=begin 
 clase Course, con propiedades básicas: nombre, link de imagen, link de url (si fuera posible), descripción, fecha, institución (universidad, empresa); definir los métodos getters/setters para estos atributos, implementar el método registrar que recibe todos los atributos y los guarda en un archivo CSV.
=end

class Deporte
    attr_accessor :nombreNoticia, :link, :categoria, :resumen, :fecha
  
    def initialize(nombreNoticia, link, categoria, resumen, fecha)
      @nombreNoticia = nombreNoticia
      @link = link
      @categoria = categoria
      @resumen = resumen
      @fecha = fecha
    end
    def registrar( ficherocsv)
      ficherocsv << [self.nombreNoticia, self.link, self.categoria, self.resumen, self.fecha]
      
    end
  end
  
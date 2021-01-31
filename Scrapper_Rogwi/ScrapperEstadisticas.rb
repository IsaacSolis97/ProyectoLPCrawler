=begin
Crear una clase Scraper, con un método extraer(url) que recibe una URL de cursos de MiriadaX. Utilice varias gemas para la extracción de datos de la web, y el uso de la clase Course para almacenar los datos extraídos en el fichero (CSV). Para poder scrapear utilice el url: https://miriadax.net/web/general-navigation/cursos (Enlaces a un sitio externo.)Enlaces a un sitio externo.
=end

#GEMAS
require 'open-uri'
require 'nokogiri'
require 'csv'




class ScrapperEstadisticas
  def initialize
  end

  def extraer(urls)
    
    CSV.open('NBA_RegularSeason.csv', 'wb') do |csv|
      #Creacion de los headers
      csv << %w[Temporada Conferencia Equipo Victorias Derrotas V/D  PuntosPorJuego PuntosRecibidosPorJuego SRS]

      #abrir link de cada temporada
      urls.each do |temporada, url|
        pagina = Nokogiri::HTML(open(url))
        #conferencias
        conferencias = {"este"=>"#confs_standings_E", "oeste"=>"#confs_standings_W"}
        conferencias.each do |llave, valor|
          #tabla de conferecia , hallo cada fila de la tabla
          
          inf = pagina.css(valor).css("tbody").css("tr")
          inf.each do |fila|
            #nombre
            nombreTag = fila.children[0]
            nombre = nombreTag.inner_text
            #victorias
            victorias = fila.children[1].inner_text
            #derrotas
            derrotas = fila.children[2].inner_text
            #balance
            balance = fila.children[3].inner_text
            #puntos por juego
            puntosPorJuego = fila.children[5].inner_text
            #recibidos
            puntosRecibidosPorJuego = fila.children[6].inner_text
            #srs
            srs = fila.children[7].inner_text

            #registro en csv
            csv << [temporada, llave, nombre, victorias, derrotas, balance, puntosPorJuego, puntosRecibidosPorJuego, srs]

            
          end
        end  
      end
    end

  end
end
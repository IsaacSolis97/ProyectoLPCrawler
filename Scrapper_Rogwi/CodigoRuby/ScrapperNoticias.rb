=begin
Crear una clase Scraper, con un método extraer(url) que recibe una URL de cursos de MiriadaX. Utilice varias gemas para la extracción de datos de la web, y el uso de la clase Course para almacenar los datos extraídos en el fichero (CSV). Para poder scrapear utilice el url: https://miriadax.net/web/general-navigation/cursos (Enlaces a un sitio externo.)Enlaces a un sitio externo.
=end

#GEMAS
require 'open-uri'
require 'nokogiri'
require 'csv'
require './Deporte'



class ScrapperNoticias
  def initialize
  end
  def prueba
    puts "prueba"
  end

  def extraer(url)
    
    CSV.open('deportes_Rogwi.csv', 'wb') do |csv|
      #nombre
      csv << %w[Titular  Link  Categoria  Resumen  Fecha]
      pagina = Nokogiri::HTML(open(url))
      inf = pagina.css(".pntc")
      inf.each do |noticia|
        #categoria
        subtitleTag = noticia.css(".subtitle");
        subitulo =""
        if subtitleTag!=nil
          subtituloA =subtitleTag.css("a")
          if subtituloA!=nil
            subtitulo = subtituloA.inner_text 
          else
            subtitulo = subtitleTag.inner_text
          end 
        end
        #titulo
        tituloTag = noticia.css(".title")
        titulo = ""
        #href
        a = tituloTag.css("a")
        link=""
        if a!=nil
          href= a.attribute("href")
          if href!=nil
            link=href.value
            titulo=a.inner_text
          end  
        else 
          titulo= tituloTag.inner_text
        end
        #resumen
        resumenTag = noticia.css(".txt")
        resumen = ""
        if resumenTag!=nil 
          resumen = resumenTag.inner_text
        end

        #fecha
        fechaTag = noticia.css(".fecha")
        fecha=""
        if fechaTag!=nil 
          fecha = fechaTag.inner_text
        end

        objDeporte =  Deporte.new(titulo,link, subtitulo, resumen, fecha)
        objDeporte.registrar(csv)

        
      end
    end

  end
end
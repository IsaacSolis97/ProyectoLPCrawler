
require 'open-uri'
require 'nokogiri'
require 'csv'
require './DeporteEcuador'



class Scraper
  def initialize
  end

  def extraer(url)
    
    CSV.open('reporte_Solis.csv', 'wb') do |csv|
      #nombre
      csv << %w[Titulo  Link  Imagen  Descripcion  Fecha]
      noticiasHTML = open(url)
      noticiaRead = noticiasHTML.read
      pagina = Nokogiri::HTML(noticiaRead)
      articulo = pagina.css(".noticia")
      articulo.each do |noticia|
         titulo = ""
         link = ""
         fecha=""
         descripcion = ""
         imagen = ""

         #obtenemos descripcion
         descripcionTag = noticia.css("p")
         if descripcionTag!=nil 
           descripcion = descripcionTag.inner_text
           #obtenemos fecha
           fechaTag = descripcionTag.css("span")
           if fechaTag!=nil 
             fecha = fechaTag.inner_text
           end
         end
        
        

        #obtenemos titulo
         tituloTag = noticia.css("h4")
         tituloSubTag = tituloTag.css("a")
         if tituloSubTag!=nil 
          titulo = tituloSubTag.inner_text
          href= tituloSubTag.attribute("href")
          if href!=nil
            link=href.value
          end  
         end

        #imagen
         imagenTag = noticia.css("a")
         refimagenTag = imagenTag.css("img")
         hrefimagen= refimagenTag.attribute("src")
           if hrefimagen!=nil
             imagen=hrefimagen.value
           end
       
        hola = "papa"
        objDeporteEcuador =  DeporteEcuador.new(titulo,link,imagen,descripcion,fecha)
        objDeporteEcuador.registrar(csv)

        
      end
    end

  end
end

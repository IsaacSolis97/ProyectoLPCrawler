require 'open-uri'
require 'nokogiri'
require 'csv'
require './Noticia'

class Scrapper

  def extraer(url)
    
    CSV.open('datos.csv', 'wb') do |csv|

        csv << %w[Titulo  Link  Resumen]
        noticiasHTML = open(url)
        datos = noticiasHTML.read
        parsed_content = Nokogiri::HTML(datos)
        informacion = parsed_content.css(".view-content")
        informacion.css(".posts").each do |noticia|
        
            titulo = noticia.css("a").inner_text

            partelink = noticia.css("a").attribute("href").value
            link = "https://www.eluniverso.com" + partelink
            
            texto = noticia.css("p").inner_text

            nuevaNoticia = Noticia.new(titulo, link, texto)
            nuevaNoticia.registrar(csv)

        end
    end

  end
end
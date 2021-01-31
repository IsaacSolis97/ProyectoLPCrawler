
require 'open-uri'
require 'nokogiri'
require 'csv'
require './DeporteEcuador'



class ScrapperResultados
  def initialize
  end
  
  def extraerInfoResultado(url)

    CSV.open('informeResultados.csv', 'a') do  |csv|
      link= ""
      liga = ""
      jornada= ""
      equipo1 = ""
      equipo2 = ""
      noGoles1 = ""
      noGoles2 = ""
    
      urlOpen = URI.open(url)
      urlRead = urlOpen.read
      urlNoko = Nokogiri::HTML(urlRead)
      articulo = urlNoko.css(".results")
      #obtenemos las jornadas del menu
      jornadasArticulo = articulo.css(".item")
      jornadasArticulo.each do |valor|
        aJornada = valor.css("a")
        hrefJornada= aJornada.attribute("href")
        linkJornada= hrefJornada.value
        arrlinkJornada = linkJornada.split("/")
        arrURL = url.split("/")
        #obtenemos la jornada y el link de cada jornada, para hacer el scrap dentro de cada una 
        jornada= arrlinkJornada[-1]
        arrURL[-1] = arrlinkJornada[-1]
        link =  "#{arrURL.join('/')}"

        
        #recorremos las jornadas y sacamos la informacion necesaria
        linkOpen = URI.open(link)
        linkRead = linkOpen.read
        linkNoko = Nokogiri::HTML(linkRead)
        linkIndividual = linkNoko.css(".blockpad")
        #obtenmos la liga y la fecha
        h1link = linkIndividual.css("h1")
        alink= h1link.css("a")
        liga = alink.inner_text

        tableResult = linkIndividual.css(".table")
        trResuts = tableResult.css("tr")
        trResuts.each do |columna|
          equipo1 = columna.css(".td1").inner_text
          equipo2 = columna.css(".td3").inner_text
          td2Marcador = columna.css(".td2")
          marcador2 =td2Marcador.inner_text
          aMarcador = td2Marcador.css("a")
          marcador = aMarcador.inner_text

          if marcador2 == nil
            arrMarcador = marcador.split("-")
            noGoles1 = arrMarcador[0]
            noGoles2 = arrMarcador[-1]
          else 
            arrMarcador = marcador2.split("-")
            noGoles1 = arrMarcador[0]
            noGoles2 = arrMarcador[-1]
          end
            
          objDeporteEcuador =  ResultadosJuegos.new(liga,jornada,equipo1,equipo2, noGoles1,noGoles2)
          objDeporteEcuador.registrar(csv)   
        end 
      end
    end
  end
  
end


require 'open-uri'
require 'nokogiri'
require 'csv'
require './DeporteEcuador'



class ScrapperJugadores
  def initialize
  end
  
  def extraerInfoJugadores(url)

    CSV.open('informeJugadores.csv', 'a') do  |csv|
      link= ""
      liga = ""
      jornada= ""
    
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

        jugadorInfo = linkIndividual.css(".jugador")
        infoLista = []
        jugadorInfo.each do |jugador|
            nameJugador = jugador.css(".name").inner_text
            numberJugador = jugador.css(".number").inner_text
            teamJugador = jugador.css(".team").inner_text

            objDeporteEcuador =  MejoresJugadores.new(liga,jornada,teamJugador,nameJugador, numberJugador)
            objDeporteEcuador.registrar(csv)
        end


        
 
=begin
         
=end
      end
    end
  end
  
end

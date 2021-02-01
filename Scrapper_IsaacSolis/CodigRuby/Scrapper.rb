
require 'open-uri'
require 'nokogiri'
require 'csv'
require './DeporteEcuador'



class Scraper
  def initialize
  end
  
  def extraerInfoGeneral(url)

    CSV.open('informacionGeneral.csv', 'a') do  |csv|
      link= ""
      liga = ""
      jornada= ""
      fecha= ""
      noGoles= ""
      porceGoles= ""
      amarillas1= ""
      amarillas2= ""
      rojas= ""
      fueraJuego= ""
      paradas= ""
      
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
        
        datelink= linkIndividual.css(".date")
        textdate = datelink.inner_text  
        arrDate= textdate.split("|")
        fecha = arrDate[-1]
 
        #obtenemos estadisticas
        statistics = linkIndividual.css(".statistics")
        itemStatistics = statistics.css(".item")
        listaestadistica = []
        itemStatistics.each do |valor|
          numberstatistics = valor.css(".number")
          valorstatistics = numberstatistics.inner_text
          listaestadistica << valorstatistics
        end
 
        noGoles =listaestadistica[0]
        porceGoles=listaestadistica[1]
        amarillas1=listaestadistica[5]
        amarillas2=listaestadistica[6]
        rojas=listaestadistica[7]
        fueraJuego=listaestadistica[8]
        paradas=listaestadistica[9]
 

        objDeporteEcuador =  InformacionGeneralLiga.new(liga,jornada,fecha, noGoles,porceGoles,amarillas1,amarillas2,rojas,fueraJuego,paradas)
        objDeporteEcuador.registrar(csv) 
      end
    end
  end
  
end

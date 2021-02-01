require 'open-uri'
require 'nokogiri'
require 'csv'
require './DeporteEcuador'
require './Scrapper'
require './ScrapperJugadores'
require './ScrapperResultados'


url1= "https://www.sport.es/es/resultados/la-liga/jornada-1/" #santader
url2= "https://www.sport.es/es/resultados/premier-league/jornada-1/" #premier
url3= "https://www.sport.es/es/resultados/europa-league/1a-eliminatoria/" #europa 
url4= "https://www.sport.es/es/resultados/champions/fase-de-grupos/" #champion
url5= "https://www.sport.es/es/resultados/segunda-division/jornada-1/" #liga 123

lista = [url1, url2, url3, url4, url5]

#scrapper 1, informacion general de las ligas Europeas
lista.each do |url|
    scrapper =Scraper.new
    scrapper.extraerInfoGeneral(url)
end
#scrapper 2, informacion de los mejores jugadores , equipo y puntos
lista.each do |url|
    scrapper =ScrapperJugadores.new
    scrapper.extraerInfoJugadores(url)
end
#scrapper 3, informacion de los resultados de los partidos
lista.each do |url|
    scrapper =ScrapperResultados.new
    scrapper.extraerInfoResultado(url)
end






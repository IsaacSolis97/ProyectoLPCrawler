#GEMAS
require 'open-uri'
require 'nokogiri'
require 'csv'

#CLASES
require './Deporte'
require './ScrapperNoticias'
require './ScrapperEstadisticas'

#url1= "https://as.com/futbol/"
#Llamamos al Scrapper de Noticias
#scrapper =ScrapperNoticias.new
#scrapper.extraer(url1)

#Llamamos al Scrapper de estadisticas de la nba en temporada regular desde 2011 hasta la actualidad
urls= conferencias = {"2015-2016"=>"https://www.basketball-reference.com/leagues/NBA_2016_standings.html","2016-2017"=>"https://www.basketball-reference.com/leagues/NBA_2017_standings.html","2017-2018"=>"https://www.basketball-reference.com/leagues/NBA_2018_standings.html","2018-2019"=>"https://www.basketball-reference.com/leagues/NBA_2019_standings.html","2019-2020"=>"https://www.basketball-reference.com/leagues/NBA_2020_standings.html"}
scrapperNBA= ScrapperEstadisticas.new
scrapperNBA.extraer(urls)


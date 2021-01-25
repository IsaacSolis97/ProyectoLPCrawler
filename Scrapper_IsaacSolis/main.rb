require 'open-uri'
require 'nokogiri'
require 'csv'
require './DeporteEcuador'
require './Scrapper'

pagina= "https://lahora.com.ec/seccion/109/deportes"

scrapper =Scraper.new
scrapper.extraer(pagina)


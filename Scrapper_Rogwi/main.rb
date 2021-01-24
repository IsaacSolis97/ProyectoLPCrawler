#GEMAS
require 'open-uri'
require 'nokogiri'
require 'csv'

#CLASES
require './Deporte'
require './Scrapper'

url= "https://as.com/futbol/"

#Llamamos al Scrapper
scrapper =Scraper.new
scrapper.extraer(url)


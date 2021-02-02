require 'open-uri'
require 'nokogiri'
require 'csv'

require './Noticia'
require './Scrapper'

scrapper = Scrapper.new
scrapper.extraer("https://fbref.com/en/")
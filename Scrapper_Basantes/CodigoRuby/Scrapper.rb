require 'open-uri'
require 'nokogiri'
require 'csv'
require './Noticia'

class Scrapper

  def extraer(url)
    
    CSV.open('datos.csv', 'wb') do |csv|

        rank=""  
        squad=""  
        matchesPlayed=""
        wins=""  
        draws=""
        losses=""  
        points=""  
        goalDiference=""

        #csv << %w[Rank  Squad  MatchesPlayed  Wins  Draws  Losses  Points  GoalDiference]
        noticiasHTML = open(url)
        datos = noticiasHTML.read
        parsed_content = Nokogiri::HTML(datos)
        informacion = parsed_content.css("tbody")
        informacion.css("tr").each do |datos|
        
            rank = datos.css("th").inner_text 

            squad = datos.css(".left").css("a").inner_text
            
            matchesPlayed = datos.css("td")[1].inner_text #attribute("data-stat").value

            wins = datos.css("td")[2].inner_text

            draws = datos.css("td")[3].inner_text

            losses = datos.css("td")[4].inner_text 

            points = datos.css("td")[5].inner_text   

            goalDiference = datos.css("td")[6].inner_text  

            #puts goalDiference
            #gets()

            nuevaNoticia = Noticia.new(rank,  squad,  matchesPlayed,  wins,  draws,  losses,  points,  goalDiference)
            nuevaNoticia.registrar(csv)

        end
    end

  end
end
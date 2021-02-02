class Noticia
  
  attr_accessor :rank,  :squad,  :matchesPlayed,  :wins,  :draws,  :losses,  :points,  :goalDiference

  def initialize(rank,  squad,  matchesPlayed,  wins,  draws,  losses,  points,  goalDiference)
    @rank = rank
    @squad = squad
    @matchesPlayed = matchesPlayed
    @wins = wins  
    @draws = draws  
    @losses = losses
    @points = points
    @goalDiference = goalDiference
  end

  def registrar(csv)
    csv << [rank.to_s, squad.to_s, matchesPlayed.to_s, wins.to_s,  draws.to_s,  losses.to_s,  points.to_s,  goalDiference.to_s]  
  end

end
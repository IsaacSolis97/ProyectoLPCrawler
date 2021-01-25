class Noticia
  
  attr_accessor :noticia, :link, :texto

  def initialize(noticia, link, texto)
    @noticia = noticia
    @link = link
    @texto = texto
  end

  def registrar(csv)
    csv << [noticia.to_s, link.to_s, texto.to_s]  
  end

end
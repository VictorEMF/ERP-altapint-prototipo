# ERP-altapint-prototipo


<h2>Excel antigo</h2>
<p>
  A ideia do projeto original da empresa era que apenas 1 arquivo excel fizesse todo o controle manual do estoque, nele tinha 127 s estoqueheets para cada tinta e dentro deles tinha todo o historico da tinta, a idei de remodelação do arquivo foi criar um novo excel com apenas com 3 sheets onde tem menu principal, tintas e historico. Desse jeito fica mais facil a visualização dos dados.
</p>

![Excel Antigo](https://github.com/VictorEMF/ERP-altapint-prototipo/blob/main/02%20-%20ARQUIVOS/IMAGEN/EXCEL%20ANTIGO.png)

<p>
  O metodo utilizado para extrair os dados foi o python, porem mesmo pos a extração os dados precisavam ser tratatos ja que do jeito que eles ficaram nem mesmo ferramentas de ETL como o propio Pentaho Data Integration(PDI) poderia compreender, entao utilizando o python novmanete foi feito um secundo tratamento para deixar os dados mais faceis de comprender e em segunda foi tulizado o Pentaho pegar esses dados e transformar em finalmente no objetivo final. 
</p>

IMG AQUI

<p>
  Depois dessa extração os arquivos ficavam em um pasta e para transforma isso para apenas 2 arquivos foi utilizado o pentaho data integration(PDI) para agrupar todos os dados 
</p>

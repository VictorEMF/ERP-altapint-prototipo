# ERP-altapint-prototipo


<h2>Excel antigo</h2>
<p>
  A ideia do projeto original da empresa era que apenas 1 arquivo excel fizesse todo o controle manual do estoque, nele tinha 127 sheets para cada tinta e dentro deles tinha todo o historico da tinta, a idei de remodelação do arquivo foi criar um novo excel com apenas com 3 sheets onde tem menu principal, tintas e historico. Desse jeito fica mais facil a visualização dos dados.
</p>

![Excel Antigo](https://github.com/VictorEMF/ERP-altapint-prototipo/blob/main/02%20-%20ARQUIVOS/IMAGEN/EXCEL%20ANTIGO.png)

<p>
  O metodo utilizaod para extrair os dados foi utilizando o python, porem mesmo pos a extração os dados precisavam ser tratatos ja que do jeito que eles ficavam nem mesmo ferramentas de ETL como o propio Pentaho Data Integration(PDI) poderia compreender, entao foi usando o python novmanete para esse tratamento para depois pode ser utilizado um o ETL 
</p>

IMG AQUI

<p>
  Depois dessa extração os arquivos ficavam em um pasta e para transforma isso para apenas 2 arquivos foi utilizado o pentaho data integration(PDI) para agrupar todos os dados 
</p>

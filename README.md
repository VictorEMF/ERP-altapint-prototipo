# ERP-altapint-prototipo


<h2>Excel antigo</h2>
<p>
  A ideia do projeto original da empresa era que apenas 1 arquivo excel fizesse todo o controle manual do estoque, nele tinha 127 s estoqueheets para cada tinta e dentro deles tinha todo o historico da tinta, a idei de remodelação do arquivo foi criar um novo excel com apenas com 3 sheets onde tem menu principal, tintas e historico. Desse jeito fica mais facil a visualização dos dados.
</p>

![Excel Antigo](https://github.com/VictorEMF/ERP-altapint-prototipo/blob/main/02%20-%20ARQUIVOS/IMAGEN/EXCEL%20ANTIGO.png)

<p>
  O metodo utilizado para extrair os dados foi o python, porem mesmo pos a extração os dados precisavam ser tratatos ja que do jeito que eles ficaram nem mesmo ferramentas de ETL como o Pentaho Data Integration(PDI) poderia compreender, entao utilizando o python novmanete foi feito um secundo tratamento para deixar os dados mais faceis de serem compreendidos e em seguida foi utulizado o Pentaho pegar esses dados e subir em banco de dados temporarios e extrair os dados. 
</p>


<p>
  Depois dessas etapas feitas aepenas sobrou 2 arquivos, tintas.xlsx e historico.xlsx, com esses arquivos foi utilizado o Pentaho para mesclrar em apenas um arquivo com 3 sheets. Apos todas essas etapas a parte mais dificil do projeto esta finalizado e daria inicio a proxima que seria a crição da automação que foi o pedido inicial.
</p>
<p>
  A automação veio para facilitar o cadastro das atividades na empresa, pois todo trabalho de cadastro de tinta, movimentação, calculo de gasto, atualização de estoque era feito manualmente no excel pelo chefe e pela sua assistencia.
</p>
<p>
  Com isso foi criado um sistema de cadastro de tinta e um sistema para cadastrar seviços realizados junto com isso todos os calculos e edições seria feitos pelo propio VBA.
</p>

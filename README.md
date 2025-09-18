# ERP-altapint-prototipo


<h2>Excel antigo</h2>
<p>
  A ideia do projeto original da empresa era que apenas 1 arquivo excel fizesse todo o controle manual do estoque, nele tinha 127 sheets para cada tinta e dentro deles tinha todo o histórico da tinta, a ideia de remodelação do arquivo foi criar um novo excel com apenas com 3 sheets onde tem menu principal, tintas e histórico. Desse jeito fica mais fácil a visualização dos dados.
</p>

![Excel Antigo](https://github.com/VictorEMF/ERP-altapint-prototipo/blob/main/02%20-%20ARQUIVOS/IMAGEN/EXCEL%20ANTIGO.png)

<p>
  O método utilizado para extrair os dados foi o python, porem mesmo pós a extração os dados precisavam ser tratados ja que do jeito que eles ficaram nem mesmo ferramentas de ETL como o Pentaho Data Integration(PDI) poderia compreender, então utilizando o python novamente foi feito um secundo tratamento para deixar os dados mais fáceis de serem compreendidos e em seguida foi utilizado o Pentaho pegar esses dados e subir em banco de dados temporários e extrair os dados. 
</p>


<p>
  Depois dessas etapas feitas apenas sobrou 2 arquivos, tintas.xlsx e historico.xlsx, com esses arquivos foi utilizado o Pentaho para mesclar em apenas um arquivo com 3 sheets. Apos todas essas etapas a parte mais difícil do projeto esta finalizado e daria inicio a próxima que seria a criação da automação que foi o pedido inicial.
</p>

![EXCEL_NOVO](https://github.com/VictorEMF/ERP-altapint-prototipo/blob/main/02%20-%20ARQUIVOS/IMAGEN/EXCEL%20NOVO.png)

<p>
  A automação veio para facilitar o cadastro das atividades na empresa, pois todo trabalho de cadastro de tinta, movimentação, calculo de gasto, atualização de estoque era feito manualmente no excel pelo chefe e pela sua assistência.
</p>
<p>
  Com isso foi criado um sistema de cadastro de tinta e um sistema para cadastrar serviços realizados junto com isso todos os cálculos e edições seria feitos pelo propio VBA.
</p>

<strong>
  imagem do sistema de cadastro
</strong>

<p>
  O ultimo objetivo do projeto visava a visualização dos dados da empresa, o cliente não queria mais depender do excel para poder visualizar os dados, para ele o excel seria apenas o meio de cadastro das informações, com essa informação foi criado um dashboard apenas com os dados desejados. Já que foi pedido que o excel apenas fosse o sistema de cadastro houve a criação de pequeno banco de dados local utilizando o postgres, com isso houve tamebm a criação de um ETL no Pentaho para pegar os dados do excel e alimentar o banco de dados uma vez por mês,com isso o cliente pode todo inicio de mês se preparar com as informações
</p>

![DASHBOARD](https://github.com/VictorEMF/ERP-altapint-prototipo/blob/main/04%20-%20POWER_BI/IMAGEM/DASHBOARD_VENDAS.png)

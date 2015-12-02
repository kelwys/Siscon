# Siscon

**Sistema de Gestão para Monitoramento de Sensores**

**1.1	Escopo**

Descreveremos aqui a construção do sistema de aplicação web “Siscon”.
O software terá a capacidade para coletar informações geradas por sensores, sendo inicialmente projetado para atuar com área de  abrangência da Região de estado do Espirito Santo, podendo ser ampliada posteriormente pelo própio cliente de acordo com suas demandas.
A função principal do sistema consiste na geração de relatórios com gráficos gerados a partir dos dados coletados dos sensores, servindo como fonte de informação para os usuários que acessam a ferramenta.
Os dados para a população do banco virá através de arquivos de textos com configurações pré definidas.
O sistema permitirá cadastro de equipamentos (sensores), usuários e regiões. Os cadastros ocorrerão de forma manual ou através de importação (no caso de sensores e regiões) do arquivo base, necessitando nesse caso de validação manual deste cadastros para utilização dos mesmos em relatórios.
Os dados cadatrados poderão a qualquer momento serem desabilitados pelo usuario com tais permissões.
Haverão dois tipos de perfis de usuarios do sistema. O administrador que possuirá função para cadastrar e desabilitar sensores, regiões e usuários administradores e acesso a geração de relatórios. Os usuários comuns terão apenas a geração do relatórios como opção de utilização do sistema.
O projeto reunirá dados e disponibilizará os tais como informação relevante a usuários, isentando os mesmo de buscas interminváveis por informações dispersas, evitando assim a inconsistência de dados e facilitando o trabalho dos utilazadores da ferramenta, visto que terão fácil acesso a dados e historicos de sensores de diversas regiões e em tempo bem próximo do real, permitindo montagem de relatório com recursos de gráficos e seleção de filtros ideais a sua necessidade. 

Screenshots
===========

.. image:: https://raw.github.com/kelwys/Siscon/static/screen1.png
    :alt: Screenshot #1
    :align: center

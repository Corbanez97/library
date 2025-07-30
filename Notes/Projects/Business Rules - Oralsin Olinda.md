## Keys

produtividate_sk = [contract, productivity_item, location, date]

## Master Data

Relatório de Tratado x Recebido: Create Dict
	nomeProcedimento, descItem >>> Oralsin
	Status () >>> enrichment 

Concat "nomeProcedimento" "descItem" é chave forte with "productivity_item + location"

## Main goal

Por contrato temos pendências de execução seguindo o enriquecimento de dados na aba Base. Dos contratos ativos, contabilizar quais estão em etapas anteriores às flagadas com "Feito"

![[Pasted image 20250719154638.png]]


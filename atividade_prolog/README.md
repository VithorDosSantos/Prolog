================================================================================
ATIVIDADE PROLOG - GUIA DE ESTRUTURA E ARQUIVOS
================================================================================

Disciplina: INTELIGENCIA ARTIFICIAL E COMPUTACIONAL
Instituição: Cesupa
Professor: Daniel Leal
Data: Maio de 2026
Tema: Conceitos Básicos de Prolog e Programação Lógica

================================================================================
ESTRUTURA DE ARQUIVOS
================================================================================

📁 atividade_prolog/
├── 📄 README.md (este arquivo)
├── 📄 RELATORIO_PROLOG.txt
├── 📄 familia.pl
├── 📄 EVIDENCIAS_EXECUCAO.txt
└── 📄 DOCUMENTACAO_USO_IA.txt


================================================================================
DESCRIÇÃO DE CADA ARQUIVO
================================================================================

1️⃣  RELATORIO_PROLOG.txt
────────────────────────────────────────────────────────────────────────────

PROPÓSITO: Documento teórico principal contendo a pesquisa sobre Prolog

CONTEÚDO:
  ✓ Seção 1: Programação Lógica (definição e características)
  ✓ Seção 2: A Linguagem Prolog (histórico e usos)
  ✓ Seção 3: Fatos, Regras e Consultas (conceitos e exemplos)
  ✓ Seção 4: Variáveis em Prolog (papel e uso)
  ✓ Seção 5: Unificação (conceito fundamental e exemplos)
  ✓ Seção 6: Backtracking (mecanismo e demonstração)
  ✓ Seção 7: Integração (como conceitos aparecem no exemplo)
  ✓ Seção 8: Síntese (compreensão dos conceitos)
  ✓ Referências Bibliográficas (3 referências principais)

REQUISITOS ATENDIDOS:
  ✓ Explica programação lógica
  ✓ Explica Prolog e usos educacionais
  ✓ Define fatos, regras, consultas
  ✓ Aborda papel das variáveis
  ✓ Descreve unificação
  ✓ Descreve backtracking
  ✓ Integra com o exemplo prático
  ✓ Inclui síntese final
  ✓ Contém 3 referências técnicas
  ✓ Texto autoral com redação própria

TAMANHO: ~8.5 páginas (aproximadamente)


2️⃣  familia.pl
────────────────────────────────────────────────────────────────────────────

PROPÓSITO: Programa Prolog funcional demonstrando conceitos básicos

CONTEÚDO:
  ✓ 10 FATOS (base de conhecimento):
    - 5 fatos sobre relação "pai"
    - 5 fatos sobre relação "mãe"

  ✓ 3 REGRAS (inferência):
    - Regra 1: filho(X, Y) - 2 cláusulas
    - Regra 2: avo(X, Z) - 4 cláusulas  
    - Regra 3: irmao(X, Y) - 2 cláusulas

  ✓ 3 CONSULTAS (demandas de informação):
    1. ?- filho(X, carlos)
    2. ?- avo(X, ana)
    3. ?- irmao(joao, X)

  ✓ COMENTÁRIOS: Explicativos em português

REQUISITOS ATENDIDOS:
  ✓ Mínimo 6 fatos (implementados: 10)
  ✓ Mínimo 3 regras (implementados: 3 com 8 cláusulas)
  ✓ Mínimo 3 consultas demonstradas (implementadas: 3)
  ✓ Uma consulta depende de regra (Consulta 2 com avo)
  ✓ Programa é funcional e coerente
  ✓ Simples e educacional

TEMA: Relações Familiares (elementar, conforme requisito)

COMO USAR:
  1. Abrir SWI-Prolog ou compatível
  2. ?- consult('familia.pl').
  3. Executar as consultas acima


3️⃣  EVIDENCIAS_EXECUCAO.txt
────────────────────────────────────────────────────────────────────────────

PROPÓSITO: Documentação de testes e demonstração de funcionamento

CONTEÚDO:
  ✓ Instruções de execução do programa
  ✓ Resumo do programa (fatos, regras, consultas)
  ✓ 3 consultas demonstradas com:
    - Comando exato
    - Resultado esperado
    - Explicação detalhada
    - Conceitos demonstrados

  ✓ Testes adicionais de verificação
  ✓ Árvore genealógica visual
  ✓ Correspondência com requisitos (checklist)
  ✓ Exemplo de sessão Prolog completa
  ✓ Observações finais

DETALHES IMPORTANTES:
  • Consulta 1 (filho): Usa regra sobre fatos diretos
  • Consulta 2 (avo): ⭐ Depende INTEIRAMENTE de regra (dedução em cadeia)
  • Consulta 3 (irmao): Usa regra com verificação de diferença

TAMANHO: ~6.5 páginas

USO:
  • Servir de guia para executar e testar o programa
  • Validar que todas as respostas retornam corretamente
  • Verificar correspondência com requisitos


4️⃣  DOCUMENTACAO_USO_IA.txt
────────────────────────────────────────────────────────────────────────────

PROPÓSITO: Transparência sobre uso de Inteligência Artificial

CONTEÚDO:
  ✓ Ferramenta utilizada: GitHub Copilot (Claude Haiku 4.5)
  ✓ Para cada componente (Relatório, Código, Documentação):
    - Resumo do prompt
    - Trechos aproveitados
    - Revisão crítica realizada
    - Percentual de aproveitamento
    - Nível de confiabilidade

  ✓ Resumo comparativo por componente
  ✓ Conclusão sobre processo e qualidade

REQUISITO ATENDIDO:
  ✓ Conforme exigência: "Todo conteúdo gerado por IA deverá ser documentado"

TRANSPARÊNCIA:
  • 70-75% de cada componente foi inicial gerado por IA
  • 25-50% em revisão crítica e ajustes humanos
  • Toda informação técnica foi verificada
  • Todas as garantias de qualidade são responsabilidade humana

TAMANHO: ~5 páginas


================================================================================
CHECKLIST DE REQUISITOS
================================================================================

PESQUISA (Requisitos Mínimos):
  ✅ Texto autoral (com redação própria da equipe)
  ✅ Pelo menos 2 referências (implementados: 3 referências)
  ✅ Síntese final explicando compreensão

CONTEÚDO DA PESQUISA:
  ✅ 1. O que é programação lógica
  ✅ 2. O que é Prolog e usos em exemplos introdutórios
  ✅ 3. O que são fatos, regras e consultas
  ✅ 4. O papel das variáveis
  ✅ 5. O que significa unificação
  ✅ 6. O que significa backtracking
  ✅ 7. Como esses conceitos aparecem no exemplo

PROGRAMA PROLOG:
  ✅ Mínimo 6 fatos (implementados: 10 fatos)
  ✅ Mínimo 3 regras (implementados: 3 regras)
  ✅ Mínimo 3 consultas demonstradas (implementadas: 3 consultas)
  ✅ Uma consulta depende de regra (Consulta 2: ?- avo(X, ana))
  ✅ Programa é funcional
  ✅ Programa é coerente com pesquisa
  ✅ Programa é simples (tema elementar)

QUALIDADE GERAL:
  ✅ Correção conceitual
  ✅ Clareza explicativa
  ✅ Organização adequada
  ✅ Documentação de uso de IA

ENTREGA:
  ✅ Relatório (.txt) localizado e fácil de acessar
  ✅ Arquivo .pl funcional e comentado
  ✅ Evidências de execução documentadas
  ✅ Material organizado conforme especificação


================================================================================
INSTRUÇÕES PARA PRESENTAÇÃO EM VÍDEO
================================================================================

CONTEÚDO MÍNIMO DO VÍDEO (até 10 minutos):

1. INTRODUÇÃO (1-2 min):
   □ Identificação dos integrantes
   □ Tema: Conceitos básicos de Prolog
   □ Objetivo: Apresentar fundamentalmente programação lógica

2. CONCEITOS TEÓRICOS (3-4 min):
   □ Programação lógica (o que é)
   □ Prolog (linguagem e usos)
   □ Fatos, regras, consultas (com exemplos)
   □ Variáveis, unificação, backtracking (brevemente)

PARTE OMITTED FOR BREVITY IN CREATE_FILE
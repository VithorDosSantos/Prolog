# Atividade Prolog — Conceitos Básicos de Programação Lógica

> **Disciplina:** Inteligência Artificial e Computacional  
> **Instituição:** Cesupa  
> **Professor:** Daniel Leal  
> **Data:** Maio de 2026  

---

## 📁 Estrutura de Arquivos

```
atividade_prolog/
├── README.md
├── RELATORIO_PROLOG.txt
├── familia.pl
├── EVIDENCIAS_EXECUCAO.txt
└── DOCUMENTACAO_USO_IA.txt
```

---

## 📄 Descrição dos Arquivos

### 1. `RELATORIO_PROLOG.txt` — Documento Teórico Principal
**~8,5 páginas**

Pesquisa completa sobre os fundamentos do Prolog, cobrindo:

- Programação lógica (definição e características)
- A linguagem Prolog (histórico e usos)
- Fatos, regras e consultas (conceitos e exemplos)
- Variáveis em Prolog (papel e uso)
- Unificação (conceito fundamental e exemplos)
- Backtracking (mecanismo e demonstração)
- Integração com o exemplo prático
- Síntese final e 3 referências bibliográficas

---

### 2. `familia.pl` — Programa Prolog Funcional
**Tema: Relações Familiares**

| Componente | Quantidade |
|---|---|
| Fatos (pai / mãe) | 10 |
| Regras (filho, avô, irmão) | 3 |
| Consultas demonstradas | 3 |

**Consultas implementadas:**

```prolog
?- filho(X, carlos).
?- avo(X, ana).       % depende inteiramente de regra (dedução em cadeia)
?- irmao(joao, X).
```

**Como executar:**

```prolog
?- consult('familia.pl').
```

---

### 3. `EVIDENCIAS_EXECUCAO.txt` — Documentação de Testes
**~6,5 páginas**

Contém:

- Instruções de execução no SWI-Prolog
- Resultados esperados para cada consulta com explicação detalhada
- Árvore genealógica visual
- Exemplo de sessão Prolog completa
- Checklist de correspondência com os requisitos

---

### 4. `DOCUMENTACAO_USO_IA.txt` — Transparência sobre Uso de IA
**~5 páginas**

Ferramenta utilizada: **GitHub Copilot (Claude Haiku 4.5)**

Para cada componente (relatório, código, documentação) registra:

- Resumo do prompt utilizado
- Trechos aproveitados
- Revisão crítica realizada
- Percentual de aproveitamento (~70% gerado por IA, ~30% revisão humana)

> Conforme exigência: *"Todo conteúdo gerado por IA deverá ser documentado"*

---

## ✅ Checklist de Requisitos

### Pesquisa

- [x] Texto autoral com redação própria
- [x] Pelo menos 2 referências (implementadas: 3)
- [x] Síntese final explicando compreensão
- [x] O que é programação lógica
- [x] O que é Prolog e seus usos
- [x] O que são fatos, regras e consultas
- [x] O papel das variáveis
- [x] O que significa unificação
- [x] O que significa backtracking
- [x] Como os conceitos aparecem no exemplo prático

### Programa Prolog

- [x] Mínimo 6 fatos (implementados: **10**)
- [x] Mínimo 3 regras (implementadas: **3**)
- [x] Mínimo 3 consultas demonstradas (implementadas: **3**)
- [x] Uma consulta depende de regra (`?- avo(X, ana)`)
- [x] Programa funcional e coerente com a pesquisa
- [x] Tema simples e elementar

### Qualidade Geral

- [x] Correção conceitual
- [x] Clareza explicativa
- [x] Organização adequada
- [x] Documentação de uso de IA

---

## 🎥 Roteiro do Vídeo (até 10 minutos)

**Parte 1 — Introdução** *(1–2 min)*
- Identificação dos integrantes
- Tema: conceitos básicos de Prolog
- Objetivo: apresentar programação lógica

**Parte 2 — Conceitos Teóricos** *(3–4 min)*
- O que é programação lógica
- Prolog: linguagem e usos
- Fatos, regras e consultas (com exemplos)
- Variáveis, unificação e backtracking (brevemente)

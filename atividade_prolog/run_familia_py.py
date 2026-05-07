#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simulação das consultas Prolog a partir de familia.pl
Extrai fatos do arquivo .pl e responde as 3 consultas
"""

import re
from collections import defaultdict
from pathlib import Path

# Localiza familia.pl no mesmo diretório deste script
BASE_DIR = Path(__file__).resolve().parent
pl_path = BASE_DIR / 'familia.pl'

print(f"Lendo arquivo: {pl_path}")
print("=" * 80)

# Estruturas para guardar relações
parent_of = defaultdict(set)  # pai/mae -> filhos
parents_of = defaultdict(set) # filho -> pais/maes

# Regex para extrair fatos de pai(X, Y) e mae(X, Y)
fact_re = re.compile(r"\b(pai|mae)\s*\(\s*([^,\s]+)\s*,\s*([^\)\s]+)\s*\)\s*\.")

# Ler arquivo
with open(pl_path, 'r', encoding='utf-8') as f:
    for line in f:
        m = fact_re.search(line)
        if m:
            pred = m.group(1)
            p = m.group(2)
            c = m.group(3)
            parent_of[p].add(c)
            parents_of[c].add(p)

print(f"✓ Fatos carregados com sucesso!")
print()

# ============================================================================
# CONSULTA 1: filho(X, carlos)
# ============================================================================
def filhos_de(person):
    """Retorna filhos de uma pessoa (baseado em pai ou mae)"""
    return sorted(parent_of.get(person, []))

q1 = filhos_de('carlos')
print("CONSULTA 1: filho(X, carlos).")
print(f"Resposta: {q1}")
print(f"Explicação: Carlos é pai de {' e '.join(q1)}")
print()

# ============================================================================
# CONSULTA 2: avo(X, ana)
# ============================================================================
def avos_de(person):
    """Retorna avós de uma pessoa (pais dos pais)"""
    avos = set()
    for p in parents_of.get(person, []):
        for gp in parents_of.get(p, []):
            avos.add(gp)
    return sorted(avos)

q2 = avos_de('ana')
print("CONSULTA 2: avo(X, ana).")
print(f"Resposta: {q2}")
print(f"Explicação: Os avós de Ana são {' e '.join(q2)}")
print("(Raciocínio: João é pai de Ana. Carlos e Luís são pais de João.)")
print()

# ============================================================================
# CONSULTA 3: irmao(joao, X)
# ============================================================================
def irmaos_de(person):
    """Retorna irmãos de uma pessoa (compartilham pelo menos um pai/mãe)"""
    irmaos = set()
    for p in parents_of.get(person, []):
        for sib in parent_of.get(p, []):
            if sib != person:
                irmaos.add(sib)
    return sorted(irmaos)

q3 = irmaos_de('joao')
print("CONSULTA 3: irmao(joao, X).")
print(f"Resposta: {q3}")
print(f"Explicação: {' e '.join(q3)} é irmã de João")
print("(Raciocínio: João e Maria compartilham os mesmos pais.)")
print()

# ============================================================================
# RESUMO
# ============================================================================
print("=" * 80)
print("✓ EXECUÇÃO COMPLETA!")
print()
print("Isso demonstra:")
print("  • Fatos: pai(X, Y) e mae(X, Y) são declarações de verdade")
print("  • Regras: filho(X,Y), avo(X,Z), irmao(X,Y) derivam de fatos")
print("  • Consultas: perguntas que o Prolog responde por dedução")
print("  • Unificação: correspondência automática entre padrões")
print("  • Backtracking: exploração de múltiplas soluções")
print()

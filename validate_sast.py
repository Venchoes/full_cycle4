#!/usr/bin/env python3
import json
import sys

# Lendo o relatório SAST
with open('gl-sast-report.json') as f:
    report = json.load(f)

# Obtendo as vulnerabilidades
vulnerabilities = report.get('results', [])

if vulnerabilities:
    print(f'\n== Relatório de Vulnerabilidades ({len(vulnerabilities)} encontradas) ==')
    for vuln in vulnerabilities:
        rule_id = vuln.get('check_id', 'Sem ID')
        severity = vuln.get('extra', {}).get('severity', 'Severidade não especificada')
        message = vuln.get('extra', {}).get('message', 'Sem mensagem').replace('\n', ' ')
        file = vuln.get('path', 'Arquivo não especificado')
        start_line = vuln.get('start', {}).get('line', 'Início desconhecido')
        end_line = vuln.get('end', {}).get('line', 'Fim desconhecido')
        
        print(f'\n- ID da Regra: {rule_id}')
        print(f'  Severidade: {severity}')
        print(f'  Mensagem: {message}')
        print(f'  Arquivo: {file}')
        print(f'  Linhas: {start_line}-{end_line}')
    
    sys.exit(1)
else:
    print('Nenhuma vulnerabilidade encontrada.')
    sys.exit(0)

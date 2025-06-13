# 🚍 Sistema de Gestão de Transportes Públicos

## 📝 Descrição
Um sistema completo para gerenciamento de redes de transporte público, desenvolvido em Python, que permite cadastrar e consultar carreiras (linhas), paragens (paradas) e suas ligações com custos e tempos associados.

## ✨ Funcionalidades Principais

| Comando | Descrição | Exemplo |
|---------|-----------|---------|
| `c` | Lista todas as carreiras | `c` |
| `c <nome>` | Cria ou mostra paragens de uma carreira | `c 28` |
| `c <nome> inverso` | Lista paragens em ordem inversa | `c 28 inverso` |
| `p` | Lista todas as paragens | `p` |
| `p <nome>` | Mostra coordenadas de uma paragem | `p Alameda` |
| `l` | Adiciona ligação entre paragens | `l 28 Alameda Campo-Grande 1.50 5.0` |

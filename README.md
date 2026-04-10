# MGPEB - Módulo de Gerenciamento de Pouso e Estabilização de Base

Este projeto foi desenvolvido como parte dos requisitos da **Missão Aurora Siger**. O objetivo é simular o sistema responsável por organizar pousos de módulos de uma colônia em Marte, gerenciar informações críticas da operação e estabelecer diretrizes de governança.

## 🚀 Sobre o Projeto

O **MGPEB** (Módulo de Gerenciamento de Pouso e Estabilização de Base) atua como a central de controle de tráfego orbital da colônia. Ele utiliza algoritmos clássicos de computação para garantir que módulos de habitação, energia, médicos e laboratoriais decolem e pousem com máxima segurança e prioridade técnica.

### Funcionalidades
- **Modelagem de Módulos**: Cada módulo possui atributos como combustível, massa, criticidade e prioridade.
- **Estruturas de Dados Lineares**: Utilização de filas (queues), pilhas (stacks) e listas para gerenciar o fluxo orbital.
- **Lógica de Decisão**: Aplicação de funções booleanas para autorização ou bloqueio de pouso baseada em telemetria em tempo real.
- **Algoritmos de Ordenação**: Implementação de *Bubble Sort* e *Selection Sort* para organização dinâmica da fila de pouso.
- **Algoritmos de Busca**: Busca linear e binária para localização rápida de módulos críticos.

## 🎨 Interface Visual

O projeto conta com uma interface de console customizada utilizando a biblioteca `colorama`, seguindo uma paleta de cores temática:
- **Ciano**: Sucesso e Dados Nominais.
- **Magenta/Roxo**: Estrutura e Critérios de Risco.
- **Amarelo**: Alertas e Destaques de Busca.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Bibliotecas**: `colorama` (Interface Visual), `collections` (Estruturas de Dados).
- **Conceitos**: Portas Lógicas, Algoritmos de Busca e Ordenação, Princípios ESG (Governança).

## ⚙️ Como Executar

1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd MGPEB_Aurora_Siger
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o sistema**:
   ```bash
   python main.py
   ```

---
Este projeto faz parte da Fase 2 do curso de Ciência da Computação (FIAP).

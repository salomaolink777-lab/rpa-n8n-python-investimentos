# RPA com N8N e Python — Assistente de Investimentos

Este projeto consiste numa automação de RPA desenvolvida para processar dados de clientes e automatizar o envio de propostas de investimento personalizadas.

## 🛠️ Tecnologias Utilizadas
- **Python**: Extração, tratamento e estruturação dos dados dos clientes.
- **N8N**: Orquestração do workflow, receção de dados via Webhook e automação do fluxo.
- **Gmail**: Envio automatizado de e-mails com sugestões personalizadas de investimento.

## 🔄 Fluxo do Processo
1. O script Python processa os dados dos clientes e faz uma requisição HTTP POST para o Webhook do n8n.
2. O n8n recebe o payload JSON e valida a informação recebida.
3. Com base no perfil de investimento do cliente, o fluxo seleciona a melhor sugestão de produto financeiro.
4. O nó do Gmail dispara um e-mail formatado com as recomendações de investimento.

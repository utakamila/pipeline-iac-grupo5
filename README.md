# Pipeline e IaC – Equipe 5
**Integrantes e papéis:**
- Gustavo Aprígio Jesuíta – Coordenador do repositório e Relator
- Brian Lucas – Responsável pela pipeline
- Enzo Santana - Responsavel pelo IaC
## Evidências
1. Print da execução verde (jobs testar e infraestrutura)
   <img width="1899" height="591" alt="image" src="https://github.com/user-attachments/assets/f2d86882-50ee-4e57-b0cc-d3f3f3927e6c" />
   <img width="1900" height="473" alt="image" src="https://github.com/user-attachments/assets/4e6eb7bb-ba6f-4fe1-88e0-f387e10c0071" />

2. Print do passo terraform plan com a linha &quot;Plan: 1 to add&quot;
    <img width="1896" height="946" alt="image" src="https://github.com/user-attachments/assets/7f7f5572-3c38-427f-95c2-4c1a3037da53" />

3. Print do pull request com o teste falhando (vermelho)
   <img width="1908" height="632" alt="image" src="https://github.com/user-attachments/assets/04cf2a4d-e81e-4159-a5eb-42779f809a43" />

4. Print do pull request corrigido (verde) e do merge
   <img width="1882" height="856" alt="image" src="https://github.com/user-attachments/assets/4aab1a8c-925f-4572-9a2d-347c83cba14d" />
   <img width="1889" height="850" alt="image" src="https://github.com/user-attachments/assets/9cafee2f-be7c-4acf-a9f2-e9049b676e1c" />


## Respostas
**Pergunta 1:** Eles conferem se o desconto esta sendo aplicado corretamente, se não, gera um erro
**Pergunta 2:** Gatilho: linha "on: ", job linha "jobs: ", e os passos comecam na linha "steps: " e seguem adiante ate o fim do codigo
**Pergunta 3:** Declarativa, a criação do arquivo "ambiente-criado" e seu conteudo
**Pergunta 4:** Nada, "Ambiente: homologacao Equipe: Grupo 5"
**Pergunta 5:** Parou no passo 3, pois o "test_loja" foi executado e brecou a aplicação, de que o programa deve ter confiabilidade nas informações exibidas
## O que aprendemos
Em 3 ou 4 frases, com as palavras do grupo: o que a automação
mudou em relação a fazer tudo à mão?
A aula nos ajudou a entender como o git e github funciona
o conceito de branch, merge, commit, e etc
O git/github auxilia muito no gerenciamento e historico do codigo, melhorando a organização do projeto, que resulta em mais eficiencia

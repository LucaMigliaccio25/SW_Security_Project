# Analisi del tool FlashSyn e classificazione delle vulnerabilità

## Descrizione
Questo progetto ha come obiettivo la riproduzione e l'analisi degli esperimenti del tool FlashSyn,
un sistema per l'identificazione automatica di vulnerabilità nei protocolli DeFi tramite attacchi di
tipo Flash Loan. Il lavoro riproduce parte degli esperimenti presentati nel paper "FlashSyn: Flash
Loan Attack via Counter Example Driven Approximation" (ICSE 2024), valutando l’efficacia del tool e
classificando le vulnerabilità rilevate secondo standard CWE/CVE.

## Osservazione
La prima parte del progetto si rifà alla seguente repository: "https://github.com/FlashSyn-Artifact/FlashSyn-Artifact-ICSE24."
In particolare, il contributo che si è cercato di dare è stato quello di vedere come il lavoro
precedentemente svolto potesse o meno cambiare in base al sistema utilizzato.

## Strumenti utilizzati
- Docker: piattaforma di containerizzazione	utilizza per l'esecuzione isolata e portabile del tool FlashSyn
- FlashSyn: tool di analisi per attacchi flash loan (ICSE 2024)
- Python_ linguaggio utilzizato per l'analisi dei risultati
- Foundry: framework per smart contract	utilizzato per la validazione runtime degli attacchi sintetizzati
- WSL (Ubuntu 22.04): ambiente di sviluppo compatibile con FlashSyn
- MITRE ATT&CK Navigator:	tool per mappatura di minacce informatiche, utilizzato per la classificazione delle vulnerabilità a livello tattico
- CWE/CVE Database: standard di sicurezza informatica, utilizzato per la classificazione delle vulnerabilità rispetto a quelle note
- Bash: linguaggio di shell scripting

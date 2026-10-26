
```markdown
# UFHB-Net : Topologie SDN pour le projet fil rouge

## 📌 Description
Ce dépôt contient le script de topologie Mininet développé dans le cadre du **TP 0** du module **Réseaux Programmables (SDN et NFV)** en M2 RIST à l'Université Félix Houphouët-Boigny (UFHB).

Le script `ufhb_net.py` modélise une première version de l'infrastructure réseau du campus UFHB-Net. Il s'agit d'une topologie en étoile comprenant :
- **5 commutateurs OpenFlow 1.3** (`s1` à `s5`).
- **11 hôtes** répartis en 4 zones :
  - Administration (`adm1`, `adm2`, `adm3`)
  - UFR (`ufr1`, `ufr2`, `ufr3`)
  - Cité universitaire (`cit1`, `cit2`, `cit3`)
  - Centre de données (`web1`, `web2`)

Tous les hôtes partagent le sous-réseau `10.0.0.0/24`. Les liens sont configurés avec des débits et des délais spécifiques (via `TCLink`) pour simuler des conditions réseau réalistes.

## 🛠️ Prérequis
- Ubuntu 22.04 LTS
- Mininet 2.3.1b4
- Open vSwitch
- Contrôleur Ryu 4.34

##  Utilisation
1. Lancer le contrôleur Ryu :
   ```bash
   ryu-manager ryu.app.simple_switch_13
   ```
2. Dans un autre terminal, lancer la topologie :
   ```bash
   sudo python3 ufhb_net.py
   ```

##  Auteur
TOURE ALPHA MAMOUD
- **Mamoud23** (Étudiant M2 RIST - UFHB)
- Année universitaire : 2026-2027
```
Binôme : DIBI KOUASSI JEAN-MARC

---

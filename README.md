# Final_AI_Stage_GABRIELE_MASIERO_VR474762

This repository contains my **final-year Computer Science internship and thesis project** at the University of Verona.  
The project focuses on **Multi-Agent Reinforcement Learning (MARL)** experiments using [BenchMARL](https://github.com/facebookresearch/BenchMARL), [PettingZoo](https://www.pettingzoo.ml/), and [VMAS](https://github.com/facebookresearch/vmas).

---

## 📂 Repository Structure
Final_AI_Stage_GABRIELE_MASIERO_VR474762/
│
├── BenchMARL/ # Cloned submodule or vendored copy of BenchMARL
│ └── benchmarl/conf/ # Hydra YAML configs (algorithms, tasks, experiments)
│
├── outputs/ # Generated logs/results
├── requirements.txt # Final list of Python dependencies
├── run_experiment.py # Entry point to run experiments
└── README.md # Project description

---

## ⚙️ Installation

Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 🚀 Running Experiments
run command:
```bash
HYDRA_FULL_ERROR=1 python run_experiment.py 
```
You can change the configuration in the "def run_multiple_experiments(seeds):" overriding algorithm, task and seed (you can add overrides follow the BenchMARL readme inside of BencMARL/)
I prefered adding a simple "python run_experiment.py" and override configurations with a python functions for ease of use.
the "HYDRA_FULL_ERROR=1" is optional and returns the fullstack of errors that sometimes is more useful.

## 🔧 Configurations
Configurations are managed with Hydra:

- Algorithms: BenchMARL/benchmarl/conf/algorithm/*.yaml

- Tasks: BenchMARL/benchmarl/conf/task/*.yaml

- Experiment defaults: BenchMARL/benchmarl/conf/experiment/*.yaml

## 📊 Logging & Outputs
- wandb is highly advised for logging
- it might ask you to login 
```bash
wand login
```
and follow the instrucions

## 📝 Notes
- This github repo is a fast setup of [BenchMARL](https://github.com/facebookresearch/BenchMARL/tree/main)
- For detailed instructions, check the original [BenchMARL README](BenchMARL/README.md)




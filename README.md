# Continuous Experimentation Example

## Setup

TBD

## Tools used

- `GitHub Action` to trigger running jobs when code is pushed to a certain branch.
- `Weight and Biases (WandB)` to initialize hyperparameter-tuning and experiment tracking.

## Adding a new machine to your arsenal 

### Setup a new machine
- Go to your repo's `Settings` > `Actions` > `Runners`
- Add a machine by pressing `New self-hosted runner`
- Follow the instructions in `Download` section on your machine
- (Optional if you are running as a root) Run `export RUNNER_ALLOW_RUNASROOT="1"` 
- When running `./config --url ...` command, make sure you add a unique label to your runner when asked.
- Run `./run.sh` for the machine to listen to GitHub servers.

### Using the machine

Add the machine's label to `os: [MACHINE_LABEL]` in `.github/workflows/ce.yml` to have the system to run.


## More things to explore

- Data versioning using [`Data Version Control (DVC)`](https://dvc.org/).
- Logging experiments to issues/PRs using [`Continuous Machine Learning (CML)`](https://cml.dev/).
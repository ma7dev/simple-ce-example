# Continuous Experimentation Example

## Adding a new runner

- Go to your repo's `Settings` > `Actions` > `Runners`
- Add a machine by pressing `New self-hosted runner`
- Follow the instructions in `Download` section on your machine
- (Optional if you are running as a root) Run `export RUNNER_ALLOW_RUNASROOT="1"` 
- When running `./config --url ...` command, do the following:
  - 
- Add to the new machine's label to `os: [MACHINE_LABEL]` in `.github/workflows/ce.yml`

Check []() for more infomation.
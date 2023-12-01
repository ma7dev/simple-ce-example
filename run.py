import wandb

sweep_configuration = {
    "name": "my-awesome-sweep",
    "project": "my-awesome-project",
    "metric": {"name": "accuracy", "goal": "maximize"},
    "method": "grid",
    "parameters": {"a": {"values": [1, 2, 3, 4]}},
}


def my_train_func():
    wandb.init()
    a = wandb.config.a

    wandb.log({"a": a, "accuracy": a + 1})


if __name__ == "__main__":
    my_train_func()
import wandb
import os
import random
import string

def my_train_func():
    machine_num = os.environ.get("MACHINE_NUM")
    random_string=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    wandb.init(group=machine_num, name=f"{machine_num}-{random_string}")
    a = wandb.config.a

    wandb.log({"a": a, "accuracy": a + 1})


if __name__ == "__main__":
    my_train_func()
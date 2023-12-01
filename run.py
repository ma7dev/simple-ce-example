import wandb
import os
import random
import string

def func():
    machine_num = os.environ.get("MACHINE_NUM")
    random_string=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    wandb.init(group=machine_num, name=f"{machine_num}-{random_string}")
    
    x = wandb.config.x
    
    acc = x+1
    
    wandb.log({"x": x, "accuracy": acc})


if __name__ == "__main__":
    func()
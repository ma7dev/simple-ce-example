import wandb
import os
import random
import string

def func():
    # get machine number
    machine_num = os.environ.get("MACHINE_NUM") or "0"
    
    # get random 5 character string
    random_string=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    
    # set experiment name
    exp_name = f"{machine_num}-{random_string}"
    
    # initialize experiment
    wandb.init(name=exp_name)
    
    # get x from config
    x = wandb.config.x
    
    # calculate accuracy
    acc = abs(x - 0.5)
    
    # log x and accuracy to wandb
    wandb.log({"x": x, "accuracy": acc})


if __name__ == "__main__":
    func()
import wandb
import os
import random
import string


if __name__ == "__main__":
    # get machine number
    machine_id = os.environ.get("MACHINE_ID") or "local"
        
    # get random 5 character string
    random_string=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    
    # set experiment name
    exp_name = f"{machine_id}-{random_string}"
    
    # initialize experiment
    wandb.init(name=exp_name)
    
    # get x from the experiment's config
    x = wandb.config.x
    
    # calculate accuracy
    acc = x**2
    
    # log x and accuracy to wandb
    wandb.log({"x": x, "accuracy": acc})
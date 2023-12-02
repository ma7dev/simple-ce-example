import wandb
import yaml

if __name__ == "__main__":
    # load config
    with open("config.yml", 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    print(config)
    
    # initialize sweep
    sweep_id = wandb.sweep(config)
    
    # get sweep url
    sweep_url = f"{config['entity']}/{config['project']}/{sweep_id}"
    
    print(sweep_url)
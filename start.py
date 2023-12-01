import wandb
import yaml

if __name__ == "__main__":
    with open("config.yml", 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    print(config)
    entity = config['entity']
    project = config['project']    
    sweep_id = wandb.sweep(config)
    sweep_url = f"{entity}/{project}/{sweep_id}"
    print(sweep_url)
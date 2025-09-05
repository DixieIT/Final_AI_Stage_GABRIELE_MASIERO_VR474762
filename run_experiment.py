import os
import platform

def setup_virtual_display():
    """
    Sets up a virtual display on Linux for headless plotting/rendering.
    On Windows, does nothing.
    """
    if platform.system() == "Linux":
        try:
            from pyvirtualdisplay import Display
            display = Display(visible=False, size=(1400, 900))
            display.start()
            print("Virtual display started.")
        except Exception as e:
            print("[WARNING] Could not start virtual display. "
                  "If you need plotting/rendering, ask your admin to install Xvfb.")
            print(f"Error: {e}")
    else:
        print("Virtual display not needed on Windows.")

def run_multiple_experiments(seeds):
    for seed in seeds:
        print(f"\n[RUN] Starting experiment with seed={seed}\n")
        os.system(
            f'python BenchMARL/benchmarl/run.py '
            f'algorithm=iddpg '
            f'task=vmas/balance '
            f'task.max_steps=300 ' 
            f'seed={seed} '
            f'experiment.loggers=[wandb] '
            f'experiment.wandb_extra_kwargs={{project:benchmarl,name:seed_{seed}}}'

        )

def main():
    setup_virtual_display()
    run_multiple_experiments(seeds=[1, 2, 3])

if __name__ == "__main__":
    main()

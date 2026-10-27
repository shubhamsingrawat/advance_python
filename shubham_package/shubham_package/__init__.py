from time import sleep
import tqdm

progress_bar_length = 20

for i in tqdm.trange(progress_bar_length):
    sleep(0.1)  # Simulate some work being done



if __name__ == "__main__":
    print("This is the main entry point of the package.")
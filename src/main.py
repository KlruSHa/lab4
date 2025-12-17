from simulation import run_simulation


def main() -> None:
    steps = int(input("Введите количество шагов: "))
    seed = int(input("Введите seed: "))
    run_simulation(steps=steps, seed=seed)


if __name__ == "__main__":
    main()

import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]  # argus_platform/
JMETER_BIN = "/usr/local/bin/jmeter"  # при необходимости поменяешь
TESTPLANS_DIR = REPO_ROOT / "src" / "jmeter" / "testplans"
RESULTS_DIR = REPO_ROOT / "src" / "jmeter" / "results"


def run_jmeter(testplan_name: str, env: str = "local") -> int:
    """
    Запускает JMeter .jmx из папки testplans и кладёт результат в results/
    """
    testplan = TESTPLANS_DIR / testplan_name
    if not testplan.exists():
        raise FileNotFoundError(f"Testplan not found: {testplan}")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    result_file = RESULTS_DIR / f"{testplan.stem}_{env}.jtl"

    cmd = [
        JMETER_BIN,
        "-n",
        "-t",
        str(testplan),
        "-l",
        str(result_file),
        "-Jenv=" + env,
    ]

    print("Running:", " ".join(cmd))
    return subprocess.call(cmd)


if __name__ == "__main__":
    # Пример: python -m python.utils.jmeter_runner smoke/login.jmx
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m python.utils.jmeter_runner <relative_jmx_path> [env]")
        raise SystemExit(1)

    jmx = sys.argv[1]
    env = sys.argv[2] if len(sys.argv) > 2 else "local"
    exit_code = run_jmeter(jmx, env)
    raise SystemExit(exit_code)

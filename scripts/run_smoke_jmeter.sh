#!/usr/bin/env bash
set -e

# Запуск smoke-тестов JMeter из Python-раннера
python -m python.utils.jmeter_runner "smoke/example_smoke.jmx" "local"

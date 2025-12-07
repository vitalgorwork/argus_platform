# Argus Platform

Учебный репозиторий для практики:
- Git / GitHub
- Jira + ветки / тикеты
- JMeter load testing
- Python-утилиты вокруг нагрузочного тестирования

## Структура проекта

```text
argus_platform/
├── config/
│   └── jmeter/
│       └── jmeter.properties      # настройки JMeter (потом наполнишь)
├── docs/
│   └── jmeter_guide.md            # твои заметки по JMeter
├── scripts/
│   └── run_smoke_jmeter.sh        # пример запуска smoke-нагрузки
├── src/
│   ├── jmeter/
│   │   ├── testplans/
│   │   │   ├── smoke/
│   │   │   └── regression/
│   │   ├── data/
│   │   └── results/               # результаты .jtl (в .gitignore)
│   └── python/
│       ├── main.py
│       └── utils/
│           └── jmeter_runner.py
└── README.md

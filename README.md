# Касперский SafeBoard тестовое задание

## Описание работы и запуска

В качестве процесса было принято решение запускать <code>perf-bench</code>
от <code>phoronix-test-suite</code>.
Все зависимости кроме него, требуемые для запуска сервера лежат [тут](requirements.txt).
Сам же <code>phoronix-test-suite</code> устанавливается через <code>[Dockerfile](Dockerfile)</code>
Так же требуется чтобы пользователь, который запускал API, был в группе <code>docker</code>
Запускать сервер надо через [скрипт](run.sh)

## Предложения по улучшению API

На мой взгляд хотелось бы чуточку более единообразное API для этого надо разбить <code>/api/pn</code> на три endpointa
<code>/api/pn/start</code>,<code>/api/pn/stop</code> и <code>/api/pn/status</code> соответственно

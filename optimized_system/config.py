# 固定服務時間（秒）
SERVICE_TIME = 20

# 初始執行緒數
INIT_THREAD_COUNT = 8

# 最大 CPU 使用率（例如超過此值就認為 CPU 負載過高）
MAX_CPU_USAGE = 85

# 最小 CPU 使用率（例如超過此值就認為 CPU 正處於閒置）
MIN_CPU_USAGE = 40

# 最大等待任務總數（例如等待中的任務超過此數量則認為系統需要增加 Thread Pool 中的執行緒數）
# 等待任務過多
MAX_TOTAL_WAITING_TASK_COUNT = 10

# 最小等待任務總數（例如等待中的任務低於此數量則認為系統可以減少 Thread Pool 中的執行緒數）
# 等待任務過少
MIN_TOTAL_WAITING_TASK_COUNT = 3

# 當低 CPU 使用率且等待任務多時，最佳執行緒數的倍率
INCREASE_THREAD_COUNT_MAGNITUDE = 1.4

# 當高 CPU 使用率且等待任務少時，最佳執行緒數的倍率
DECREASE_THREAD_COUNT_MAGNITUDE = 0.6

# 最小執行緒數
MIN_WORKER_COUNT = 3

# 最大執行緒數
MAX_WORKER_COUNT = 20

# 提高執行緒數的優先值基準
WAIT_TIME_THRESHOLD = 300

# 執行緒執行時間上限
RUN_TIME_THRESHOLD = 30
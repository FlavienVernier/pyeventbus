source venv/bin/activate
python IO_performance_testing.py startCPUHeavyTestInMain
python IO_performance_testing.py startCPUHeavyTestInBackground
python IO_performance_testing.py startCPUHeavyTestInGreenlet
python IO_performance_testing.py startCPUHeavyTestInParallel
python IO_performance_testing.py startCPUHeavyTestInConcurrent
# python performance_testing.py startCPUHeavyTestInMain
# python performance_testing.py startCPUHeavyTestInBackground
# python performance_testing.py startCPUHeavyTestInGreenlet
# python performance_testing.py startCPUHeavyTestInParallel
# python performance_testing.py startCPUHeavyTestInConcurrent
deactivate
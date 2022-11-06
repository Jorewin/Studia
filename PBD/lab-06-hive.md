4.
Connecting to jdbc:hive2://localhost:10000/default
Connected to: Apache Hive (version 3.1.2)
Driver: Hive JDBC (version 3.1.2)
Transaction isolation: TRANSACTION_REPEATABLE_READ
Beeline version 3.1.2 by Apache Hive
5.
    - blazejowski_j
    - default
    - NaN
6.
    - hive.execution.engine=tez
    - hive.cbo.enable=true
    - hive.compactor.initiator.on=false
    - hive.stats.autogather=true
10.
    2411
    - rozproszony system plików
    - analizowano polecenie, konstruowano plan wykonania w silniku TEZ, wykonywano polecenie
    - TEZ
    - N/A
    - 2
    - MapTezProcessor
    - ReduceTezProcessor
11.
    - 2
    - brak zmian
12.
    2410
    - zasługa formatu ORC
    - zasługa formatu ORC
18.
    TAK
19.
    TAK
20.
    - 1
    - beers_orc
    - 1 NIE
    - plik bazowy
    - 000000_0
    - NIE
    - NIE
    - NIE
    - org.apache.hadoop.hive.ql.io.orc.OrcSerde
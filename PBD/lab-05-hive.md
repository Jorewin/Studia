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

21.

name,ibu
Bitter Bitch Imperial IPA,138.0
Troopers Alley IPA,135.0
Dead-Eye DIPA,130.0

22.

0.05977342423329049

23.

style,abv
English Barleywine,0.1076666663090388
Quadrupel (Quad),0.10400000214576721
American Barleywine,0.0989999994635582
American Malt Liquor,0.0989999994635582

24.

name,abv,city
Lee Hill Series Vol. 5 - Belgian Style Quadrupel Ale,0.128,Boulder

25.

_c0,name
138.0,Oregon
135.0,Virginia
130.0,Massachusetts

26.

beer_density,name
55.75426301769013,Colorado

27.

    - states_orc
    - 3
    - 2
    - LIMIT, SELECT, GROUP BY

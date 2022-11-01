## MAPREDUCE

2022-10-27 14:03:51,251 [main] WARN  org.apache.pig.newplan.BaseOperatorPlan - Encountered Warning IMPLICIT_CAST_TO_DOUBLE 1 time(s).
2022-10-27 14:03:51,255 [main] INFO  org.apache.pig.tools.pigstats.ScriptState - Pig features used in the script: HASH_JOIN,GROUP_BY
2022-10-27 14:03:51,277 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - yarn.resourcemanager.system-metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
2022-10-27 14:03:51,279 [main] INFO  org.apache.pig.data.SchemaTupleBackend - Key [pig.schematuple] was not set... will not generate code.
2022-10-27 14:03:51,279 [main] INFO  org.apache.pig.newplan.logical.optimizer.LogicalPlanOptimizer - {RULES_ENABLED=[AddForEach, ColumnMapKeyPrune, FilterConstantCalculator, ForEachConstantCalculator, GroupByConstParallelSetter, LimitOptimizer, LoadTypeCastInserter, MergeFilter, MergeForEach, NestedLimitOptimizer, PartitionFilterOptimizer, PredicatePushdownOptimizer, PushDownForEachFlatten, PushUpFilter, SplitConstantCalculator, SplitFilter, StreamTypeCastInserter]}
2022-10-27 14:03:51,301 [main] INFO  org.apache.pig.newplan.logical.rules.ColumnPruneVisitor - Columns pruned for trip: $0, $2, $3, $5, $6, $7, $8, $9, $11
2022-10-27 14:03:51,306 [main] INFO  org.apache.pig.newplan.logical.rules.ColumnPruneVisitor - Columns pruned for weather: $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19
2022-10-27 14:03:51,340 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MRCompiler - File concatenation threshold: 100 optimistic? false
2022-10-27 14:03:51,366 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MRCompiler$LastInputStreamingOptimizer - Rewrite: POPackage->POForEach to POPackage(JoinPackager)
2022-10-27 14:03:51,372 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MultiQueryOptimizer - MR plan size before optimization: 2
2022-10-27 14:03:51,373 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MultiQueryOptimizer - MR plan size after optimization: 2
2022-10-27 14:03:51,397 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - yarn.resourcemanager.system-metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
2022-10-27 14:03:51,459 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:03:51,668 [main] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:03:51,708 [main] INFO  org.apache.pig.tools.pigstats.mapreduce.MRScriptState - Pig script settings are added to the job
2022-10-27 14:03:51,714 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - mapred.job.reduce.markreset.buffer.percent is deprecated. Instead, use mapreduce.reduce.markreset.buffer.percent
2022-10-27 14:03:51,714 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - mapred.job.reduce.markreset.buffer.percent is not set, set to default 0.3
2022-10-27 14:03:51,718 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - mapred.output.compress is deprecated. Instead, use mapreduce.output.fileoutputformat.compress
2022-10-27 14:03:51,720 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Reduce phase detected, estimating # of required reducers.
2022-10-27 14:03:51,721 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Using reducer estimator: org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.InputSizeReducerEstimator
2022-10-27 14:03:51,731 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.InputSizeReducerEstimator - BytesPerReducer=1000000000 maxReducers=999 totalInputFileSize=39330570
2022-10-27 14:03:51,732 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Setting Parallelism to 1
2022-10-27 14:03:51,732 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - mapred.reduce.tasks is deprecated. Instead, use mapreduce.job.reduces
2022-10-27 14:03:51,732 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - This job cannot be converted run in-process
2022-10-27 14:03:51,747 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - mapred.submit.replication is deprecated. Instead, use mapreduce.client.submit.file.replication
2022-10-27 14:03:51,818 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Added jar file:/usr/lib/pig/piggybank.jar to DistributedCache through /tmp/temp-1458138690/tmp103662755/piggybank.jar
2022-10-27 14:03:51,899 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Added jar file:/usr/lib/pig/pig-0.18.0-SNAPSHOT-core-h3.jar to DistributedCache through /tmp/temp-1458138690/tmp-1193431211/pig-0.18.0-SNAPSHOT-core-h3.jar
2022-10-27 14:03:51,931 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Added jar file:/usr/lib/pig/lib/automaton-1.11-8.jar to DistributedCache through /tmp/temp-1458138690/tmp-82777213/automaton-1.11-8.jar
2022-10-27 14:03:51,956 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Added jar file:/usr/lib/pig/lib/antlr-runtime-3.4.jar to DistributedCache through /tmp/temp-1458138690/tmp1800383896/antlr-runtime-3.4.jar
2022-10-27 14:03:52,225 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Added jar file:/usr/lib/hive/lib/hive-exec-3.1.2.jar to DistributedCache through /tmp/temp-1458138690/tmp952733255/hive-exec-3.1.2.jar
2022-10-27 14:03:52,251 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Added jar file:/usr/lib/pig/lib/RoaringBitmap-shaded-0.7.45.jar to DistributedCache through /tmp/temp-1458138690/tmp379237605/RoaringBitmap-shaded-0.7.45.jar
2022-10-27 14:03:52,285 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Setting up single store job
2022-10-27 14:03:52,289 [main] INFO  org.apache.pig.data.SchemaTupleFrontend - Key [pig.schematuple] is false, will not generate code.
2022-10-27 14:03:52,289 [main] INFO  org.apache.pig.data.SchemaTupleFrontend - Starting process to move generated code to distributed cache
2022-10-27 14:03:52,289 [main] INFO  org.apache.pig.data.SchemaTupleFrontend - Setting key [pig.schematuple.classes] with classes to deserialize []
2022-10-27 14:03:52,362 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - 1 map-reduce job(s) waiting for submission.
2022-10-27 14:03:52,368 [JobControl] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:03:52,370 [JobControl] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:03:52,384 [JobControl] INFO  org.apache.hadoop.conf.Configuration.deprecation - yarn.resourcemanager.system-metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
2022-10-27 14:03:52,459 [JobControl] INFO  org.apache.hadoop.mapreduce.JobResourceUploader - Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/blazejowski_j/.staging/job_1666877288422_0001
2022-10-27 14:03:52,476 [JobControl] WARN  org.apache.hadoop.mapreduce.JobResourceUploader - No job jar file set.  User classes may not be found. See Job or Job#setJar(String).
2022-10-27 14:03:52,540 [JobControl] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input files to process : 1
2022-10-27 14:03:52,540 [JobControl] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 1
2022-10-27 14:03:52,546 [JobControl] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths (combined) to process : 1
2022-10-27 14:03:52,549 [GetFileInfo #1] WARN  org.apache.hadoop.util.concurrent.ExecutorHelper - Thread (Thread[GetFileInfo #1,5,main]) interrupted:
java.lang.InterruptedException
at com.google.common.util.concurrent.AbstractFuture.get(AbstractFuture.java:510)
at com.google.common.util.concurrent.FluentFuture$TrustedFuture.get(FluentFuture.java:88)
at org.apache.hadoop.util.concurrent.ExecutorHelper.logThrowableFromAfterExecute(ExecutorHelper.java:48)
at org.apache.hadoop.util.concurrent.HadoopThreadPoolExecutor.afterExecute(HadoopThreadPoolExecutor.java:90)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1157)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
at java.lang.Thread.run(Thread.java:750)
2022-10-27 14:03:52,572 [JobControl] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input files to process : 3
2022-10-27 14:03:52,572 [JobControl] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 3
2022-10-27 14:03:52,572 [JobControl] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths (combined) to process : 1
2022-10-27 14:03:52,576 [GetFileInfo #1] WARN  org.apache.hadoop.util.concurrent.ExecutorHelper - Thread (Thread[GetFileInfo #1,5,main]) interrupted:
java.lang.InterruptedException
at com.google.common.util.concurrent.AbstractFuture.get(AbstractFuture.java:510)
at com.google.common.util.concurrent.FluentFuture$TrustedFuture.get(FluentFuture.java:88)
at org.apache.hadoop.util.concurrent.ExecutorHelper.logThrowableFromAfterExecute(ExecutorHelper.java:48)
at org.apache.hadoop.util.concurrent.HadoopThreadPoolExecutor.afterExecute(HadoopThreadPoolExecutor.java:90)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1157)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
at java.lang.Thread.run(Thread.java:750)
2022-10-27 14:03:52,644 [JobControl] INFO  org.apache.hadoop.mapreduce.JobSubmitter - number of splits:2
2022-10-27 14:03:52,873 [JobControl] INFO  org.apache.hadoop.mapreduce.JobSubmitter - Submitting tokens for job: job_1666877288422_0001
2022-10-27 14:03:52,876 [JobControl] INFO  org.apache.hadoop.mapreduce.JobSubmitter - Executing with tokens: []
2022-10-27 14:03:53,019 [JobControl] INFO  org.apache.hadoop.mapred.YARNRunner - Job jar is not present. Not adding any jar to the list of resources.
2022-10-27 14:03:53,104 [JobControl] INFO  org.apache.hadoop.conf.Configuration - resource-types.xml not found
2022-10-27 14:03:53,104 [JobControl] INFO  org.apache.hadoop.yarn.util.resource.ResourceUtils - Unable to find 'resource-types.xml'.
2022-10-27 14:03:53,574 [JobControl] INFO  org.apache.hadoop.yarn.client.api.impl.YarnClientImpl - Submitted application application_1666877288422_0001
2022-10-27 14:03:53,681 [JobControl] INFO  org.apache.hadoop.mapreduce.Job - The url to track the job: http://pbdcluster-m:8088/proxy/application_1666877288422_0001/
2022-10-27 14:03:53,681 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - HadoopJobId: job_1666877288422_0001
2022-10-27 14:03:53,681 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Processing aliases projected_trip,projected_weather,trip,trip_with_weather,trip_with_weather_simple,weather
2022-10-27 14:03:53,681 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - detailed locations: M: trip[3,7],projected_trip[-1,-1],trip_with_weather[31,20],weather[13,10],weather[-1,-1],projected_weather[29,20],trip_with_weather[31,20] C:  R: trip_with_weather_simple[32,27]
2022-10-27 14:03:53,720 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - 0% complete
2022-10-27 14:03:53,722 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Running jobs are [job_1666877288422_0001]
2022-10-27 14:04:18,323 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - 25% complete
2022-10-27 14:04:18,323 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Running jobs are [job_1666877288422_0001]
2022-10-27 14:04:27,835 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - 50% complete
2022-10-27 14:04:27,835 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Running jobs are [job_1666877288422_0001]
2022-10-27 14:04:33,858 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:04:33,859 [main] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:04:33,873 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2022-10-27 14:04:34,850 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:04:34,852 [main] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:04:34,857 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2022-10-27 14:04:34,906 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:04:34,907 [main] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:04:34,916 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2022-10-27 14:04:35,036 [main] INFO  org.apache.pig.tools.pigstats.mapreduce.MRScriptState - Pig script settings are added to the job
2022-10-27 14:04:35,041 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - mapred.job.reduce.markreset.buffer.percent is not set, set to default 0.3
2022-10-27 14:04:35,041 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Reduce phase detected, estimating # of required reducers.
2022-10-27 14:04:35,042 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Using reducer estimator: org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.InputSizeReducerEstimator
2022-10-27 14:04:35,048 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.InputSizeReducerEstimator - BytesPerReducer=1000000000 maxReducers=999 totalInputFileSize=9320775
2022-10-27 14:04:35,048 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Setting Parallelism to 1
2022-10-27 14:04:35,048 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - This job cannot be converted run in-process
2022-10-27 14:04:35,094 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Added jar file:/usr/lib/pig/piggybank.jar to DistributedCache through /tmp/temp-1458138690/tmp2049327548/piggybank.jar
2022-10-27 14:04:35,142 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Added jar file:/usr/lib/pig/pig-0.18.0-SNAPSHOT-core-h3.jar to DistributedCache through /tmp/temp-1458138690/tmp329676078/pig-0.18.0-SNAPSHOT-core-h3.jar
2022-10-27 14:04:35,170 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Added jar file:/usr/lib/pig/lib/automaton-1.11-8.jar to DistributedCache through /tmp/temp-1458138690/tmp1979253753/automaton-1.11-8.jar
2022-10-27 14:04:35,211 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Added jar file:/usr/lib/pig/lib/antlr-runtime-3.4.jar to DistributedCache through /tmp/temp-1458138690/tmp-1909605356/antlr-runtime-3.4.jar
2022-10-27 14:04:35,486 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Added jar file:/usr/lib/hive/lib/hive-exec-3.1.2.jar to DistributedCache through /tmp/temp-1458138690/tmp-1261937616/hive-exec-3.1.2.jar
2022-10-27 14:04:35,520 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Added jar file:/usr/lib/pig/lib/RoaringBitmap-shaded-0.7.45.jar to DistributedCache through /tmp/temp-1458138690/tmp-507586841/RoaringBitmap-shaded-0.7.45.jar
2022-10-27 14:04:35,535 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Setting up single store job
2022-10-27 14:04:35,536 [main] INFO  org.apache.pig.data.SchemaTupleFrontend - Key [pig.schematuple] is false, will not generate code.
2022-10-27 14:04:35,537 [main] INFO  org.apache.pig.data.SchemaTupleFrontend - Starting process to move generated code to distributed cache
2022-10-27 14:04:35,537 [main] INFO  org.apache.pig.data.SchemaTupleFrontend - Setting key [pig.schematuple.classes] with classes to deserialize []
2022-10-27 14:04:35,572 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - 1 map-reduce job(s) waiting for submission.
2022-10-27 14:04:35,576 [JobControl] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:04:35,578 [JobControl] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:04:35,585 [JobControl] INFO  org.apache.hadoop.conf.Configuration.deprecation - yarn.resourcemanager.system-metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
2022-10-27 14:04:35,594 [JobControl] INFO  org.apache.hadoop.mapreduce.JobResourceUploader - Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/blazejowski_j/.staging/job_1666877288422_0002
2022-10-27 14:04:35,596 [JobControl] WARN  org.apache.hadoop.mapreduce.JobResourceUploader - No job jar file set.  User classes may not be found. See Job or Job#setJar(String).
2022-10-27 14:04:35,647 [JobControl] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input files to process : 1
2022-10-27 14:04:35,647 [JobControl] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 1
2022-10-27 14:04:35,647 [JobControl] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths (combined) to process : 1
2022-10-27 14:04:35,650 [GetFileInfo #1] WARN  org.apache.hadoop.util.concurrent.ExecutorHelper - Thread (Thread[GetFileInfo #1,5,main]) interrupted:
java.lang.InterruptedException
at com.google.common.util.concurrent.AbstractFuture.get(AbstractFuture.java:510)
at com.google.common.util.concurrent.FluentFuture$TrustedFuture.get(FluentFuture.java:88)
at org.apache.hadoop.util.concurrent.ExecutorHelper.logThrowableFromAfterExecute(ExecutorHelper.java:48)
at org.apache.hadoop.util.concurrent.HadoopThreadPoolExecutor.afterExecute(HadoopThreadPoolExecutor.java:90)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1157)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
at java.lang.Thread.run(Thread.java:750)
2022-10-27 14:04:35,706 [JobControl] INFO  org.apache.hadoop.mapreduce.JobSubmitter - number of splits:1
2022-10-27 14:04:35,772 [JobControl] INFO  org.apache.hadoop.mapreduce.JobSubmitter - Submitting tokens for job: job_1666877288422_0002
2022-10-27 14:04:35,772 [JobControl] INFO  org.apache.hadoop.mapreduce.JobSubmitter - Executing with tokens: []
2022-10-27 14:04:35,776 [JobControl] INFO  org.apache.hadoop.mapred.YARNRunner - Job jar is not present. Not adding any jar to the list of resources.
2022-10-27 14:04:35,839 [JobControl] INFO  org.apache.hadoop.yarn.client.api.impl.YarnClientImpl - Submitted application application_1666877288422_0002
2022-10-27 14:04:35,846 [JobControl] INFO  org.apache.hadoop.mapreduce.Job - The url to track the job: http://pbdcluster-m:8088/proxy/application_1666877288422_0002/
2022-10-27 14:04:36,074 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - HadoopJobId: job_1666877288422_0002
2022-10-27 14:04:36,074 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Processing aliases 1-110,final_result,trip_with_weather_grouped,unique_days
2022-10-27 14:04:36,074 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - detailed locations: M: trip_with_weather_grouped[38,28] C:  R: final_result[39,15],1-110[40,23],unique_days[40,14],1-110[40,23],unique_days[40,14]
2022-10-27 14:04:55,176 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - 75% complete
2022-10-27 14:04:55,176 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Running jobs are [job_1666877288422_0002]
2022-10-27 14:05:03,188 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Running jobs are [job_1666877288422_0002]
2022-10-27 14:05:06,208 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:05:06,209 [main] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:05:06,219 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2022-10-27 14:05:06,356 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:05:06,357 [main] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:05:06,364 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2022-10-27 14:05:06,422 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:05:06,423 [main] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:05:06,427 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2022-10-27 14:05:06,469 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - 100% complete
2022-10-27 14:05:06,503 [main] INFO  org.apache.pig.tools.pigstats.mapreduce.SimplePigStats - Script Statistics:

HadoopVersion   PigVersion      UserId  StartedAt       FinishedAt      Features
3.2.3   0.18.0-SNAPSHOT blazejowski_j   2022-10-27 14:03:51     2022-10-27 14:05:06    HASH_JOIN,GROUP_BY

Success!

Job Stats (time in seconds):
JobId   Maps    Reduces MaxMapTime      MinMapTime      AvgMapTime      MedianMapTime  MaxReduceTime    MinReduceTime   AvgReduceTime   MedianReducetime        Alias   FeatureOutputs
job_1666877288422_0001  2       1       7       7       7       7       6       6      66       projected_trip,projected_weather,trip,trip_with_weather,trip_with_weather_simple,weather        HASH_JOIN
job_1666877288422_0002  1       1       6       6       6       6       6       6      66       1-110,final_result,trip_with_weather_grouped,unique_days        GROUP_BY,DISTINCT    hdfs://pbdcluster-m/tmp/temp-1458138690/tmp-519444141,

Input(s):
Successfully read 689 records from: "hdfs://pbdcluster-m/user/blazejowski_j/input/weather.csv"
Successfully read 236065 records from: "hdfs://pbdcluster-m/user/blazejowski_j/input/trips"

Output(s):
Successfully stored 70 records (2598 bytes) in: "hdfs://pbdcluster-m/tmp/temp-1458138690/tmp-519444141"

Counters:
Total records written : 70
Total bytes written : 2598
Spillable Memory Manager spill count : 0
Total bags proactively spilled: 0
Total records proactively spilled: 0

Job DAG:
job_1666877288422_0001  ->      job_1666877288422_0002,
job_1666877288422_0002


2022-10-27 14:05:06,512 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:05:06,513 [main] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:05:06,520 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2022-10-27 14:05:06,552 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:05:06,552 [main] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:05:06,555 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2022-10-27 14:05:06,583 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:05:06,584 [main] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:05:06,587 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2022-10-27 14:05:06,618 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:05:06,618 [main] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:05:06,622 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2022-10-27 14:05:06,650 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:05:06,650 [main] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:05:06,653 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2022-10-27 14:05:06,672 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
2022-10-27 14:05:06,673 [main] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
2022-10-27 14:05:06,678 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2022-10-27 14:05:06,701 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Success!
2022-10-27 14:05:06,704 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - yarn.resourcemanager.system-metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
2022-10-27 14:05:06,705 [main] INFO  org.apache.pig.data.SchemaTupleBackend - Key [pig.schematuple] was not set... will not generate code.
2022-10-27 14:05:06,717 [main] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input files to process : 1
2022-10-27 14:05:06,717 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 1
((,,2014),98,205148.40440740756)
((,,2015),199,445027.3776701039)
((,,2016),171,389560.11681428447)
((,Fog,2014),90,272469.5775000001)
((,Fog,2015),58,110981.48100000006)
((,Fog,2016),63,120830.60624999992)
((,Rain,2014),69,118180.36086000012)
((,Rain,2015),80,169560.4068194449)
((,Rain,2016),75,166490.67570652202)
((,Snow,2015),77,184098.85750000004)
((,Fog-Rain,2015),17,25782.478666666662)
((,Fog-Rain,2016),45,101279.65466666665)
((,Rain-Snow,2016),30,37182.6465)
((,Fog , Rain,2015),43,71183.77071428568)
((,Rain , Snow,2014),27,26226.917000000005)
((,Rain-Thunderstorm,2015),11,22825.825)
((,Rain-Thunderstorm,2016),93,200014.23300000012)
((,Rain , Thunderstorm,2015),188,410317.3243333332)
((Male,,2014),131,77478.71674074062)
((Male,,2015),208,119546.91009793807)
((Male,,2016),151,85533.86058571417)
((Male,Fog,2014),74,56769.31650000001)
((Male,Fog,2015),196,104778.00330000013)
((Male,Fog,2016),139,77485.485)
((Male,Rain,2014),145,89389.18299999993)
((Male,Rain,2015),158,85232.3073124997)
((Male,Rain,2016),118,64866.22548387091)
((Male,Snow,2015),117,62720.50499999999)
((Male,Fog-Rain,2015),198,101499.37533333329)
((Male,Fog-Rain,2016),162,84563.07300000003)
((Male,Rain-Snow,2016),69,36189.129999999976)
((Male,Fog , Rain,2015),173,94534.7742857144)
((Male,Rain , Snow,2014),32,22438.111)
((Male,Rain-Thunderstorm,2015),165,79544.26100000007)
((Male,Rain-Thunderstorm,2016),152,78336.03000000003)
((Male,Rain , Thunderstorm,2015),210,123088.59933333342)
((Other,,2014),2,1852.1052857142859)
((Other,,2015),5,3545.4963333333303)
((Other,,2016),5,2942.4874338235277)
((Other,Fog,2015),3,2111.3694444444454)
((Other,Fog,2016),4,2344.772)
((Other,Rain,2014),3,2443.4865813953493)
((Other,Rain,2015),3,2095.3303650793655)
((Other,Rain,2016),4,2275.7969438202254)
((Other,Snow,2015),5,2875.298)
((Other,Fog-Rain,2015),3,1792.6963333333333)
((Other,Fog-Rain,2016),4,2035.1146666666666)
((Other,Rain-Snow,2016),2,1641.016)
((Other,Fog , Rain,2015),3,1362.0443333333335)
((Other,Rain-Thunderstorm,2015),4,2039.62)
((Other,Rain-Thunderstorm,2016),4,2537.1665)
((Other,Rain , Thunderstorm,2015),3,2377.3406666666665)
((Female,,2014),35,26921.667629629657)
((Female,,2015),57,42284.3727525774)
((Female,,2016),41,27710.431307142753)
((Female,Fog,2014),14,9477.920999999998)
((Female,Fog,2015),49,35472.70290000002)
((Female,Fog,2016),36,25252.802)
((Female,Rain,2014),33,26665.13370000001)
((Female,Rain,2015),41,28744.50234722225)
((Female,Rain,2016),32,20565.195537634405)
((Female,Snow,2015),32,21999.945000000003)
((Female,Fog-Rain,2015),41,22050.211666666666)
((Female,Fog-Rain,2016),39,24654.118000000017)
((Female,Rain-Snow,2016),25,13032.461999999998)
((Female,Fog , Rain,2015),44,28272.9822857143)
((Female,Rain , Snow,2014),4,3873.288)
((Female,Rain-Thunderstorm,2015),42,24226.612)
((Female,Rain-Thunderstorm,2016),43,27808.834499999994)
((Female,Rain , Thunderstorm,2015),49,34462.47566666669)

## TEZ

2022-10-27 14:22:09,939 [main] WARN  org.apache.pig.newplan.BaseOperatorPlan - Encountered Warning IMPLICIT_CAST_TO_DOUBLE 1 time(s).
2022-10-27 14:22:09,951 [main] INFO  org.apache.pig.tools.pigstats.ScriptState - Pig features used in the script: HASH_JOIN,GROUP_BY
2022-10-27 14:22:09,977 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - yarn.resourcemanager.system-metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
2022-10-27 14:22:09,984 [main] INFO  org.apache.pig.data.SchemaTupleBackend - Key [pig.schematuple] was not set... will not generate code.
2022-10-27 14:22:10,025 [main] INFO  org.apache.pig.newplan.logical.optimizer.LogicalPlanOptimizer - {RULES_ENABLED=[AddForEach, ColumnMapKeyPrune, FilterConstantCalculator, ForEachConstantCalculator, GroupByConstParallelSetter, LimitOptimizer, LoadTypeCastInserter, MergeFilter, MergeForEach, NestedLimitOptimizer, PartitionFilterOptimizer, PredicatePushdownOptimizer, PushDownForEachFlatten, PushUpFilter, SplitConstantCalculator, SplitFilter, StreamTypeCastInserter]}
2022-10-27 14:22:10,068 [main] INFO  org.apache.pig.newplan.logical.rules.ColumnPruneVisitor - Columns pruned for trip: $0, $2, $3, $5, $6, $7, $8, $9, $11
2022-10-27 14:22:10,073 [main] INFO  org.apache.pig.newplan.logical.rules.ColumnPruneVisitor - Columns pruned for weather: $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19
2022-10-27 14:22:10,146 [main] INFO  org.apache.pig.impl.util.SpillableMemoryManager - Selected heap (PS Old Gen) of size 699400192 to monitor. collectionUsageThreshold = 489580128, usageThreshold = 489580128
2022-10-27 14:22:10,227 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - yarn.resourcemanager.system-metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
2022-10-27 14:22:10,238 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezLauncher - Tez staging directory is /tmp/temp-1507209125 and resources directory is /tmp/temp-1507209125
2022-10-27 14:22:10,269 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.plan.TezCompiler - File concatenation threshold: 100 optimistic? false
2022-10-27 14:22:10,355 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - mapreduce.inputformat.class is deprecated. Instead, use mapreduce.job.inputformat.class
2022-10-27 14:22:10,561 [main] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input files to process : 3
2022-10-27 14:22:10,561 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 3
2022-10-27 14:22:10,563 [GetFileInfo #1] WARN  org.apache.hadoop.util.concurrent.ExecutorHelper - Thread (Thread[GetFileInfo #1,5,main]) interrupted:
java.lang.InterruptedException
at com.google.common.util.concurrent.AbstractFuture.get(AbstractFuture.java:510)
at com.google.common.util.concurrent.FluentFuture$TrustedFuture.get(FluentFuture.java:88)
at org.apache.hadoop.util.concurrent.ExecutorHelper.logThrowableFromAfterExecute(ExecutorHelper.java:48)
at org.apache.hadoop.util.concurrent.HadoopThreadPoolExecutor.afterExecute(HadoopThreadPoolExecutor.java:90)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1157)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
at java.lang.Thread.run(Thread.java:750)
2022-10-27 14:22:10,581 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths (combined) to process : 1
2022-10-27 14:22:10,656 [main] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input files to process : 1
2022-10-27 14:22:10,656 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 1
2022-10-27 14:22:10,666 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths (combined) to process : 1
2022-10-27 14:22:10,667 [GetFileInfo #1] WARN  org.apache.hadoop.util.concurrent.ExecutorHelper - Thread (Thread[GetFileInfo #1,5,main]) interrupted:
java.lang.InterruptedException
at com.google.common.util.concurrent.AbstractFuture.get(AbstractFuture.java:510)
at com.google.common.util.concurrent.FluentFuture$TrustedFuture.get(FluentFuture.java:88)
at org.apache.hadoop.util.concurrent.ExecutorHelper.logThrowableFromAfterExecute(ExecutorHelper.java:48)
at org.apache.hadoop.util.concurrent.HadoopThreadPoolExecutor.afterExecute(HadoopThreadPoolExecutor.java:90)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1157)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
at java.lang.Thread.run(Thread.java:750)
2022-10-27 14:22:11,301 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezJobCompiler - Local resource: automaton-1.11-8.jar
2022-10-27 14:22:11,301 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezJobCompiler - Local resource: pig-0.18.0-SNAPSHOT-core-h3.jar
2022-10-27 14:22:11,301 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezJobCompiler - Local resource: hive-exec-3.1.2.jar
2022-10-27 14:22:11,302 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezJobCompiler - Local resource: antlr-runtime-3.4.jar
2022-10-27 14:22:11,302 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezJobCompiler - Local resource: RoaringBitmap-shaded-0.7.45.jar
2022-10-27 14:22:11,302 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezJobCompiler - Local resource: piggybank.jar
2022-10-27 14:22:11,343 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - yarn.resourcemanager.system-metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
2022-10-27 14:22:11,357 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - mapred.output.compress is deprecated. Instead, use mapreduce.output.fileoutputformat.compress
2022-10-27 14:22:11,403 [main] INFO  org.apache.hadoop.conf.Configuration - resource-types.xml not found
2022-10-27 14:22:11,404 [main] INFO  org.apache.hadoop.yarn.util.resource.ResourceUtils - Unable to find 'resource-types.xml'.
2022-10-27 14:22:11,433 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - mapred.task.id is deprecated. Instead, use mapreduce.task.attempt.id
2022-10-27 14:22:11,544 [main] INFO  org.apache.hadoop.conf.Configuration.deprecation - yarn.resourcemanager.system-metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
2022-10-27 14:22:11,579 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - For vertex - scope-96: parallelism=1, memory=3072, java opts=-Djava.net.preferIPv4Stack=true -Dhadoop.metrics.log.level=WARN -Xmx2457m -Dlog4j.configuratorClass=org.apache.tez.common.TezLog4jConfigurator -Dlog4j.configuration=tez-container-log4j.properties -Dyarn.app.container.log.dir=<LOG_DIR> -Dtez.root.logger=INFO,CLA
    2022-10-27 14:22:11,579 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Processing aliases: projected_trip,trip,trip_with_weather
    2022-10-27 14:22:11,579 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Detailed locations: trip[1,7],projected_trip[-1,-1],trip_with_weather[27,20]
    2022-10-27 14:22:11,579 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Pig features in the vertex:
    2022-10-27 14:22:11,710 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - For vertex - scope-97: parallelism=1, memory=3072, java opts=-Djava.net.preferIPv4Stack=true -Dhadoop.metrics.log.level=WARN -Xmx2457m -Dlog4j.configuratorClass=org.apache.tez.common.TezLog4jConfigurator -Dlog4j.configuration=tez-container-log4j.properties -Dyarn.app.container.log.dir=<LOG_DIR> -Dtez.root.logger=INFO,CLA
        2022-10-27 14:22:11,711 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Processing aliases: projected_weather,trip_with_weather,weather
        2022-10-27 14:22:11,711 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Detailed locations: weather[9,10],weather[-1,-1],projected_weather[25,20],trip_with_weather[27,20]
        2022-10-27 14:22:11,711 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Pig features in the vertex:
        2022-10-27 14:22:11,784 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Set auto parallelism for vertex scope-98
        2022-10-27 14:22:11,784 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - For vertex - scope-98: parallelism=2, memory=3072, java opts=-Djava.net.preferIPv4Stack=true -Dhadoop.metrics.log.level=WARN -Xmx2457m -Dlog4j.configuratorClass=org.apache.tez.common.TezLog4jConfigurator -Dlog4j.configuration=tez-container-log4j.properties -Dyarn.app.container.log.dir=<LOG_DIR> -Dtez.root.logger=INFO,CLA
            2022-10-27 14:22:11,784 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Processing aliases: trip_with_weather,trip_with_weather_grouped,trip_with_weather_simple
            2022-10-27 14:22:11,784 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Detailed locations: trip_with_weather[27,20],trip_with_weather_simple[28,27],trip_with_weather_grouped[35,28]
            2022-10-27 14:22:11,785 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Pig features in the vertex: HASH_JOIN
            2022-10-27 14:22:11,882 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Set auto parallelism for vertex scope-99
            2022-10-27 14:22:11,882 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - For vertex - scope-99: parallelism=20, memory=3072, java opts=-Djava.net.preferIPv4Stack=true -Dhadoop.metrics.log.level=WARN -Xmx2457m -Dlog4j.configuratorClass=org.apache.tez.common.TezLog4jConfigurator -Dlog4j.configuration=tez-container-log4j.properties -Dyarn.app.container.log.dir=<LOG_DIR> -Dtez.root.logger=INFO,CLA
                2022-10-27 14:22:11,882 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Processing aliases: 1-34,final_result,unique_days
                2022-10-27 14:22:11,882 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Detailed locations: final_result[36,15],1-34[37,27],unique_days[37,18],1-34[37,27],unique_days[37,18]
                2022-10-27 14:22:11,882 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezDagBuilder - Pig features in the vertex: GROUP_BY,DISTINCT
                2022-10-27 14:22:11,937 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezJobCompiler - Total estimated parallelism is 24
                2022-10-27 14:22:11,967 [PigTezLauncher-0] INFO  org.apache.pig.tools.pigstats.tez.TezScriptState - Pig script settings are added to the job
                2022-10-27 14:22:11,990 [PigTezLauncher-0] INFO  org.apache.tez.client.TezClient - Tez Client Version: [ component=tez-api, version=0.9.2, revision=10cb3519bd34389210e6511a2ba291b52dcda081, SCM-URL=scm:git:https://gitbox.apache.org/repos/asf/tez.git, buildTime=2019-03-19T20:44:07Z ]
                2022-10-27 14:22:12,018 [PigTezLauncher-0] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at pbdcluster-m/10.164.0.18:8032
                2022-10-27 14:22:12,213 [PigTezLauncher-0] INFO  org.apache.hadoop.yarn.client.AHSProxy - Connecting to Application History server at pbdcluster-m/10.164.0.18:10200
                2022-10-27 14:22:12,217 [PigTezLauncher-0] INFO  org.apache.tez.client.TezClient - Session mode. Starting session.
                2022-10-27 14:22:12,241 [PigTezLauncher-0] INFO  org.apache.tez.client.TezClientUtils - Using tez.lib.uris value from configuration: file:/usr/lib/tez,file:/usr/lib/tez/lib,file:/usr/local/share/google/dataproc/lib
                2022-10-27 14:22:12,241 [PigTezLauncher-0] INFO  org.apache.tez.client.TezClientUtils - Using tez.lib.uris.classpath value from configuration: null
                2022-10-27 14:22:12,366 [PigTezLauncher-0] INFO  org.apache.tez.client.TezClient - Tez system stage directory hdfs://pbdcluster-m/tmp/temp-1507209125/.tez/application_1666877288422_0003 doesn't exist and is created
                2022-10-27 14:22:12,373 [PigTezLauncher-0] INFO  org.apache.hadoop.conf.Configuration.deprecation - yarn.resourcemanager.system-metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
                2022-10-27 14:22:12,601 [PigTezLauncher-0] INFO  org.apache.hadoop.yarn.client.api.impl.YarnClientImpl - Submitted application application_1666877288422_0003
                2022-10-27 14:22:12,604 [PigTezLauncher-0] INFO  org.apache.tez.client.TezClient - The url to track the Tez Session: http://pbdcluster-m:8088/proxy/application_1666877288422_0003/
                2022-10-27 14:22:21,308 [PigTezLauncher-0] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezJob - Submitting DAG PigLatin:DefaultJobName-0_scope-0
                2022-10-27 14:22:21,308 [PigTezLauncher-0] INFO  org.apache.tez.client.TezClient - Submitting dag to TezSession, sessionName=PigLatin:DefaultJobName, applicationId=application_1666877288422_0003, dagName=PigLatin:DefaultJobName-0_scope-0, callerContext={ context=PIG, callerType=PIG_SCRIPT_ID, callerId=PIG-default-34f944e2-0304-45ae-bfb8-b1e3aedbf2cf }
                2022-10-27 14:22:21,898 [PigTezLauncher-0] INFO  org.apache.tez.client.TezClient - Submitted dag to TezSession, sessionName=PigLatin:DefaultJobName, applicationId=application_1666877288422_0003, dagId=dag_1666877288422_0003_1, dagName=PigLatin:DefaultJobName-0_scope-0
                2022-10-27 14:22:21,920 [PigTezLauncher-0] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezJob - Submitted DAG PigLatin:DefaultJobName-0_scope-0. Application id: application_1666877288422_0003
                2022-10-27 14:22:21,946 [main] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezLauncher - HadoopJobId: job_1666877288422_0003
                2022-10-27 14:22:22,924 [Timer-0] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezJob - DAG Status: status=RUNNING, progress=TotalTasks: 3 Succeeded: 0 Running: 0 Failed: 0 Killed: 0, diagnostics=, counters=null
                2022-10-27 14:22:42,110 [PigTezLauncher-0] INFO  org.apache.tez.common.counters.Limits - Counter limits initialized with parameters:  GROUP_NAME_MAX=256, MAX_GROUPS=500, COUNTER_NAME_MAX=64, MAX_COUNTERS=120
                2022-10-27 14:22:42,114 [PigTezLauncher-0] INFO  org.apache.pig.backend.hadoop.executionengine.tez.TezJob - DAG Status: status=SUCCEEDED, progress=TotalTasks: 4 Succeeded: 4 Running: 0 Failed: 0 Killed: 0, diagnostics=, counters=Counters: 57
                org.apache.tez.common.counters.DAGCounter
                NUM_SUCCEEDED_TASKS=4
                TOTAL_LAUNCHED_TASKS=4
                DATA_LOCAL_TASKS=2
                AM_CPU_MILLISECONDS=3030
                AM_GC_TIME_MILLIS=21
                File System Counters
                FILE_BYTES_READ=11186556
                FILE_BYTES_WRITTEN=11136143
                FILE_READ_OPS=0
                FILE_LARGE_READ_OPS=0
                FILE_WRITE_OPS=0
                HDFS_BYTES_READ=39330570
                HDFS_BYTES_WRITTEN=2598
                HDFS_READ_OPS=9
                HDFS_LARGE_READ_OPS=0
                HDFS_WRITE_OPS=3
                org.apache.tez.common.counters.TaskCounter
                REDUCE_INPUT_GROUPS=1448
                REDUCE_INPUT_RECORDS=472819
                COMBINE_INPUT_RECORDS=0
                SPILLED_RECORDS=977326
                NUM_SHUFFLED_INPUTS=24
                NUM_SKIPPED_INPUTS=0
                NUM_FAILED_SHUFFLE_INPUTS=0
                MERGED_MAP_OUTPUTS=564872
                GC_TIME_MILLIS=636
                CPU_MILLISECONDS=20860
                PHYSICAL_MEMORY_BYTES=1957691392
                VIRTUAL_MEMORY_BYTES=17526288384
                COMMITTED_HEAP_BYTES=1957691392
                INPUT_RECORDS_PROCESSED=236754
                INPUT_SPLIT_LENGTH_BYTES=39330570
                OUTPUT_RECORDS=472889
                OUTPUT_LARGE_RECORDS=0
                OUTPUT_BYTES=17468670
                OUTPUT_BYTES_WITH_OVERHEAD=10332313
                OUTPUT_BYTES_PHYSICAL=10332409
                ADDITIONAL_SPILLS_BYTES_WRITTEN=564767
                ADDITIONAL_SPILLS_BYTES_READ=10570686
                ADDITIONAL_SPILL_COUNT=0
                SHUFFLE_CHUNK_COUNT=3
                SHUFFLE_BYTES=10332409
                SHUFFLE_BYTES_DECOMPRESSED=10332313
                SHUFFLE_BYTES_TO_MEM=0
                SHUFFLE_BYTES_TO_DISK=0
                SHUFFLE_BYTES_DISK_DIRECT=10332409
                NUM_MEM_TO_DISK_MERGES=0
                NUM_DISK_TO_DISK_MERGES=1
                SHUFFLE_PHASE_TIME=265
                MERGE_PHASE_TIME=360
                FIRST_EVENT_RECEIVED=137
                LAST_EVENT_RECEIVED=137
                MultiStoreCounters
                Output records in _0_tmp-1705843840=70
                Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
                2022-10-27 14:22:42,957 [main] INFO  org.apache.pig.tools.pigstats.tez.TezPigScriptStats - Script Statistics:

HadoopVersion: 3.2.3
PigVersion: 0.18.0-SNAPSHOT
TezVersion: 0.9.2
UserId: blazejowski_j
FileName:
StartedAt: 2022-10-27 14:22:10
FinishedAt: 2022-10-27 14:22:42
Features: HASH_JOIN,GROUP_BY

Success!


DAG 0:
Name: PigLatin:DefaultJobName-0_scope-0
ApplicationId: job_1666877288422_0003
TotalLaunchedTasks: 4
FileBytesRead: 11186556
FileBytesWritten: 11136143
HdfsBytesRead: 39330570
HdfsBytesWritten: 2598
SpillableMemoryManager spill count: 0
Bags proactively spilled: 0
Records proactively spilled: 0

DAG Plan:
Tez vertex scope-96     ->      Tez vertex scope-98,
Tez vertex scope-97     ->      Tez vertex scope-98,
Tez vertex scope-98     ->      Tez vertex scope-99,
Tez vertex scope-99

Vertex Stats:
VertexId Parallelism TotalTasks   InputRecords   ReduceInputRecords  OutputRecords  FileBytesRead FileBytesWritten  HdfsBytesRead HdfsBytesWritten Alias        Feature Outputs
scope-96           1          1         236065                    0         236065            112          4435670       39274054                0 projected_trip,trip,trip_with_weather
scope-97           1          1            689                    0            689            112            20129          56516                0 projected_weather,trip_with_weather,weather
scope-98           2          1              0               236754         236065        4460550          5877210              0                0 trip_with_weather,trip_with_weather_grouped,trip_with_weather_simple HASH_JOIN
scope-99          -1          1              0               236065             70        6725782           803134              0             2598 1-34,final_result,unique_daysGROUP_BY,DISTINCT       hdfs://pbdcluster-m/tmp/temp-2141316/tmp-1705843840,

Input(s):
Successfully read 236065 records (39274054 bytes) from: "hdfs://pbdcluster-m/user/blazejowski_j/input/trips"
Successfully read 689 records (56516 bytes) from: "hdfs://pbdcluster-m/user/blazejowski_j/input/weather.csv"

Output(s):
Successfully stored 70 records (2598 bytes) in: "hdfs://pbdcluster-m/tmp/temp-2141316/tmp-1705843840"

2022-10-27 14:22:42,977 [main] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input files to process : 1
2022-10-27 14:22:42,977 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 1
((,,2014),98,205148.4044074072)
((,,2015),199,445027.3776701035)
((,,2016),171,389560.11681428604)
((,Fog,2014),90,272469.57749999996)
((,Fog,2015),58,110981.48099999999)
((,Fog,2016),63,120830.60624999992)
((,Rain,2014),69,118180.36085999991)
((,Rain,2015),80,169560.40681944485)
((,Rain,2016),75,166490.67570652175)
((,Snow,2015),77,184098.85749999998)
((,Fog-Rain,2015),17,25782.478666666666)
((,Fog-Rain,2016),45,101279.65466666663)
((,Rain-Snow,2016),30,37182.646499999995)
((,Fog , Rain,2015),43,71183.77071428575)
((,Rain , Snow,2014),27,26226.916999999998)
((,Rain-Thunderstorm,2015),11,22825.825)
((,Rain-Thunderstorm,2016),93,200014.2329999999)
((,Rain , Thunderstorm,2015),188,410317.3243333331)
((Male,,2014),131,77478.71674074054)
((Male,,2015),208,119546.9100979383)
((Male,,2016),151,85533.86058571412)
((Male,Fog,2014),74,56769.316500000015)
((Male,Fog,2015),196,104778.00330000001)
((Male,Fog,2016),139,77485.48500000002)
((Male,Rain,2014),145,89389.18300000047)
((Male,Rain,2015),158,85232.30731249957)
((Male,Rain,2016),118,64866.22548387077)
((Male,Snow,2015),117,62720.50500000001)
((Male,Fog-Rain,2015),198,101499.37533333329)
((Male,Fog-Rain,2016),162,84563.07300000002)
((Male,Rain-Snow,2016),69,36189.130000000005)
((Male,Fog , Rain,2015),173,94534.77428571427)
((Male,Rain , Snow,2014),32,22438.111)
((Male,Rain-Thunderstorm,2015),165,79544.26100000001)
((Male,Rain-Thunderstorm,2016),152,78336.02999999996)
((Male,Rain , Thunderstorm,2015),210,123088.59933333333)
((Other,,2014),2,1852.1052857142859)
((Other,,2015),5,3545.4963333333344)
((Other,,2016),5,2942.4874338235277)
((Other,Fog,2015),3,2111.3694444444445)
((Other,Fog,2016),4,2344.7719999999995)
((Other,Rain,2014),3,2443.4865813953484)
((Other,Rain,2015),3,2095.3303650793646)
((Other,Rain,2016),4,2275.796943820225)
((Other,Snow,2015),5,2875.298)
((Other,Fog-Rain,2015),3,1792.696333333333)
((Other,Fog-Rain,2016),4,2035.114666666667)
((Other,Rain-Snow,2016),2,1641.016)
((Other,Fog , Rain,2015),3,1362.0443333333333)
((Other,Rain-Thunderstorm,2015),4,2039.62)
((Other,Rain-Thunderstorm,2016),4,2537.1665000000003)
((Other,Rain , Thunderstorm,2015),3,2377.3406666666665)
((Female,,2014),35,26921.667629629657)
((Female,,2015),57,42284.3727525773)
((Female,,2016),41,27710.431307142877)
((Female,Fog,2014),14,9477.920999999998)
((Female,Fog,2015),49,35472.70290000001)
((Female,Fog,2016),36,25252.802)
((Female,Rain,2014),33,26665.133700000028)
((Female,Rain,2015),41,28744.502347222176)
((Female,Rain,2016),32,20565.195537634438)
((Female,Snow,2015),32,21999.944999999996)
((Female,Fog-Rain,2015),41,22050.211666666673)
((Female,Fog-Rain,2016),39,24654.118000000006)
((Female,Rain-Snow,2016),25,13032.462000000003)
((Female,Fog , Rain,2015),44,28272.982285714304)
((Female,Rain , Snow,2014),4,3873.288)
((Female,Rain-Thunderstorm,2015),42,24226.612000000005)
((Female,Rain-Thunderstorm,2016),43,27808.8345)
((Female,Rain , Thunderstorm,2015),49,34462.475666666665)

## script

REGISTER /usr/lib/pig/piggybank.jar;

trip = LOAD '$input_dir/trips'
USING org.apache.pig.piggybank.storage.CSVExcelStorage(',','NO_MULTILINE','NOCHANGE','SKIP_INPUT_HEADER')
AS (
trip_id:int, starttime:chararray, stoptime:chararray, bikeid:chararray, tripduration:double,
from_station_name:chararray, to_station_name:chararray, from_station_id:chararray,
to_station_id:chararray, usertype:chararray,
gender:chararray, birthyear:int
);

weather = LOAD '$input_dir/weather.csv'
USING org.apache.pig.piggybank.storage.CSVExcelStorage(',', 'NO_MULTILINE','NOCHANGE','SKIP_INPUT_HEADER')
AS (
Date:chararray, Max_Temperature_F:double, Mean_Temperature_F:double,
Min_TemperatureF:double, Max_Dew_Point_F:double,
MeanDew_Point_F:double, Min_Dewpoint_F:double,
Max_Humidity:double, Mean_Humidity:double,
Min_Humidity:double, Max_Sea_Level_Pressure_In:double,
Mean_Sea_Level_Pressure_In:double, Min_Sea_Level_Pressure_In:double,
Max_Visibility_Miles:double, Mean_Visibility_Miles:double,
Min_Visibility_Miles:double, Max_Wind_Speed_MPH:double,
Mean_Wind_Speed_MPH:double, Max_Gust_Speed_MPH:chararray,
Precipitation_In:double,Events:chararray
);

projected_trip = FOREACH trip
GENERATE REGEX_EXTRACT(starttime, '(.*) (.*)', 1) AS startday, tripduration, gender;

projected_weather = FOREACH weather
GENERATE Date, Events, SUBSTRING(Date, (int)SIZE(Date)-4, (int)SIZE(Date)) as year;

trip_with_weather = JOIN projected_trip BY startday, projected_weather BY Date;

trip_with_weather_simple = FOREACH trip_with_weather
GENERATE
startday as startday,
tripduration as tripduration,
gender as gender,
Events as events,
year as year;

trip_with_weather_grouped = GROUP trip_with_weather_simple BY (gender, events, year);

final_result = FOREACH trip_with_weather_grouped {
    unique_days = DISTINCT trip_with_weather_simple.startday;
    GENERATE
    group,
    COUNT(trip_with_weather_simple)/COUNT(unique_days),
    SUM(trip_with_weather_simple.tripduration)/COUNT(unique_days);
    };

STORE final_result INTO '$output_dir' USING JsonStorage();

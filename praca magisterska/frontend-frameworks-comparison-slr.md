---
title: "React vs. its competitors: a Systematic Literature Review"
author: Jakub Błażejowski
bibliography: ./citations.bib
nocite:
  - "@ollila2022modern"
  - "@mlynarski2017comparative"
  - "@nv2022evaluating"
  - "@xing2019research"
  - "@a2020methodology"
  - "@ramos2017angularjs"
  - "@ilievska2022analysis"
  - "@nakajima2019jact"
  - "@tripon2021angular"
  - "@ivanova2019using"
  - "@delcev2018modern"
  - "@novac2021comparative"
  - "@ollila2021performance"
  - "@helenius2022web"
  - "@siahaan2022comparative"
---

# Introduction

According to sources like the Stack Overflow 2023 developer survey or the State of JavaScript survey, React remains the most popular library for web application front end creation, with its reported usage being almost double of that achieved by its main competitors — Angular and Vue. It is that much more surprising, considering the fact that Vue and other, newer frameworks, like Solid or Svelte, are steadily gaining developers' interest as stated by the same sources. Because of that, finding out why React maintains its position, is an important problem. One method that could potentially help to explain that, would be to compare the other libraries to React.

# Background

React is a JavaScript library used to create the front end part of web application. It was developed by Facebook and its first version was published in 2013. Besides React, there are many other frameworks and libraries which serve this purpose, while sometimes also providing other functionalities. Among them, there are Vue, Angular, Preact, Ember, Svelte and Solid.

# Aim and research questions

The purpose of this work was to find out the current state of knowledge on what comparisons had already been done, what were their results and how were they conducted. With that knowledge, it became possible to tell if the answer to the problem already exists and how to prepare an experiment that achieves that. The research was done in the form of a Systematic Literature Review to make sure that all available data on the topic has been analyzed.

<dl>
  <dt>RQ1</dt>
  <dd>How do React's alternatives compare to it?</dd>
  <dt>RQ2</dt>
  <dd>How to compare front end libraries?</dd>
</dl>

# Method

To make sure that the Systematic Literature Review (SLR) provided complete and reproducible results, it was conducted according to the following protocol.

## Acceptance criteria

The following criteria were used to preliminarily filter out the works which weren't relevant to the research questions.

<dl>
  <dt>Date range</dt>
  <dd>Years 2013–2022 — the start date marks the date React, which is the main focus of this work, was first published. Because of the ever-changing nature of technology, the newer articles proved to be more useful.</dd>
  <dt>Language</dt>
  <dd>English — it was assumed that all important and impactful publications eventually get published in English.</dd>
  <dt>Publication type</dt>
  <dd>Articles and conference papers — to make sure only the newest data makes it into the analysis.</dd>
</dl>

## Selection steps

During the selection phase, articles, which are supposed to represent the state of knowledge, got selected. The process was split into several phases. Every phase was concluded with a manual filtration, which, based on the title and the abstract, eliminated entries which were not related to the study.

### Database-driven selection

The first step in the selection process was performed using a reference and citation database. The choice of the database was done with the help of the supervisor, who suggested Web of Science (WoS) as the database which would provide most useful results. For this step, a following query was used.

```sql
(TS=(comparison) OR TS=(effectiveness) OR TS=(efficiency)
	OR TS=(speed) OR TS=(performance)) AND
(TS=(Svelte) OR TS=(Solid) OR TS=(React)) AND
TS=(JavaScript) AND
WC=(Computer Science, Software Engineering) AND
PY=(2013-2022)
```

The query was executed on 2023-05-05 and it generated 29 results. Previous iterations, which did not include the frameworks or the programming language specification, returned thousands of results from fields unrelated to the study, so those restrictions were added. After the manual selection, only 5 articles remained.

### Snowballing

This step was planned as a mean to generate more results in case the previous step did not provide satisfying results. It could have been repeated multiple times, where each iteration would have involved previously unvisited references and citing articles of papers from the previous phase. In the end, it got executed one time, generating 167 results (50 citing articles and 117 references), out of which 10 got selected (3 citing articles and 7 references).

## Data extraction table

A data extraction table was a tool used to gather information, which could help answer the research questions, from the articles returned from the selection procedure. It comprised the following columns:

<dl>
  <dt>Tools used</dt>
  <dd>JavaScript libraries compared in the article.</dd>
  <dt>Characteristics</dt>
  <dd>Characteristics that could be used to compare JavaScript libraries.</dd>
  <dt>Methodology</dt>
  <dd>The procedure and tools that were used in order to analyse the libraries.</dd>
  <dt>Results</dt>
  <dd>Results of the comparisons.</dd>
  <dt>Validity threats</dt>
  <dd>Anything that may make the article's results less viable.</dd>
</dl>

# Results analysis

In this section, an attempt was made to answer the research questions, based on the results of the Systematic Literature Review.

## RQ1: How do React's alternatives compare to it?

There are libraries which are in many ways better than React, but it still is a solid option and probably will be actively used in the future.

Performance-wise, applications designed with React are worse than those made with, for example, Svelte or Vue, but the difference is mostly negligible, especially in smaller applications. Frameworks like Angular or Blazor perform significantly worse, which was one of the reasons for React's broad adoption, but they are still worth considering because of the bigger set of out-of-the-box functionalities like testing support or routing. For React, it is easy to learn and find answers to questions, because of a big and active community. It is also easy to find experienced developers. This isn't at all the case for Angular and Blazor, with Vue being the closest competitor and Svelte and other newer frameworks having an active community, but a significantly smaller number of experienced developers.

## RQ2: How to compare front end libraries?

Library comparison should ideally consist of as many characteristics as possible, as long as the characteristics are relevant to every compared library. The areas to prioritize are: web application performance, the ecosystem and the available documentation.

Performance is by far the most often considered characteristic. It is usually done with Google Lighthouse tool, but it can also be done manually, which can sometimes prove beneficial. Google's tool, while very useful, is not able to generate some metrics, such as the Script Execution Time. (full render cycle without the rendering part). In component-based libraries, it can also be worthwhile to group the measurements by, for example: operation type (create, update, delete), component type (static, dynamic), part of the component tree that is operated on (tree root, tree element) or the size of the component tree. Sometimes the functionalities provided by the library, or availability of complementary libraries, can be an important factor that improves both the developer's and end-user's experience. Depending on the size of the application and time available, the learning curve becomes relevant alongside of availability of learning resources and community quality. Other properties, which could be useful in case the compared libraries prove to be very similar, are: build size, build time, rebuild time and  startup time.

# Validity threats
The following factors could endanger the validity of this study's findings:

<dl>
  <dt>Data completeness</dt>
  <dd>There is a real possibility that important articles or other sources exist, that weren't included in this analysis. What mitigates a possible impact of this threat is that the articles, which were included in the review, presented consistent results.</dd>
  <dt>Methodology difference</dt>
  <dd>Each of the analyzed articles defined its own methodology and focused on slightly different characteristics. The fact that the results were mostly similar counteracts this threat, but the comparisons should be treated separately.</dd>
  <dt>Technology evolution</dt>
  <dd>Because the libraries get updated over the years, results of earlier research can quickly become inapplicable. Most analyzed papers were from recent years, which makes this a small risk.</dd>
  <dt>Unknown framework versions</dt>
  <dd>Almost no papers specified which framework versions were tested, which could make the results unreliable. An assumption was made that researchers probably used the newest versions available at the time, which, combined with the fact that the papers were relatively new, mitigates this threat.</dd>
  <dt>Vague methodologies</dt>
  <dd>Because the results of this work relies heavily on other people's work, when the methodologies or sources are not well-defined it puts their validity under question, which in turn propagates to this paper. Most of the encountered articles had their methodologies thoroughly described, which partially eliminates this threat.</dd>
</dl>

# Conclusions
This work's aim was to try to find out why React is the most-used JavaScript front end library. It was found out that one of those reasons is that React does really well in comparison with other libraries and while there are alternatives which could one day overthrow it, it probably won't happen in the nearest future. After collecting the results from many articles, Vue seemed to be the biggest competitor, that's capable of doing so. However, because all the analyzed comparisons used different methodologies and the libraries are constantly evolving, this prediction might prove to be incorrect. What was also gathered, was information on conducting quality library comparisons. Future work could focus on applying the findings to further comparisons, or potentially devising a comparison method that would eliminate the time factor.

# References


> [!NOTE]  
> The following is the published protocol has describe by [OpenSAFELY](https://docs.opensafely.org/protocol/). The produced outputs may not be reflected exactly from the described output given in the protocol.

# Examining changes in ADHD diagnosis and pathways in primary care pre and post Covid

Contents
========

[Introduction](#introduction)

[Aims](#aims)

[Methodology](#methodology)

[Study Measures](#study-measures)

[Discussion](#discussion)

[References](#references)

Introduction
============

Attention Deficit Hyperactivity Disorder (ADHD) is a condition that
affects people's behaviour. People with ADHD can seem restless, may have
trouble concentrating and may act on impulse.

The symptoms of ADHD can be categorised into 2 types of behavioural
problems (NHS UK, 2021):

1.  inattentiveness (difficulty concentrating and focusing) – main signs
    include:

    -   having a short attention span and being easily distracted

    -   making careless mistakes – for example, in schoolwork

    -   appearing forgetful or losing things

2.  hyperactivity and impulsiveness – main signs include:

    -   being unable to sit still, especially in calm or quiet
        surroundings

    -   constantly fidgeting

    -   being unable to concentrate on tasks

The National Institute for Health and Care Excellence (NICE) currently
estimate the global prevalence of ADHD in children to be around 5%,
however this estimate is based on data published up to 2005 (Polanczyk,
2007). For adults in the UK NICE estimate the prevalence of ADHD to be
around 3-4% (NICE, 2018), however the method of this research cannot be
identified.

A large representative cohort study (McKechnie, 2023) examining ADHD
diagnoses and prescriptions in UK primary care between 2000 and 2018
reported that overall rate of new ADHD diagnoses increased in this time.
The rate doubled in males under 18; increased almost 20-fold in males
over 18; quadrupled in females under 18 and increased 15-fold in females
over 18.

The Covid-19 pandemic, declared on March 11, 2020, led to significant
impacts on the UK healthcare system and services, including mental
health services, with the first UK lockdown announced on March 23, 2020.

There was a reduction of over 10% in new referrals to general adult
mental health services, including secondary care and NHS psychological
therapies services, between April and August 2020, when compared to the
previous year. In the same time period, there was a 14.8% reduction in
the number of people in contact with NHS adult mental health services,
reflecting the lowered referrals made by primary care (Armitage, 2021).

A year later in April 2021, the number of people contacting the NHS for
help with mental health problems was at an all-time high. In 2022
approximately 1.6 million people in England were on the waiting list for
specialised treatment, and an additional eight million would benefit
from support. The number of young people completing an urgent pathway
for eating disorders increased by 72% between Q4 in 2019/20 to Q3
2021/22 (NHS Confederation, 2022). Paediatricians who provide ADHD
services for children and young people reported huge service
disruptions, almost half ceased the assessment of new patients with ADHD
(Ogundele, 2022).

Two studies researching the consumption of ADHD medications using sales
volume data across Europe and the world found that in 2020 in most
countries there was a drop in the actual consumption of medications
compared to what was expected. In 2021 and 2022, most countries consumed
more ADHD drugs than what was expected based on previous trends,
concluding that the pandemic had an accelerating effect on the already
present trend of increased consumption, making it even more pronounced
than before (Gimbach, 2023) (Gimbach, 2024).

Despite knowledge that ADHD diagnoses and medication use has been rising
over the past two decades, and that the Covid-19 pandemic had
substantial impact on the UK NHS mental health services, there has been
little comprehensive research into changes in ADHD diagnoses and
referrals post-pandemic.

Our work will use primary care data in England to further investigate
the previously observed rise in ADHD diagnoses and prescriptions.
Additionally, we seek to explore whether the pandemic has had a notable
impact on these figures, as indicated by previous research on medication
consumption trends.

Aims
====

Primary Aims
------------

The primary aim is to obtain counts and descriptive statistics pre and
post Covid of patients with an ADHD or receiving prescription to ADHD.
The details are as follows:

1.  To quantify the counts and its variance of patients pre and post
    Covid of the following:

    -   Recorded diagnosis of ADHD.

    -   Prescription of ADHD medicine.

    -   Remission of ADHD.

2.  To quantify different stages of the patients’ pathways and how these
    stages change pre and post Covid. The protocol considers the
    following activities:

    -   GP activity for ADHD and these activities over time.

    -   Pathways from diagnosis to remission for ADHD.

    -   Changes in prescribing ADHD over time.

    -   Referring patients in primary care to secondary care.

Secondary Aim
-------------

The secondary aim concerns calculating the prevalence of ADHD pre and
post Covid. In addition, the protocol will reproduce the previous study
in the [learning disabilities (LD)
dataset](https://digital.nhs.uk/data-and-information/publications/statistical/learning-disability-services-statistics)
(NHS England, 2023) comparing prevalence of ADHD patients with and
without a registered learning difficulties. The final result will be a
set of prevalence rates pre and post Covid.

Methodology
===========

Data Source
-----------

The project will analyse GP data through the software provider, The
Phoenix Partnership (TPP). The GP data will be accessed via the
platform; OpenSAFELY-TPP. This is a secure portal to allow computation
of NHS GP records while maintaining privacy preserving features for
example pseudonymisation and obfuscation of granular records to the end
user.

Inclusion criteria
------------------

The following records will be included in our study; either:

-   Patients with an ADHD diagnostic code between January 2016 to
    January 2024. This may include patients with other neurodiverse
    conditions, for example autism spectrum disorder (ASD) and
    Tourette’s syndrome.

-   Patients with ADHD prescription drug classed as “CNS stimulants and
    drugs for attention deficit hyperactivity disorder.” The cohort may
    include patients that receive an ADHD prescription without a
    diagnosis.

### Exclusion criteria

Patients must have a complete date of birth and no older than 100 years
old at the first logging of the ADHD code during the specified time
period.

### Variables to capture

The counts of patients with ADHD diagnostics code will includes the
following demographic and timely data:

-   Sex

-   Age with a focus on granular details on children and young persons

-   Ethnicity

-   Geographic area (ICS or GP Practice) at Lower Layer Super Output
    Area (LSOA)

-   Date of diagnostic code.

In terms of prescription records, the study will collect the following
information:

-   ADHD prescription drug with and without an ADHD diagnosis

-   Dose and quantity of the drug

-   Changes in the pharmacological treatment

-   Nonpharmacological treatment

### Outcomes of the study

The outcome of the study can be interpreted in three parts. The first
part are counts of patients that have ADHD and include the following
results:

-   A breakdown of patients with ADHD and whether they are on ADHD
    prescriptions.

-   Patients with an ADHD prescription without a diagnosis.

-   Rates of diagnosis broken down by age, sex, and ethnicity.

-   Prevalence of ADHD diagnosis.

-   Prevalence of ADHD remission.

The second part is to describe the timeliness of the patient pathway for
ADHD, there will be a comparison of these activities pre and post covid.

-   The average time between when a patient as an ADHD diagnosis and
    prescription.

-   The changes in prescription for ADHD after diagnosis.

The third and final part are a set of prevalence rates of patients with
and without learning disabilities who have been diagnosed.

Code List
---------

Code lists are codes that can query against patient’s records in
OpenSafely to determine an event. The provisional code list to determine
if a patient is diagnosis with ADHD can be found in (Bennett Institute
for Applied Data Science, n.d.). Table 1 describes a non-exhaustive code
lists for medication of ADHD. In the project, work is required to
compete the code lists for the following:

-   Exhaustive list of ADHD medication

-   Learning difficulties

-   Nonpharmacological treatment of ADHD.

-   ADHD remission

<table>
<tbody>
<tr class="odd">
<td><strong>Drug</strong></td>
<td><strong>Licence</strong></td>
<td><strong>Codelists</strong></td>
</tr>
<tr class="even">
<td>Dexamfetamine</td>
<td>ADHD in 6-17y. Some products also licenced for narcolepsy.</td>
<td>(Brown, *MEDICATION*: Dexamfetamine, 2024)</td>
</tr>
<tr class="odd">
<td>Methylphenidate</td>
<td>ADHD in 6-17y</td>
<td>(Brown, *MEDICATION*: Methylphenidate, 2024)</td>
</tr>
<tr class="even">
<td>Lisdexamfetamine</td>
<td>ADHD in 6y+</td>
<td>(Brown, *MEDICATION*: Lisdexamfetamine, 2024)</td>
</tr>
<tr class="odd">
<td>Atomoxetine</td>
<td>ADHD in 6y+</td>
<td>(Brown, *MEDICATION*: Atomoxetine, 2024)</td>
</tr>
<tr class="even">
<td>Guanfacine</td>
<td>ADHD in 6-17y</td>
<td>(Brown, *MEDICATION*: Guanfacine, 2024)</td>
</tr>
</tbody>
</table>

Table 1:Non exhaustive list of ADHD medication and the associated code
list.

Study Measures
==============

Primary Aim Results
-------------------

In the primary aim, the protocol will generate a series of tables to
compute prevalence of selected populations. For the prevalence, the
population in defined as the GP population at the point in time that
prevalence calculation is made. The results are summaries as follows:

-   Table 2 describes the prevalence rate in terms of patients with an
    ADHD diagnosis and remission code.

-   Table 3 describes the prevalence of patients being prescribed ADHD
    medication. The table will include patients that are prescribed ADHD
    medication without a diagnostic code.

-   Table 4 describes the prevalence of the population that have at
    least one change in ADHD medication.

-   Table 5 describes the average time from diagnosis to treatment of
    ADHD when the suspicion starts a given year.

-   Table 6 describes the prevalence of patients with
    non-pharmacological treatments with and without treatment.

In each table, the statistics will be broken down into demographics in
terms of sex, age, ethnicity, and geography. The results are displayed
in years from pre covid to post covid, highlighted green to blue
respectively.

| Year |  $${\color{Green}2016}$$ | $${\color{Green}2017}$$  | $${\color{Green}2018}$$  | $${\color{Green}2019}$$   |2020 | $${\color{Blue}2017}$$  | $${\color{Blue}2021}$$ | $${\color{Blue}2022}$$ | $${\color{Blue}2023}$$  | $${\color{Blue}2024}$$ |
| --- | ---   |---  |--- |---  |--- |---  | ---| --- |--- |---  | 
| Prevalence of ADHD Diagnosis  |    |  | |  | |  | |  | |  | 
| Prevalence of ADHD Remission  |    |  | |  | |  | |  | |  |  

Table 2: Template of the proposed results on the ADHD prevalence for
diagnosis and remission. The green and blue coloured region corresponds
to post and pre covid region respectively.

| Year |  $${\color{Green}2016}$$ | $${\color{Green}2017}$$  | $${\color{Green}2018}$$  | $${\color{Green}2019}$$   |2020 | $${\color{Blue}2017}$$  | $${\color{Blue}2021}$$ | $${\color{Blue}2022}$$ | $${\color{Blue}2023}$$  | $${\color{Blue}2024}$$ |
| --- | ---   |---  |--- |---  |--- |---  | ---| --- |--- |---  | 
| Prevalence receiving ADHD medication without an ADHD diagnosis |    |  | |  | |  | |  | |  | 
| Prevalence with ADHD that are prescribed ADHD medication  |    |  | |  | |  | |  | |  |  
| Prevalence with ADHD that do not prescribed ADHD medication  |    |  | |  | |  | |  | |  |  

Table 3: Template of the proposed results on ADHD prescription with
patients with and without an ADHD diagnosis. The green and blue coloured
region corresponds to post and pre covid region respectively.

| Year |  $${\color{Green}2016}$$ | $${\color{Green}2017}$$  | $${\color{Green}2018}$$  | $${\color{Green}2019}$$   |2020 | $${\color{Blue}2017}$$  | $${\color{Blue}2021}$$ | $${\color{Blue}2022}$$ | $${\color{Blue}2023}$$  | $${\color{Blue}2024}$$ |
| --- | ---   |---  |--- |---  |--- |---  | ---| --- |--- |---  | 
| Prevalence of at least one change in ADHD prescription|    |  | |  | |  | |  | |  | 

Table 4: Template of the proposed results on the prevalence of at least
one change in ADHD prescription taken. The green and blue coloured
region corresponds to post and pre covid region respectively.

| Year |  $${\color{Green}2016}$$ | $${\color{Green}2017}$$  | $${\color{Green}2018}$$  | $${\color{Green}2019}$$   |2020 | $${\color{Blue}2017}$$  | $${\color{Blue}2021}$$ | $${\color{Blue}2022}$$ | $${\color{Blue}2023}$$  | $${\color{Blue}2024}$$ |
| --- | ---   |---  |--- |---  |--- |---  | ---| --- |--- |---  | 
| Median time from diagnosis to treatment|    |  | |  | |  | |  | |  | 
| Mean time from diagnosis to treatment  |    |  | |  | |  | |  | |  |  

Table 5: Template of proposed results concerning the medium and mean
time from diagnosis to treatment. The year corresponds to year of
diagnosis. The green and blue coloured region corresponds to post and
pre covid region respectively.

| Year |  $${\color{Green}2016}$$ | $${\color{Green}2017}$$  | $${\color{Green}2018}$$  | $${\color{Green}2019}$$   |2020 | $${\color{Blue}2017}$$  | $${\color{Blue}2021}$$ | $${\color{Blue}2022}$$ | $${\color{Blue}2023}$$  | $${\color{Blue}2024}$$ |
| --- | ---   |---  |--- |---  |--- |---  | ---| --- |--- |---  | 
| Prevalence of patients with ADHD non pharmacological treatments without prescription |    |  | |  | |  | |  | |  | 
| Prevalence of patients with ADHD non pharmacological treatments with prescription   |    |  | |  | |  | |  | |  |  

Table 6: The prevalence of patients with ADHD with non-pharmacological
treatments with and without ADHD prescription. The green and blue
coloured region corresponds to post and pre covid region respectively.

Secondary Aim Results
---------------------

The secondary results will present the prevalence of ADHD patients with
learning difficulties and compare the results with the experimental
statistics from NHS England (NHS England, 2023).

| Year | Cohort | Prevalence from NHS England | Prevalence from OpenSafely |
| --- | ---   |---  |--- |
|2022-23|Learning Disability|8.56	| 
|2021-22|Learning Disability|8.04	|
|2020-21|Learning Disability|7.42	|
|2019-20|Learning Disability|6.45	|
|2018-19|Learning Disability|5.98	|
|2022-23|Without Learning Disability|0.99	|
|2021-22|Without Learning Disability|0.81	|
|2020-21|Without Learning Disability|0.69	|
|2019-20|Without Learning Disability|0.63	|
|2018-19|Without Learning Disability|0.57	|

Table 7: Template of the results comparing the computed prevalence from
NHS England (NHS England, 2023) with figures computed from OpenSafely.

Discussion 
==========

The protocol will quantify ADHD in primary care in terms of diagnostic
prevalence, pharmacological treatment, and the effects of Covid. The
advantages of the protocol are: First, the coverage of TPP in the
OpenSafely platform covers a large part GP Data in England, this
provides greater confidence than other NHS studies which uses a sample
group of GP data (NHS England, 2023). Secondly, the threshold of
diagnosis of ADHD is made by a clinician rather than a self-validated
questionnaire as done in previous NHS surveys (Health and Social Care
Information Centre, 2016). Finally, the study considers a wide of range
of demographic and protected characteristics thus potentially indicted a
range of patients where care has worsened pre covid.

There are limitations of the protocol: First the study does not consider
the effects of other neurodevelopmental diagnoses like autism on the
ADHD patient pathway, the study may be intractable to compute given the
many permutations if the protocol includes different conditions.
Secondary, in our proposal, we consider the earliest point in the
patient pathway is at diagnosis. The study will not consider suspicion
of ADHD, which is the earliest point of the patient pathway. There is no
code for suspicion of ADHD thus no reliable statistics can be derived.

Conclusion
----------

The protocol seeks to understand changes (if any) in the diagnosis and
pathways for ADHD pre and post Covid in England. To this end, the
protocol aims to queries a set of records that either have an ADHD code
or is provided with a prescription for ADHD. The results will assist NHS
policymakers on the changes in demand and determine if NHS patients’
needs are met. In addition, aids the understanding of ADHD services.

References
==========

Armitage, R. (2021). Antidepressants, primary care, and adult mental
health services in England during COVID-19. *The Lancet
Psychiatry*.Bennett Institute for Applied Data Science. (n.d.).

*Attention Deficit Hyperactivity Disorder codes*. Retrieved from
OpenCodelists:
https://www.opencodelists.org/codelist/nhsd-primary-care-domain-refsets/adhd\_cod/20200812/

Brown, A. (2024, 5 7). *\*MEDICATION\*: Atomoxetine*. Retrieved from Github:
https://github.com/opensafely/codelist-development/issues/313

Brown, A. (2024, 5 7). *\*MEDICATION\*: Dexamfetamine*. Retrieved from GitHub:
https://github.com/opensafely/codelist-development/issues/310

Brown, A.
(2024, 5 7). *\*MEDICATION\*: Guanfacine*. Retrieved from Github:
https://github.com/opensafely/codelist-development/issues/314

Brown, A.
(2024, 5 7). *\*MEDICATION\*: Lisdexamfetamine*. Retrieved from Github:
https://github.com/opensafely/codelist-development/issues/312

Brown, A.
(2024, 5 7). *\*MEDICATION\*: Methylphenidate*. Retrieved from Github:
https://github.com/opensafely/codelist-development/issues/311

Gimbach, S.
(2023). The impact of the COVID-19 pandemic on ADHD medicine consumption
in 47 countries and regions. *European Neuropsychopharmacology*,
24-35.

Gimbach, S. (2024). ADHD medicine consumption in Europe after
COVID-19: catch-up or trend change? *BMC Psychiatry*, 112.

Health and
Social Care Information Centre. (2016, September 29). *Adult Psychiatric
Morbidity Survey 2014.* Retrieved from NHS Digital:
https://files.digital.nhs.uk/pdf/2/f/adult\_psychiatric\_study\_ch8\_web.pdf

McKechnie,
D. G. (2023). Attention-deficit hyperactivity disorder diagnoses and
prescriptions in UK primary care, 2000–2018: population-based cohort
study. *BJPsych Open*, 121.

NHS Confederation. (2022). *Running hot: the
impact of the pandemic on mental health service.* Retrieved from NHS Confederation: https://www.nhsconfed.org/publications/running-hot


NHS England. (2023, December 7). Health and Care of People with Learning Disabilities,
Experimental Statistics 2022 to 2023*. Retrieved from NHS England:
https://digital.nhs.uk/data-and-information/publications/statistical/health-and-care-of-people-with-learning-disabilities/experimental-statistics-2022-to-2023

NHS UK. (2021, December 24). *Overview - Attention deficit hyperactivity
disorder (ADHD)*. Retrieved from
https://www.nhs.uk/conditions/attention-deficit-hyperactivity-disorder-adhd/

NICE. (2018). *Attention deficit hyperactivity disorder: diagnosis and
management.* Retrieved from NHS Confederation: https://www.nice.org.uk/guidance/ng87 

Ogundele, M. O. (2022). The impact of Covid-19 pandemic on
services for children and adolescents with ADHD: results from a survey
of paediatricians in the United Kingdom. *AIMS Public Health*.

Polanczyk, G. (2007). The Worldwide Prevalence of ADHD: A Systematic Review and
Metaregression Analysis. *American Journal of Psychiatry*.
